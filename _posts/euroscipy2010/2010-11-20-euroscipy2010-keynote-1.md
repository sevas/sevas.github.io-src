---
layout: post
title: EuroScipy 2010 - Advanced Teaching and Research with Python 
---


*These are some notes taken during the keynote talk of Prof.
[Hans Petter Langtangen](http://vefur.simula.no/~hpl/) at the
EuroScipy 2010 conference in Paris.*



## Teaching science and engineering


### Case study : University of Oslo, Norway

Mathematics and engineering sciences should be taught with a very
hands-on approach. Students need to launch simulations, tinker
with parameters, vizualize outcomes from day one. This is the
future of science education.

Undergrads mathematics and mathematical modeling courses were recently
redesigned at University of Oslo.
The current, revamped cursus includes calculus, numerical calculus,
scientific programming using python, 
vector calculus and linear algebra, mechanics with simulation.

There is a very strong focus on experimentation.
An example of first year project is the numerical simulation of a
pendulum with friction. This is fairly advanced material that wasn't
covered by previous undergrad courses. This approach was really well
received by the students.



### Why python is the language of choice ?

Python is a great tool for quick prototyping, unlike Java. It also is a
general purpose programming language, suitable for many kinds of computing tasks,
unlike matlab.
In previous years, students were doing matlab after an introduction
course with Java. It was hard to establish a connection between what
was learned in the programming course, and all the apparent magic going on in matlab. 
Python offers a natural transition from matlab-style flat
scripts, to full fledged object-oriented applications with complex
GUIs, data processing and results reporting.

Python is executable pseudo-code. This helps students focus on the problem
to solve, rather than deal with the syntax. Producing an algorithmic
solution improves how student effectively understands the material. This
is what should matter first.



### Fighting deployment hell

One of the biggest problem with a python scientific stack, is the pain involved
when deploying an application with its dependencies, or just
setting up the right development environment for scientific computing.
There are several distributions ([Enthought Python Distribution](http://www.enthought.com/products/epd.php), [python(x,y)](http://www.pythonxy.com/), [SAGE](http://www.sagemath.org/), linux distribution
package systems, ...). This is a lot to maintain in parallel.
Throw in some C and FORTRAN extensions (which are ubiquituous as soon
as you're using python for science) and you're in for hell of a
ride.

To prevent spending too much time on this, the course officially
supports Ubuntu as the only platform (dualboot or
[virtualbox](http://www.virtualbox.org/)). Students can then get all
the required software through a dedicated package repository (e.g. `apt-get install
mycourse`).

Install parties are organized to help beginners get their setup ready.
Experience shows that people are more happy with this approach.

People who don't like Ubuntu will need to figure out the installation by themselves.



## Research & High Performance Computing


### *"Python is slow"*

Addressing the myth: it turns out all you really need
is to compile your number crunching loops and call it a day. Popular strategies for
this includes [cython](http://www.cython.org/) and
[scipy.weave](http://www.scipy.org/Weave). 



### Large scale projects

Python is not just suitable for small school projects. 
[fenics](http://www.fenicsproject.org), [pyadh](https://adh.usace.army.mil/pyadh/),
[fipy](http://www.ctcms.nist.gov/fipy/), [hedge](http://mathema.tician.de/software/hedge),
[gpaw](https://wiki.fysik.dtu.dk/gpaw/),
[pNbody](http://obswww.unige.ch/~revaz/pNbody/) are examples of
python-based software packages aimed at solving real-world engineering
problems. 



### Parallel computing

Scientists often need to launch long computations on computer
clusters. 
[mpi4py](http://mpi4py.scipy.org/docs/usrman/index.html) are python
bindings for the popular message passing library
[MPI](http://www.mpi-forum.org/), which is one way to enable
exploitation of multiprocessor architectures.

A typical scenario would be using python to control the pipeline, set
the simulation parameters, and let the high-performance, often legacy FORTRAN code, do
the number crunching. Numpy and scipy can also be used for
that kind of heavy lifting.


### Further improving the adoption of python in science

One of the strong points of matlab is the ubiquity of code samples
available. We need that for the python scientific stack. 

Unification of interfaces between
ODE solvers, linear algebra packages, visualization packages is much
needed.

There are still skeptics about whether a "scripting language" can be a
fitting choice for high-performance computations. Finding and referencing
real-world examples in which python was succesfully used helps. The
bottom line being that one doesn't need to write the whole application
in C or C++ for it to be fast.


