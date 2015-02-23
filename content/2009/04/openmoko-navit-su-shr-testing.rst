Openmoko: Navit su SHR-testing
==============================

:date: 2009-04-07 18:26:28
:tags: gnulinux, gps, navit, openmoko, openstreetmap, ubuntu

.. raw:: html

   <center>

|Navit on Openmoko|

.. raw:: html

   </center>

Questo è un velocissimo post su come installare e rendere perfettamente
funzionante Navit sul Neo FreeRunner con distribuzione SHR-testing. È
anche una valida maniera per prendere una nota, visto che certe cose
tendo a dimenticarle :D

1. installare Navit con il comando ``opkg install navit``; è possibile
   reperire anche la versione svn da `qui`__.

2. di default, Navit presenta una configurazione a dir poco schifosa.
   Per ottenere una configurazione quantomeno accettabile, occorre
   sostituire il file XML che la gestisce. Se non avete voglia di
   indagare le misteriose (ma non troppo) configurazioni di Navit, vi
   consiglio di `scaricare il mio file`__ di configurazione e inserirlo 
   nelle cartelle ``~/.navit`` e ``/usr/share/navit`` (sostituendo 
   eventualmente un navit.xml già presente).

3. installare la libreria libgps17 con il comando "ipkg install
   libgps17" (notare bene, "ipkg" non "opkg"!)

4. andare nella cartella ``/usr/lib`` e dare il comando
   ``ln -s libgps.so.17 libgps.so.16`` per fare in modo che Navit faccia
   riferimento alla libreria giusta

5. scaricare la cartografia di OpenStreetMap per l'Italia da
   `CloudMade`__; al termine del download, estrarre il file compresso

6. spostare sul palmare il file ``italy.navit.bin`` appena estratto,
   nella cartella ``~/.navit``

7. avviare Navit e godersi lo spettacolo del routing completamente
   realizzato con dati, software e hardware LIBERO :D

Per ulteriori info, ecco la `pagina dei tweak`__ di SHR e il 
`wiki di Navit`__. Si ringrazia per l'aiuto `Christ van Willegen`__.

.. |Navit on Openmoko| image:: http://farm4.static.flickr.com/3568/3421188433_2fba0f8fed_o.png
   :target: http://www.flickr.com/photos/leron/3421188433/

.. _qui: http://download.navit-project.org/navit/openmoko/svn/
.. _scaricare il mio file: http://dl.getdropbox.com/u/369614/navit.xml
.. _CloudMade: http://downloads.cloudmade.com/europe/italy#breadcrumbs
.. _pagina dei tweak: http://shr-project.org/trac/wiki/Tweaks>`__ di SHR e il `wiki di Navit <http://wiki.navit-project.org/index.php/Main_Page
.. _Christ van Willegen: https://launchpad.net/%7Ecvwillegen+launchpad
