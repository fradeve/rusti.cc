Title: Le sbalorditive prestazioni GPS del Neo FreeRunner
Date:  2008-04-24 22:47:41
tags: openmoko, ubuntu, gps

Nel giorno dell'uscita di Ubuntu Hardy, parlo di tutt'altro... Secondo un test
"amatoriale" effettuato da uno degli sviluppatori che ha in testing uno dei
circa 50 esemplari di **Neo FreeRunner** che attualmente girano per il mondo,
il ricevitore **GPS** integrato del Neo GTA02v5 (nome in codice con cui ci si
riferisce al modello in questione) sarebbe **più veloce del ricevitore GPS del
TomTom** e dell'[eTrex Geko][1]. I modelli in questione non hanno bisogno di
molte spiegazioni: il [TomTom][2] lo conoscete tutti; il Geko è un ricevitore
GPS che integra un display non touchscreen, utilizzato da molti
OpenStreetMappers per svolgere il loro lavoro di mappatura delle strade. Per
la sua maneggevolezza, è comunque uno dei migliori alleati degli sportivi che
fanno GeoCaching.

Tornando al Neo: il nostro tester ha provato ad accenderli tutti e tre, e a
cronometrare sia il tempo che i 3 ricevitori impiegavano per connettersi al
satellite ("a freddo"), il tempo che impiegavano a ricevere l'ora corretta
dal satellite e il tempo per divenire finalmente operativi, ricevendo dal
satellite la posizione corretta. In tutte e tre le occasioni, il Neo
FreeRunner si è dimostrato il migliore, in alcuni casi ha addirittura
dimezzato il tempo di connessione e quindi il tempo di operatività. Inutile
dire che tutte le misurazioni sono state effettuate nello stesso luogo alla
stessa ora (dato che i satelliti GPS si spostano intorno alla Terra). Infine,
bisogna ricordare che il Neo, il primo palmare/cellulare completamente Open
Source ed in molti casi, meglio, Free Software della storia, per il GPS
utilizza ancora (purtroppo) driver proprietari (i "gllin") forniti
dall'azienda che ha progettato il chip GPS. Per dovere di cronaca, un altro
sviluppatore ha confermato che il suo Neo FreeRunner funziona correttamente
come navigatore satellitare in città, ricevendo la posizione dal satellite con
un errore medio di circa 1 metro. Quindi, non resta che aspettare l'uscita del
Neo a fine aprile!! :D

Ecco l'email completa come è apparsa nella mailing-list degli sviluppatori:

> From my office, downtown Buenos Aires, indoors, 21th floor, facing north,
> clear field about 120 deg horizontally, 45 deg vertically, horizon at +5 deg,
> foggy afternoon, 15C, 50% humidity. All devices cold-started.
> 
> Garmin eTrex (2001): ~45s sees the first satellite ~75s gets a firm lock on it
> 5+ min still no position It does get the correct time.
> 
> TomTom GO (2004-ish ?) 20s gets time 20s sees satellites
> 7-8min later, gets a fix, but comes and goes
> 
> GTA02v5 (2008): ~10s sees 1st sat (in GSV sentence *) ~20s we have the time
> ~180s gets position
> 
> (*) GPS sentences are explained here:
> http://www.gpsinformation.org/dale/nmea.htm From my rooftop terrace,
> outdoors, 22nd floor, horizon at -5...0 deg for 240 deg hor, +10 deg very for
> 70 deg, +45 deg for 50 deg (yours truly standing in the way), i.e., almost as
> good as standing in the middle of the pampa in terms of clearance. Same
> weather conditions.
> 
> Garmin: 15s sees satellites 50s gets first firm satellite fix 110s gets
> position
> 
> TomTom: 50s gets position
> 
> GTA02: 45s gets first firm satellite fix (in GSA sentence) 60s gets position
> 
> Full disclosure: the GTA02 had a slight advantage because I left the top off,
> so it could also see satellites that would normally be covered by the
> earpiece.

   [1]: http://wiki.openstreetmap.org/index.php/Garmin#Geko_201

   [2]: http://www.tomtom.com/?Lid=7
