---
layout: post
title: Managing multiple python installations on Mac OS X - A  minor update
---



### Digression: Enthought Python Distribution considered awesome

The main reason I made this program is because, alongside the
Apple-supplied python and the vanilla pythons from [python.org](http://python.org), I use a 
[pretty badass python distribution](http://www.enthought.com/products/epd.php)
dedicated to scientific work. 

Anyone who ever lost an afternoon trying to install
[numpy and scipy](http://www.scipy.org/Installing_SciPy ) from sources
should make herself a favor and try this instead.
It's not merely a collection of compiled packages. It's a damn platform.

You should be thankful for this.
I know I am. 
 

### Alright, alright. So what's new?


Well, the program described in
[my latest entry](/2011/06/14/multiple-python-osx.html ) suffered from
at least one major flaw: it did not detect the 64bits builds of EPD.


The reason for this is that they are installed under yet another directory (namely, ``/Library/Frameworks/EPD64.framework``.)
 
That's it.
It's still a really simple program, but serves its purpose.
Grab it on [github](https://github.com/sevas/dotfiles/blob/0.2.1/scripts/update_python_switchers.py ).



### What's next?

I realize that this is a really simple and, perhaps, clumsy way to
switch between multiple python runtimes. 

Ideally, this should be built
into the OS. For every interpreter or compiler you might want
concurrent versions of. Something along the lines of the
'alternatives' system you can find in some linux distros.

But for now, that's all there is. 



Priorities.
