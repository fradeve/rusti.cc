Neo FreeRunner: SHR in testing e nuova Openmoko nel 2009
========================================================

:date: 2009-03-02 19:10:17
:tags: freerunner, gnulinux, openmoko, ubuntu,

.. raw:: html

   <center>

|Neo FreeRunner|

.. raw:: html

   </center>

Questi sono giorni veramente "caldi" per il pianeta del primo cellulare
completamente composto da hardware e software libero, il `Neo FreeRunner`_.

.. _Neo FreeRunner: http://wiki.openmoko.org/wiki/Neo_FreeRunner/it

SHR entra in testing
--------------------

L'`annuncio`_ è stato dato nel pomeriggio di ieri, sul `blog ufficiale`_ 
della distribuzione SHR (**S**\ table **H**\ ybrid **R**\ elease): 
quella che fino a ieri era chiamata SHR-unstable, adesso è "stable", 
e sulla unstable verranno effettuate tutte le modifiche che porteranno, 
tra le altre cose, all'integrazione della nuova versione di Illume 
(Enlightment per dispositivi mobile).

.. _annuncio: http://blog.shr-project.org/2009/03/time-for-testing.html
.. _blog ufficiale: http://blog.shr-project.org

Ciò significa che tutti i proprietari di un Neo FreeRunner che hanno
installato SHR-unstable devono al più presto editare i file dei
repository presenti in ``/etc/opkg``, per evitare che ulteriori
aggiornamenti tramite ``opkg update`` portino ad aggiornare la
distribuzione del proprio palmare ad "unstable", che sarà tale nel vero
senso della parola.

Come si legge nel post, tutte le modifiche nel nuovo rilascio stabile
saranno orientate ad ottenere un sistema operativo quanto più affidabile
possibile. Nel contempo, nella unstable si lavorerà a:

-  riscrittura di ophonekitd in vala
-  aggiornamento all'ultima versione di Enlightment
-  avvio dell'integrazione di opimd
-  sostituzione di udev con mdev
-  basare SHR sulla nuova configurazione minima della distribuzione
   promossa da mickeyl

Mi permetto di ricordare ancora una volta a tutti di cambiare
l'indirizzo dei propri feed di opkg, altrimenti con il prossimo
aggiornamento si passerà alla unstable, che sarà probabilmente
inutilizzabile.

FIC annuncia un nuovo rilascio nel 2009
---------------------------------------

È invece notizia delle 17.00 circa di oggi che alla FIC si sta lavorando
per rilasciare a Maggio la versione stabile di Openmoko 2009. Questa la
roadmap:

-  fine Marzo: verranno completate tutte le caratteristiche ancora in
   sospeso del sistema operativo; le immagini rilasciate saranno
   chiamate Alpha;

-  ad Aprile verranno rilasciate immagini stabili, le Beta, disponibili
   per il testing vero e proprio.

-  entro la fine di Maggio verranno chiusi tutti i bug.

-  entro la seconda settimana di Giugno verrà rilasciata l'immagine
   definitiva che renderà il telefoninux perfettamente funzionante, ad
   un anno esatto dal suo rilascio.

Il team di Openmoko ovviamente punta a rendere partecipe tutta la
comunità di utenti allo sviluppo, bugfixing, testing. È inoltre
suggerito (in maniera abbastanza forte, a dir la verità) di non aprire
altre richieste per nuove features nel sistema, ma ad organizzare e
sviluppare al meglio quelle già presenti.

.. |Neo FreeRunner| image:: http://dl.dropbox.com/u/369614/blog/img_red/2821406019_8bfcc8b2b2.jpg
   :target: http://www.flickr.com/photos/ksyz/2821406019/
