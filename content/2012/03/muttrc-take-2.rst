muttrc, take 2
==============

:date: 2012-03-18 14:00:00
:featured: yes
:tags: mail, mutt
:modified: 2012-08-09

NB: una versione differente di questo stesso muttrc, con meno funzioni e
flessibilità, è reperibile nel mio `post di gennaio`_; ho voluto conservare
il vecchio post senza aggiornarlo perché potrebbe tornare utile a chi
cerca configurazioni più semplici e *monolitiche* (passatemi il
termine).

La caratteristica principale di questo nuovo muttrc è la modularità:
ogni account ha un suo file di configurazione, nel quale sono riportati
i settaggi validi per il medesimo, rimuovendo ogni configurazione
precedente nel momento del caricamento, che avviene grazie a semplici
shortcut.

Rimangono valide le spiegazioni date nel post di gennaio. Tutti i file
usati in questo tutorial sono hostati su `GitHub`_, con l'esclusione di
`mutt-notmuch`_. Il codice è scaricabile dopo aver installato GIT, 
con il seguente comando:

.. code-block:: bash

   git clone https://github.com/fradeve/dotfiles.git

I file utili a configurare mutt sono nella cartella `mutt-fradeve`.

Perché un muttrc modulare
-------------------------

Ciò che ho imparato dal precedente muttrc è che, se si vuol essere
perfezionisti, è poco pratico e molto laborioso mantenere tutti i
settaggi in un unico file. In fondo, ogni file occupa qualche kilobyte,
non rovina la vita a nessuno.

Perché sbattersi
----------------

Questo muttrc è fortemente orientato alla privacy. I settaggi danno per
scontato che:

- si stia lavorando con una $HOME criptata
- si voglia comunque avere un backup in tempo reale dei settaggi nella
  propria Dropbox, ma senza fare in modo che dal cloud si possa avere
  accesso a password, documenti, mail, etc.

Inoltre, questo muttrc lavora (insieme ad altri programmi) per offrire
la lettura di email sia tramite IMAP (quindi in near-real-time), sia
tramite un archivio locale di tutta la posta di ogni account,
sincronizzato ogni 5 minuti con `offlineIMAP`_
all'interno della propria $HOME criptata. In questa maniera posso
leggere la posta velocemente e direttamente da IMAP quando sono a casa,
o dall'archivio aggiornato in locale quando sono in viaggio. Questo
significa che per ogni account da configurare viene creato:

- un file di configurazione per la lettura via IMAP (`conf_on`)
- un file di configurazione per la lettura via archivio locale (`conf_off`)

Ovviamente, ci sarà:

- un file per la configurazione di mutt in modalità IMAP (`muttonrc`)
- un file per la configurazione di mutt in modalità archivio locale (`muttrc`)

Può tornare utile inserire in `.bashrc` degli alias per avviare mutt
in una delle due modalità:

.. code-block:: bash

   alias mutt='mutt -n -F /home/user/.mutt/muttrc'
   alias mutton='mutt -n -F /home/user/.mutt/muttonrc'

INSTALL
-------

Il file INSTALL riporta tutto ciò che serve per far funzionare il gioco.

La sezione 2 riporta i software da installare per far funzionare tutto.
Alcuni di questi vengono esplicitamente richiamati nei due file rc di
mutt, e sono riportare le linee in cui ciò avviene; altri offrono
semplicemente funzioni utili, e nessun numero di riga è stato riportato.

In particolare, tra i passaggi preliminari (sezione 3), troviamo:

-  file da copiare, spesso nella cartella di mutt nella propria home
-  file da decifrare e inserire nella propria home (contenenti le
   password ed i dati sensibili)
-  file che rimangono al loro posto in Dropbox e vengono caricati
   direttamente da lì
-  file che rimangono al loro posto in Dropbox e vengono *symlinkati*
   nella home

La sezione 4 riporta la riga da inserire in crontab (`crontab -e`) per
avviare la sincronizzazione di offlineIMAP ogni 5 minuti.

File cifrati
------------

Il contenuto dei file cifrati è il seguente.

muttpass.gpg
~~~~~~~~~~~~

.. code-block:: bash

   account1:   pw
   account2:   pw  
   account3:   pw

offlineimaprc.gpg
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   [general]
   metadata = ~/.offlineimap
   accounts = account1,account2,account3
   maxsyncaccount = 4
   socktimeout = 60
   ui = TTY.TTYUI

   ### account1@host1.com 
   #######################

   [Account account1]
   localrepository = local-account1
   remoterepository = remote-account1

   [Repository local-account1]
   type = Maildir
   localfolders = /home/user/.mail/account1

   [Repository remote-account1]
   type = Gmail
   remotehost = imap.host1.com
   remoteuser = account1@host1.com
   remotepass = pw
   ssl = yes
   realdelete = no

   ### account2@host2.com
   ######################################

   [Account account2]
   localrepository = local-account2
   remoterepository = remote-account2

   [Repository local-account2]
   type = Maildir
   localfolders = /home/user/.mail/account2

   [Repository remote-account2]
   type = IMAP
   ssl = yes
   #remoteport = 995
   remotehost = mail.host2.org
   remoteuser = account2@host2.org
   remotepass = pw
   realdelete = no

   ### account3@host3.net
   ######################################

   [Account account3]
   localrepository = local-account3
   remoterepository = remote-account3

   [Repository local-account3]
   type = Maildir
   localfolders = /home/user/.mail/account3

   [Repository remote-account3]
   type = IMAP
   ssl = yes
   #remoteport = 995
   remotehost = mail.host3.net
   remoteuser = account3@host3.net
   remotepass = pw
   realdelete = no

~/.netrc
~~~~~~~~

.. code-block:: bash

   machine host1.com
   login account1@host1.com
   password pw


.. _post di gennaio: {filename}/2012/01/my-muttrc.rst
.. _GitHub: https://github.com/fradeve/dotfiles
.. _mutt-notmuch: http://upsilon.cc/~zack/blog/posts/2011/01/how_to_use_Notmuch_with_Mutt
.. _offlineIMAP: http://offlineimap.org
