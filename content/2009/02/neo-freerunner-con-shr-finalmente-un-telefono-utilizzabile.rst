Neo FreeRunner con SHR: finalmente un telefono utilizzabile!
============================================================

:date: 2009-02-23 15:57:55
:tags: freerunner, gnulinux, kernel, openmoko, openstreetmap, python, tangogps, ubuntu

Come molti di voi sapranno, nel luglio 2008 un'intraprendente società
taiwanese ha rilasciato la prima versione "mass market" del Neo
FreeRunner, il primo telefono/palmare completamente open source della
Storia. Sono passati molti mesi dal rilascio, e tutto il mondo si è
precipitato a creare la propria versione del sistema operativo per il
palmare, partendo da zero o "portando" qualcosa che già esiste (è
quest'ultimo il caso di Debian e Gentoo). Comunque, la FIC paga un
consistente numero di sviluppatori per lavorare ad una versione
"ufficiale" del sistema operativo, chiamato Openmoko, e che in linea
teorica vorrebbe diventare IL sistema operativo per dispositivi palmari,
compatibile con quanti più modelli possibili. Non si può creare un
sistema operativo universale per palmari in un anno, ma almeno sul Neo
FreeRunner le cose sembrano andare per il meglio. Dopo qualche delusione
dovuta all'ultima versione di Openmoko (datata a Dicembre 2008), e dopo
aver cercato di riparare ai continui freeze installando il kernel
compilato da Trevino, ho deciso di spostarmi definitivamente sulla
versione più aggiornata del sistema,
`SHR`_ (**S**\ table **H**\ ibrid **R**\ elease), che pur essendo 
disponibile in versione "unstable", offre una stabilità e un look 
veramente accattivanti.

Cos'e SHR?
----------

Quando si è pensato ad un sistema operativo per palmari, si è avuta la
necessita di creare un framework basato su Dbus al quale tutti gli
sviluppatori potessero fare riferimento per creare le proprie
applicazioni. Questo framework per palmari non esisteva, e ci sta
pensando un impiegato della FIC, `Mickey Lauer`_. Come per
il desktop, si è scelto di rispettare le specifiche di
`Freedesktop.org`_, creando `Freesmartphone.org`_, al fine di
ottenere una base Dbus comune per tutte le distribuzioni GNU/Linux per
palmari. Quindi, SHR è una versione di Openmoko che ha come base **FSO**
(**F**\ ree the **S**\ mart\ **P**\ hone), che dovrebbe rappresentare lo
stack del futuro, come Freedestkop.org lo è adesso per tutte le
distribuzioni desktop GNU/Linux (compresa Ubuntu). Per questo, il nome
SHR: "*rilascio ibrido stabile*\ ". Insomma, alla FIC si sta costruendo
il futuro di GNU/Linux sui palmari.

.. _SHR: http://shr-project.org/trac/wiki/WikiStart
.. _Mickey Lauer: http://www.vanille-media.de/site/index.php/about/
.. _Freedesktop.org: www.freedesktop.org
.. _Freesmartphone.org: http://www.freesmartphone.org

Quale versione installare?
--------------------------

SHR è disponibile sia in versione "stable" che "unstable": quella stable
- non ancora disponibile - sarà un freeze delle caratteristiche alla
data prescelta. La unstable attualmente disponibile è in costante
lavorazione, ma è sufficientemente stabile da poter essere usata come
telefono quotidiano, più di Openmoko 2008.12. È inoltre disponibile la
versione "lite" del filesystem di root, più leggera e veloce da
scaricare sul PC e flashare sul Neo.

Perché SHR (Pro)?
-----------------

-  Perché il suo stack basato su FSO è il futuro di GNU/Linux su
   dispositivi mobile;

-  Per la maneggevolezza di una versione di Illume personalizzata per la
   distribuzione e molto finger-friendly;

-  Per il power management: la batteria in standby arriva a durare anche
   60 ore, contro le 24 - 30 ore di Openmoko di dicembre.

-  Perché e aggiornata costantemente, al contrario di Openmoko 2008.12;

-  Perché non utilizza Qtopia, che appesantisce il sistema a fronte di
   una suite PIM comunque incompleta e non perfettamente aderente alle
   esigenze di Openmoko;

-  Per l'eliminazione dell'eco quando e attivo il viva voce;

-  Per un manager delle impostazioni in Python completamente
   personalizzabile ed espandibile, e che comunque comprende tutto ciò
   di cui c'è bisogno per controllare il palmare (al contrario del
   "Settings" di Openmoko).

