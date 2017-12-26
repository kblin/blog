Title: Model vs. Reality
Date: 2013-03-21 07:34
Author: Kai Blin
Tags: nontechnical, rant, science
Slug: model-vs-reality
Status: published

My twitter feed currently is ablaze with discussions about sexism in
[tech](http://ivory.idyll.org/blog/pycon-2013-and-codes-of-conduct.html)
and
[science](http://www.guardian.co.uk/science/us-news-blog/2013/mar/20/i-love-science-woman-facbook).
As a member of the social group that goes through life with difficulty
set to "easy", of course none of this has happened to me. I don't know
what it feels like to go to a conference where people constantly comment
on my looks or gender instead of my work. As I lack the experience, and
I also lack solid data, I don't want to write about that in this post.

However, as a computational biologist, I do have some experience with
model vs. reality clashes, and I believe that might be the reason why
people on the internet are surprised about the existence of female
scientists or engineers. People also tend to get upset when they realize
their mental model doesn't match reality, which might explain some of
the emotional upset males show in the discussions I mentioned in the
first paragraph.

Now, instead of taking the easy way out and blaming this on [internet
stupidity](http://ars.userfriendly.org/cartoons/?id=19991114), I want to
put another theory out there. **People often don't get statistics.**
In my day-to-day work, I frequently run into publications where there is
at best a [loose correlation between the data and the model supposed to
explain said
data](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0013060).
And I believe that's what is happening here as well.

So by the time-proven method of pulling data out of my hat, I propose
that when you graph the "ability to do science" against the sex
chromosome layout of individuals, you'll get something similar to this:

------------

<div style="text-align:center" markdown="1">
[![Data]({filename}/images/gender_science_data.png){width="50%"}]({filename}/images/gender_science_data.png)
</div>

------------

So far, so good. The problem is that despite "ability to do science" not
clustering for any sane definition of a cluster, the mental model of
many people seems to look like this:

------------

<div style="text-align:center" markdown="1">
[![A model fitting the data?]({filename}/images/gender_science_model.png){width="50%"}]({filename}/images/gender_science_model.png)
</div>

------------

If you have settled for a given model, there is quite some inertia to
stay with your chosen model, even if the data doesn't back it up. If
reality dares to come up with conflicting data, blame reality! The
ripples of a lot of mental models running into reality hard are
currently washing over my twitter feed. The inertia of sticking with
your model makes it hard to realize it, but in the end **when reality
and your model disagree, it is easier to change your model**. In my
example graph, a lot of lines I could put in there would likely have a
similar quadratic error. To me, this is a warning sign that my model
probably is bad. In the example, the conclusion should be that not only
"women are bad at science, men are great" (the red line) is wrong, but
also every other attempt at constructing a linear correlation between
the parameters. "Ability to do science" and "sex chromosome layout" are
orthogonal characteristics\*. Also, why is there an arrow on the x axis,
when we're looking at discrete parameters?

<small>\* According to my hat, of course.</small>
