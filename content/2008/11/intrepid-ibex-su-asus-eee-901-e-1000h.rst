Intrepid Ibex su Asus EEE 901 e 1000(H)
=======================================

:date: 2008-11-11 00:07:07
:tags: gnulinux, kernel, ubuntu

<center>

|image0|

</center>

In questi giorni, dopo aver venduto a giugno il mio storico Asus 701 (su
cui era installata Ubuntu EEE 7.10) ho ricevuto il nuovo Asus EEE 901
con monitor da 8,9''. Un bel passo avanti, e finalmente uno schermo un
po' più grande su cui prendere appunti in università. Tuttavia, ho
impiegato circa 1 giorno e mezzo per riuscire a renderlo perfettamente
funzionante con Ubuntu 8.10 Intrepid Ibex. Molte delle informazioni
descritte di seguito sono state reperite semplicemente googlando in giro
e raccogliendo consigli ed howto da forum per lo più in inglese. Vediamo
come sistemarlo a puntino :)

*ATTENZIONE: al termine di questo how-to il vostro Asus 901/1000 sarà
perfettamente funzionante in tutto e per tutto con Ubuntu, con
l'eccezione del microfono: allo stato attuale, non esiste ancora un
workaround per far riconoscere il microfono dei due modelli di EEE PC ad
Ubuntu. Il bug è già stato segnalato su Launchpad e non penso passerà
molto tempo prima che venga risolto (soprattutto perché sulla Xandros
installata di default il microfono funziona), ma per il momento, il
microfono non è utilizzabile.*

Installare la ISO su USB
------------------------

Prima di tutto, avremo bisogno di una ISO della nostra versione di
Ubuntu preferita (Desktop, Alternate, Server, Ubuntu, Kubuntu, Xubuntu,
non è importante).

-  Grazie ad IsoStick, potremo "trapiantare" la nostra .iso in una penna
   USB (dovrebbe essere almeno da 1 Gib) che verrà anche resa
   "avviabile" (*bootable*).

-  Come alternativa, possiamo installare sulla nostra Ubuntu (nel fisso
   o in altro PC disponibile) il comodissimo usb-creator, disponibile
   `qui`_.

Fatto ciò, non resta che inserire la penna USB nell'Asus, riavviare il
PC, premere ripetutamente il tasto Esc durante l'accensione, per
ottenere un menù da cui selezionare la periferica d'avvio. Selezioniamo
USB ed installiamo Ubuntu come nostro solito.

Piccola nota: l'Asus 901 viene venduto con una capacità di 20 Gib,
distribuiti su due hard disk separati, uno da 4 e l'altro da 16 Gib. Ciò
significa che avremo la possibilità di installare la root nella
partizione da 4 Gib e la Home in quella da 16 Gib (oltre allo swap che
verrà ricavato in questa stessa partizione). Non è una cattiva idea,
rende l'installazione molto ordinata, e dopo aver fatto un po' di
pulizia, nella root mi avanza addirittura 1 Gib di spazio per altri
programmi. La cosa è tutto dire, considerato che utilizzo una Ubuntu
"sporca" da cui ho rimosso metà dei programmi preinstallati di GNOME, ed
installato molti programmi di KDE come Kile, Konsole, Digikam, Dolphin,
LyX. Oltre a questi nei 3 Gib occupati in root son riuscito a farci
entrare PyTube, Inkscape, Gimp, Vim-gtk, Gnome-do. Se non avete voglia
di pulire il sistema o pensate di occupare ben più di 4 Gib nella root,
allora vi consiglio di non installare la root nella partizione da 4 Gib,
ma di mettere tutto in quella da 16 Gib e utilizzare quella da 4 Gib
come archivio.

*EDIT: Su segnalazione di PauLoX, che ringrazio, aggiungo che è
possibile fare in modo che Ubuntu riconosca i due hard disk separati del
901 o del 1000H come un unico hard disk, che verrà partizionato secondo
le nostre esigenze. È possibile farlo con LVM (Local Volume Manager),
strumento disponibile nella versione alternate di Ubuntu. Non ho trovato
riferimenti in italiano, ma
`questa <http://www.debuntu.org/how-to-install-ubuntu-over-lvm-filesystem>`_
sembra fare al caso nostro.*

Ora, abbiamo la nostra Ubuntu Intrepid installata nell'Asus, ma non
funziona praticamente niente: out-of-the-box **non** sono supportati
wifi, webcam, tasti funzione. La soluzione al problema arriva da un
simpatico personaggio che ha deciso di modificare il kernel 2.6.27-7 di
Intrepid (ma anche quello precedente di Hardy) per adattarlo alle
esigenze degli Asus 901 e 1000. Il nuovo kernel si chiama
2.6.27-7-eeepc, e per installarlo è necessaria una connessione cablata
ad un modem o router, dato che la nostra wifi non funziona ancora. Una
volta ottenuta la rete, aggiungiamo questa riga ai nostri repository:

