Title: Solarized Light color scheme for PyCharm 
Date: 2011-04-26 10:20
Modified: 2015-06-20 22:22
Category: misc
Tags: python, PyCharm
Slug: pycharm-colors
Authors: sevas
Summary: Contrast is good


# A matter of taste

[PyCharm](http://www.jetbrains.com/pycharm/ ) 
is a neat development environment, especially if you're
working with [Google App Engine](http://code.google.com/appengine/ )
or [Django](http://www.djangoproject.com/ ). But the default color
scheme is pretty horrendous, and their effort to bundle additional schemes has been less than
fruitful, in my opinion (seriously, [WarmNeon](http://dl.dropbox.com/u/260262/blog/2011-04-26-pycharm-colors/warmneon.png)?)

In addition, I find that using dark color schemes in a environment where a
significant area will stay white and bright is pretty idiotic. And I know
this because I did it for a year.


# Enters Solarized (Light)

Recently, the [Solarized](http://ethanschoonover.com/solarized ) 
color schemes were picked on by
[Hacker News](http://news.ycombinator.com/item?id=2393976 ), and several
people ported it to their favourite editor. However, I could not find
anything good enough for PyCharm (or any other
[IntelliJ](http://www.jetbrains.com/ )-based
IDE). It was often wrong, incomplete, or both. 

This is my attempt to make a coherent theme from these colors, for all
the file types supported by
PyCharm: python, of course, but also HTML, css, YAML, django templates, and so on.

It's just one XML file to download. Grab it on 
[github](https://github.com/sevas/pycharm-color-schemes ).


# Installation

The downloaded file should be copied to the following directory:

* MacOS X: ``~/Library/Preferences/PyCharm10/colors``
* GNU/Linux: ``~/.PyCharm10/config/color``
* Windows Vista and 7: ``C:\Users\$USER\.PyCharm10\config\colors``
* Windows XP: ``C:\Documents and Settings\$USER\.PyCharm10\config\colors``
  


Restart PyCharm, change the editor colors in the settings, and you're gold.


# Final note

I try not to be a typography nerd or anything, but I do like when
things look nice.

Because I mainly use PyCharm on MacOS X, the font used 
is Menlo. This font ships with OS X, but is not likely to be on your
Windows or Linux computer.

On modern Windows systems, tasteful people use
[Consolas](http://en.wikipedia.org/wiki/Consolas ) (I know I do.)
On a GNU/Linux box, you're probably good with the default monospace font
shipping with your desktop environment.



But stay away from Courier New.
