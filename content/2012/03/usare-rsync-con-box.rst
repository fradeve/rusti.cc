Usare rsync con Box.net
=======================

:date: 2012-03-23 23:00:00
:featured: yes
:tags: server
:modified: 2012-04-17

In questi giorni, `Box.net`_ sta regalando 50 Gb di
spazio a chiunque apra un nuovo account e faccia almeno un login
dall'applicazione ufficiale per Android, occasione davvero ghiotta. È la
prima volta che utilizzo questo servizio e la prima cosa che ho notato,
con enorme sconcerto, è che Box.net non supporta in nessun modo il
*timestamp* dei file. In altre parole, tutte le informazioni presenti
nel file relativi alla data dell'ultima modifica (tanto per dirne una)
vengono sovrascritte, con `sommo disappunto degli utenti`_.
Per chi avrebbe tanto voluto 50 Gb di cloud per fare una copia speculare
e sincronizzata delle proprie foto, video, documenti con lo
straordinario `rsync`_, tempi bui.

Almeno, fino all'arrivo di tale S0M30N3 che, in un fantastico quanto
`conciso howto`_
ha tirato fuori dal cilindro un sistema per usare rsync in una
partizione criptata con `EncFS`_ creata
all'interno della propria Box cloud. Ho testato personalmente il gioco
e, porca paletta, funziona. Il tutorial che segue è stato provato su
Ubuntu 11.04.

.. _Box.net: http://box.net
.. _sommo disappunto degli utenti: http://community.box.com/boxnet/topics/does_box_net_support_timestamps?from_gsfn=true
.. _rsync: https://rsync.samba.org
.. _conciso howto: http://www.heise.de/mobil/newsticker/foren/S-Re-rsync-zu-Box-net/forum-222786/msg-21487182/read
.. _EncFS: http://www.arg0.net/encfs

Pro
~~~

- i dati vengono trasmessi via https e inseriti in una partizione
  criptata all'interno della cartella: sono illeggibili da chiunque non
  conosca la password non solo dell'account Box.net, ma del filesystem
  criptato
- è l'unico modo per usare lo straordinario rsync con i propri 50 Gb di
  cloud
- tutti i vantaggi che derivano da rsync: personalizzazione del backup,
  integrazione con cron, ecc.

Contro
~~~~~~

- i dati essendo cifrati sui server di Box.net, non possono essere
  letti dalle varie app (compresa quella per Android); occorre avere
  una macchina su cui montare la partizione EncFS e solo allora potremo
  accedere ai dati; a anche se, a ben pensarci... leggete fino in fondo ;)
- Box.net per gli account gratuiti ha un limite di 100 Mb/file, non
  dimenticatelo; lo script di rsync riportato di seguito penserà a
  limitare la sincronizzazione ai soli file al di sotto di questa
  dimensione
- la sincronizzazione sembra essere un po' lenta

1 - Montare la Box in ``/media`` tramite WebDAV
-----------------------------------------------

La cartella di WebDAV può essere montata sia dall'utente che sta
utilizzando la macchina sia dall'account di root. In questa guida è
seguita la prima opzione, che unita ad una adeguata `cifratura della cartella Home`_,
permette di mantenere un buon livello di privacy sui propri dati.

.. _cifratura della cartella Home: http://steghide.sourceforge.net/documentation.php

Installare davfs2

.. code-block:: bash

   sudo apt-get install davfs2

Permettere all'utente non-root di montare DavFS, rispondendo ``Yes``
alla riconfigurazione del pacchetto

.. code-block:: bash

   sudo dpkg-reconfigure davfs2

Aggiungere l'utente che utilizzerà DavFS2 al gruppo omonimo:

.. code-block:: bash

   sudo adduser $USER davfs2

creare la cartella in cui verrà montata la Box

.. code-block:: bash

   sudo mkdir /media/box

inserire la seguente riga in ``/etc/fstab``:

.. code-block:: bash

   https://www.box.com/dav /media/box      davfs   noauto,user   0   0

Il file `/etc/davfs2/davfs2.conf` contiene le impostazioni valide per
tutto il sistema; decommentare la seguente riga:

.. code-block:: bash

   use_locks       0

Creare una copia del file delle configurazioni nella propria home

.. code-block:: bash

   mkdir ~/.davfs2
   cp /etc/davfs2/davfs2.conf ~/.davfs2

