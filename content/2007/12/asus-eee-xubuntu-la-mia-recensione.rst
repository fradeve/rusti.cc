Asus EEE e Xubuntu: la mia recensione
=====================================

:date: 2007-12-25 17:47:47
:tags: gnulinux, ubuntu

Premessa
--------

Prima di acquistare questo gioiellino ho letto talmente tante recensioni
(per lo più in inglese) da far venire il mal di testa. Ciò significa
anche che alcune delle informazioni che troverete scritte di seguito
probabilmente le avrete lette già in qualche altra occasione. È
sottinteso: non inviatemi mail o messaggi privati sul forum per
chiedermi dove l'ho acquistato: su eBay lo si trova come il pane (da
rivenditori statunitensi), su quasi tutti i negozi online europei è
esaurito e le spedizioni ricominceranno a gennaio (per lo meno non si
pagano le tasse di dogana, all'interno dell'UE). Fate voi.

Introduzione
------------

Tutto ciò che leggerete è scritto in riferimento alla versione da 4 Gib,
con wireless integrato, webcam, casse audio, tastiera inglese (l'ho
acquistato dagli USA). Vi prego di ricordare che è tutto scritto
seguendo i miei particolarissimi metri di misura, che prevedono anche il
tatto, il gusto e l'udito, quindi non venite a dirmi "secondo me non è
plasticosa come hai detto tu" o "non è vero, quei 3,5 Mib di RAM per il
sistema operativo a me non ci sono" o cose del genere.

La prima impressione all'apertura del pacco è quella che in molti hanno
scritto, ma vi assicuro che non potrebbe essere altrimenti: "Caspita, è
veramente piccolo...". Si, effettivamente non ci si rende conto delle
ridotte dimensioni fino a quando non lo si prende in mano per la prima
volta. Il colore del mio modello è il nero (quello bianco si
sporcherebbe troppo facilmente, e *non sono* un fan del Mac, anzi...).
Il contenuto della confezione credo lo conosciate abbastanza bene;
sicuramente la cosa inclusa nella confezione che ho trovato più utile è
stata la custodia imbottita: è molto sottile, ma a meno che non vogliate
portare il vostro Asus EEE ad un concerto ska, credo che svolga
abbastanza bene il proprio dovere. Sono rimasto anche entusiasta del
caricatore: è poco più grande di quello del mio Nokia 6630, ovvero
rientra nelle dimensioni medie di un caricatore per cellulari, e questo
lo rende l'ideale per il trasporto in valigie o negli zainetti delle
vacanze.

Primo impatto con il software
-----------------------------

L'accensione è veramente *molto* rapida, una ventina di secondi circa
(forse 25). La prima cosa che salta all'occhio è l'abbondante luminosità
dello schermo: mi ha lasciato sbalordito. Anche la risoluzione molto
alta lo rende l'ideale per far vedere agli amici in facoltà le foto del
matrimonio della propria sorella (o, più probabilmente, quelle
dell'amico ubriaco la sera prima o dell'ultimo liquido fosforescente per
l'impianto di raffreddamento a liquido del proprio PC fisso). In un
certo senso, lo schermo non ha niente da invidiare a quello di altri
portatili (certo, se lo volete spettacolare da rimanere con la lingua a
terra, compratevi un Vaio e portatevi in giro 2 Kg di portatile...). Il
software si interfaccia molto semplicemente ed in maniera molto diretta
con l'utente: come avrete visto dagli innumerevoli screenshots online, è
diviso in schede a seconda dell'area di competenza dei programmi, una
scelta molto intelligente. Ovviamente, non vi parlerò del software
programma per programma: sono cose che trovate scritte dappertutto e poi
OpenOffice lo conoscete anche meglio di me (si, è vero, OO su EEE carica
in 5 secondi). Quelle che sto per descrivere, sono le pecche evidenti
della distribuzione Xandros preinstallata.

Anzi, prima di tutto, cominciamo da una scelta molto saggia: KDE.
Onestamente non ho controllato quanta RAM venga impiegata per il solo
avvio del sistema, ma nel complesso non credo molta perché è veramente
reattivo. L'aspetto è WindowsXP- like (a partire dallo stile dei tasti
di chiusura, minimizza, ecc). Dicevo, le pecche: credetemi, mi sono
sentito un attimo **perso** quando, tentando di installare un pacchetto
via :span:`apt|code`, mi sono chiesto: "**dov'e il terminale**"?? Ebbene, il
terminale non è tra i programmi listati. Infatti, per averne uno bisogna
usare la combinazione di tasti CTRL+ALT+T. Non la trovo una scelta molto
saggia, ma comunque comprensibile, considerato il pubblico al quale è
destinato l'oggetto. All'inserimento di una penna USB, appare
un'iconcina nella traybar, pace all'anima sua... niente icona enorme,
bisogna andare a fare il tiro a segno nella tray. Comunque, vengono
montate automaticamente e viene visualizzata la classica finestra in cui
scegliere l'operazione da eseguire (dalla tradizionale apertura in
finestra ad altre opzioni a seconda del contenuto della perferica di
archiviazione). Se chiudiamo questa finestra bisogna andare a prendere
l'icona della USB in tray, non lo auguro a nessuno.

