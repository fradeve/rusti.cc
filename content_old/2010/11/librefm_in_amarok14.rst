Utilizzare LibreFM su Amarok
============================

:date: 2010-11-08 14:00:00
:featured: yes
:tags: amarok

`LibreFM>`__ è nato come "clone" (anche se molto immaturo) di `LastFM`__. 
Per il momento l'unico servizio offerto è quello dello *scrobbling*, ovvero le statistiche
sulla musica ascoltata (che tra l'altro, per quanto ricordo, è l'unico
servizio offerto gratuitamente anche da LastFM). Le mie statistiche
personali, ad esempio, sono diponibili sul `mio profilo in LibreFM`__. LibreFM è basato
interamente su Software Libero, ed il sorgente del sistema è scaricabile
dal sito ufficiale del progetto (che si chiama in realtà
`GNUFM`__). È possibile
inviare le statistiche sulla propria musica a LastFM direttamente da
Amarok e da altri programmi di riproduzione musicale, e con questo
piccolo accorgimento sarà possibile invarle anche (o solo) verso
LibreFM.

-  Installare il pacchetto lastfmsubmitd

   ::

       :::bash
       sudo apt-get install lastfmsubmitd

-  Durante l'installazione, inserire il proprio nome utente e password
   di LibreFM e mantenere il gruppo "lastfm", quindi confermare.
-  Dare i permessi di lettura/scrittura al file di configurazione di
   lastfmsubmitd:

   ::

       :::bash
       sudo chmod 777 /etc/lastfmsubmitd.conf

-  In linea di massima, bisogna assicurarsi che l'utente con il quale si
   utilizza il pc sia nel gruppo indicato durante l'installazione
   (*lastfm*), e che il suddetto gruppo sia proprietario della cartella
   nella quale vengono tenuti i log della musica ascoltata da inviare a
   Libre.fm (ma per quest'ultimo punto, dovrete attendere l'ultimo punto
   della guida).

-  Modificare il file ``/etc/lastfmsubmitd.conf`` e fare in modo che il
   risultato finale sia questo (inserendo ovviamente al posto degli
   asterischi nome utente e password del proprio account libre.fm):

   ::

       :::bash
       [server]
       url=http://turtle.libre.fm/

       [account]
       user = *****
       password = *****

-  Scaricare e installare il plugin per Amarok 1.4:

   ::

       :::bash
       wget http://ebanana.orconhosting.net.nz/librefm.amarokscript.tar.gz

Da amarok: Tools --> Gestore script --> Installa script --> Selezionare
il tar.gz appena scaricato --> Esegui

-  Impostare i permessi nelle cartelle con i log e l'accesso al gruppo
   selezionato durante l'installazione:

   ::

       :::bash
       sudo chown :lastfm /var/log/lastfm/ /var/spool/lastfm/ -R
       sudo chmod -R 775 /var/log/lastfm/ /var/spool/lastfm/

-  Fare in modo che lastfmsubmitd si avvii automaticamente all'ingresso
   in Ubuntu, inserendo una voce in "Applicazioni d'Avvio": Sistema -->
   Preferenze --> Applicazioni d'avvio --> Aggiungi

   ::

       :::bash
       Nome: lastfmsubmitd
       Comando: /usr/bin/lastfmsubmitd
       Commento: qualsiasi cosa

Amarok 2
--------

Seguire esattamente la stessa procedura; lo script da installare si
chiama `Amarok2LibreFm`__
Un consiglio: se avete lo script attivo, evitate nella maniera più
assoluta di usare il player youtube integrato in Amarok 2 per guardare
video del brano che state ascoltando, perché lo script registra i dati
del video, la cui sintassi però non corrisponde a quella accettata nel
database di Libre.fm, per cui da quel momento in poi nessuna canzone
verrà inviata al sito. Ho testato personalmente il problema e sono stato
costretto a cancellare un paio di registrazioni dal log in
``/var/log/lastfm/``. Per ulteriori info sul funzionamento per Amarok 2,
consultare la `pagina apposita`__ sul wiki di Amarok.

Buono scrobbling!

.. _LibreFM: http://alpha.libre.fm
.. _LastFM: http://www.lastfm.it
.. _mio profilo in LibreFM: http://alpha.libre.fm/user/fradeve
.. _GNUFM: https://savannah.gnu.org/projects/librefm
.. _Amarok2LibreFm: http://kde-apps.org/content/show.php/Amarok2LibreFM?content=107339
.. _pagina apposita: http://userbase.kde.org/Amarok/Scrobbling_to_Libre.fm
