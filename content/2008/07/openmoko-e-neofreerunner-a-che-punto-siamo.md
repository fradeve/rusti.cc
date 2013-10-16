Title: Openmoko e NeoFreerunner: a che punto siamo...
Date:  2008-07-15 17:59:24
tags: freerunner, gnulinux, nokia, openmoko, python, tangogps, wikipedia

Dopo l'entrata in vendita (meno di un mese fa)
del NeoFreerunner, il primo palmare/telefono completamente open-source,
finalmente anche qualche italiano ha cominciato a ricevere a casa il magico
pacchettino nero, contenente la straordinaria saponetta elettronica che farà
felice moltissimi smanettoni ed amanti del Software Libero. Ci sono una serie
di rivelazioni/novità del tutto sconcertanti: comincio da quelle più "banali"
per arrivare alle più "succose". Molte notizie sono conosciute già da secoli,
ma questo post e un vero e proprio brainstorming...


## Statistiche ##

Secondo le statistiche di Giugno del Wiki di Openmoko (wiki.openmoko.org) l'Italia è
al 3° posto nel mondo per "interesse" nei confronti del palmare, con 5177
visite al giorno, preceduta da Germania (14666) e USA (17243). Dietro l'Italia
troviamo Francia, Regno Unito, Taiwan e Cina. Sono sbalordito da un così
imponente interesse nel nostro Bel Paese, è un segnale molto positivo.


## Vendite ##

In 2 giorni il Neo Freerunner è andato completamente esaurito
in *tutti* i negozi d'Europa (i distributori erano 4!). Secondo alcuni calcoli
sulla mailing list ufficiale, se ne sono venduti in 10 giorni più di
10.000.... spaventoso.


## Sviluppo ##

Secondo un sondaggio, la piattaforma di
sviluppo Openmoko è al 2° posto in assoluto come preferenza da parte degli
sviluppatori, dopo Android di Google; segue Windows Mobile; Symbian all'ultimo
posto. [Ho perso il link, quindi scusate se non vi cito la fonte; ve ne parlo
sulla fiducia]


## Funzioni ##

