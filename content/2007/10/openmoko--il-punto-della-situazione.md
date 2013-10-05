Title: Openmoko: il punto della situazione
Date:  2007-10-02 15:07:08
tags: nokia, openmoko, ubuntu,

Consultando un po' gli ultimi aggiornamenti alle Wiki ufficiali, e
scartabellando mail dalla mailing list e con qualche domanda sul canale IRC,
ho fatto una piccola raccolta di informazioni su questo progetto. Il
risultato: la versione _mercato di massa_ (mass market) di Dicembre conterrà:

 * Quad-band GSM, GPRS Class12/CS4 2.5G (Non EDGE)
 * bluetooth 2.0
 * wi-fi
 * GPS
 * 2 accelerometri 3D (l'iPhone ne ha 2, ma sono 2D)
 * un altoparlante, sul retro (i 2 altoparlanti della versione precedente rockeggiavano, ma anche uno è eccellente)
 * due tasti sul lato, ci cui uno per l'accensione, entrambi retroilluminati
 * schermo LCD touchscreen con risoluzione di circa 280 dpi (l'iPhone ha lo schermo un po più grande, diciamo
enorme, ma la risoluzione è molto più bassa: solo 160 dpi!)
 * RAM da 128 Mib e processore da 400 MHz
 * Dimensioni: 120.7 x 62 x 18.5 mm
 * Memoria interna: Flash da 256 Mb
 * Accelerazione 3D: SMedia 3362 Graphics Accelerator

Insieme al palmare, si riceverà (sempre nel pacchetto base):
 * cavo USB/alimentazione
 * custodia in neoprene
 * penna/stilo/laser
 * plettro per chitarra (per aprire il cell)
 * batteria da 1700 (identica a quella dei Nokia serie 60)
 * Scheda di memoria MicroSD da 512 Mb (il Neo1973 supporta MicroSD fino ad 8 Gb!)

**Quando uscirà:**  
tra il 1° ed il 15 Dicembre  

**Ora dov'è:**  
ultima fase di produzione  

**Cosa funziona:**  
le chiamate, gli SMS, il wifi; il GPS è utilizzabile a metà (funziona ma dovrebbe essere perfezionato), tutte
le applicazioni sono perfettamente utilizzabili, se non si e terrorizzati da
qualche piccolo bug.  

**Nel frattempo che faccio?**  
Se hai un Neo1937 e pensi che non riesca a soddisfare le tue esigenze, a causa del software non pronto,
installa[ Qtopia][1].  

**Quanto costa?**  
325€ (450$) + 22 di [spese spedizione][2] = 347€ a casa :)  

**Verrà venduto solo online?**  
Per il momento sembra di si, e possiamo darvene certezza quasi
matematica.  

**Ed Ubuntu?**  
Sarà possibile in un futuro forse non vicinissimo,
farci girare anche Ubuntu, in versione [Lpia][3].  

**Hai curiosità / indiscrezioni?**  
Sono riusciti a far girare su Openmoko sia Emacs che Ekiga, e
qualcuno sostiene che in futuro possa essere utilizzabile anche Skype. Il
player audio funziona, riproduce mp3 ed ovviamene Ogg, supporta le playlists,
ma sono attesi ulteriori miglioramenti al software. Il player video non c'è e
devono lavorarci sopra un bel po' per ottenerne uno funzionante su Openmoko.  

**Batteria: qual'è? Quanto costa? Quanto dura?**  
La gestione della batteria
non è eccezionale, è molto migliorabile, ma comunque per essere i primi mesi
di sviluppo, e già eccellente. Se poi tenete conto che una batteria come
quella su eBay costa 5€, tanto vale comprarsene un paio per andare sicuri. La
durata media della batteria e di 5 ore. La batteria è la BL-5C. Per chi non lo
sapesse, è la stessa batteria dei Nokia serie 60.  

**E gli HIDs (_Human Interface Device_)?**  
Si possono collegare (testate e funzionanti)
all'Openmoko/Neo1937 sia le tastiere bluetooth (testate quelle Nokia) sia gli
auricolari bluetooth.  

**Come accedo ai dati del Neo?**  
Via bluetooth, via usb, via ssh (alternativamente, si può estrarre la MicroSD e inserirla in un
lettore di memory card).  

**Che schede di memoria posso utilizzare?**  
MicroSD,
con capacità teorica fino ad 8 Gib. Sono state testate e dichiarate compatibili
(per il momento) schede fino a 6 Gib.  

**Sarà multitouch?**  
L'hardware del touchscreen lo permette, ma il software per utilizzare questa funzione non è
ancora stato sviluppato. Tuttavia, molte cose lasciano pensare che avremo il
multitouch sul Neo1937 in un futuro non troppo lontano, dato che l'hardware lo
consente...  

**E la fotocamera?**  
Il Neo1973 è solo il primo dei tanti palmari
che la FIC (l'azienda che promuove il progetto) ha in mente. È ovvio che le
prossime versioni dei palmari FIC avranno la fotocamera. In qualsiasi caso, la
versione GTA02 in uscita a Dicembre, non l'avrà.  

Altre informazioni:  
[http://wiki.openmoko.org/wiki/IPhone/it][4]  

Dai dicci qualcosa di piu sui
programmi:  
**Thumbtribes** È un programma sviluppato su e per
Openmoko, che sfrutta le enormi potenzialità del GPS per creare un sistema di
localizzazione tra amici/conoscenti, che in futuro sarà integrato nei PIM
(_Personal Information Manager_). In parole poverissime, dopo che il potenziale
utente si e registrato al servizio sul sito, potrà aprire il programma su
Openmoko e fare il login. In questa maniera, il programma visualizzerà tutti i
contatti "in linea", ovvero connessi al servizio, e li localizzerà utilizzando
il GPS. Come e scritto sul commento al video di YouTube che illustra le
funzionalità del programma, può essere utile sia per localizzare gli amici che
per "spiarli" nei loro movimenti :D


Questo il [link][5] alla notizia sul blog
di riferimento.

   [1]: http://wiki.openmoko.org/wiki/Qtopia_on_Neo_1973

   [2]: http://www.jesc.ch/openmoko

   [3]: https://wiki.ubuntu.com/MobileAndEmbedded

   [4]: http://wiki.openmoko.org/wiki/IPhone/it

   [5]: http://blogs.gnome.org/thos/2007/10/02/two-neo1973s-calling-each-other/
