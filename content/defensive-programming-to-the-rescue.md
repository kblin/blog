Title: Defensive programming to the rescue
Date: 2011-01-21 09:14
Author: Kai Blin
Tags: debugging, defensive programming, printf debugging
Slug: defensive-programming-to-the-rescue
Status: published

I've just fixed a bug in a web app that I'm working on with a couple of
colleagues, a bug that is a great example of a hard to find, easy to fix
bug that could have been avoided by some defensive programming.

I thought I'd share this titbit to illustrate why defensive programming
is a good idea.

The application we're working on consists of three parts:

- a web front-end that accepts jobs (php based)
- a database keeping the job queue (SQL)
- the back-end that runs the jobs (python)

The job is actually an external script, which is important for this bug
as well.

On the web front-end, the user gets to choose a couple of options for
the job using check-boxes.

The bug we were seeing was that if the user just clicked one checkbox
(and that wasn't the "all" checkbox), the external script would die with
an "invalid options" error.

The options are passed into the SQL database as a comma-separated
string, and our first suspicion was that for single options, there was a
trailing comma left. A quick look at the database dump showed that this
was not the case.

The next idea was that the back-end was not constructing the command
line for the external script correctly. The code looked sane, but just
to be sure I decided to do some printf debugging. In the printout of the
command line, I finally found the bug. It was in the web front-end after
all. Let's look at the code (changed a bit for brevity).


```perl
    // 1 is "all"
    if($_POST["1"] == "on" ){
      $options = "1";
    } else {
      for ($i = 2; $i <= 10; $i++) {
          if($_POST["$i"] == "on") {
              $options .= " " . $i . ",";
          }
      }
      $suffix = strripos($options, ",");
      $options = substr($options, 0, $suffix);
    }
```

Can you spot the problem? `$options .= " " . $i . ",";`
is the culprit. It adds a leading white-space to the \$options string.
Looking at the database dump, that's easy to miss.

Now, why is this a problem? Let's look at the back-end code (changed for
clarity again):

```python
    job = get_next_job_from_work_queue()
    args = ['./do_stuff.py', job.filename]
    args += ['--options', job.options != None and
                          jobs.options or '1']
    subprocess.call(args)
```

The back-end uses an array for its command line arguments to avoid
having to call out to a shell first. This has the side effect that all
the arguments are passed to the called script verbatim. Thus, a leading
space character is kept and passed to the called application. This is
**defensive programming fail \#1**.

Still, this doesn't explain why the white-space is a problem. For that,
we need to look at `do_stuff.py` (Changed for clarity again).

```python
    value = options[options.index(i) + 1]
    if i == "--options":
        if "," not in value and value not in ["1","2","3","4","5",
                                              "6","7","8","9","10"]:
            invalidoptions(i)

```
Assuming we clicked on the \#7 check-box in the front-end, `" 7"` is
passed to `do_stuff.py`. `" 7"` is not in
`["1","2","3","4","5","6","7","8","9","10"]`, so we fail. **Defensive
programming fail \#2** is in the `value = options[options.index(i) + 1]`
line. Adding a `strip()` here would have avoided the bug. This was not
found in manual testing, as the shell takes care of stripping the
white-space characters for us. Still, a bit of defensive programming
would have helped to avoid the issue.

If I ever teach a programming course, one of the assignments will be
finding and fixing a bug like this.


**Update:** 2011-08-08 Pretty-print code.
