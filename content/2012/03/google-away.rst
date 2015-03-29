Seeking for freedom
===================

:date: 2012-03-31 10:30:00
:tags: privacy, server
:modified: 2012-12-11

In questa pagina raccolgo alcune note sul mio progetto per il biennio
2011-2012: eliminare quasi totalmente la mia dipendenza da servizi web
che non danno garanzie sulla sicurezza e sulla privacy dei dati, per
passare ad un insieme di servizi basati sulla fiducia in chi li
gestisce, e soprattutto sull'utilizzo di software libero. Questa idea
nasce nell'estate del 2011 ed è cresciuta piano piano con il passare del
tempo; probabilmente vedrà il compimento quest'anno. Gli ultimi a morire
saranno sicuramente i social network, ma vedo `Diaspora`_ sempre più
vicino. Questa pagina è anche un'ottima occasione per fare il punto sui
vari howto che ho scritto per il blog.

Come sempre, perché sbattersi?

- `Google tracks you`_
- `Internet privacy`_
- `Debian: leaving the cloud`_ interessante elenco di software
  liberi che possono sostituire quelli dei servizi cloud

Da sistemare, parziali
----------------------

Contatti
~~~~~~~~

Attualmente Google Contacts, in fase di sperimentazione
`OwnCloud`_ contacts.

Calendario
~~~~~~~~~~

Attualmente Google Calendar, in fase di sperimentazione OwnCloud
calendar. Update: con OwnCloud 3.0.1 da GIT l'importazione da Google
Calendar funziona!

Pinging
~~~~~~~

Lo smistamento degli aggiornamenti "social" è affidato a `Brdcst it!`_, 
software libero per il *pinging*, che però è insufficiente e
viene affiancato da `ifttt`_ e `FeedBurner`_ (purtroppo
proprietari) e dal supporto ai feed RSS con OAuth di TT-RSS sulle
etichette di Gmail. Qualche idea su come funziona la mia rete social ce
la si può fare in `questo post`_.

Sincronizzazione dati
~~~~~~~~~~~~~~~~~~~~~

Attualmente Dropbox, in fase di sperimentazione `SparkleShare`_.

Funzionanti
-----------

Sistemi operativi
~~~~~~~~~~~~~~~~~

- Vedi pagina hardware su `sito`_
- tutti i servizi su server sono offerti grazie a `Lighttpd`_, su 
  server amministrato con `Webmin`_

Motore di ricerca
~~~~~~~~~~~~~~~~~

Ovviamente, `DuckDuckGo`_.

Backup dei dati
~~~~~~~~~~~~~~~

Per ogni file, una copia locale e una copia online. La copia online è
hostata su `Box.net`_, in una cartella cifrata con `EncFS`_, montata con
`Davfs2`_ e sincronizzata con rsync, quest'ultimo usato sia verso la 
copia web che locale. Howto `qui`_.

In fase di sperimentazione:

- la possibilità di accedere ai dati via web tramite OwnCloud che legge
  la Box montata sul server tramite Davfs2 + EncFS; accesso mobile
  tramite `applicazione ufficiale`_ per Android
- la possibilità di usare un server domestico basato su RaspberryPi e
  OwnCloud su filesystem criptato

Il backup dei social network viene effettuato da `Backupify`_, in
cerca di un sostituto *free software*.

Blog
~~~~

Generato tramite `Markdown`_ + `Hyde`_ + GIT, sincronizzato via rsync, con
statistiche offerte da `Awstats`_. In sperimentazione interfaccia 
realizzata con `Bootstrap`_.

Mail
~~~~

- mailing lists: Gmail
- personale: `Autistici/Inventati`_
- lavoro: `Riseup.net`_

- Client desktop: `Mutt`_, sia via IMAP che con
  copia offline grazie ad `OfflineIMAP`_,
  corredato da varie altre funzionalità offerte da software libero
  installato in locale; potete trovare i file di configurazione e tutto
  il codice in questo `post`_
- Client mobile: `K-9 Mail`_ per Android
- Client web: vari, in funzione del sito

Chat
~~~~

Jabber via Google Talk

