Title: Samba4 DNS sprint, day 1
Date: 2012-03-26 09:56
Author: Kai Blin
Category: Samba
Tags: DNS, Samba
Slug: samba4-dns-sprint-day-1
Status: published

Samba has it's own small DNS server built in, but it's still lacking a
couple of very nice-to-have features. This week, I'll be trying to get
as many of those in as possible.

There's two big parts here. One is getting forwarder support, so we can
query other name servers on behalf of our clients. The other big item is
getting signed updates to work so windows clients can sign their dynamic
update requests.

My battle plan for this week is:

-   Have a quick stab at a really simple forwarder library, but fall
    back to running dnsmasq with forwarding set up if I don't get
    anywhere until early afternoon today
-   Implement shared secret TSIG updates, to get the TSIG logic sorted
    out
-   Implement TKEY exchanges as specified in RFC2930, to set up the TKEY
    handling infrastructure
-   Make GSS-TSIG work as a possible signing method, so Windows is happy
    finally
-   More work on the forwarder library if needed/I have the time

Let's see how far I'll get, I'll post another update with what I
accomplished today in the evening.
