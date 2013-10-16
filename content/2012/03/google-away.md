Title: Seeking for freedom
Date:  2012-03-31 10:30:00
tags: privacy, server
Modified: 2012-12-11

In questa pagina raccolgo alcune note sul mio progetto per il biennio 2011-2012: eliminare quasi totalmente la mia dipendenza da servizi web che non danno garanzie sulla sicurezza e sulla privacy dei dati, per passare ad un insieme di servizi basati sulla fiducia in chi li gestisce, e soprattutto sull'utilizzo di software libero. Questa idea nasce nell'estate del 2011 ed è cresciuta piano piano con il passare del tempo; probabilmente vedrà il compimento quest'anno. Gli ultimi a morire saranno sicuramente i social network, ma vedo [Diaspora][35] sempre più vicino. Questa pagina è anche un'ottima occasione per fare il punto sui vari howto che ho scritto per il blog.

Come sempre, perché sbattersi?

* [Google tracks you][33]
* [Internet privacy][34]
* [Debian: leaving the cloud][44], interessante elenco di software liberi che possono sostituire quelli dei servizi cloud


## Da sistemare, parziali ##

### Contatti ###
Attualmente Google Contacts, in fase di sperimentazione [OwnCloud][2] contacts.

### Calendario ###
Attualmente Google Calendar, in fase di sperimentazione OwnCloud calendar. Update: con OwnCloud 3.0.1 da GIT l'importazione da Google Calendar funziona!

### Pinging ###
Lo smistamento degli aggiornamenti "social" è affidato a [Brdcst it!][29], software libero per il _pinging_, che però è insufficiente e viene affiancato da [ifttt][30] e [FeedBurner][41] (purtroppo proprietari) e dal supporto ai feed RSS con OAuth di TT-RSS sulle etichette di Gmail. Qualche idea su come funziona la mia rete social ce la si può fare in [questo post][32].

### Sincronizzazione dati ###
Attualmente Dropbox, in fase di sperimentazione [SparkleShare][50]


## Funzionanti ##

### Sistemi operativi ###
* Vedi pagina hardware su [sito][1]
* tutti i servizi su server sono offerti grazie a [Lighttpd][8], su server amministrato con [Webmin][46]

### Motore di ricerca ###
Ovviamente, [DuckDuckGo][9]

### Backup dei dati ###
Per ogni file, una copia locale e una copia online. La copia online è hostata su Box.net, in una cartella cifrata con EncFS, montata con [Davfs2][10] e sincronizzata con rsync, quest'ultimo usato sia verso la copia web che locale. Howto [qui][28].

In fase di sperimentazione:

* la possibilità di accedere ai dati via web tramite OwnCloud che legge la Box montata sul server tramite Davfs2 + EncFS; accesso mobile tramite [applicazione ufficiale][27] per Android
* la possibilità di usare un server domestico basato su RaspberryPi e OwnCloud su filesystem criptato

Il backup dei social network viene effettuato da [Backupify][49], in cerca di un sostituto _free software_.

### Blog ###
Generato tramite [Markdown][11] + [Hyde][12] + GIT, sincronizzato via rsync, con statistiche offerte da [Awstats][13]. In sperimentazione interfaccia realizzata con [Bootstrap][51]

### Mail ###
* mailing lists: Gmail
* personale: [Autistici/Inventati][14]
* lavoro: [Riseup.net][15]

* Client desktop: [Mutt][16], sia via IMAP che con copia offline grazie ad [OfflineIMAP][17], corredato da varie altre funzionalità offerte da software libero installato in locale; potete trovare i file di configurazione e tutto il codice in [questo post][36]
* Client mobile: [K-9 Mail][18] per Android
* Client web: vari, in funzione del sito

### Chat ###
Jabber via Google Talk

* client desktop: [IRSSI][19], con supporto OTR, registrazione di logs e impostazioni hostati su un filesystem cifrato con EncFS all'interno di Dropbox
* client mobile: Gtalk mobile
* client web: GTalk da web
* backup dei log: via IMAP con OfflineIMAP

### Coding ###
* editing: [Vim][22]
* hosting: [GitHub][20], in cerca di una soluzione git-based migliore

### Documenti, pubblicazioni ###
* editing: [Vim][22] per documenti offline
* pubblicazioni [LaTeX][37], usato con [vim-latex][38] da TeXLive, [howto qui][39]

### Bookmarks ###
[A/I Bookmarks][24], offerto da Autistici/Inventati, e basato su [Scuttle][23].

### Aggregatore RSS ###
* web: [TT-RSS][25], hostato su server personale
* mobile: [TT-RSS][26] per Android (applicazione non ufficiale, ma sviluppata più attivamente)

### Musica ###
* desktop: libreria gestita con [Amarok][3]
* social: statistiche sull'ascolto inviate a [Libre.fm][47] tramite [lastfmsubmitd][48]

### Video ###
* [videodb][21] per tenere traccia dei film, hostato su server personale

### Todo ###
Lista delle cose da fare sincronizzata su PC e cellulare grazie ad [Todo.txt][40]

   [1]: http://me.fradeve.org/interessi.html
   [2]: http://owncloud.org/
   [3]: http://amarok.kde.org/
   [4]: https://rsync.samba.org/
   [5]: https://play.google.com/music
   [6]: http://www.box.com
   [7]: http://www.arg0.net/encfs
   [8]: http://www.lighttpd.net/
   [9]: https://duckduckgo.com/
   [10]: https://savannah.nongnu.org/projects/davfs2
   [11]: http://daringfireball.net/projects/markdown/
   [12]: http://hyde.github.com/
   [13]: http://awstats.sourceforge.net/
   [14]: http://www.autistici.org/it/
   [15]: https://riseup.net/it
   [16]: http://www.mutt.org/
   [17]: http://offlineimap.org/
   [18]: https://code.google.com/p/k9mail/
   [19]: http://www.irssi.org/
   [20]: http://www.github.com
   [21]: http://www.videodb.net/blog/
   [22]: http://www.vim.org/
   [23]: http://sourceforge.net/projects/scuttle/ 
   [24]: https://link.autistici.org/
   [25]: http://tt-rss.org
   [26]: https://code.google.com/p/ttrss-reader-fork/
   [27]: https://gitorious.org/owncloud/android
   [28]: [[log/2012/03/usare-rsync-con-box.html]]
   [29]: http://brdcst.it/
   [30]: http://ifttt.com
   [31]: http://www.mmmmail.com/
   [32]: http://www.fradeve.org/blog/posts/2011/02/how-do-I-blog/
   [33]: http://donttrack.us/
   [34]: https://en.wikipedia.org/wiki/Internet_privacy
   [35]: http://diasporaproject.org/
   [36]: http://www.fradeve.org/blog/posts/2012/03/muttrc-take-2/
   [37]: http://www.guit.sssup.it/
   [38]: https://github.com/jcf/vim-latex
   [39]: http://www.fradeve.org/blog/posts/2010/08/installare-texlive-da-ctan-su-ubuntu-lucid/
   [40]: http://www.todotxt.com/
   [41]: http://feedburner.google.com 
   [42]: http://jappix.org/
   [43]: http://www.autistici.org/it/services/chat.html
   [44]: http://wiki.debian.org/FreedomBox/LeavingTheCloud
   [45]: http://beem-project.com/
   [46]: http://www.webmin.com/
   [47]: http://libre.fm/
   [48]: http://www.red-bean.com/decklin/lastfmsubmitd/
   [49]: https://www.backupify.com/
   [50]: http://sparkleshare.org/
   [51]: http://twitter.github.com/bootstrap/index.html
