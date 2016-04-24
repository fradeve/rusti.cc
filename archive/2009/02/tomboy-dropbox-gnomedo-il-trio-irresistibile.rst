TomBoy + DropBox + GnomeDO, il trio irresistibile
=================================================

:date: 2009-02-24 01:48:16
:tags: dropbox, gnulinux, python, ubuntu

Dopo aver usato per quasi un anno e mezzo `Basket`_, e dopo essere
passato (un anno e mezzo fa) a GNOME da KDE, oggi mi sono finalmente
redento all'irresistibile fascino di
`TomBoy`_, l'arcinoto programma per
prendere note ed appunti sull'ambiente desktop GNOME.

.. _TomBoy: http://projects.gnome.org/tomboy
.. _Basket: http://basket.kde.org

Dando per scontato che lo conosciate tutti, non sto qui a tessere le
lodi del software giallo ed appiccicoso. Invece, proprio oggi ho
ripensato allo storico detto:

*Le persone nel mondo possono essere divise in due categorie: chi ha
perso i dati, e chi li perderà.*

Per carità, il mio laptop (nonché PC principale) gode di ottima salute
anche dopo aver attraversato 3 upgrade di Ubuntu. Pero, sapete com'è...
non si sa mai. E poi in università mi porto dietro l'Asus 901, e mi
piacerebbe avere le mie note TomBoy aggiornate con quelle prese "a
casa". E allora?

Allora, TomBoy offre tre tipi di servizi di sincronizzazione delle note:
uno con sshfs (con FUSE), l'altro con un server WebDAL, ed infine uno
con una cartella locale. Ora, provate a guardarmi in volto: non sono
tipo che mette su un servizio sshfs o un server WebDAL solo per
sincronizzarsi le note sui PC. Invece, sono un affezionato utente
`DropBox`_. Ciò significa che ho creato nella mia dropbox una cartella 
di nome "tomboy" e ho ordinato ad entrambi i TomBoy (quello sul Dell di 
casa e sull'Asus nello zaino) di usarla come cartella di sincronizzazione 
locale delle note. Risultato: note sincronizzate tra i due PC, via internet, 
senza il minimo sforzo!

Infine, un paio di cose: il plugin "Tomboy" di `GnomeDO`_
integra una funzione veloce per creare/modificare/cercare note
all'interno di TomBoy senza staccare le mani dalla tastiera, consiglio
vivamente l'attivazione. Inoltre, TomBoy è estensibile con un plugin che
trovo molto utile, `reminder`_. Questo plugin ha lo scopo di far saltare 
in primo piano la nota in un giorno stabilito dall'utente, in maniera tale 
che l'utente se ne ricordi. Per installarlo, scaricare `questo file`_ ed 
inserirlo nella cartella dei plugin di TomBoy, con il seguente comando da 
terminale (che necessita di password di amministratore):

.. _DropBox: http://www.getdropbox.com
.. _GnomeDO: http://do.davebsd.com/wiki/index.php?title=Main_Page
.. _reminder: http://flukkost.nu/blog/tomboy-reminder
.. _questo file: http://flukkost.nu/tomboy-reminder.dll


.. code-block:: bash

    sudo mv tomboy-reminder.dll /usr/lib/tomboy/addins/

Detto ciò... Buon lavoro!!