I repository attivati di default sono quelli della distro integrata. Non
hanno i 25.000 pacchetti di Ubuntu, ma per un uso essenziale dello
strumento vanno bene (ok, per un geek non esiste un uso essenziale,
LOL). Si possono tranquillamente aggiungere i repo di Debian e tentare
di installare qualcosa. Ma perché farsi del male in questa maniera?

eeeXubuntu
----------

Poco prima che arrivasse il pacco dell'Asus, il buon vecchio stinco di
santo di Alessio mi ha illuminato sull'esistenza si eeeXubuntu, una
versione di Xubuntu modificata appositamente per adattarsi alle esigenze
(spesso hardware) dell'Asus. Un esempio su tutti, il mitologico chip
Atheros del wifi integrato, che normalmente necessiterebbe di
ndiswrapper per essere sistemato a dovere, che con eeeXubuntu viene
riconosciuto e connesso al primo avvio. La trovo una cosa fantastica. Il
motto di eeeXubuntu, per il momento, è ancora "simply, works".
L'installazione è veramente molto semplice: si scarica la iso (circa 530
Mib se ricordo bene), la si masterizza, e si avvia la live riavviando il
PC. Dalla live, si apre un terminale e (dopo aver inserito una penna USB
da, immagino, qualcosa più di 530 Mib) si digitano pochi comandi, che
copieranno la live di installazione sulla USB. Si stacca la USB, la si
inserisce nell'Asus, si accende il portatilino, e come per magia, si
avrà davanti il solito menù della live. Si seleziona l'opzione di avvio
per Asus EEE (la seconda, credo) e si avvierà la live sul proprio Asus.
Il resto è esattamente come una normale installazione di X/K/Ubuntu.

.. figure:: {filename}/images/screenshot1ga7.png
   :width: 80%
   :align: center
   :alt: screen1

   Screen 1