Per evitare di dover inserire ogni volta le credenziali di accesso alla
Box in fase di mount, creare il file `secrets`, attribuirgli i
permessi corretti (`600`)

.. code-block:: bash

   sudo cp /etc/davfs2/secrets ~/.davfs2
   sudo chown $USER ~/.davfs2/secrets
   sudo chmod 600 ~/.davfs2/secrets

ed inserirvi i dati di accesso

.. code-block:: bash

   /media/box  user@email.com  password

Il file `~/.davfs/davfs2.conf` contiene le impostazioni per l'utente;
in questo, specificare la posizione del file delle password appena
creato, decommentando la riga come segue

.. code-block:: bash

   secrets         ~/.davfs2/secrets

Possiamo dotarci di *alias* in `~/.bashrc` per montare e smontare
rapidamente la Box (ricordando di dare un `source ~/.bashrc` per
rendere operativi gli alias):

.. code-block:: bash

   alias boxmount='mount /media/box'
   alias boxumount='umount /media/box'

Proviamo a montare la Box con il comando `boxmount`. Il montaggio
della Box al login (e solo dopo la disponibilità di una connessione
internet, per evitare errori) può essere `automatizzato`_.
Se tutto procede bene, andiamo oltre.

*ATTENZIONE*: Il parametro ``cache_size`` in ``~/.davfs2/davfs2.conf`` è
commentato di default. Ciò significa che man mano che DavFS2 trasferisce
i file dal filesystem locale a quello remoto di Box, ne lascia una copia
(criptata) nella cache. Non avendo nessun limite impostato, ciò potrebbe
riempire la partizione in cui è presente la cache (impedendo ad Ubuntu
di avviarsi se la cache è nella partizine root -- GNU/Linux deve avere
almeno il 4% di spazio libero in root). È pertanto vivamente consigliato
di abilitare il parametro ``cache_size``, impostando un limite
ragionevole (per me 250 Mb).

.. _automatizzato: http://blog.nguyenvq.com/2011/12/08/mount-box-net-on-ubuntu-linux-via-webdav

2 - Creare una cartella criptata nella Box
------------------------------------------

Alcune spiegazioni:

- ``media/box``: punto di mount della Box via WebDAV
- ``media/box/backup``: la cartella che ``fisicamente`` conterrà i dati,
  nella nostra Box
- ``media/box.encfs`` la cartella in cui verrà montato il filesystem
  criptato, non leggibile
- ``media/box.backup``: la cartella in cui riverseremo i nostri dati da
  backuppare, collegata a ``box.encfs``

Installare EncFS ed aggiungere il proprio utente al gruppo ``fuse``

.. code-block:: bash

   sudo apt-get install encfs
   sudo addgroup <USER> fuse

decommentare la seguente riga in ``/etc/fuse.conf``

.. code-block:: bash

   user_allow_other

creare la cartella che conterrà il filesystem criptato, sistemare i
permessi (sostituire ad ``<USER>`` il proprio nome utente sulla
macchina)

.. code-block:: bash

   sudo mkdir /media/box.encfs
   sudo chown <USER>:<USER> /media/box.encfs

creare la cartella che ospiterà il filesystem criptato e il filesystem
criptato

.. code-block:: bash

   mkdir /media/box/backup/
   encfs /media/box/backup/ /media/box.encfs/

durante la creazione, ci verranno chieste informazioni relative al
sistema di cifratura; consiglio di selezionare l'opzione di default. Al
termine della procedura, il filesystem criptato sarà attivo nella nostra
Box.

3 - Installare gli script per correggere le timestamp
-----------------------------------------------------

La vera chicca: questi script fanno in modo che i file nel nostro
filesystem criptato conservino le timestamp, permettendo a rsync di
lavorare. Scaricare gli script con

.. code-block:: bash

   wget http://bazaar.launchpad.net/~germar/fusetime/trunk/download/head:/fusetime.py-20120119150228-brsqa2ewllb9euc5-1/fusetime.py
   wget http://fusepy.googlecode.com/svn/trunk/fuse.py

correggere i permessi, spostarli nella cartella degli eseguibili

.. code-block:: bash

   sudo chown root:root fusetime.py fuse.py
   sudo chmod 755 fusetime.py fuse.py
   sudo mv fusetime.py fuse.py /usr/local/bin/

4 - Creare la cartella per la sincronizzazione e avviare rsync
--------------------------------------------------------------