Cosa può fare attualmente il Neo Freerunner con
Openmoko: tutto. Telefona, manda SMS, copia la rubrica ed i contatti
direttamente dalla SIM, funge da navigatore GPS con mappe vettoriali
(OpenStreetMap) ed anche con fotografie aeree; naviga nel web con connessione
Wifi e si collega ad altri dispositivi tramite Bluetooth. Grazie a Cerebro
[http://lyme.media.mit.edu/cerebro/index.php/Welcome_to_Cerebro] permette di
creare reti mesh Wifi senza necessità di connessione ad internet, permettendo
ai Neo di comunicare fra loro e scambiarsi dati. Inoltre funzionano benissimo
anche le altre applicazioni come l'agenda, il lettore di feed RSS, ecc.


## Ambienti software ##

Tra gli aspetti più interessanti, non comuni a nessun
altro palmare/telefonino, è la presenza di [*molti* ambienti "desktop"][1]. Il
Neo viene distribuito con il rilascio di Openmoko 2007.2, un'interfaccia
basata su GTK che svolge egregiamente tutte le funzioni per cui è stato
programmato. Tuttavia, sono in lavorazione un'interfaccia basata su Qtopia,
che integra Gtk, Qt ed e17 (le librerie di Enlightment9), chiamata ASU (April
Software Update) ed un'ulteriore ambiente ancora completamente work in
progress chiamato FSO, il cui obiettivo è semplicemente avere una stabilità
pazzesca (non che il 2007.2 non lo sia, eh).


## Batteria ##

Grazie ad una patch, la batteria con lo stack FSU raggiunge le 21 ore di durata :D Secondo
gli sviluppatori, ci sono in cantiere altre modifiche al sistema che ne
allungheranno ancora di più la vita. Per il momento la vita media di un Neo
Freerunner si aggira intorno alle 6 o 7 ore.


## Componenti aperte ##

Il Neo Freerunner, essendo completamente aperto, non sopporta l'hardware
proprietario. Niente POP-port come nei Nokia Serie 60 per gli spinotti, ma un
[meraviglioso jack da 2,5 mm][2] per le cuffie e una stupenda porta micro-USB
per collegarlo al PC. La batteria in dotazione con il palmare è la BL-5C,
usata nei Nokia Serie 60 (come il 6600 o il 6630) e comprarne una
"compatibile" costa solo 5€, motivo per cui non c'è da preoccuparsi se -
attualmente - la batteria dura cosi poco.


## Penne USB ##

La [porta USB del Neo][3] è alimentata: ciò significa che è possibilissimo collegarci una penna
USB (con apposito adattatore USB-microUSB) e utilizzare i dati in essa
contenuti (anche se gli sviluppatori avvisano che ciò potrebbe diminuire
sensibilmente la vita del palmare... certo, se avete una batteria di scorta è
tutto più semplice).


## Librerie grafiche ##

Openmoko, lo do per scontato, è un sistema GNU/Linux, con tutto ciò che ne consegue: sono supportati Python,
Perl, C++ ed altri linguaggi di programmazione sia compilati che interpretati.
Sono supportati [Gtk+, Qt ed e17][4], quindi ci si può sbizzarrire con il
software libero e con il porting di software già esistente.


## Il prezzo in Italia ##

Grazie ad una [azienda italiana][5], il Neo Freerunner entrerà
in vendita in Italia dal 1° settembre, alla modica cifra (e dico sul serio) di
329€ + 10€ di spedizione. Nel prezzo, oltre al palmare, è inclusa una custodia
in neoprene e le cuffie con jack da 2,5 mm. [Nella confezione][6], oltre agli
oggetti appena citati, sono presenti: un cavo USB-microUSB per connettere il
palmare al PC; un adattatore per ricaricarlo dalla presa elettrica, con
ulteriore adattatore per prese europee/inglesi ed una microSD da 512 Mib. Nel
prezzo è compreso un servizio "DebugBoard on call service" per l'affitto
settimanale delle debug-board.


## Il GPS ##

Oggi è stato scoperto un bug nell'hardware del Neo Freerunner; si tratta di un [EMC][7] derivante dallo
slot che contiene la microSD e che interferisce con il ricevitore GPS, che non
riesce (o in alcuni casi ci mette moooolto tempo) ad agganciarsi ad alcun
satellite. Fin quando gli sviluppatori non troveranno una maniera per fare
fronte al bug (ovviamente la risoluzione dovrebbe arrivare dal software non da
una modifica dell'hardware) il problema può essere risolto rimuovendo la
microSD quando bisogna usare il GPS (lo so, è una proposta indecente perché
nella microSD possono essere salvate tutte le mappe necessarie alla
navigazione) oppure utilizzando un'antenna GPS esterna via bluetooth.
Comunque, non in tutti i casi succede quanto descritto sopra, ad alcuni sembra
funzionare bene. Aspettiamo fiduciosi ulteriori sviluppi sul tema.


## La navigazione satellitare ##

In compenso, sono stati elaborati software
semplicemente magnifici per la navigazione GPS su Openmoko: sto parlando di
[gvSIG][8], [tangoGPS][9], che supportano mappe da [OSM][10], e foto aeree da
OpenAerialMap.org e Maps-For-Free.org. Questi programmi sono l'ideale anche
per tutti i mapper che vogliono cimentarsi in OSM.


## I browser ##

Openmoko ha un browser integrato [WebKit][11] ed è già stato inoltre testato Firefox
per dispositivi mobile, che prende il nome di "[Minimo Web Browser][12]", e
funziona benissimo.


## Java ##

Openmoko adesso, grazie allo sviluppo di
[Jalimo][13], supporta anche Java: è anche per questo che [gvSIG][14] gira sul
palmare. Con questo porting di Java, si apre un mondo di possibilità!


## Design aperto e creatività ##

I [file CAD][15] con cui sono progettate le
mascherine di plastica che ospitano e contengono l'hardware del Neo (il "case"
o "chassis", per capirci) sono sotto licenza Creative Commons, e sono
liberamente modificabili e ridistribuibili. Uno studente di design industriale
in uno stage all'Openmoko, ha progettato una [stupenda guaina][16], una cover
in plastica per il palmare, che gli conferisce un aspetto veramente robusto e
resistente, quasi come gli astucci dei telecomandi. Non ci vorrà molto che
qualche azienda non approfitti dell'idea e ne produca dei modelli reali,
mettendoli in commercio. I vantaggi dell'hardware libero ;)

   [1]: http://www.vanille-media.de/site/index.php/2008/06/28/gtk-asu-fso-tmtla/

   [2]: http://wiki.openmoko.org/wiki/Getting_Started_with_your_Neo_FreeRunner

   [3]: http://wiki.openmoko.org/images/f/fa/Menu9.jpg

   [4]: http://wiki.openmoko.org/images/b/bb/OpenmokoFramework08.png

   [5]: http://www.eurofaxsas.it/

   [6]: http://wiki.openmoko.org/images/2/22/GTA02ALL.png

   [7]: http://it.wikipedia.org/wiki/Compatibilit%C3%A0_elettromagnetica

   [8]: http://blogs.thehumanjourney.net/finds/resource/4.png

   [9]: http://www.youtube.com/watch?v=hn7wuxlTNvs

   [10]: http://www.openstreetmap.org/

   [11]: http://www.monochromementality.com/data/phoo/2008_01_15/medium/moko-browser-on-monochromementality.jpg

   [12]: http://www.mozilla.org/projects/minimo/

   [13]: https://wiki.evolvis.org/jalimo/index.php/Main_Page

   [14]: http://en.wikipedia.org/wiki/GvSIG

   [15]: http://openmoko.com/download-cad.html

   [16]: http://www.sureda.org/Portfolio/Portfolio.htm
