Title: War on Legacy Code
Date: 2011-08-08 06:04
Author: Kai Blin
Tags: antiSMASH, code cleanup, debugging, defensive programming, war on legacy code
Slug: war-on-legacy-code
Status: published

Following the hallowed US American tradition of declaring war on whatever things
you don't like, I've decided to declare war on legacy code this week.

By legacy code, I mostly mean untested code, following the definition of Michael
Feathers' book _Working with Legacy Code_. That's a great read, by the way. If
you're working with old code, you should go read it. I found that I've been
doing most of the things mentioned already, but it's nice to see a systematic
write-up about it.

My chosen battlefield in this war is the code at my day job, mostly because it's
in a much worse shape than the code I deal with in the various Open Source
projects I'm involved in. Seeing how my day job code is a Frankenstein's monster
of Perl, PHP and Python parts, some of the work will be to get some of the tests
done twice. In particular, I really want to get rid of the PHP parts.

I won't delve into the particulars of the code too much, it's published under
the GPLv3 if anyone is interested. I will however try to post some daily news
from the front lines, with things that I have thought about during that
particular day of the battle.