-  Perché supporta i messaggi speciali dell'operatore (per esempio il
   numero *123*\ 15# della Wind per visualizzare i minuti residui di una
   certa promozione);

-  Perché finalmente funziona il led BLU/ROSSO sotto il tasto Power;

-  Perché la gestione di GSM, GPS, Bluetooth e Wifi è completamente
   centralizzata e attivabile su richiesta dei vari programmi (questo
   sistema lo spiegheremo meglio in seguito).

Perché evitarla? (Contro)
-------------------------

-  Per il bug del Gtk+-fastscaling (facilmente risolvibile con un
   --force- depends, come vedremo di seguito)

-  Per qualche minore problema di instabilità (mi è capitato un paio di
   volte in una settimana che la vibrazione continui anche dopo aver
   risposto ad una telefonata, costringendomi al riavvio del cell).

Installazione
-------------

Personalmente ho installato
`shr-lite-image-om-gta02.jffs2 <http://build.shr-project.org/shr-unstable/images/om-gta02/shr-lite-image-om-gta02.jffs2>`_
e
`uImage-2.6.28-[...].bin <http://build.shr-project.org/shr-unstable/images/om-gta02/uImage-2.6.28-oe1+gitr34240a1c06ae36180dee695aa25bbae869b2aa26-r3-om-gta02.bin>`_,
ovvero le ultime versioni del filesystem di root e del kernel
(suggeritemi nella mailing list ufficiale). Ricordo al gentile lettore
che le immagini possono essere comodamente flashate nel Neo usando
`NeoTool <http://wiki.openmoko.org/wiki/NeoTool>`_. La prima cosa da
fare dopo il primo boot è *riavviare* il Neo, perché al primo boot il
GSM non funziona. Fatto ciò, potremo constatare al successivo riavvio
che di default funziona il collegamento ad internet via USB e funziona
anche SSH.

`shr-lite-image-om-gta02.jffs2 <http://build.shr-project.org/shr-unstable/images/om-gta02/shr-lite-image-om-gta02.jffs2>`_
`uImage-2.6.28-[...].bin <http://build.shr-project.org/shr-unstable/images/om-gta02/uImage-2.6.28-oe1+gitr34240a1c06ae36180dee695aa25bbae869b2aa26-r3-om-gta02.bin>`_,
`NeoTool <http://wiki.openmoko.org/wiki/NeoTool>`_. La prima cosa da

Sistemare il tasto Power
------------------------

Di default, alla pressione del tasto Power, appare prima un menù che
comprende le opzioni per lo standby, lo spegnimento e la chiusura della
sessione (proprio come un PC!), poi il Neo va in standby. La spiacevole
quanto inutile apparizione del menù può essere evitata dando i seguenti
comandi:

1. xrandr -o 1

2. fare click sulla chiave inglese presente nell'angolo in alto a
   sinistra della barra superiore

3. fare click su "input" e poi su "key binding"

4. cancellare la voce: "Execute" e applicare le modifiche con il tasto
   "Apply"

Risolvere il problema del pacchetto gtk+-fastscaling
----------------------------------------------------

In SHR (ed FSO se ricordo bene) il pacchetto gtk+-fastscaling è stato
rinominato semplicemente in gtk+, ma molti programmi non lo sanno, per
questo hanno come dipendenza il *fastscaling* che in realtà è già
installato nel sistema come "gtk+". Quando si vanno ad installare
pacchetti del genere, può capitare di ricevere un errore e si
interromperà l'installazione. Per ovviare a questo problema, sarà
sufficiente ridare il comando di installazione, inserendo la dicitura *
--force-depends* tra opkg e install. Ad esempio, per installare Navit:

::

    opkg --force-depends install navit

Inserire un tasto per lo spegnimento
------------------------------------

