Alex Zahang: Openmoko Multi-boot su A2100 da scheda SD
======================================================

:date: 2007-10-22 22:44:38
:tags: kernel, openmoko

Un felice annuncio di Alex Zhang sul suo `blog`_
ha sconvolto la comunità Openmoko più di una decina di giorni fa: è
finalmente disponibile il multi-boot a scelta tra Openmoko ed OpenEZX.
Notare bene, non un semplice *dual*-boot, ma *multi*. L'esigenza è nata
dal fatto che Alex non voleva essere costretto a flashare il suo "phone"
(se cosi si può chiamare) ogni volta che aggiornava il kernel. Voleva
fare il boot del kernel dalla scheda MicroSD. Voleva anche mettere un
file come il menu.lst del GRUB nella scheda SD, così da poter
controllare facilmente i parametri del kernel. Il sistema da lui creato
funziona cosi:

1. Carica il :span:`menu.lst|code` dalla scheda MicroSD, e mostra un menù di
   boot, dal quale si possono selezionare i parametri di boot.
2. Carica :span:`zlimage|code` da scheda MicroSD, e ne fa il boot.

Tutto questo è stato testato sul palmare Motorola di Alex... chissà se
il multi-boot sarà disponibile anche su Openmoko!!! Qui sotto, il video
:D

.. youtube:: -QqWIl-_KO4


.. _blog: http://thisvip.wordpress.com/2007/10/05/multi-boot-on-a1200-from-sd-card
