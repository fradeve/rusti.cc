Installare Flickrfs su Ubuntu 8.10 Intrepid Ibex
================================================

:date: 2008-12-09 15:22:23
:tags: gnulinux, python, ubuntu,

Forse tra di voi ci sono moltissimi utenti
`Flickr`__. Bisogna ammettere che da quando
molti di noi sono diventati dipendenti dai vari servizi online (da
Imageshack a Flickr, da Google a `OpenStreetMap`__, da Launchpad a LastFM)
questi fornitori di servizi hanno compreso come possa essere utile, al
fine di integrare il maggior numero possibile di sistemi operativi con
il proprio prodotto, realizzare delle API utilizzabili indipendentemente
dal proprio sistema operativo.

.. __Flickr: http://www.flickr.com
.. __OpenStreetMap: http://www.openstreetmap.org

È ciò che è successo pressappoco per Flickr: sulla base delle API
rilasciate dal vincente progetto di Yahoo!, sono stati realizzati
qualcosa come 37 software per gestire le proprie foto su Flickr.com.
Molti di questi sono compatibili con GNU/Linux, alcuni scritti in C,
altri in Java, altri in Python, altri in Perl. Esistono validissimi
software in Gtk, altri in Qt o in Tcl/Tk, ma esistono anche alcuni tool
da linea di comando. Altri strumenti sono stati integrati nei più noti
gestori di fotografie per GNU/Linux (F-Spot, Digikam). Ed infine,
qualcuno ha pensato di realizzare l'integrazione con Nautilus, partendo
da un menù di servizio per caricare le foto selezionate direttamente su
Flickr, e finendo con l'integrazione di un filesystem basato su FUSE con
le API di Flickr e con Nautilus.

Ed è proprio di quest'ultimo che vorrei parlarvi in questo post. Il
software si chiama Flickrfs, è disponibile nei repository di Ubuntu
Intrepid e consente di sfogliare il contenuto del proprio account Flickr
come se fosse una cartella in Nautilus, quasi un FTP. Vediamo come
installarlo.

Prima di tutto, faccio notare che non sono ancora riuscito a far
caricare dei video a FlickrFS, ma solo fotografie. Se non avete un
account PRO, è esattamente cio che fa per voi ;)

Passo 1
-------

Installiamo il pacchetto `flickrfs` da Synaptic o da linea di comando:

::

    sudo apt-get install flickrfs

Passo 2
-------

Assicuriamoci che FUSE sia incluso tra i moduli del kernel (e ciò
dovrebbe essere vero di default nel 99% dei casi):

::

    lsmod | grep -i fuse

Se tutto è ok, dovrebbe essere visualizzata una linea del genere:

::

    fuse        52892 3

Passo 3
-------

Creiamo una cartella (dove più ci piace) in cui verranno "ospitate" le
nostre cartelle di Flickr; io l'ho montata in ``/media``, come qualsiasi
altra penna USB o hard disk esterno:

::

    sudo mkdir /media/flickrfs

Passo 4
-------

Ordiniamo a Flickrfs di "montarsi" all'interno della cartella appena
creata:

::

    sudo flickrfs /media/flickrfs

Appena il programma avrà terminato di aggiornare i nostri set, potremo
aprire Nautilus con privilegi di amministratore e accedere alla nostra
cartella:

::

    sudo nautilus /media/flickrfs

Ed ecco le nostre cartelle. Potremo importare/esportare foto come se
fossimo in una nostra normalissima cartella di sistema, con il
drag&drop, con il copia/incolla, ecc..

È utile comunque crearsi un collegamento sul desktop o aggiungere
l'indirizzo nei preferiti per aprire direttamente la cartella flickrfs.
