SPyQR: dalla comunità pugliese di Ubuntu-it una GUI per qrencode
================================================================

:date: 2010-02-08 23:24:50
:tags: ubuntu, puglia, gnulinux,

.. raw:: html

   <center>

|image0|

.. raw:: html

   </center>

Ebbene si, è disponibile direttamente dai PPA l'invenzione che tutti noi
stavamo aspettando! SPyQR, un'interfaccia grafica per le librerie open
source che generano il codici QR! Pasquale Ambrosini aka Pakizip,
programmatore emergente (nonché mapper di OpenStreetMap e amico) ha
appena rilasciato SpyQR, che consente, attraverso interfaccia grafica
user fiendly scritta in pyGTK, di generare QR codes in maniera facile ed
intuitiva.

Caratteristiche:

-  Supporta più di 4000 caratteri

-  Possibilità di aumentare la grandezza di output del QRCode

-  Possibilità di scegliere dove salvare il QRCode

Per aggiungere il repository alla propria lista, dare il seguente
comando:

::

    :::bash
    sudo add-apt-repository ppa:pasquale-ambrosini/spyqr

Quindi aggiornare i propri repository ed installare il pacchetto con

::

    :::bash
    sudo apt-get install spyqr

È ancora in fase di test, per segnalare bug, malfunzionamenti o
suggerimenti non esitate a contattarlo (pasquale.ambrosini@gmail.com).

Buon coding!!

.. |image0| image:: http://dl.dropbox.com/u/369614/blog/img_red/spqr2.png
