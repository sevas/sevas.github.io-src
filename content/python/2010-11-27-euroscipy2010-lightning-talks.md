Title: EuroScipy 2010 Lightning Talks
Date: 2010-11-27 10:20
Modified: 2017-06-20 19:30
Category: Python
Tags: euroscipy, python
Slug: euroscipy-2010-lightning-talks
Authors: sevas
Summary: Notes taken during the lightning talks session EuroScipy 2010 conference in Paris

*Notes taken during the lightning talks session EuroScipy 2010
 conference in Paris. Most talks were about presenting a new
 scientific python
 module or software package. This was also an opportunity for the
 authors to make a call for contributions.*
 
 
### [glumpy](http://code.google.com/p/glumpy/)

A lightweight visualization library
based on PyOpenGL and numpy. Does not attempt to replace [Mayavi](http://code.enthought.com/projects/mayavi/) and
serves a different purpose. A nice
way to have fast animations for figures rendered with
[matplotlib](http://matplotlib.sourceforge.net/). 


### [joblib](http://github.com/GaelVaroquaux/joblib)

A lightweight pipelining library.
Syntatic sugar over the [multiprocessing](http://docs.python.org/library/multiprocessing.html) module

### [NPK 2.0](http://abcis.cbs.cnrs.fr/NPK/index.html) 

A nuclear magnetic
resonance processing kernel. The current version uses a Java GUI with
some [Jython](http://www.jython.org/ ) . It does not currently use numpy/scipy, but there is an
ongoing rewrite in that direction.


### fermhub

Multiple notebooks for [SAGE](http://www.sagemath.org/ ). 


### [peewit](http://www.ke.tu-darmstadt.de/resources/peewit)

An agnostic machine learning framework.
Rather than focusing on the actual computations, peewit aims to do the
housekeeping of running the experiments.


### [scikits.learn](http://scikit-learn.sourceforge.net/)

A machine learning library, implements general-purpose ML
algorithms. It has efficient bindings to [libSVM](http://www.csie.ntu.edu.tw/~cjlin/liblinear/ ) 
  and [LibLinear](http://www.csie.ntu.edu.tw/~cjlin/liblinear/). Many
  examples on the site.
  
  
*From the audience : *
> How does it compare to
>  [Orange](http://www.ailab.si/orange/)?
 
Orange is a GUI over many algorithms. It also has many dependencies.
scikits.learn aims to be an easy to install, easy to use API.

> There are many machine learning libraries currently being
> developed. There should be an effort to unify everything.

Author does not disagree.


### RST/Sphinx based thesis authoring tool-chain

This is more a wish than an actual implementation. 
[LaTeX](http://en.wikipedia.org/wiki/LaTeX) has many great features and beautiful typography, for text and
equations, but is too complicated. Any self-respecting scientist won't
use Word to publish her work.

[reStructuredText](http://docutils.sourceforge.net/rst.html ) and 
 [Sphinx](http://sphinx.pocoo.org/ ) fit nicely in the middle of this
spectrum. However, as a tool originally developed for making documentation
and manuals, it currently lacks some basic functionality to author
scientific work. The most critical one being proper support for citations. 

An RST-based presentation tool would also be nice. An audience member
pointed to the [rst2beamer](http://www.agapow.net/software/rst2beamer) package.


*Personal note : It's not RST, but the [markdown](http://daringfireball.net/projects/markdown/)-based
 [showoff](https://github.com/schacon/showoff) presentation system is pretty enjoyable.*




### [uncertainties](http://packages.python.org/uncertainties/)

A python module to handle calculations on numbers with uncertainties. Uses error
propagation theory.



### [upy](https://github.com/friedrichromstedt/upy)

Another python module to handle error propagation and uncertainty in computations.
Uses Gaussian error propagation.


### [SNPedia](http://www.snpedia.com/index.php/SNPedia)

An effort to centralize informations about [SNPs](http://www.snpedia.com/index.php/SNP) (*"snips"*).

For every SNP, SNPedia links to related research papers. The database
is used by the
[Promethease](http://www.snpedia.com/index.php/Promethease ) reporting
tool, which can import data data from genetic testing services like
[23andme](https://www.23andme.com/).

The slides are still available as a [Google Docs presentation](http://tinyurl.com/mydna123).


### Interfacing with instruments for experimental physics

This is call for feedback on how python could help replacing  [Labview](http://www.ni.com/labview/), to interface with
measurements and control hardware used in experimental physics.
Vendors rarely ships a python API. And a GUI tool like Labview does
not shine to run batch experiments, where a script would be great. 


*Questions : *

> Why and when did you leave matlab and labview?

The speaker did not leave matlab. Only the *"nightmare"* (sic) that is Labview.

> If you get a binary vendor DLL, why not use ctypes ?

ctypes works well with DLLs written in C, not so much when they are
written in C++. In that case, you need to write a C wrapper first.


### matplotlib and HTML5/Canvas

As of version 1.0, the popular python plotting library
[matplotlib](http://matplotlib.sourceforge.net/) got a  
[HTML5 Canvas](http://en.wikipedia.org/wiki/Canvas_element) backend.
Really useful for SAGE. A nice step to make [anything with a modern
browser](http://www.apple.com/ipad/) a decent platform for scientific work. 
The 3D plot demo wasn't really convincing though.
