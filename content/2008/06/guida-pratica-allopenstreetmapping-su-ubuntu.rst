Guida pratica all'OpenStreetMapping su Ubuntu
=============================================

:date: 2008-06-01 09:43:13
:tags: gnulinux, nokia, openstreetmap, python, terlizzi, ubuntu, wikipedia


.. figure:: {filename}/images/magmap120x120iy3.png
   :alt: http://www.openstreetmap.org

Questa guida non ha la pretesa di essere esauriente, e per forza di cose
alcuni argomenti piuttosto lunghi o che richiedono semplicemente la sana
lettura di qualche pagina tecnica verranno saltati a piè pari. Invece,
troverete qui il riassunto della mia piccola esperienza di mapper, e
tanti consigli su come affrontare il mapping. L'obiettivo è dare delle
risposte alle domande che solitamente vengono fatte sul canale IRC, e
farvi risparmiare tempo.

1) Perché OSM?
--------------

Voglio evitare di ripetere quanto scritto nei `precedenti post`_
quindi faccio un riassunto:

-  per creare una cartografia libera del pianeta
-  per ottenere una cartografia corretta e dettagliata del pianeta
   (senza villaggi fantasma e uova di pasqua)
-  per liberare i geodati e sensibilizzare il pubblico al tema dei
   prodotti degli investimenti pubblici che dovrebbero essere proprietà
   comune (la cartografia finanziata con i soldi pubblici non e di
   pubblico dominio in quasi tutti gli stati europei)
-  per fare sport, per rivalutare la bicicletta e il trasporto
   sostenibile, per valorizzare le piste ciclabili, i percorsi pedonali
   e la mobilita ecologica ed alternativa.

Spero di non aver dimenticato niente, si accettano suggerimenti.

.. _precedenti post: http://fradeve.org/2008/05/perche-google-maps-fa-schifo.html

2) Cosa serve?
--------------

Un navigatore satellitare di qualsiasi genere: va bene un Garmin,
TomTom, sia da auto che pedonale, cosi come è possibile utilizzare
qualsiasi dispositivo in grado di registrare i dati del GPS che abbia un
minimo di mobilità: un portatile, un cellulare con bluetooth, possono
essere collegati senza fili all'antenna GPS (prezzo indicativo intorno
ai 50€). Personalmente, utilizzo un Nokia 6630 con antenna bluetooth
Hamlet (chip GPS SirfStrar III).

3) Come acquistare?
-------------------

Ognuno ha i suoi canali d'acquisto preferiti: Trony, MediaWorld, il
negozio sotto casa, eBay. Se siete principianti ed avete un telefonino
od un palmare con bluetooth e che permetta di installare almeno un
programmino, vi consiglio di cominciare con i mezzi che avete, senza
spendere un centinaio di euro in altri navigatori. In fin dei conti, ciò
che ci interessa è solo registrare i dati dal GPS, tutto il resto è solo
questione di comodità. La scelta delle antenne bluetooth è relativamente
ampia, vi consiglio un'antenna con chip SirfStar III.

4) Il software
--------------

Solitamente, i programmi installati nei navigatori da auto non includono
alcun programma per registrare le tracce GPS. In questa guida tratteremo
soltanto la configurazione dei Nokia con Symbian v2 e v3. È comunque
possibile installare applicazioni adeguate anche sul TomTom, e tutte le
informazioni in merito possono essere trovate sul Wiki ufficiale di OSM
(`qui`_ per la precisione) o chieste direttamente sul canale IRC italiano. Per il mio
Nokia 6630 (e quindi faccio riferimento anche a tutta la Serie60 e quasi
tutta la Serie N), utilizzo due programmi: AFTrack e WhereAmI. Il primo
è software proprietario (si acquista direttamente dal sito del
produttore per circa 10€, ed è reperibile anche attraverso le solite vie
"traverse" e non legali). WhereAmI è software libero sotto licenza GNU.
In generale, fanno sostanzialmente le stesse cose, ma ritengo che
AFTrack sia più versatile e semplice da usare, lo raccomando ai meno
esperti, anche se sono uno strenuo difensore del software libero.
Entrambi permettono di registrare le tracce GPS ma WhereAmI permette
anche di visualizzare agevolmente le mappe scaricate da OSM, e quindi di
testarne l'accuratezza (è teoricamente possibile farlo anche con
AFTrack, ma è molto più complesso impostarlo, io non ci sono riuscito).
Nella mia esperienza quotidiana, è possibile usare AFTrack per
registrare le tracce GPS, e WhereAmI come navigatore che utilizza le
mappe di OSM, testando quelle da create personalmente.

