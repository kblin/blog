Title: From the frontline, day 1
Date: 2011-08-08 09:17
Author: Kai Blin
Tags: debugging, python, war on legacy code
Slug: from-the-frontline-day-1
Status: published


I've decided to start the campaign by ditching the existing PHP web app.
I lost all confidence in it last Friday, when I found that it only
worked by accident, due to a well-placed typo.
As I'm rewriting the web app anyway, I thought I could also ditch PHP
altogether. Not that it's necessarily a bad language for web apps, but
the rest of the code is perl or python, so getting rid of php means one
less language to get confused by.


Because this is the [War on Legacy Code]({filename}/war-on-legacy-code.md),
I'm not going to write untested code in this campaign. So first I need
to brush up my python unit testing skills. I do have parts of a python
version of the web app already (untested, that won't work later), but
it's missing a user feedback form.
I don't want to send an email for every run of the test suite, so I need
to mock up `smtplib.SMTP`. After some web research, I'll be using Ian
Bicking's [minimock](http://blog.ianbicking.org/minimock.html) to
provide my mock objects. As I don't just run doctests (even though
they're pretty cool), I decided to also throw in
[MiniMockUnit](http://blog.webmynd.com/2009/02/18/mocking-objects-in-python-unit-tests/),
which makes minimock print the output to a StringIO buffer instead of
stdout. That way, you can easily put it in a normal unit test.


I usually run my tests using nosetests. Turns out, nosetests allows me
to run both vanilla unit tests and doctests, and it also has a code
coverage plugin. Thus,

```bash
nosetests -v --with-doctest --with-coverage --cover-html --cover-package="testmodule"
```

will get the module "testmodule" tested using available unit tests,
doctests and the test coverage will be reported in html in the cover/
directory. The `--cover-package` part seems to be needed to stop the
coverage code from trying (and failing) to create coverage information
files in the standard lib paths.

To sum up, I didn't actually see much battle.. er.. code today but my
arsenal is filled with testing tools, and I'm well prepared to jump into
the fray tomorrow. Also, thanks to some help from the folks on \#gsoc
IRC on freenode, I now have decent syntax highlighting and formatting on
my blog, so I might be able to post code samples for real now. Life is
good so far.

