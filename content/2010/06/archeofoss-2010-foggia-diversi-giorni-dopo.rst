ArcheoFOSS 2011, Foggia: diversi giorni dopo
============================================

:date: 2010-06-01 18:42:41
:tags: ubuntu, openmoko, gnulinux, gis, foggia, archaeology

Ho ripescato dalla mia penna USB alcune annotazioni scritte in treno
durante i giorni dell'ArcheoFOSS di Foggia 2010. Le pubblico, con un pò
di ritardo ;)

.. figure:: {filename}/images/DSCF3738.JPG


   Le giovani leve del software libero in archeologia :)


ArchaeoFOSS, primo giorno
=========================

Ieri e oggi [sono stato] sarò a Foggia, nel Museo Civico, per il
`Workshop Nazionale sul Software Libero in Archeologia`_,
l'ArchaeoFOSS 2010. La conferenza è alla sua quinta edizione, e per
quanto possano piacerci i formalismi, permettetemi, è proprio il caso di
dire che "ruleggia". È diventata un'incredibile fucina di idee,
innovazione e proposte. La conferenza ha visto la partecipazione di più
di una cinquantina di persone, di diversa estrazione, ma uniti dal
proprio lavoro o dalla propria passione, l'informatica ed il software
libero applicati al campo archeologico. Il workshop, che l'anno scorso
era a Roma, quest'anno è stato ospitato nel Museo Civico di Foggia (che
consiglio a tutti di visitare, molto ricco e ben organizzato). Programma
della mattina:

- breve introduzione dei professori e del rettore;
- prima carrellata di interventi sulle tecnologie da campo open source
   (GPS e affini);
- pausa pranzo (è incredibile quanto siano convenienti i ristoranti in
   centro a Foggia);
- seconda carrellata pomeridiana sui database, condita da cenni sulle
   licenze libere;
- tanta allegria.

Volendo fare una breve panoramica, negli ultimi anni si è avuta una vera
e propria trasformazione del settore. Il campo dei beni culturali,
nonostante possa essere trainante per l'economia del Paese, sta vivendo
in questi anni un lento declino, dovuto soprattutto alla mancanza di
fondi per gli interventi di valorizzazione del patrimonio (ricordate il
crollo di una stanza della Domus Aurea a Roma qualche tempo fa?). A
questa situazione imbarazzante gli archeologi hanno risposto con il
software libero: è nata addirittura una distribuzione GNU/Linux,
ArcheOS, che integra tutto il software necessario al lavoro
"scientifico" dello scavo. Vi starete chiedendo: "sul serio gli
archeologi capiscono qualcosa di informatica?". Beh... si :) In soldoni,
lo scavo archeologico a partire dagli Anni '60 è diventato uno scavo
"stratigrafico", ovvero un'analisi minuziosa delle sovrapposizioni di
più "strati" di cultura umana nel corso dei secoli. Il compito
dell'archeologo è smontare pezzo per pezzo questi strati, rispettando la
cronologia e facendo un viaggio nel tempo partendo dal più esterno (e
recente) per finire allo strato più interno (antico).

In tutto questo processo analitico l'archeologo viene aiutato da
strumentazione scientifica importante: laser scanner, stazione totale,
database, nei casi più tecnologici persino reti wifi ad ampio raggio per
la trasmissione dei dati, reti bluetooth,  e soprattutto dispositivi GPS
e DGPS, sino ad arrivare a sistemi GIS anche molto complessi. Il
mestiere dell'archeologo sta diventando sempre più scientifico e sempre
più preciso, oltre che più tecnologico. Ma la tecnologia, si sa, costa.
Soprattutto quando l'hardware è molto particolare (ad esempio la
stazione totale, ed i driver sono proprietari. In quest'ottica,
l'importanza del Software Libero è fondamentale, perché permette di
risparmiare sulle licenze ed ottenere risultati identici se non migliori
di quelli ottenuti con software proprietari. Ed è così che nascono i
progetti presentati all'ArchaeoFOSS.