Dopo l'installazione, è tutto funzionante e riconosciuto: il wireless
(ho faticato due giorni per far funzionare lo stesso identico chip
sull'Acer di mio fratello!), i tasti funzione: aumenta/diminuisci
luminosità, standby, arriva/disattiva wireless, ecc. Una delle cose che
si nota subito, è che non vengono riconosciuti i tasti di
aumenta/diminuisci/disattiva volume. A tutt'ora, l'unico modo per
ammutolire il mio Asus è abbassare manualmente il suono dal regolatore
di Xubuntu. Per il solo avvio, Xubuntu impiega solo 110/120 Mib dei 512
totali, un vero successo. Il rapporto tra mousepad e schermo è studiato
molto bene, a primo impatto il mousepad è troppo piccolo per uno schermo
del genere, ma "*la sensazione è illusoria*" (frase da Elii?). La mia
MMC, munita di apposito adattatore che l'ha fatta diventare una SD,
viene perfettamente riconosciuta e montata da eeeXubuntu, che ci impiega
meno di un nanosecondo, ed eccola lì sul Desktop.

Onestamente, non avevo mai usato Xubuntu (ho trascorso 2 anni su Kubuntu
e da qualche settimana sono passato ad Ubuntu). Non ha niente da
invidiare ai sui fratelli maggiori, ed è di una leggerezza mostruosa.

Le note dolenti (molto dolenti)
-------------------------------

Tra i tanti tasti funzione, c'è anche quello **dolente**: la webcam
integrata. Ovviamente, perfettamente funzionante e riconosciuta sulla
Xandros preinstallata (con una definizione d'immagine peraltro molto
gradevole), non viene automagicamente riconosciuta da eeeXubuntu. Ad
essere sinceri, non mi sono ancora informato in merito, ho solo
installato Skype e notato che la webcam non funge. In fin dei conti se
sono riuscito a far fungere l'Atheros a mio fratello, uscirò vivo anche
da questo. Se ci sono sviluppi, vi terrò aggiornati. Però non vi
nascondo che mi sarebbe davvero tanto piaciuto vederla funzionare a
dovere al primo avvio. E adesso, il tasto più cattivo, malvagio e
devastante di tutti: le penne USB.

Cercate di non piangere mentre lo dico: non vengono montate. Anzi, ci ho
speso 10 minuti, ma non sono riuscito a farle fungere. Parlo di
*qualsiasi* periferica di archiviazione USB. Sotto questo punto di
vista, eeeXubuntu mi ha molto deluso. Ma voglio smanettarci ancora un
po' prima di giungere a conclusioni affrettate, quindi abbiate pazienza.

.. figure:: {filename}/images/screenshot2ht4.png
   :width: 80%
   :align: center
   :alt: screen1

   Screen 1


La fisicità
-----------

La tastiera è ovviamente quella inglese (come ho specificato
nell'introduzione), e fortunatamente da un paio d'anni ho superato il
mio rapporto adolescenziale con la tastiera, e scrivo senza guardarla,
quindi per me non è cambiato niente, le lettere italiane sono sempre al
loro posto, anche se sui tasti le lettere non sono quelle. In molti vi
starete chiedendo se la tastiera sia così "plasticosa" come dicono.
Effettivamente, mi aspettavo molto peggio. Una volta fatta l'abitudine
all'insolitamente piccola dimensione dei tasti (che sono grandi
esattamente quanto i miei rinsecchiti polpastrelli callosi di bassista),
si scrive alla grande (anche se, personalmente, trovo che la "A" sia un
po' troppo a sinistra del *baricentro ideale* della tastiera, ed è la
lettera che dopo 10 giorni sbaglio ancora frequentemente). Come sempre,
è solo questione d'abitudine, dopo qualche ora o qualche giorno si
acquisisce piena padronanza della situazione.

Dimenticavo, la durata della batteria. La leggerezza e la modestia di
risorse di eeeXubuntu sembra in qualche modo aiutare noi poveri
giramondo: quelle poche volte che ho provato ad usarlo per ore
ininterrottamente in facoltà, dura realmente le 3 ore che sono indicate
nelle recensioni (badate, con il wireless disattivato e la luminosità
dello schermo a metà).

Conclusioni
-----------

So che non avete ancora tutte le risposte che vorreste, ma non riesco a
fare di meglio: il metro di valutazione di strumenti "ampi" come i
portatili (in questo caso sarebbe meglio parlare di UMPC) sono cosi vari
e soggettivi che sarebbe impossibile dare un senso compiuto ad ogni
singola impressione. Nel complesso, sono assolutamente entusiasta
dell'acquisto, anche perché prima mi portavo in giro (in facoltà,
s'intende) ogni giorno il mio fidatissimo laptop Dell da 1050€ (la
bellezza di 2,5 Kg circa). Adesso sono passato agli 850 g circa
dell'Asus EEE, e non immaginate quanto ne sia felice. Soprattutto per
chi, come me, non ha molto tempo per rivedere i propri appunti
dell'università o le dispense del prof (dopo 8 ore di lezione
giornaliere, permettete....), finalmente ho tra le mani un laptop che
posso comodamente uscire e mettere sulle ginocchia in treno, senza fare
acrobazie per evitare di uccidere le tre persone che mi circondano (i
treni pugliesi per il 40% risalgono ai gloriosissimi Anni '60, roba di
qualità!). Per quanto mi riguarda, l'Asus EEE sta aprendo un'era:
l'aumento di PC portatili di dimensioni ridotte faciliterà lo scambio
delle informazioni, ridurrà la costosissima (ed anti-ecologica)
comunicazione cartacea, e catapulterà una marea di nuovi utenti in rete,
liberando l'informazione (e le comunicazioni). D'altro canto, l'adozione
di un sistema operativo GNU/Linux convincerà gli utenti a superare i
pregiudizi secolari che continuano a circolare diffusamente sul software
libero. Speriamo che il mondo ne prenda consapevolezza, piano, piano....

*PS: ovviamente, questa recensione è stata scritta mentre sono in
macchina giù a casa della mia ragazza. La sto aspettando da mezz'ora,
sono collegato ad internet tramite la sua Fonera, e sto scrivendo
sull'Asus* ;)
