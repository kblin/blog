Title: On the way to Samba 4, week 45
Date: 2010-11-17 22:25
Author: Kai Blin
Category: Samba
Tags: Samba
Slug: on-the-way-to-samba-4-week-45
Status: published

A bit late, as usual, but I finally have something productive again.
I've got a Samba4 UDP echo server and async client library (including
torture test suite), and they're almost working. :)
I'm saying almost because I can only get it to work manually right now,
not from "make test". I'm sure it's some small thing I'm missing, I'm
expecting this to be fixed soon.
The code also still lacks some explanatory comments, but should be ready
for the mainline for the week 46 report.

The client library and torture test also runs against netcat, so two
"implementations" of echo servers are supported for sure. ;)
