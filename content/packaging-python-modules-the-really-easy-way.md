Title: Packaging python modules, the really easy way
Date: 2011-02-17 15:24
Author: Kai Blin
Tags: Launchpad, OBS, packaging, py2pack, python
Slug: packaging-python-modules-the-really-easy-way
Status: published

I just had to package up a python package to make installation of a
software we use at work easier. The systems we run here are Suse- and
Ubuntu-based, so I got to package RPMs and debs.

I did package the odd perl package and some bioinformatics tool before,
but I haven't looked at it for a while, so I was pretty rusty. I use the
[OpenSuse Build Service](http://build.opensuse.org/) to build RPMs, and
the nice folks in FreeNode's `#opensuse-buildservice` pointed me a
[py2pack](http://saschpe.wordpress.com/2010/12/12/braindead-python-packaging/),
a truly amazing piece of software that creates a .spec file for you from
package information in pypi.

Now, I had to package pysvn, which happens to not link to the
downloadable file from pypi. As it turns out, this just stopped me from
using py2pack for downloading the file, `py2pack generate` works fine.
Filling in the missing License and Description information was easy, and
my package was building on OBS in under five minutes.

For Ubuntu, [Python packaging
guide](https://wiki.ubuntu.com/PackagingGuide/Python) was a bit less
comfortable, but a short while afterwards my Ubuntu package was built on
[Launchpad](https://launchpad.net/) as well.

Life is good. At least so far, now I get to make all of that work for
system \#3 in the department. This happens to be an OS sold by a company
from the northern west coast of the USA, and it doesn't have an execute
bit and can't deal with hashbang lines. Oh well, two out of three isn't
too bad.
