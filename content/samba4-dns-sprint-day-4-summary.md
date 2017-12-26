Title: Samba4 DNS sprint, day 4 summary.
Date: 2012-03-29 23:28
Author: Kai Blin
Category: Samba
Tags: DNS, Samba
Slug: samba4-dns-sprint-day-4-summary
Status: published

I'm still a but stuck with TKEY/TSIG, unfortunately. While looking at
the GSS-TSIG implementation we have in libaddns, I realized that I could
simplify my time handling. That ended up fixing my TSIG issues from
yesterday. That is, I can now correctly generate the client/request side
of a HMAC-MD5 TSIG. The server side still seems broken, at least I can't
get dig to accept my reply signature, and if I query bind the server
reply differs from what I would calculate fore it. Oh well.

I've looked at plain TKEY, but for now it doesn't really seem worth the
effort. So I've decided to work on GSS-TSIG directly instead. I don't
really know how to deal with the Gensec side of this, though, so it's a
bit hard to keep the momentum going for this. I'm beginning to fear that
I won't get this implemented this week. Not because any part of it was
particularly hard, but because there's tons of little things that all
take a couple of minutes. And of course sitting in front of the computer
alone lone ranger style isn't the most fun way to develop software.

For tomorrow, I hope to get a bit more done than today. I'll be working
on a little gss-tsig test utility based on libaddns that I can use to
test my server implementation. That should at least allow me to figure
out what's going on at specific steps. I still might need some help on
the Gensec side.