.. _qui: http://wiki.openstreetmap.org/index.php/GPS_Reviews

5) Cominciamo
-------------

Una volta installato AFTrack (meglio installarlo sulla MMC e non nella
memoria del Nokia), all'avvio chiederà di accendere il bluetooth per
collegarsi all'antenna GPS, che viene riconosciuta nel giro di qualche
secondo. Ho volutamente tralasciato il processo di prima accensione
dell'antenna, che varia a seconda della marca e del modello (si presume
quindi che l'antenna sia già accesa e funzionante). Ricordate che spesso
le antenne impiegano qualche minuto per collegarsi ai satelliti, è bene
aspettare che siano già collegate prima di aprire AFTrack. Il programma
è strutturato in "schede", ognuna delle quali contiene informazioni
sulle attività in corso del programma; la descrizione completa delle
funzionalità è contenuta nel `sito ufficiale`_.

-  Direzione: contiene la bussola con la direzione attuale;
-  Posizione: indica la posizione attuale e fornisce dati in tempo reale
   su posizione e velocità;
-  Andatura: velocità dello spostamento, il minimo, massimo, la media;
-  Mappa: è sicuramente la scheda più interessante, contiene la mappa
   delle tracciature delle coordinate GPS (tracks) da noi percorse in
   tempo reale. Ha funzione puramente informativa. Sulla Mappa, il
   pallino verde in basso a sinistra contiene il numero di satelliti
   agganciati, che e auspicabile sia almeno di 6.

.. _sito ufficiale: http://www.afischer-online.de/sos/AFTrack

6) Impostare software e hardware prima di partire
-------------------------------------------------

Entrate in macchina, salite sulla bicicletta, cominciate a camminare,
salite sul treno, quel che vi pare. È tuttavia sempre importante
posizionare l'antenna GPS nel punto più alto del proprio corpo (o del
mezzo in cui ci si sta muovendo), per ricevere bene anche il segnale dei
satelliti alle proprie spalle. Se siete in bici o a piedi, l'ideale
sarebbe fissare l'antenna sul proprio casco (si, qualcuno lo fa). In
auto, il ricevitore sul cruscotto va benissimo. Dato che antenna e Nokia
comunicano via bluetooth, potete metterli in tasche diverse, nella
giacca, nel portaoggetti dell'auto, nello zaino o comunque non per forza
l'uno vicino all'altro. Prima di cominciare, è utile impostare un po'
AFTrack. Il programma non fa altro che registrare, in base a schemi
configurabili, le coordinate, l'altitudine e l'ora esatta in una
sequenza, che formerà un percorso (track) poi esportabile in un file
(IGN). Dobbiamo regolare la maniera in cui il programma registrerà i
punti: potrebbe registrare un punto ogni X secondi, oppure variare la
frequenza di registrazione dei punti in funzione del fatto che siamo a
piedi, in bici o in auto. Tutto ciò è regolabile dal menù *MENU*. Per
esperienza personale, uso sempre la modalità più "intensiva", ovvero 1
punto / secondo. Fatto ciò, posizionate AFTrack sulla scheda che più vi
interessa (di solito Posizione o Mappa), premete il tasto sinistro del
Nokia, e dal menù "Percorso" selezionate "Inizia percorso". Da questo
momento in poi, il programma comincerà a registrare il vostro percorso,
quindi... buon mapping!

Come prima mappatura, vi consiglio di fare avanti e indietro per un paio
di centinaia di metri, giusto per ottenere un primo semplice tracciato.
Quando avete finito, selezionate il menù con il tasto sinistro "Percorso
-- Stop percorso". NON CHIUDETE il programma.

7) Esportazione e conversione delle tracce
------------------------------------------

AFTrack permette di esportare il percorso in formato IGC, tramite il
menù "Percorso -- Esporta percorso (IGC)". Il file viene salvato in C: o
E: (a seconda di dove avete installato il programma)

::

    E:/Nokia/Others/AFTrack/nomefile.igc

