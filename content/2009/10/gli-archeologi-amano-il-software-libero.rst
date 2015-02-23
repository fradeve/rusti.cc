Gli archeologi amano il software libero
=======================================

:date: 2009-10-19 15:11:22
:tags: archaeology, gis, gnulinux, ubuntu

.. raw:: html

   <center>

|Practical Archaeology Course, measuring|\ \ *Practical Archaeology
Course by Wessex Archaeology, on Flickr, licensed CC-BY- NC-SA*

.. raw:: html

   </center>

Dov'è finito Fradeve? In molti se lo saranno chiesto vedendomi
scomparire dal blog per quasi un mese. Non si è nascosto in un bunker
antiatomico dopo le pericolose dichiarazioni del precedente post, ma è
semplicemente finito a mangiare polvere. Francesco è uno dei 50
volontari che per 6 settimane hanno "dato una mano" negli scavi
archeologici di `Siponto`__ 2009. Siponto (adesso quartiere turistico di
`Manfredonia`__ - FG) era una cittadina medievale sorta sulle vestigia 
dell'omonima città di epoca romana, tanto importante da essere riportata 
sulla `Tabula Peuntingeriana`__.

Siponto, ed altri scavi didattici (in Puglia un altro sito importante da
questo punto di vista è Egnazia, nei pressi di Monopoli) è un esempio di
come nella gran parte dei casi funziona (o non funziona) il settore dei
Beni Culturali in Italia. Considerato che non sono disponibili (da parte
delle Università, delle Regioni, del Comuni, ecc.) abbastanza fondi per
pagare gli operai, gran parte delle campagne archeologiche si basano
sulla buona volontà degli studenti di corsi di laurea come Storia
dell'Arte, Restauro, Diagnostica e Scienze applicate ai BB.CC.,
Archeologia, ecc.; studenti che lavorano gratuitamente 8 ore al giorno
(e conservano i dolori per la fatica fisica per un bel po' di giorni
dopo), sotto l'attenta direzione degli archeologi messi a disposizione
dalle università. Nei casi migliori, ogni 50 studenti ci sono 4 o 5
operai pagati per i lavori più pesanti. Agli studenti l'università paga
soltanto vitto e alloggio nel luogo dello scavo.

Ho sentito qualcuno affermare che l'archeologia non fosse una priorità
per il nostro paese. Ho anche sentito qualcuno ribadire che la cultura
non è fondamentale quanto lo sviluppo industriale. Il mio punto di vista
è del tutto opposto: vedo come fondamentale spinta all'economia
l'industria dei Beni Culturali; in Italia potremmo vivere solo di
quello. Sono veramente poche le zone italiane in cui non ci siano beni
culturali di un qualche interesse turistico, o che non riescano ad
offrire un paesaggio o dei prodotti tipici che tutto il mondo ci
invidia.

Eppure, lo sappiamo, per certe cose il denaro non c'è mai. Ed allora,
gli archeologi si arrangiano. O meglio, hanno cominciato scegliendo il
Software Libero perché è gratuito, ed hanno finito con l'adottarlo
perché offre maggiori possibilità ed è decisamente più flessibile di
quello proprietario. Tenendo anche conto del fatto che l'Archeologia
Stratigrafica è ormai una disciplina quasi geospaziale, e facile intuire
la quantità di software che possa orbitare intorno a queste esigenze. Di
seguito, ne riporto una brevissima lista:

-  **GRASS**: il software di analisi geospaziale per eccellenza,
   straordinariamente potente e flessibile, indicato per la gestione
   avanzata dei dati di scavo e per la costruzione di DEM e DTM;

-  **Quantum GIS**: più che un sistema di analisi, è un visualizzatore
   con qualche funzione di editing; il suo punto di forza risiede
   sicuramente, rispetto a GRASS, nella facilità di utilizzo e nella
   possibilità di scrivere plugin ad-hoc per qualsiasi tipo di utilizzo:
   per gli archeologi c'è il plugin in Python PyArchInit, creato da Luca
   Mandolesi;

-  **R**: software per l'analisi statistica, utilissimo per analizzare
   la distribuzione dei reperti ed ottenere nuove interpretazioni dei
   dati di scavo;

-  **gdal**: libreria geospaziale, indispensabile per gestire,
   convertire coordinate e tantissimi formati georeferenziati utilizzati
   oggi per trasferire i dati geografici;

-  **OpenLayers**: software in javascript per la visualizzazione online
   avanzata di dati cartografici, ricavati da tileserver (in forma di
   raster) o direttamente da database (usando per esempio MapServer);

-  **NVIZ**: va in coppia con GRASS, è un visualizzatore di dati
   geospaziali in tre dimensioni, e permette di creare interessanti
   prospettive di analisi, compresi modelli di elevazione digitale, ecc.

-  **Blender**: software per la creazione di modelli tridimensionali: se
   gli diamo in pasto le nuvole di punti rilevate con il laser-scanner,
   con un po' d'abilita riusciremmo ad ottenere modelli tridimensionali
   dei reperti ritrovati, che possono così essere spediti ed analizzati
   in tutto il mondo.

-  **Python**: grazie ai suoi moduli per la gestione del dato geografico
   e per la stesura di report partendo da database (reportlab), uniti
   alla semplicità d'apprendimento, è semplicemente il massimo per
   scrivere programmi adatti alla gestione del database archeologico.

-  **OpenOffice.org**: la suite da ufficio libera per eccellenza,
   integra una quantità straordinaria di strumenti interessanti per la
   gestione delle informazioni di scavo, in maniera del tutto analoga a
   Microsoft Office; uno tra tutti, lo strumento che permette di creare
   schede di unità stratigrafica partendo dal database in OpenOffice
   Base.

Tutti questi software, combinati insieme ed utilizzati sapientemente,
offrono possibilità del tutto maggiori e più stimolanti per lo sviluppo
di prodotti basati su dati archeologici. In Ubuntu tutto ciò può essere
installato facilmente tramite apt-get o con il comune gestore di
pacchetti. Non è un caso che sia stata proprio Ubuntu la distribuzione
scelta come base per il sistema operativo libero per gli archeologi,
`ArcheOS`__, sviluppato da `Arc-Team`__.

Ancora una volta, il software libero si dimostra non solo all'altezza
delle più sfrenate aspettative ed esigenze, ma molto più potente,
flessibile e creativo di quello proprietario. Archeologi, alla
riscossa!!

*PS: tempo fa (e mi scuso per il ritardo) `M.
Fioretti <http://digifreedom.net/>`__ mi ha segnalato un `suo
articolo <http://www.linux.com/archive/articles/55248>`__ su linux.com,
a proposito di archeologia open source: lettura vivamente consigliata.*

.. |Practical Archaeology Course, measuring| image:: http://dl.dropbox.com/u/369614/blog/img_red/2897528561_885ed21ae0.jpg
   :target: http://www.flickr.com/photos/wessexarchaeology/2897528561/
.. _Siponto: http://it.wikipedia.org/wiki/Siponto
.. _Manfredonia: http://it.wikipedia.org/wiki/Manfredonia
.. _Tabula Peuntingeriana: http://it.wikipedia.org/wiki/Tabula_Peuntingeriana
.. _ArcheOS: http://www.arc-team.com/archeos/wiki/doku.php
.. _Arc-Team: http://www.arc-team.com
