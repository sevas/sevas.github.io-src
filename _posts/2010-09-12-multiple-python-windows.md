---
layout: post
title: Managing mutliple python installations on Windows
---


# Problem

So sometimes, it might be good idea to keep several sandboxed python installations.

Here are some examples where such scenario may occur:
* My default python installation is 2.7
* The [Ogre3D bindings](http://www.pythonogre.com/) are only available for Python2.6 at the moment
* I want to keep my [EPD](http://www.enthought.com/products/epd.php) distribution clean
* What about using python3 alongside everything else?


# A Solution

First, you need a `.bat` file that will set various environment
variables. Here is such a file, targetted at my EPD installation,
which is installed in `C:\Python26_EPD622`:

<script src="http://gist.github.com/575989.js?file=epd62.bat"></script>

Next, we will create a shortcut to a windows command prompt that will
automatically call that script, and setup your environmnent.

Locate the folder containing the original *Command Prompt* shortcut.
> C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessories

Copy it, and rename it, for example to `Python26 (EPD 6.2) Command Prompt`.
Rigth click on it, select *Properties*. This should appear:

![](http://dl.dropbox.com/u/260262/blog/2010-09-12/lnk_before.png)

Change the target to:
> %comspec% /k ""c:\path\to\epd62.bat""

and click `Ok`. Notice the two pairs of double quotes.


![](http://dl.dropbox.com/u/260262/blog/2010-09-12/lnk_after.png)

You can now move this shortcut wherever you see fit. You can keep it
in the start menu, create a special start menu folder for all your
python prompts, move it to the quicklaunch bar, and so on.

Once this is done, you can now:

* Launch a (i)python shell
* Install packages with `easy_install` or `pip`
* Launch any binary third party tool shipped with your python distribution

![](http://dl.dropbox.com/u/260262/blog/2010-09-12/success.png)


Repeat for every python installation.

# Final note

This is not a mean to register several python distribution with your IDE.
Any decent python IDE, such as [Pydev](http://pydev.org/) for eclipse or
[PyCharm](http://www.jetbrains.com/pycharm/) let you register several
python interpreters.