Per navigare tra le cartelle del Nokia vi consiglio il programma
`FExplorer`_. Potete
inviarlo via bluetooth al PC, oppure inserire la MMC in un lettore
apposito integrato nel PC/portatile oppure da lettore esterno via USB.
Una volta copiato il/i file nel PC, occorre convertire il file IGC in
GPX, formato universalmente compatibile, accettato da OpenStreetMap. Per
farlo, possiamo usare l'arcifamoso programma GPSBabel. Su Ubuntu si
trova già nei repository, dovrebbe essere così anche per altre
distribuzioni. In generale, su GNU/Linux GPSBabel funziona solo da riga
di comando, mentre per Windows c'è un programma in *.exe* dotato di una
comodissima interfaccia grafica. Se come me non avete tempo e voglia di
destreggiarvi con decine di opzioni da terminale, installate Wine su
GNU/Linux e fate partire l'exe per Windows: il programma è standalone e
non necessita di installazione. Una volta avviato GPSBabel,
l'interfaccia forse non è il massimo dell'intuitività, ma meglio del
terminale (almeno per me). Dal primo menù a tendina selezionare come
formato di input FAI/IGC. Nella prima riga, con il pulsante a destra si
possono sfogliare le cartelle e caricare il proprio file IGC. Nella
seconda riga, premere sempre il pulsante a destra per selezionare un
percorso in cui salvare il file, dandogli un nome che termini con
".gpx". Premere "Let's Go" per avviare la conversione, che dovrebbe
essere istantanea. Possiamo chiudere GPSBabel. È possibile fare la
stessa cosa da terminale, il comando è (ovviamente, posizionarsi nella
cartella che contiene i file igc prima di dare il comando):

::

    gpsbabel -i igc -f nomefile.igc -o gpx -F nomefile.gpx

Per tenerlo meglio a mente, la struttura delle opzioni comando dovrebbe
essere questa (correggetemi se sbaglio):

-  **-i**: "input", viene seguito dall'estensione del file da
   trasformare (nel nostro caso, igc);
-  **-f**: "file" identifica il nome del file di input;
-  **-o**: "output", viene seguito dall'estensione del file di
   destinazione (per noi, gpx);
-  **-F**: "File" identifica il nome del file di output.

.. _FExplorer: http://www.gosymbian.com/fexplorer_new.php

8) Elaborare e disegnare la mappa
---------------------------------

Adesso siamo al bivio tra due filosofie di pensiero, e la soluzione sta
sempre nel mezzo. *Long story short*: la base del sistema di OSM è un
grande database di tracce GPX, che vengono poi messe tutte insieme e
sulle quali, tramite un editor, si disegna la mappa. Quindi, possiamo
dire che le tracce GPX delle strade da noi percorse fungono da
"riferimento visivo" per disegnarci sopra la strada, piazza, chiesa,
rotatoria, ecc.. Sarà il layer da noi disegnato a costituire la mappa
vera e propria, e verrà caricato anch'esso su OSM, andando ad integrare
le mappe già disegnate da altri (se nella nostra zona ci sono altri
mapper). Quindi, semplificando, possiamo dire che tutto il lavoro su OSM
e organizzato su due livelli paralleli:

1. livello "inferiore", dei GPX, funge da riferimento
2. livello "superiore", della mappa, e il risultato della nostra
   attività di disegno della mappa