Anche in questo caso, è facile dirlo, molti di "noi" salgono già sulle
spalle dei giganti. Tanti software GIS offrono soluzioni già pronte per
immagazzinare i dati ed elaborarli secondo i più efficaci algoritmi.
Molti software per la gestione del dato geografico offrono soluzioni di
impressionante potenza per la gestione di basi di dati geografiche, come
PostGIS e PostgreSQL, passando per QuantumGIS e GRASS GIS. Salvo poi
svilupparle appositamente per le proprie esigenze, come accade in altre
occasioni. Oppure, tentare di sviluppare dei driver alternativi per il
trasferimento dei dati da dispositivi completamente proprietari, come
hanno fatto Stefano Costa e Luca Bezzi, con `TotalOpenStation`_, un 
software per il trasferimento dei dati registrati dalla stazione totale 
al PC e ai palmari dotati di sistemi operativi GNU/Linux, come
`Openmoko`_ o Maemo.

Ma le novità hanno raggiunto orizzonti impressionanti. Sono allo studio
da parte di alcune università di sistemi di analisi basati su software
GIS open source, mentre in alcuni punti d'Italia (soprattutto a Napoli e
`Foggia`_)
sono allo studio sistemi di ricostruzione di scavi archeologici in 3D,
in stile Second Life, realizzati rigorosamente su Debian e solo con
software open source (ricordate Blender?).

Comunque, resta invariata la mia opinione sulle comunità di sviluppo
open source: detto in parole spicciole "si sta troppo bene". Per quanto
le conferenze tra archeologi possano apparire "noiose" agli osservatori
esterni, bisogna riconoscere che la transizione è ormai completa: con
l'ArcheoFOSS assistiamo ad un libero scambio di idee, progetti ed
osservazioni, dibattiti accesi, confronti aperti in pieno stile open
source. Le giacche eleganti e le cravatte hanno abbandonato la sala per
fare spazio a soluzioni più "smart", come gli scarponcini da escursione
e i pantaloni con i tasconi. I taccuini lasciano spazio ai portatili. La
simpatia scorre a fiumi e l'atmosfera positiva permea un po' tutto. In
effetti, c'è molto da stare allegri. Ho visto persino qualche
partecipante in giro con una lattina di Coca "Ubuntu" :D Ce n'è insomma
per tutti i gusti. Ora sono in treno verso Foggia per una mattinata di
dibattito sullo scenario dell'open source in archeologia e per un
pomeriggio di laboratori pratici con MeshLab.

ArcheoFOSS, secondo giorno
==========================

Uno degli aspetti più interessanti dell'ArcheoFOSS è l'accento che è
stato posto sulla collaborazione: adesso lascio da parte la mia
inclinazione a considerare le discipline scientifiche più
"collaborative" di quelle umanistiche; d'altro canto è anche vero che
l'ambito archeologico è da sempre soggetto (almeno per la mia limitata
esperienza) a "particolarismi" nella ricerca e gelosia delle proprie
scoperte. Se questo comportamento può essere considerato "normale" o
"accettabile" nel contesto accademico, diventa assolutamente deleterio
quando si discute di software libero e ci si confronta sulle metodologie
scientifiche da applicare alla comunicazione e diffusione del dato.
Avere delle buone fonti, è importante. Citarle anche. Ma condividere
probabilmente lo è di più. Ma condividere significa anche avere delle
licenze che riescano a garantire le condizioni della condivisione, che
riescano a tutelare chi pubblica e chi utilizza il dato. Tali licenze
non dovrebbero essere necessariamente sviluppate da zero, esiste un
enorme e variegato ventaglio di possibilità, per divulgare sia contenuti
multimediali che database di varia natura. Insomma, il XXI secolo
porterà con se una modalità di ricerca che va ben oltre quella
tradizionale, che coinvolge tutti i ricercatori in varie discipline.

