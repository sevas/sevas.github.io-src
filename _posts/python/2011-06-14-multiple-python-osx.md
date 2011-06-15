---
layout: post
title: Managing multiple python installations on Mac OS X
---


### There is a party in my OSX

And all the pythons got invited.


    $ ls -l /System/Library/Frameworks/Python.framework/Versions/
    total 8
    drwxr-xr-x   8 root  wheel  272 Mar 29 19:20 2.3
    drwxr-xr-x  12 root  wheel  408 Apr 11 13:48 2.5
    drwxr-xr-x  12 root  wheel  408 Apr 11 13:48 2.6
    lrwxr-xr-x   1 root  wheel    3 Mar 29 19:20 Current -> 2.6


    $ ls -l /Library/Frameworks/Python.framework/Versions/
    total 8
    drwxrwxr-x  10 root  admin  340 Nov 30  2010 2.7
    drwxrwxr-x   9 root  admin  306 Nov 30  2010 3.1
    drwxrwxr-x   9 root  admin  306 Feb 20 20:14 3.2
    drwxrwxr-x  19 root  admin  646 Jan 15 19:26 6.3
    lrwxr-xr-x   1 root  admin    3 Jan 15 19:21 Current -> 6.3


Alright.



### Fast switching

What I want, is an easy way to switch between all these different
python installations from my shell. For instance, going from the OSX
python 2.6 installation to python 3.1:

    $ select_macpython31    
    Setting environment for MacPython 3.1

    $ python3
    Python 3.1.3 (r313:86882M, Nov 30 2010, 09:55:56) 
    [GCC 4.0.1 (Apple Inc. build 5494)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> exit()
    

And then, I could switch to the new python 3.2 you just got from [python.org](http://www.python.org/download/):


    $ select_macpython32
    Setting environment for MacPython 3.2

    $ python3    
    Python 3.2 (r32:88452, Feb 20 2011, 11:12:31) 
    [GCC 4.2.1 (Apple Inc. build 5664)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 


That would be nice. And that's exactly what this page is about.


### Show me the code

What we need is a bunch of bash functions to update the ``PATH``
environment variable, so that the selected python installation is the
default. If you had 3 pythons, it would look like this:

<script src="https://gist.github.com/1021380.js?file=gistfile1.bash"> </script>
<br/>

But because I'm lazy, I don't want to write a switching
function everytime I add a python, I made
[this](https://github.com/sevas/dotfiles/blob/0.1/scripts/update_python_switchers.py)
instead. 

This script looks in the directories where python is usually installed,
detects all the versions, and generates a ``.python_switchers.sh``
file. This file will have all the switching functions.

If you download and run it, you should see something like this:

    $ update_python_switchers.py 
    Using generic prompt
    Adding System Python 2.3
    Adding System Python 2.5
    Adding System Python 2.6
    Adding MacPython 2.7
    Adding MacPython 3.1
    Adding MacPython 3.2
    Adding EPD 6.3
    Saved python switcher bash functions to /Users/sevas/.python_switchers.sh


Next, you will need to add this to your ``$HOME/.bash_profile``:

<script src="https://gist.github.com/1021386.js?file=gistfile1.bash"> </script>
<br/>

Now you will be able to use the switching functions from your shell,
like I showed earlier





### What have you done to my prompt?

If you read until now, maybe you tried it, and noticed your prompt was different.
The reason is that the generated switchers actually look more like this:

<script src="https://gist.github.com/1021391.js?file=gistfile1.bash"> </script>
<br/>

This is because I find it useful to know at a glance in which environment
I'm working, so I modified the ``PS1`` variable accordingly. 



### Fancy colors for fancy people

If you run:

     $ update_python_switchers.py --use-fancy-prompt
     
you will get my carefully crafted prompt with fancy colors.  

This is how it looks:

![Alt Text](http://dl.dropbox.com/u/260262/blog/2011-06-14/fancy_prompt.png ) 


You will find the color variables in my
[``.bash_profile``](https://github.com/sevas/dotfiles/blob/master/.bash_profile
) file. 


If you already have a custom prompt, just go ahead and edit the function
generation template in ``update_python_switchers.py`` to your liking. 

And if you don't like it, well, it's pretty easy to remove anyway.
This could obviously be improved. Maybe I will.


### You should use [virtualenv](http://www.virtualenv.org/en/latest/index.html ) and [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/ ) 


Well I do. These switchers are working on another level.
virtualenv is mostly about having many concurrent ``site-packages`` directories.



### One more thing

This script requires the [``argparse``](http://code.google.com/p/argparse/) module, so you should go
ahead and install it with:

    $ easy_install argparse
    
if it's not part of your python, which will be the case if you're not
running python 2.7 or 3.2.
