Title: Samba4 DNS sprint, day 2 summary
Date: 2012-03-27 21:08
Author: Kai Blin
Category: Samba
Tags: DNS, Samba
Slug: samba4-dns-sprint-day-2-summary
Status: published

I actually spent my time working out some smaller kinks in the DNS
server that I ran into while using it as the only DNS server on my
development machine. I also started with restructuring my dns processing
code a bit so I can handle TSIGs in a sensible way. I've got dig set up
to send TSIGs with an all-0 hmac key, so for tomorrow I should be ready
to go.

Oh, and I pushed my dns forwarder work to master, and it passed
autobuild. Life is good.