Multidisciplinarietà, ecco la parola d'ordine. È quindi naturale che
occorre coinvolgere nel nuovo panorama archeo-informatico persone che
abbiano un'idea precisa di cosa siano le licenze, così come sono
indispensabili archeologi, informatici, geek, geografi, analisti,
esperti nel 3D e nella storiografia, nello stesso tempo e nello stesso
luogo: la rete. Da questo punto di vista negli ultimi anni si sono fatti
enormi passi avanti, anche grazie alla consapevolezza che condividere
porta alla crescita, ma molto c'è ancora da fare. Un buon punto di
partenza è il sistema dell'istruzione superiore, l'ambiente accademico.
Gran parte dei laboratori di rilievo archeologico sparsi per la Penisola
usano solo software proprietario (e Bari non fa eccezione), laddove il
software libero in campo geografico costituisce un'eccellenza su sistemi
GNU/Linux.

Ecco, partire dall'istruzione significa formare una nuova generazione di
archeologi dalla mente aperta. Provando a discuterne con un professore
universitario, la prima obiezione mossa è stata "Ok, se volessi
cominciare domani, che risorse abbiamo? Possiamo scrivere delle
dispense?" L'osservazione è comprensibile e giustificabile. Ed ecco
secondo me il punto nodale: le risorse. Esistono centinaia di
pubblicazioni sull'argomento, ma pochi howto. Partendo dalla mia
esperienza nel campo del software libero, mi sembra quasi naturale che
il maggior coinvolgimento attivo di nuovi volontari si abbia nei
progetti ben documentati, che hanno un corpus di manuali e wiki
attivamente sviluppati ed aggiornati (un modello a noi vicino, tra
tutti, è proprio il wiki di Ubuntu-it). E qui torniamo a bomba.

Per sviluppare il settore del software libero in archeologia, i temi del
libero accesso alla conoscenza e della libertà di scelta, servono
persone consapevoli ed esperte. Queste persone vanno formate. Il luogo
di formazione, almeno in ambito archeologico, dovrebbe essere una specie
di limbo a metà strada tra la rete e le università. Ma per insegnare
serve una buona documentazione, che solo una comunità di sviluppatori
coesa è in grado di scrivere. La morale dal mio punto di vista: dobbiamo
fare comunità. Può sembrare quasi scontato, e forse non c'era bisogno di
tutte queste parole per arrivarci, ma credo di aver fatto un buon sunto
dei vari aspetti che portano a condensare l'importanza di uno spazio
aperto a tutti ma comune a tutti, dove si possano raccogliere le
esperienze, le idee e gli interrogativi sull'informatica libera
applicata all'archeologia e alla tutela dei beni culturali. Il nostro
punto di partenza: creare un wiki, un forum o un canale IRC, una mailing
list e un planet. Incontrarsi e discutere, essere multidisciplinari e
aperti, organizzare e creare degli standard: sono tutti attributi di una
comunità libera. Dopo qualche anno di ArcheoFOSS, quest'anno il
Laboratorio di Informatica Applicata all'Archeologia dell'Università di
Foggia si è accollata l'impegno di creare un'infrastruttura di
comunicazione. Cercherò dal canto mio di contribuire quanto più
possibile a costruire una realtà online nella quale confrontarsi.
Concludo con l'osservazione IMHO più interessante emersa quest'anno
(alla quale non posso però associare un autore): il tecnologo che aiuta
lo storico/archeologo è una figura superata: il tecnologo contribuisce
attivamente alla ricerca e all'introduzione di nuove idee.

Speriamo sia così :)

.. _Workshop Nazionale sul Software Libero in Archeologia: http://www.archeologiadigitale.it/archeofoss/2010.html
.. _TotalOpenStation: http://tops.berlios.de
.. _Openmoko: http://www.openmoko.com
.. _Foggia: http://www.archeologiadigitale.it/progetti/progetti.html