I file GPX possono essere utilizzati in locale, sul proprio PC, per
disegnare la mappa che poi verrà caricata su OSM, oppure possono essere
prima caricati su OSM e poi utilizzati. La differenza tra le due
situazioni è che nella prima solo noi avremo a disposizione il
riferimento dei GPX, mentre nel secondo caso, essendo caricati su OSM,
sono a disposizione di tutti, e si potrà dare l'opportunità anche ad
altri di usarli come riferimento per disegnare le strade nella zona.
Personalmente, vi consiglio sempre di caricare i GPX. Per farlo, è
necessario registrarsi sulla mappa di OSM, come se si fosse su
Wikipedia. Dal proprio profilo personale, è possibile caricare i file
GPX, associando ad ogni file caricato una descrizione ed un tag, che
permetterà agli utenti di rintracciarlo facilmente in caso di necessita.
Ovviamente, è meglio se il tag è un toponimo, ovvero il nome della
località mappata (per esempio, i miei tag contengono il nome di
"terlizzi", "molfetta", "canosa", ecc - `vedi qui`_).
Purtroppo, le risorse di banda attualmente a disposizione del progetto
sono inferiori a quelle che servirebbero, motivo per cui ci vuole più di
qualche ora perché una traccia venga caricata (vi consiglio di metterle
a caricare la sera, e la mattina dovreste ricevere l'email di conferma
dell'avvenuto upload).

.. _vedi qui: http://www.openstreetmap.org/traces/mine/tag/terlizzi

Adesso, è tempo di imparare qualcosa sugli editor. Ovviamente, non mi
sogno neanche lontanamente di insegnarvi ad usare i due editor esistenti
per OSM (sono niubbo persino io, e per quello ci sono ottime guide in
italiano sul wiki di OSM), ma piuttosto di rispondere ad alcuni
interrogativi comuni che tutti prima o poi ci poniamo. I due editor
disponibili si chiamano Potlatch e JOSM. Potlatch è un editor online,
accessibile solo via browser (bisogna quindi essere per forza connessi
ad internet), ha il vantaggio di essere estremamente semplice e molto
diretto; è l'ideale per i principianti ma anche per gli esperti che
abbiano voglia di fare modifiche veloci e senza troppe pretese. Al
contrario, JOSM è un programma in Java, da scaricare sul PC, eseguibile
anche offline, contenente molte opzioni per gli esperti, ed espanso
tramite vari plugin che aggiungono molte funzionalità. La differenza
secondo me più importante tra i due e legata (oltre a quelle citate
prima) all'impostazione del lavoro. Infatti, se vogliamo lavorare su
Potlatch, e INDISPENSABILE aver caricato i nostri GPX su OSM, e ciò può
richiedere anche un giorno intero, a seconda del carico dei server. Ciò
significa che se ho una voglia pazza di fare OSM, esco in bici la
mattina alle 8, torno a casa alle 10, se uso Potlatch devo per forza
prima caricare i GPX ed aspettare almeno 5 ore finché il server le
carichi; ciò rende impossibile per me lavorare sulla mappa quella
mattina stessa, ma mi lega ai tempi d'attesa dei server di OSM. Al
contrario, con JOSM abbiamo un comodo bottone "Apri" per caricare nel
programma i GPX e disegnare la mappa, che poi può sia essere caricata
direttamente sui server, sia salvata in un file con estensione ".osm"
sul proprio PC, per essere caricata in un secondo momento, magari perché
mentre la stiamo disegnando non siamo in linea.

9) Un insano aiuto per l'editing
--------------------------------

Quando vi troverete a dover disegnare le strade su un file GPX, spesso
la tentazione sarà quella di aprire Google Maps e guardare come sono
posizionate le vie, perché magari non vi ricordate esattamente lungo
quali vie siete passati. Ricordate che il vero mapping prevede che,
oltre a registrare i GPX, dobbiate anche segnarvi su un taccuino il nome
delle vie che attraversate, perché la posizione delle vie e i nomi
forniti da Google Maps sono totalmente inaffidabili. Fatte queste
precisazioni, potrebbe esservi utile `questo link`_:
è un sito che permette di caricare i
propri GPX e "sovrapporli" ad una cartina di Google Maps, in modo da
avere almeno idea delle strade percorse, se non le ricordiamo. Per
caricare i file c'è la casella "Upload your GPS data file here", che
accetta molti file diversi (anche GPX e IGC) e può sovrapporne fino a 3
contemporaneamente.

Appena selezionati i file, premere il pulsante "Draw the map" in fondo a
destra. ***RIPETO:** non fidarsi troppo di GMaps e soprattutto, nella
maniera più assoluta, non copiare i nomi delle strade da li! Utilizzate
questo servizio solo se siete disperati e cercate sempre di preferire il
taccuino a Google Maps, che potrebbe inficiare ciò che vogliamo
realizzare: una mappa libera, pulita, sicura.*

.. _questo link: http://www.gpsvisualizer.com/map

10) Visualizzare i risultati
----------------------------

