Title: Samba4 DNS sprint, day 2
Date: 2012-03-27 07:12
Author: Kai Blin
Category: Samba
Tags: DNS, Samba
Slug: samba4-dns-sprint-day-2
Status: published

Ok, so I cheated a bit and kept poking at the DNS forwarder code a bit
more yesterday after posting my summary. I didn't quite get anywhere
final before I went to bed, but this morning, while waiting for my
coffee to run through the machine, I got this thing set up. I now can
forward requests the internal server doesn't feel responsible for to
another DNS server and get the reply back to the client. :) It's not
quite production-ready code, but it sure works good enough to switch my
DNS settings on my development machine to use Samba DNS.

That makes today TSIG-day. Time to re-read RFC2845 and see if I can get
this implemented in my test client.
