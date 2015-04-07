Compiling VIM with Breakindent patch
====================================

:date: 2012-09-10 10:00:00
:featured: yes
:lang: en
:modified: 2015-04-08
:tags: vim

Update: this guide is not useful anymore, since Breakindent has been
`integrated`_ in Vim. Enjoy!


`VIM Breakindent patch`_'s
story is quite frustrating, since it is a nice piece of code (really
useful when you work with tag-like structured coding languages, e.g.
LaTeX) but it has been `never integrated in standard VIM`_
due to some instability issues. In 2012, you always have to patch and
compile VIM manually to get it working. This guide has been tested on
Ubuntu 12.04 (many thanks to
`ephemient`_ for pointing out the correct procedure, as a result of a
`discussion`_ on Stackexchange).

Get the sources:

.. code-block:: bash

   sudo apt-get sources vim

Download VIM breakindent patch file:

.. code-block:: bash

   wget

Set permissions on the sources and move the patch into the set of Debian
patches:

.. code-block:: bash

   cd vim-7.3.429
   sudo chmod u=rw,g=r,o=r ../vim-breakindent.patch
   sudo cp ../vim-breakindent.patch debian/patches/debian/.

Add one new entry in ``debian/changelog``, bumping version from
``vim_7.3.429-2ubuntu2.1`` to ``vim_7.3.429-2ubuntu2.2``.

Add ``debian/vim-breakindent.patch`` at the end of
``debian/patches/series``

Generate new source package

.. code-block:: bash

   sudo pdebuild

Compile the new ``.dsc``:

.. code-block:: bash

   sudo pbuilder build vim_7.3.429-2ubuntu2.2.dsc

Install new debs:

.. code-block:: bash

   sudo dpkg -i /var/cache/pbuilder/result/*.deb


Debian package
~~~~~~~~~~~~~~

As I write, `Eudoxos`_ is maintaining a `Launchpad repository`_ with Vim
breakindent-patched compiled ``.deb`` packages.

.. _VIM Breakindent patch: https://retracile.net/wiki/VimBreakIndent
.. _never integrated in standard VIM: https://groups.google.com/forum/#!msg/vim_dev/VdMLVy_ZS2I/KsRNkREcBhgJ
.. _ephemient: http://stackoverflow.com/users/20713/ephemient
.. _discussion: http://stackoverflow.com/questions/10998516/compiling-vim-with-breakindent-patch
.. _Eudoxos: http://stackoverflow.com/users/761090/eudoxos
.. _Launchpad repository: https://launchpad.net/~eudoxos/+archive/ppa
.. _integrated: https://retracile.net/blog/2014/07/18/18.00