Questo passaggio permetterà di correggere le timestamp grazie agli
script installati prima e di avere in ``/media`` una cartella che avremo
come destinazione per i nostri backup, collegata con quella criptata
creata precedentemente. Creare la cartella, attribuire i permessi e
avviare lo script sulle cartelle

.. code-block:: bash

   sudo mkdir /media/box.backup
   sudo chown <USER>:<USER> /media/box.backup
   fusetime.py /media/box.encfs/ /media/box.backup/

In caso di problemi o errori relativi a con ``fusermount``, soluzione è
`a portata di mano`_.

Installare rsync


.. code-block:: bash

   sudo apt-get install rsync

Avviare *finalmente* la sincronizzazione, sostituendo ``/path/to/files``
al percorso che vogliamo backuppare; di seguito è riportata un'istanza
di rsync con opzioni "base", che andrà bene per qualsiasi esigenza

.. code-block:: bash

   rsync -r -a -i --times --delete --max-size=99.5M --no-perms --no-group --progress /path/to/files /media/box.backup/

Per sincronizzare le mie immagini, ho inserito qualche altra opzione per
non copiare nel backup i file ``Thumbs.db``, quelli che con estensione
``.xmp`` e ``.bak``; vengono inoltre usati dei file parziali (così da
non dover ricominciare da capo il backup di file di grosse dimensioni in
caso di interruzioni) e man mano che il programma opera viene mostrato
un log in tempo reale che mostra ogni singola operazione di rsync:

.. code-block:: bash

   rsync -r -a -i --times --exclude '*.xmp' --exclude '*.bak' --exclude 'Thumbs.db' --delete \\
   --max-size=99.5M --no-perms --no-group -P -v -v /media/dati/archivio/immagini/ /media/box.backup/

Ricordare che in ``/media/box.backup/`` possiamo creare qualsiasi
sottocartella, abbiamo la massima libertà; ad esempio, potremo avere
rispettivamente come origine e destinazione del backup:

.. code-block:: bash

   /home/fradeve/Immagini  /media/box.backup/Immagini
   /home/fradeve       /media/box.backup/fradeve

Potremo quindi dimenticarci di tutte le altre cartelle create, che sono
soltanto funzionali al sistema degli script e del filesystem, lavorando
semplicemente su ``/media/box.backup``. Quando la sincronizzazione sarà
finita, potremo smontare le partizioni con i seguenti comandi

.. code-block:: bash

   fusermount -u /media/box.backup
   fusermount -u /media/box.encfs
   umount /media/box

Consiglio vivamente, dopo aver dato il comando di ``umount`` per
smontare la Box via WebDAV, di attendere che davfs finisca di scrivere
le modifiche ancora in cache sulla risorsa WebDAV che, come si può
intuire dal parametro ``async`` di ``/etc/fstab``, era stata montata per
l'I/O asincrono per ottimizzarne le prestazioni; se si tenta di killare
il processo mentre sta scrivendo i dati ancora in cache potrebbero
verificarsi perdite di dati.

Dopo un eventuale riavvio del sistema, potremo far ripartire tutto
montando nuovamente il filesystem criptato e avviando lo script

.. code-block:: bash

   encfs /media/box/backup/ /media/box.encfs/
   fusetime.py /media/box.encfs/ /media/box.backup/