Dopo aver eliminato il menù che appare alla pressione del tasto Power,
non ci sarà più modo di spegnere il Neo senza un terminale. Possiamo
ovviare a questo problema creando uno shortcut sul desktop. Basterà
inserire il seguente file, che chiameremo *shutdown.desktop* nella
cartella */usr/share/applications/*:

::

    :::bash
    [Desktop Entry]
    Encoding=UTF-8
    Version=0.7
    Name=Shutdown
    Type=Applicat=UTF-8
    Version=0.7
    Name=Shutdown
    Type=Application
    Comment=Show System Processes
    Terminal=true
    Exec=shutdown now
    Path=
    Icon=/usr/share/icons/openmoko-standard/128x128/apps/openmoko-system-default.png
    Categories=ConsoleOnly;System;Application
    GenericName=Process Viewer
    Categories=Office;
    Exec=shutdown now

Una nota su GPS, Bluetooth, GSM e Wifi
--------------------------------------

Il nuovo framework FSO su cui si basa SHR ha il grande vantaggio di
tenere spenti tutti questi servizi all'avvio del sistema. Inoltre, esso
si pone come "gestore" di questi servizi tra le applicazioni ed il
kernel; in altre parole, noi non avremo bisogno di "attivare" il GPS
prima di aprire TangoGPS o Navit: sarà sufficiente aprire uno di questi
programmi, e poi ci penserà il sistema operativo ad attivare il GPS.
Nella stessa maniera, quando chiuderemo tutti i programmi che utilizzano
il GPS, il ricevitore verrà spento. Il Wifi ed il Bluetooth devono
essere accesi e spenti "manualmente" dall'apposito menù *Settings*.
Anche il GSM come il GPS viene acceso solo su richiesta dal sistema
operativo, ed in particolare questa richiesta avviene nel momento stesso
dell'accensione del Neo, quindi a noi sembra che venga acceso di
default. Se vogliamo risparmiare sulla batteria e non ci serve il GSM,
possiamo disattivarlo dal menù *Settings*. Molto comodo, non trovate?
Niente di tutto questo esiste su Openmoko 2008.12.

TangoGPS e Yaouh!
-----------------

Yaouh! è un'applicazione scritta da un italiano, Carlo Minucci, che
scansiona tutte le mappe presenti in TangoGPS e le aggiorna scaricando
da OpenStreetMap solo le parti che sono state aggiornate dopo l'ultimo
rendering settimanale (che avviene ogni giovedì solitamente). Purtroppo,
a partire dall'ultima versione di TangoGPS, la 0.9.5, i repository delle
mappe del programma vengono scritti all'interno del codice stesso del
programma, e non sono più reperibili da Yaouh!, che non riesce quindi a
scaricare alcun aggiornamento. Per ovviare a questo inconveniente,
almeno per le mappe "standard" di OpenStreetMap (quelle di Mapnik, per
capirci), è sufficiente sostituire nel file
*~/.gconf/apps/tangogps/%gconf.xml* questa riga:

::

    :::bash
    OSM

con questa

::

    :::bash
    OSM|http://tile.openstreetmap.org/%d/%d/%d.png|/home/root/Maps/OSM|0

rispettando gli spazi e la sintassi del resto del file. Attenzione però:
il file in questione viene sovrascritto da TangoGPS ad ogni chiusura del
programma, quindi dopo aver modificato il file aprite Yaouh! e
aggiornate le mappe senza aprire/chiudere TangoGPS, altrimenti avrete
perso tempo...

Navit
-----

La versione più aggiornata di Navit installabile sul Neo è quella SVN, e
può essere installata dando i seguenti comandi:

::

    :::bash
    echo src navit http://download.navit-project.org/navit/openmoko/svn >/etc/opkg/navit-feed.conf
    opkg update
    opkg install navit

Scarichiamo la cartografia italiana di OpenStreetMap aggiornata
settimanalmente fornita da CloudMade, da
`qui <http://downloads.cloudmade.com/europe/italy/italy.navit.bin.zip>`_,
e dopo averlo estratto dall'archivio, spostiamo il file nella cartella
*~/.navit*. Quindi, bisognerà sistemare il file di configurazione, con
il seguente comando:

::

    :::bash
    cp /usr/share/navit/navit.xml ~/.navit/navit.xml

Adesso inseriamo nel file una nuova dicitura "mapset", più o meno nei
pressi del rigo 148:

::

    :::html
    <mapset enabled="yes">
               <map type="binfile" enabled="yes" data="/home/root/.navit/italy.navit.bin" />
    </mapset>

Fatto ciò, possiamo ancora fare in modo che Navit visualizzi i tasti "+"
e "-" per lo zoom, per ingrandire e diminuire lo zoom della mappa
durante la navigazione, portando da "enables=no" a "enables=yes" le voci
ai righi 53 e 54:

::

    :::html
    <osd enabled="yes" type="button" x="-96" y="-96" command="zoom_in()" src="zoom_in.xpm"/>
    <osd enabled="yes" type="button" x="0" y="-96" command="zoom_out()" src="zoom_out.xpm"/>

Tutte le indicazioni per il tweak dell'interfaccia grafica di Navit sono
qui. Per usare Navit è molto utile ruotare lo schermo in orizzontale; è
possibile ottenere una comoda applicazione con tanto di icona nel menù
