St, Solarized, custom fonts
===========================

:date: 2016-09-04 16:00:00
:featured: no
:lang: en
:tags: tools
:headline: A minimal Solarized terminal

I have quite happily been using Suckless' St terminal for a while, but when I
recently got a Mac with a retina display and ArchLinux, any effort to make the
terminal font bigger has been not very productive, until today.

Get the sourcecode of the Solarized version of the St terminal with Powerline
support:

.. code-block:: bash

    st-solarized-powerline
   
Edit to set the right font and size:

.. code-block:: bash

    cd st-solarized-powerline/src
    vim config.h

.. code-block:: c

    /* static char font[] = "DejaVu Sans Mono for Powerline:pixelsize=12:antialias=true"; */

    static char font[] = "DejaVu Sans Mono for Powerline:pixelsize=14:antialias=true";

Build the modified package and install it:

.. code-block:: bash

    cd ..
    makepkg
    sudo pacman -U st-solarized-powerline-0.6-1-x86_64.pkg.tar.xz

