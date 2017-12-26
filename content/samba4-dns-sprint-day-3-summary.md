Title: Samba4 DNS sprint, day 3 summary
Date: 2012-03-29 06:04
Author: Kai Blin
Category: Samba
Tags: DNS, Samba
Slug: samba4-dns-sprint-day-3-summary
Status: published

Some progress on the TSIG front, but I'm stuck with the exact signing
method for a packet.
For some reason dig and I disagree on what the HMAC-MD5 of a specific
query should be. [The RFC](http://www.ietf.org/rfc/rfc2845.txt) is a bit
vague, and the BIND code of that area seems to be in assembler. (Ok,
it's C, but their coding conventions differ so much from ours that I
probably have to spend a week getting my brain to adjust to that)

So I'm not continuing on hmac-md5 support, but will instead look at
GSS-TSIG directly today. That's the must-have feature, and the whole
week would be wasted if I didn't get *that* in.

TL;DR: HMAC-MD5-TSIG stupid, working on GSS-TSIG now.
