TexLive and ArchLinux
=====================

:date: 2015-11-09 16:00:00
:featured: no
:lang: en
:tags: archlinux, latex

After some troubles with getting :span:`tlmgr|code` to work on ArchLinux, I decided to switch to a more "archist" way to handle my TeXLive installation: :span:`texlive-localmanager-git|code`. Few notes below.

.. code-block:: bash

   yaourt -S texlive-localmanager-git

This will also install :span:`texlive-core|code` package from the Arch's repositories.
To install a new package from CTAN:

.. code-block:: bash

   tllocalmgr install packagename
   sudo texhash

Install a new font
------------------

We will use a dedicated script to install non-free fonts for TexLive:

.. code-block:: bash

   wget https://tug.org/fonts/getnonfreefonts/install-getnonfreefonts
   chmod +x install-getnonfreefonts
   ./install-getnonfreefonts
 
Installing a new font will be as easy as:

.. code-block:: bash

   getnonfreefonts -l
   getnonfreefonts fontname

Dealing with missing font maps
------------------------------

Sometimes, we may get something like this:

.. code-block:: bash

   !pdfTeX error: /usr/texbin/pdflatex (file mt2exf): Font mt2exf at 2400 not found

In the same error message, some lines above, we may have the directory used to get the :span:`pdftex.map|code`. In my case, this pointed to the local dir created by :span:`tllocalmanager|code`:

.. code-block:: bash

   /home/fradeve/.texlive/texmf-var/fonts/map/pdftex/updmap
   mv pdftex.map pdftex_bak.map

This will force TeX to use the global map instead of the local map. To refresh the maps:

.. code-block:: bash

   sudo mktexlsr
   sudo updmap
   sudo updmap-sys