Adesso, tutti quanti vorremmo vedere la nostra mappa trasformarsi in un
bel file SVG o PDF. Per gli utenti meno smaliziati, purtroppo, c'è da
aspettare. Una volta che i dati sono stati caricati sui server di OSM,
la mappa principale, quella disponibile all'indirizzo
`www.openstreetmap.org`_, viene aggiornata ogni
martedì. Ciò significa che se abbiamo fatto delle modifiche il mercoledì
mattina, dovremo aspettare la sera del martedì successivo per vedere
(soddisfatti) cosa abbiamo combinato. Per fortuna, esistono dei metodi
per scavalcare l'attesa ed ottenere una visualizzazione più rapida:
`www.informationfreeway.org`_ offre la
visualizzazione dei dati di OSM entro un intervallo di un paio d'ore
(comunque variabile a seconda della quantità di strade presenti
nell'area in cui si sta operando). Per utilizzare informationfreeway, è
necessario fare una "richiesta" di aggiornamento dell'area interessata.
Per farlo, zoomare la mappa nell'area su cui abbiamo lavorato, fino a
quando non compaiono dei quadrati tratteggiati in rosso. Posizionarsi
sul quadrato che racchiude l'area che ci interessa, e premere il tasto
"r". Nel giro di qualche ora potremo ritornare in quel punto della mappa
e vedere le modifiche che abbiamo apportato. Ora, è forse il caso di
spendere due parole sulle differenti modalità di "rendering", ovvero di
generazione della mappa.

.. _www.openstreetmap.org: http://www.openstreetmap.org>
.. _www.informationfreeway.org: http://www.informationfreeway.org

La mappa di informationfreeway.org è generata da
`Osmarender`_, un software che per mezzo di un
insieme di regole che permettono di creare la mappa con un certo stile,
che pero non è quello "ufficiale" di openstreetmap.org, che invece è
generato da `Mapnik`_, un altro software che usa differenti
regole. La differenza tra i due stili, per un occhio
non esperto, è legata a pochi dettagli grafici della mappa. Questa
spiegazione è essenziale per capire che, dato che tutti i programmi
utilizzati in OSM sono `software libero`_, è possibile
scaricare sul proprio PC sia Osmarender sia Mapnik, e creare
direttamente sul proprio PC la propria mappa, senza aspettare
openstreetmap.org o informationfreeway.org. Da questo punto di vista, la
differenza tra Osmarender e Mapnik è che il primo è molto più semplice
da eseguire sul PC, mentre l'altro necessita di molte configurazioni.
Per quella che è la mia esperienza, ho notato che su distribuzioni
GNU/Linux e molto semplice utilizzare Osmarender.

.. _Osmarender: http://wiki.openstreetmap.org/index.php/Osmarender
.. _Mapnik: http://wiki.openstreetmap.org/index.php/Mapnik
.. _software libero: http://it.wikipedia.org/wiki/Software_libero

11) Osmarender sul PC
---------------------

Con pochi semplici passi, è possibile ottenere, partendo dai dati di
OSM, una mappa in SVG perfettamente disegnata, grazie ad Osmarender.
Ecco come procedere:

1. Creare nel proprio PC (in questo esempio do per scontato che la
   cartella venga creata nella Home) una cartella in cui salvare i file
   che andremo a scaricare; in questo esempio la chiameremo
   "osmarender".

2. Scaricare i seguenti file e spostarli nella cartella appena creata:
   `osm-map-features-z17.xml`_, `osmarender.xsl`_

3. Aprire JOSM, scaricare i dati relativi alla zona che ci interessa e
   salvarli in un file di nome "data.osm" (rispettate il nome,
   altrimenti non sarà possibile creare la mappa!). Anche questo file va
   inserito nella cartella "osmarender".

4. Installare i seguenti programmi (su Ubuntu si trovano tranquillamente
   nei repository; ecco una `guida all'installazione`_
   per i principianti):
   `xmlstarlet`_, `inkscape`_

5. Nel terminale, digitare il seguente comando, impostandolo a seconda
   delle proprie esigenze (questo va benissimo se avete seguito le
   istruzioni sopra):

       xmlstarlet tr ~/osmarender/osmarender.xsl ~/osmarender/osm-map-features-z17.xml > ~/osmarender/map.svg

