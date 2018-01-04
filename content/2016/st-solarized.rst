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

This guide is based on the ArchLinux version of the package, but it can be
easily used on any distro.

Get the sourcecode of the Solarized version of the St terminal with Powerline
support:

.. code-block:: bash

    yaourt -G st-solarized-powerline
   
Edit to set the right font and size:

.. code-block:: bash

    cd st-solarized-powerline
    vim config.h

.. code-block:: c

    /* static char font[] = "DejaVu Sans Mono for Powerline:pixelsize=16:antialias=true"; */

    static char font[] = "DejaVu Sans Mono for Powerline:pixelsize=14:antialias=true";


Ignore the checksum of the file, replacing the md5sum of ``config.h`` with
``SKIP`` in ``md5sums``.

Build the modified package and install it:

.. code-block:: bash

    makepkg
    sudo pacman -U st-solarized-powerline-0.6-1-x86_64.pkg.tar.xz