::

    :::bash
    deb http://www.array.org/ubuntu intrepid eee

Scarichiamo ed aggiungiamo la chiave per i nuovi repository

::

    :::bash
    wget http://www.array.org/ubuntu/array-apt-key.asc
    sudo apt-key add http//www.array.org/ubuntu/array-apt-key.asc

Installiamo il nuovo kernel con tutti i pacchetti raccomandati:

::

    :::bash
    sudo apt-get install linux-eeepc linux-headers-eeepc

Rimuoviamo il vecchio kernel per liberare spazio sull'hard disk:

::

    :::bash
    sudo apt-get remove linux-generic linux-image-generic linux-headers-generic linux-restricted-modules-generic

*EDIT: Xan mi segnala che negli ultimi rilasci del kernel i driver
aggiornati per il wireless sono stati inclusi. Non ho controllato, ma
nel caso fosse così, potete tranquillamente saltare a piè pari questo
passo...*

Scarichiamo ed installiamo un pacchetto *.deb* (con la sua dipendenza)
che contiene i driver wireless aggiornati che al prossimo avvio del
sistema verranno automaticamente inseriti nel nuovo kernel:

::

    :::bash
    sudo apt-get install dkms
    wget http://www.mediafire.com/?jfrgzemgnjz
    sudo gdebi rt2860sta-dkms_*.deb

Scarichiamo un pacchetto con gli script che renderanno operativi i tasti
funzione dell'Asus:

::

    :::bash
    wget http://www.informatik.uni-bremen.de/~elmurato/EeePC/Intrepid_ACPI_scripts-EeePC_900A_901_1000.tar.gz
    tar xfvz Intrepid_ACPI_scripts-EeePC_900A_901_1000.tar.gz
    cd Intrepid_ACPI_scripts-EeePC_900A_901_1000/
    chmod +x acpi-scripts.sh
    sudo ./acpi-scripts.sh install

Fatto ciò, non resta che abilitare il tasto funzione del bluetooth, che
di default è disabilitato negli script:

::

    :::bash
    sudo nano /etc/acpi/eeepc/eeepc-actions.sh

decommentando (togliendo il cancelletto) la riga 89, relativa al
bluetooth, che dovrebbe diventare così:

::

    :::bash
    /etc/acpi/eeepc/eeepc-bt-toggle.sh

Riavviamo il PC e selezioniamo dal GRUB il nostro nuovo kernel targato
eeepc, e tutto dovrebbe funzionare!!

Personalmente, ritengo utile anche dare una bella pulita al sistema
seguendo `questa guida`_.
dal Wiki di Ubuntu-it, oltre che disabilitare alcune opzioni nell'fstab
per accelerare la lettura/scrittura dei dati dagli hard disk, come
descritto qui. Inoltre, ricordo che Ubuntu di default installa una
discreta quantità di pacchetti del tutto inutili, come i driver per le
stampanti HP o i font di lingue parlate in paesi che non avete mai
neanche sentito nominare. Si può ovviare a ciò rimuovendo da Synaptic
tutti i pacchetti relativi ad "hplip" e tutti i font inutili con questo
comando:

::

    :::bash
    sudo apt-get remove ttf-arabeyes ttf-arphic-ukai ttf-arphic-uming ttf-baekmuk
    ttf-bengali-fonts ttf-devanagari-fonts ttf-gentium ttf-gujarati-fonts
    ttf-indic-fonts ttf-kannada-fonts ttf-kochi-gothic ttf-lao ttf-malayalam-fonts
    ttf-mgopen ttf-oriya-fonts ttf-punjabi-fonts ttf-tamil-fonts ttf-telugu-fonts
    ttf-thai-tlwg

Fossi in voi toglierei anche Brasero, visto che gli Asus EEE non hanno
il masterizzatore ;)

::

    :::bash
    sudo apt-get remove --purge brasero

E adesso, non vi resta che installare tutti i programmi di cui avete
bisogno!

Buon divertimento :)

.. |image0| image:: http://dl.dropbox.com/u/369614/blog/img_red/screen901tw6.jpg
.. _qui: http://packages.ubuntu.com/intrepid/usb-creator
.. _questa guida: http://wiki.ubuntu-it.org/AmministrazioneSistema/PulireUbuntu