Quando avrà terminato, nella cartella apparirà un file "map.svg", che
potrete aprire con Inkscape. Bello, vero? Potrebbe essere necessario
zoomare molto prima di poter vedere il paese sul quale state lavorando,
dipende dalle dimensioni dell'area che avete scaricato su JOSM. In
questo modo, qualsiasi modifica vogliate fare ad un file .osm su JOSM,
potrete vederlo in diretta generando il file svg sul PC, senza aspettare
ne ore ne giorni. Se volete evitare l'eventuale problema dello zoom che
avete appena incontrato, leggete il seguito.

.. _osm-map-features-z17.xml: http://svn.openstreetmap.org/applications/rendering/osmarender6/osm-map-features-z17.xml
.. _osmarender.xsl: http://svn.openstreetmap.org/applications/rendering/osmarender6/osmarender.xsl
.. _guida all'installazione: http://wiki.ubuntu-it.org/AmministrazioneSistema/InstallareProgrammi
.. _xmlstarlet: http://packages.ubuntu.com/search?suite=default&section=all&arch=any&searchon=names&keywords=xmlstarlet
.. _inkscape: http://packages.ubuntu.com/search?suite=default&section=all&arch=any&searchon=names&keywords=inkscape

12) Renderizzare aree specifiche con xmlstarlet
-----------------------------------------------

Da questo punto in poi, le impostazioni che andremo ad illustrare sono
essenzialmente per esperti, o per chi non si accontenta di renderizzare
tutto il file .osm. Mi spiego meglio: personalmente, mi sono imbattuto
nella necessità di lavorare su un'area molto ampia: solitamente su JOSM
scarico dati di due province intere (Bari e Barletta-Andria-Trani). Ciò
significa che spesso il file svg generato è veramente enorme e, oltre ad
essere lento nell'apertura, necessita di ampie zoomate per poter vedere
un singolo paese che magari ci interessa. È possibile impostare il file
delle regole con cui viene creato l'svg (osm-map-features-z17.xml) in
maniera tale che, anche partendo da un'ampia area di dati nel file
data.osm, renderizzi in svg solo una certa area da noi selezionata. Per
farlo, occorre procurarsi 4 valori: la coppia di minimo di Latitudine e
Longitudine e la coppia di massimo di Latitudine e Longitudine. Per chi
non fosse pratico di cartografia ho creato uno script in Python che
facilita molto l'operazione. Lo script (scaricabile dalla mia `pagina personale`_
nel wiki di OSM) è eseguibile con il comando da terminale "python
osmastart.py" (si da per scontato che abbiate installati i pacchetti
base di Python sul vostro PC). La mia piccola creazione permette di
scrivere (all'interno dello script) le coordinate di al massimo 3 aree
da renderizzare, che poi vengono visualizzate nel menù all'avvio dello
script. Ho in lavorazione una versione dello script molto più completa
ed accattivante, ma per il momento non ancora completa.

.. _pagina personale: http://wiki.openstreetmap.org/index.php/User:Fradeve11

13) Interagire con la comunità: le statistiche
----------------------------------------------

Nei progetti aperti e collettivi, e veramente molto importante
interagire con la comunità, soprattutto in un argomento così delicato
come le mappature. Gli esperti ragazzi del canale IRC italiano e di
quello internazionale (in inglese) sapranno fare fronte alle domande più
assurde che potranno venirvi in mente. Ultimamente, OSM si e dotata di
un "contenitore di statistiche" che permette di osservare chi sta
lavorando nella zona vicina alla vostra, o proprio accanto a casa
vostra, che magari non conoscete neanche (a me è capitato! ciao
Vincivis!). Il progetto delle statistiche si chiama
`OSMLab`_ e mette a disposizione una serie di mappe (sia osservabili 
online sia su Google Earth) in cui sono `segnate le posizioni`_
di tutti i partecipanti ad OSM nel momento in cui hanno fatto una
modifica alla mappa, e sono aggiornate quotidianamente.

Spero vivamente di non aver dimenticato niente. Sicuramente avrò
commesso delle imprecisioni, chiedo scusa per questo in anticipo ai
niubbi come me e agli esperti, ma l'intento della guida era la
chiarezza. Ovviamente, per qualsiasi domanda, commentate pure, cercherò
di rispondere come posso... Buon mapping!

.. _OSMLab: http://code.google.com/p/osmlab
.. _segnate le posizioni: http://www.fxfoo.com/osm/kml/web/web-osm-world-day-latest-v0-openlayers.html?zoom=10&lat=41.27755&lon=16.61356&layers=B0T
