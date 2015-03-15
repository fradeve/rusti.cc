Ottenere immagini planetarie di OpenStreetMap con Marble
========================================================

:date: 2009-02-19 11:06:15
:tags: gnulinux, openstreetmap, python, ubuntu, wikipedia

Ogni blog ha il suo post "tecnico", oggi è il mio turno... in questa
guida vedremo come catturare immagini ad alta risoluzione del nostro
pianeta, su cui è stata applicata come
`texture`_ la cartografia di OpenStreetMap. La guida non è farina 
nel mio sacco, ma è stata allegramente tradotta dal `sito ufficiale`_
del progetto. Le immagini possono essere utili per presentazioni, talk,
diapositive ecc. Dico questo perché la risoluzione del file è a
discrezione dell'utente, anche molto alta, ma la qualità dell'immagine
non è generalmente buona per la stampa. Purtroppo non ho ancora avuto
tempo di testare la guida.

.. _texture: http://it.wikipedia.org/wiki/Texture
.. _sito ufficiale: http://wiki.openstreetmap.org/wiki/User:Frederik_Ramm/Creating_Very_Large_Marble_Images

.. raw:: html

   <center>

|image0|

.. raw:: html

   </center>

-  Diventare root

   ::

       :::bash
       su

-  Presumendo di aver già installato Marble (peraltro già presente nei
   repository di Ubuntu 8.10), modificare il file
   ``/usr/share/kde4/apps/marble/data/maps/earth/openstreetmap/openstreetmap.dgml``
   cambiando la riga

   ::

       :::xml
       <downloadUrl protocol="http" host="a.tile.openstreetmap.org" path="/"  />

in

::

        :::xml
        <downloadUrl protocol="http" host="a.tile.openstreetmap.org" path="/"  />

ed eliminando tutte le altre due righe "downloadUrl".

-  Installare i pacchetti necessari a simulare un desktop gigante:

   ::

       :::bash
       apt-get install xvfb x11xvnc xvnc4viewer imagemagick netpbm
       mkdir /tmp/marblefb

-  Nel comando che segue, selezioniamo la risoluzione che ci interessa
   ottenere:

   ::

       :::bash
       Xvfb -ac :1 -fbdir /tmp/marblefb -screen 0 4096x4096x24
       x11vnc -scale .5 -display :1

-  Apriamo una finestra vuota e visualizziamo Marble, sostituendo nel
   secondo comando qualsiasi risoluzione abbiamo scelto di adottare:

   ::

       :::bash
       vncviewer localhost :0
       DISPLAY=:1 marble -geometry 4096x4096+0+0

-  Adesso giostrate con Marble fino a quando la figura ottenuta non vi
   piacerà, quindi date il comando per estrapolare l'immagine, che verrà
   salvata in ``/tmp/marble.png``:

   ::

       :::bash
       xwdtopnm < /tmp/marblefb/Xvfb_screen0 | pnmtopng > /tmp/marble.png

Se ne avete voglia, inviatemi pure i vostri screens *planetari*!

.. |image0| image:: http://dl.dropbox.com/u/369614/blog/img_red/marble.jpg
