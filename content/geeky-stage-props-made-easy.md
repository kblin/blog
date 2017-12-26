Title: Geeky stage props made easy
Date: 2011-06-19 20:29
Author: Kai Blin
Category: Tinkering
Tags: arduino, brechtbautheater, hardware, props
Slug: geeky-stage-props-made-easy
Status: published

Currently I'm involved in building the stage and props for an amateur
theater, the [Brechtbau Theater](http://www.brechtbautheater.de/) at my
university. We're currently preparing for an Agatha Cristie play, "And
then there were none". As a great opportunity, we are able to perform
this piece in the city's professional theater, the [Landestheater
Tübingen
(LTT)](http://www.landestheater-tuebingen.de/events/view/id/46131/date/1311026400).

Needless to say, we're really excited about this. Of course having to
build a stage for a 300 seat theater is a bit different to building a
stage for the 80 seat theater we've got at university. Also, we only
have about four hours to set up the stage, and after the last night, we
have to clear out immediately. While the way to build a modular stage
design probably is worth a blog post on it's own, I want to talk about
the electronics behind stage a bit today.

Without wanting to spoil some of the surprises we have in store for our
audience, we're working on a stage design with lots of big cogwheels and
other moving parts. We will power some of these with the cheapest and
most readily available power source we have available: actors. But some
of the stage has parts that are just out of reach, or need to be
positioned more precisely. For this, I'm currently planning to use a
combination of stepper motors and hobby servos, run by an Arduino Uno.


I'm still heavy in the prototyping stage, but I just wanted to share my
discovery on how easy it is to do stuff like this with the Arduino. My
current test setup looks a bit like

<div style="text-align:center" markdown="1">
[![Arduino setup]({filename}/images/setup.jpg){width="60%"}]({filename}/images/setup.jpg)
</div>

Using an L293D (left) and an L293NE (right) IC, I'm running two Trinamic
bipolar steppers, and I'm also controlling four servo motors. For making
all of these move forwards and backwards, I had to write about 50 lines
of code, including whitespace and some comments. Arguably, moving a
couple of motors forward and backward in a loop isn't that intersting,
but the amout of work the Arduino default libraries already take care of
is just great.

Next, I'll have to figure out how to build a lamellar transport belt and
move it with one of the steppers, while converting the circular movement
of the other stepper to a linear movement. Never played with elaborate
hardware stuff before, this is fun.
