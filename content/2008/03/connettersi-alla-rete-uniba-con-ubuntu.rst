Connettersi alla rete Uniba con Ubuntu
======================================

:date: 2008-03-19 17:35:49
:tags: gnulinux, ubuntu

Introduzione
------------

Dopo qualche iniziale momento di perplessità, sono riuscito a far
connettere il mio Asus EEE con Ubuntu alla rete wifi messa a
disposizione dall'`Università degli Studi di Bari`_. Ho parlato di perplessità
perché ho provato per due giorni a connettermi e mi sono accorto solo
oggi di aver ricordato male la password (avevo cominciato a credere che
il problema fosse Ubuntu :D ).

.. _Università degli Studi di Bari: http://www.uniba.it/studenti/wifi

*Long story short*: prima di tutto occorre avere in mano il nome utente
e la password con cui ci si è registrati alla segreteria online
dell'università, `Esse3`_. Attenzione:
di regola l'iscrizione ad Esse3 viene effettuata nel momento stesso
dell'iscrizione all'Uni, quindi occorrerà mandare una mail
all'amministratore per far associare i propri dati alla registrazione
automaticamente effettuata. Posso garantirvi che il servizio è veramente
molto efficiente ed ho sistemato tutto nel giro di un solo pomeriggio.

.. _Esse3: http://www.studenti.ict.uniba.it/esse3/Start.do

Partendo dal presupposto che siate in possesso di un nome utente ed una
password, fate come me... dimenticateli! XD Una volta entrati in
dipartimento, cominciate a considerare che è meglio essere piuttosto
vicini ai router wireless, perché la ricettività non è molto ampia,
soprattutto per dipartimenti come quello di Geomineralogia con piani
molto ampi.

Ubuntu e le Proxy
-----------------

Da Ubuntu, il network manager troverà immediatamente le reti
disponibili: *wifi-uniba* e *wifi-studenti*. La prima è quella a cui
dovrete connettervi, la seconda è una vecchia rete che, sebbene
accessibile, sarà presto sospesa. Una volta ordinato al network manager
di Ubuntu di connettersi a *wifi-uniba*, apparirà una finestrella in cui
si dovrà selezionare il tipo di login. Dovrete selezionare (tra 4
opzioni) la modalità "**LEAP**" e nel sottomenù che vi appare,
selezionare il protocollo "**IEEE 802.1x**". La modalità LEAP prevede
(a differenza delle altre) l'inserimento di due valori, un nome utente
ed una password, che sono esattamente quelli con cui vi siete registrati
ad Esse3. Fatto ciò, dovreste essere connessi. Da terminale provate a
dare il comando

::

    ping www.google.it

per scoprire che effettivamente Google risponde.

Firefox
-------

Adesso occorre configurare tutti i servizi per accedere alla Proxy
attraverso la quale l'Università filtra il traffico in uscita. Per
esempio, potremmo partire da Firefox: vi consiglio di installare il
plugin SwitchProxy che permette di poter scegliere, mentre si usa
Firefox, se usare una Proxy (che dovremmo configurare) oppure navigare
normalmente con connessione diretta ad internet (è l'ideale per chi usa
lo stesso PC sia per navigare a casa in wifi sia in facoltà). Comunque,
la proxy è normalmente configurabile selezionando da Firefox

::

    MODIFICA -- PREFERENZE -- AVANZATE -- scheda RETE -- CONNESSIONE -- Impostazioni

e selezionando l'opzione "*Configurazione automatica dei proxy
(URL)*\ ", inserendo nel campo di testo l'indirizzo

::

    http://wifiproxy.ict.uniba.it/wifi.pac

Fatto ciò, fare clic su "Ricarica" e dare l'OK. Dovrebbe essere
possibile navigare. Alternativamente, è sempre possibile usare le
impostazioni manuali:

::

    Configurazione manuale del server proxy http: wifiproxy.ict.uniba.it
    Porta: 8080 

Altro
-----

Non voglio fare un post chilometrico su come impostare MSN, ma vi
suggerisco - purtroppo - di non usare Emesene (che ancora non supporta
il messaging da Proxy) e di cambiarlo con Pidgin (che sotto questo punto
di vista è più capace). Anche l'apt di Synaptic o Adept andrebbe
configurato adeguatamente: la guida è presente sul wiki di Ubuntu-it,
`qui`_. Ancora una volta Ubuntu
GNU/Linux sembra essere all'altezza di qualsiasi situazione ;) E,
soprattutto, funziona perfettamente con 1/3 della configurazione che c'è
da fare su XP!

.. _qui: http://wiki.ubuntu-it.org/ProxyClient

Buona navigazione!