oppure, concatenando i comandi per montare la Box, montare la partizione
criptata (che richiederà comunque l'inserimento manuale della password)
e lo script fusetime, è possibile creare un alias in ``.bashrc`` che
faccia tutto da solo:

.. code-block:: bash

   alias boxmount='mount /media/box && encfs /media/box/backup/ /media/box.encfs/ && fusetime.py /media/box.encfs/ /media/box.backup/'

fatto ciò, potremo avviare il comando di rsync riportato sopra. Il
montaggio di filesystem cifrati in GNOME può essere automatizzato usando
`gnome-encfs`_.

.. _a portata di mano: http://blog.seljebu.no/2011/05/encfs-over-sshfs-on-linux-mint-10
.. _gnome-encfs: https://bitbucket.org/obensonne/gnome-encfs

5 - Aggiungere sicurezza
------------------------

ATTENZIONE: questa sezione è ancora in fase di testing, ed ho avuto
molti problemi nel farla funzionare. Attendere ulteriori sviluppi prima
di testarla sui propri dati. In breve: nonostante teoricamente tutto
debba funzionare come riportato di seguito, una volta cancellato il file
``encfs6.xml`` dalla radice della cartella cifrata, il filesystem
cifrato non viene più montato.

È sufficiente consultare qualche `howto`_
tecnico relativo ad EncFS per rendersi conto che ci sono alcune
problematiche di sicurezza all'interno di un'installazione standard:


    Most of the encrypting information (apart from password) including
    iteration count, and salt, is visible in the encfs config file at the top
    level of the encfs directory tree.  This provides valuable information to
    a hacker.

In altre parole, all'interno di ogni filesystem criptato creato con
EncFS viene generato un file, ``.encfs6.xml`` che non contiene (no di
certo!) la password di cifratura, ma riassume comunque informazioni che
potrebbero tornare utili a chiunque voglia tentare di decifrare i dati a
nostra insaputa. Inoltre, per ovvi motivi, essendo un file di
configurazione, non è criptato come il resto dei dati, per questo
sarebbe meglio copiarlo in un dispositivo sicuro (una penna USB) ed
eliminarlo dalla cartella "in chiaro" Box.net (dove rimarrebbe leggibile
a chiunque abbia la password del nostro account). Il file deve essere
comunque presente nel nostro sistema, da qualche parte, perché è
essenziale per decifrare il filesystem criptato (almeno quanto la
password). Al momento di montare il filesystem, indicheremo ad EncFS
dove prendere il file delle impostazioni. Vediamo come.

Spostiamo il file nella nostra home, eliminandolo dalla Box

.. code-block:: bash

   mv /media/box/backup/.encfs6.xml ~/.encfs6_box.xml

Al nuovo comando per montare il filesystem criptato verrà aggiunto
(anche nel vostro eventuale ``.bashrc``) un parametro che indica dove
reperire il file xml corretto; tale parametro varia in funzione della
versione di EncFS (per cui EncFS 1.6 avrà ``ENCFS&_CONFIG``, EncFS 1.7
avrà ``ENCFS7_CONFIG``):

.. code-block:: bash

   ENCFS6_CONFIG="~/.encfs6_box.xml" encfs /media/box/backup/ /media/box.encfs/

Questo significa anche che:

-  se un giorno configurerete una nuova macchina per accedere alla
   vostra Box criptata, ``.encfs6_box.xml`` dovrete inserirlo a mano nel
   sistema, perché non sarà più presente in Box. Se non sapete come
   garantire la sicurezza della copia di ``.encfs6_box.xml`` che avrete
   salvato in una penna USB, è possibile cifrarlo con `GPG`_ o usare
   la `steganografia`_
-  se usate gnome-encfs per montare la partizione all'avvio, dovrete
   fare attenzione a specificare il percorso di ``.encfs6_box.xml``
   perché tutto funzioni automaticamente al login

Integrazioni
------------

Sicuramente l'impossibilità di accedere da qualunque dispositivo ai
propri dati, e la macchinosità di dover montare sulla macchina dalla
quale si vuole accedere una partizione WebDAV e poi configurare EncFS e
i vari script è demotivante. Tuttavia, armandosi di un VPS e un po' di
pazienza, si potrebbe configurare un'istanza di
`ownCloud`_, che potrebbe accedere ai file
tramite una configurazione come quella descritta nella sezione 1,
montata semplicemente in ``/media/data``. Tra l'altro, ownCloud ha anche
un'`applicazione per Android`_: e con questo, chiudo.

Ulteriori riferimenti
---------------------

- `Guida sul wiki di Ubuntu-fr`_
- `Guida su tomalison.com`_
- `Thread su forum.ubuntu.com`_

.. _howto: http://www.ict.griffith.edu.au/anthony/info/crypto/encfs.hints
.. _GPG: http://www.gnupg.org/howtos/it/GPGMiniHowto-3.html
.. _steganografia: http://steghide.sourceforge.net/documentation.php
.. _ownCloud: http://owncloud.org
.. _applicazione per Android: http://owncloud.org/support/android
.. _Guida sul wiki di Ubuntu-fr: http://doc.ubuntu-fr.org/davfs2
.. _Guida su tomalison.com: http://tomalison.com/reference/2010/04/03/webdav
.. _Thread su forum.ubuntu.com: http://ubuntuforums.org/showpost.php?p=11258734&postcount=34