- client desktop: `IRSSI`_, con supporto OTR,
  registrazione di logs e impostazioni hostati su un filesystem cifrato
  con EncFS all'interno di Dropbox
- client mobile: Gtalk mobile
- client web: GTalk da web
- backup dei log: via IMAP con OfflineIMAP

Coding
~~~~~~

- editing: `Vim`_
- hosting: `GitHub`_, in cerca di una
  soluzione git-based migliore

Documenti, pubblicazioni
~~~~~~~~~~~~~~~~~~~~~~~~

- editing: `Vim`_ per documenti offline
- pubblicazioni `LaTeX`_, usato con `vim-latex`_ da TeXLive, `howto qui`_.

Bookmarks
~~~~~~~~~

`A/I Bookmarks`_, offerto da Autistici/Inventati, e basato su `Scuttle`_.

Aggregatore RSS
~~~~~~~~~~~~~~~

- web: `TT-RSS`_, hostato su server personale
- mobile: `TT-RSS-mobile`_ per Android (applicazione non ufficiale, 
  ma sviluppata più attivamente)

Musica
~~~~~~

- desktop: libreria gestita con `Amarok`_
- social: statistiche sull'ascolto inviate a `Libre.fm`_ tramite
  `lastfmsubmitd`_

Video
~~~~~

- `videodb`_ per tenere traccia dei film, hostato su server personale

Todo
~~~~

Lista delle cose da fare sincronizzata su PC e cellulare grazie a `Todo.txt`_.


.. _sito: http://me.fradeve.org/interessi.html
.. _OwnCloud: http://owncloud.org
.. _Amarok: http://amarok.kde.org
.. _Box.net: http://www.box.com
.. _EncFS: http://www.arg0.net/encfs
.. _Lighttpd: http://www.lighttpd.net
.. _DuckDuckGo: https://duckduckgo.com
.. _Davfs2: https://savannah.nongnu.org/projects/davfs2
.. _Markdown: http://daringfireball.net/projects/markdown
.. _Hyde: http://hyde.github.com
.. _Awstats: http://awstats.sourceforge.net
.. _Autistici/Inventati: http://www.autistici.org/it
.. _Riseup: https://riseup.net/it
.. _Mutt: http://www.mutt.org
.. _OfflineIMAP: http://offlineimap.org
.. _K-9 Mail: https://code.google.com/p/k9mail
.. _IRSSI: http://www.irssi.org
.. _GitHub: http://www.github.com
.. _videodb: http://www.videodb.net/blog
.. _Vim: http://www.vim.org
.. _Scuttle: http://sourceforge.net/projects/scuttle
.. _A/I Bookmarks: https://link.autistici.org
.. _TT-RSS: http://tt-rss.org
.. _TT-RSS-mobile: https://github.com/mboinet/ttrss-mobile
.. _applicatione ufficiale: https://gitorious.org/owncloud/android
.. _qui: {filename}/2012/03/usare-rsync-con-box.rst
.. _Brdcst it!: http://brdcst.it
.. _ifttt: http://ifttt.com
.. _questo post: {filename}/2011/02/how-do-i-blog.rst
.. _Google tracks you: http://donttrack.us
.. _Internet privacy: https://en.wikipedia.org/wiki/Internet_privacy
.. _Diaspora: http://diasporaproject.org
.. _post: {filename}/2012/03/muttrc-take-2.rst
.. _LaTeX: http://www.guit.sssup.it
.. _vim-latex: https://github.com/jcf/vim-latex
.. _howto qui: {filename}/2010/08/installare-texlive-da-ctan-su-ubuntu-lucid.rst
.. _Todo.txt: http://www.todotxt.com
.. _FeedBurner: http://feedburner.google.com
.. _Debian: leaving the cloud: http://wiki.debian.org/FreedomBox/LeavingTheCloud
.. _Webmin: http://www.webmin.com
.. _Libre.fm: http://libre.fm
.. _lastfmsubmitd: http://www.red-bean.com/decklin/lastfmsubmitd
.. _Backupify: https://www.backupify.com
.. _SparkleShare: http://sparkleshare.org
.. _Bootstrap: http://twitter.github.com/bootstrap/index.html
