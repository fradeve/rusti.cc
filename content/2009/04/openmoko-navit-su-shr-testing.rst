Openmoko: Navit su SHR-testing
==============================

:date: 2009-04-07 18:26:28
:tags: gnulinux, gps, navit, openmoko, openstreetmap, ubuntu


Questo è un velocissimo post su come installare e rendere perfettamente
funzionante Navit sul Neo FreeRunner con distribuzione SHR-testing. È
anche una valida maniera per prendere una nota, visto che certe cose
tendo a dimenticarle :D

1. installare Navit con il comando :span:`opkg install navit|code`; è possibile
   reperire anche la versione svn da `qui`_.

2. di default, Navit presenta una configurazione a dir poco schifosa.
   Per ottenere una configurazione quantomeno accettabile, occorre
   sostituire il file XML che la gestisce. Se non avete voglia di
   indagare le misteriose (ma non troppo) configurazioni di Navit, vi
   consiglio di `scaricare il mio file`_ di configurazione e inserirlo 
   nelle cartelle :span:`~/.navit|code` e :span:`/usr/share/navit|code` (sostituendo 
   eventualmente un navit.xml già presente).

3. installare la libreria libgps17 con il comando "ipkg install
   libgps17" (notare bene, "ipkg" non "opkg"!)

4. andare nella cartella :span:`/usr/lib|code` e dare il comando
   :span:`ln -s libgps.so.17 libgps.so.16|code` per fare in modo che Navit faccia
   riferimento alla libreria giusta

5. scaricare la cartografia di OpenStreetMap per l'Italia da
   `CloudMade`_; al termine del download, estrarre il file compresso

6. spostare sul palmare il file :span:`italy.navit.bin|code` appena estratto,
   nella cartella :span:`~/.navit|code`

7. avviare Navit e godersi lo spettacolo del routing completamente
   realizzato con dati, software e hardware LIBERO :D

Per ulteriori info, ecco la `pagina dei tweak`_ di SHR e il 
wiki di Navit. Si ringrazia per l'aiuto `Christ van Willegen`_.

.. _qui: http://download.navit-project.org/navit/openmoko/svn/
.. _scaricare il mio file: http://rusti.cc/static/navit.xml
.. _CloudMade: http://downloads.cloudmade.com/europe/italy#breadcrumbs
.. _pagina dei tweak: http://shr-project.org/trac/wiki/Tweaks>`_ di SHR e il `wiki di Navit <http://wiki.navit-project.org/index.php/Main_Page
.. _Christ van Willegen: https://launchpad.net/%7Ecvwillegen+launchpad
