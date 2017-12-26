Title: Running Samba's autobuild.py
Date: 2012-03-16 05:44
Author: Kai Blin
Category: Samba
Tags: Samba, testing
Slug: running-sambas-autobuild-py
Status: published

[Samba](http://samba.org/) has a lot of tests, and we like to run them
often. In order to easily do that, we've got a script that checks out a
bunch of repositories and runs all tests in them, in parallel and
independent of each other. It's living in the source tree at
`scripts/autobuild.py`. Here's my notes for running `autobuild.py` on a
local machine.

First, set up an in-memory file system. `autobuild.py` and the tests run
by it touch a lot of files, and not running these tests on a spinning
disk will speed things up a lot.

```bash
# create the memdisk location
mkdir /memdisk

# default size is half your ram, use -o size=SIZE
# to change that if needed
mount -t tmpfs tmpfs /memdisk

# now create an image file, samba's tests don't like plain tmpfs
# Needs to be bigger than 3 gig
dd if=/dev/zero of=/memdisk/build.img bs=1MiB count=4000
losetup /dev/loop0 /memdisk/build.img


# format as ext2, no need to do journalling
# it's gone when the machine fails anyway
mkfs.ext2 /dev/loop0

# mount
mkdir /memdisk/kai
mount /dev/loop0 /memdisk/kai
chown -R kai:kai /memdisk/kai
```

And now, I can just run `./script/autobuild.py` and get a coffee while
all the tests are run.
