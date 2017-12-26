Title: Playing with POSIX pipes in Python
Date: 2012-05-14 16:07
Author: Kai Blin
Tags: antiSMASH, context manager, python
Slug: playing-with-posix-pipes-in-python
Status: published

Recently I was faced with an external program that I wanted to call from
my script that only writes its output to a file, not to stdout. Faced
with having to call this program a lot of times in parallel, I decided
to fake up its output files via POSIX FIFO pipes.
Unfortunately the python API around FIFOs is pretty close to the POSIX
API, so it feels a bit un-pythonish. The following post illustrates my
approach to getting around this limitation.

### Workload

In order to simulate my workload, I came up with the following simple
script called `pipetest.py` that takes an output file name and then
writes some text into that file.

```python
#!/usr/bin/env python

import sys

def main():
    pipename = sys.argv[1]
    with open(pipename, 'w') as p:
        p.write("Ceci n'est pas une pipe!n")

if __name__ == "__main__":
    main()
```

### The Code

In my test, this "file" will be a FIFO created by my wrapper code. The
implementation of the wrapper code is as follows, I will go over the
code in detail further down this post:

```python
#!/usr/bin/env python

import tempfile
import os
from os import path
import shutil
import subprocess

class TemporaryPipe(object):
    def __init__(self, pipename="pipe"):
        self.pipename = pipename
        self.tempdir = None

    def __enter__(self):
        self.tempdir = tempfile.mkdtemp()
        pipe_path = path.join(self.tempdir, self.pipename)
        os.mkfifo(pipe_path)
        return pipe_path

    def __exit__(self, type, value, traceback):
        if self.tempdir is not None:
            shutil.rmtree(self.tempdir)

def call_helper():
    with TemporaryPipe() as p:
        script = "./pipetest.py"
        subprocess.Popen(script + " " + p, shell=True)
        with open(p, 'r') as r:
            text = r.read()
        return text.strip()

def main():
        call_helper()

if __name__ == "__main__":
    main()
```

### Code in Detail


So let's look at the code in more detail. The code I'm using relies on a
bunch of libs from the python standard library, and is working with
Python 2.6 and up.

-  `tempfile` is used to get a temporary directory for me to create the
   FIFO in.
-  `os` has the `os.mkfifo()` call.
-  `os.path` handles the path crunching required.
-  `shutil` is used to remove the temporary directory after use.
-  `subprocess` is used to run the workload script.

#### TemporaryPipe class

Next comes the nifty part, a [context manager
object](http://docs.python.org/reference/datamodel.html#context-managers)
handling the creation and removal of the temporary FIFO pipe. Let's look
at the class in detail.

```python
class TemporaryPipe(object):
    def __init__(self, pipename="pipe"):
        self.pipename = pipename
        self.tempdir = None
```

The class definition and the constructor don't really hide anything
interesting, though it's worth noting that `self.tempdir` is set to
`None`. That will make the clean-up easier further down.

#### \_\_enter\_\_

```python
def __enter__(self):
    self.tempdir = tempfile.mkdtemp()
    pipe_path = path.join(self.tempdir, self.pipename)
    os.mkfifo(pipe_path)
    return pipe_path
```

The `__enter__(self)` function is the set-up code for the context
manager. Here, a temporary directory is created. Afterwards,
`os.mkfifo()` creates the FIFO. Finally, the pipe's path is returned.


#### \_\_exit\_\_

```python
def __exit__(self, type, value, traceback):
    if self.tempdir is not None:
        shutil.rmtree(self.tempdir)
```

The `__exit__(self, type, value, traceback)` function is always called
when the context manager's block is exited. Thus, it's the ideal place
to run the clean-up, in our case removing the temporary directory and
the pipe contained within it.

`shutil.rmtree()` takes care of this just fine. If `mkdtemp()` failed,
we don't have to bother, of course. Our clean-up doesn't require any
extra knowledge of the things we're cleaning up, so we're free to ignore
all those parameters.

#### The call\_helper Function

```python
def call_helper():
    with TemporaryPipe() as p:
        script = "./pipetest.py"
        subprocess.Popen(script + " " + p, shell=True)
        with open(p, 'r') as r:
            text = r.read()
        return text.strip()
```

Because `TemporaryPipe` is a context manager, it's useable from a `with`
statement. This means that in the block inside the
`with TemporaryPipe() as p` block, there is a temporary directory
containing a FIFO pipe. Because
[`__enter__()`](#class_temporary_pipe__enter)
returns the pipe's path, that will be assigned to `p` within the block.
`subprocess.Popen()` is now used to run the [workload
script](#workload), going via a shell to evaluate
the hashtag. This probably isn't the smartest idea performance-wise, but
this is proof-of-concept code after all.
After the workload script was run, another `with` statement opens a new
block using the pipe's path, opening the FIFO for reading. The text is
read out and the newline stripped. Now, the `return` statement returns
the read text, and also causes the pipe's context manager to call the
[`__exit__()`](#__exit__)
function to clean up.

### Conclusions

I'm pretty content with the way the
[`call_helper()`](#call_helper) function reads.
The complexity of setting up and then cleaning up the FIFO is hidden
away in the `TemporaryPipe` class. I spent a bit of time coming up with
this, so I thought I'd share this solution with other people. Now I just
need to add this to my utility library and write tests for it.
