Title: Python Regexes: Named Groups. Cool Bananas
Date: 2011-12-08 08:55
Author: Kai Blin
Tags: antiSMASH, BioPython, GenBank, python, regex
Slug: python-regexes-named-groups-cool-bananas
Status: published

I'm currently writing a Python parser for GenBank files. I know
BioPython has one, and it doesn't even suck, but BioPython requires a
bunch of C extensions, so I can't go and just ship it with my Python
application.

So I'm creating a BioPython-compatible API for the classes that I need
for antiSMASH, without the dependency tail BioPython forces on me.

Having contributed to BioPerl before, I do like to use regular
expressions for token-based parsers, especially as I'm not too fond of
lexers in Python.

Now, a GenBank header is a peculiar thing that stems from the punch card
ages, with a fixed-width format. Unfortunately, at some point that
format changed, and things moved around. And there's a ton of programs
out there that produce GenBank files that are slightly off. So parsing
the header using a token-based approach seems like a good thing.

Now, let's look at the first line. That has a bunch of interesting
information.

```
LOCUS       SCU49845     5028 bp    DNA             PLN       21-JUN-1999
```

The 'LOCUS' tag explains what this line is about, then there's the
accession number for the sequence, the length of the sequence, the type
of the molecule, some classification where the sequence comes from, and
the date the sequence last saw a major update.

The regex to parse this is pretty straightforward (yeah, right):

```
LOCUS\s+([\w.]+)\s+(\d+)\sbp\s(ss-|ds-|ms-|\s{3,3})\(S{2,4})\s+(linear\s\s|circular|\s{7,7})\s+(\w{3,3})\s+(\d\d-\w{3,3}-\d{4,4})
```

Incidently, this is a great example for why people dislike regular
expressions.

Now, in both Perl and Python, there's a way to define verbose regular
expressions, so you can restate the regular expression as:

```p
LOCUS\s+        # Header line starts with LOCUS tag followed by multiple spaces
(               # accession number regex:
  [\w.]+        # any alphanumeric character or '.'
)
\s+             # skip over whitespace
(               # sequence length
  \d+           # digits only
)\sbp\s         # skip ' bp ' string
(               # single, double or mixed stranded or nothing
  ss-|ds-|ms-|\s{3,3} # can be all spaces
)
(               # Molecule type DNA, RNA, rRNA, mRNA, uRNA
  \S{2,4}
)
\s+
(               # linear, circular or seven spaces
  linear|circular|\s{7,7}
)\s+
(               # division code, three characters
 \w{3,3}
)
\s+
(               # date, in dd-MMM-yyyy
  \d\d-\w{3,3}-\d{4,4}
)
```

This is already pretty decent, but Python can do one better. With the
current version of the regex, I need to remember that the molecule type
is the 4th group, so match.group(3) will be what I'm looking for. Python
decided to extend the Perl extension syntax a bit more, to add named
groups. With `?P<name>` you can name groups. and then call
match.group('name') to access them later. So the final version of the
parser regex turns into

```
LOCUS\s+        # Header line starts with LOCUS tag followed by multiple spaces
(?P<accession>  # accession number regex:
  [\w.]+        # any alphanumeric character or '.'
)
\s+             # skip over whitespace
(?P<length>     # sequence length
  \d+           # digits only
)\sbp\s         # skip ' bp ' string
(?P<stranded>   # single, double or mixed stranded or nothing
  ss-|ds-|ms-|\s{3,3} # can be all spaces
)
(?P<molecule>   # Molecule type DNA, RNA, rRNA, mRNA, uRNA
  \S{2,4}
)
\s+
(?P<formation>  # linear, circular or seven spaces
  linear|circular|\s{7,7}
)s+
(?P<division>   # division code, three characters
 \w{3,3}
)
\s+
(?P<date>       # date, in dd-MMM-yyyy
  \d\d-\w{3,3}-\d{4,4}
)
```

and you can use speaking names to access the group's contents later.
Great to make the code more readable. Combined with a bunch of tests,
that should stay maintainable.
