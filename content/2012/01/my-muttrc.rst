My muttrc 
=========

:date: 2012-01-12 15:00:00
:tags: mutt, mail

AGGIORNAMENTO: una nuova versione di questo script è disponibile e
spiegata ampiamente in `questo`_ post.

A grande richiesta, il mio :span:`muttrc|code` per gestire due account (uno su
Gmail e l'altro su `www.autistici.org`_).
Qualche chicca, spiegata:

- :span:`set editor|code` richiama uno script che esegue dei comandi in Vim che
  permettono di settare dei parametri all'interno della mail prima
  ancora che l'editor si apra;
- :span:`unset metoo|code` permette di evitare che il mio indirizzo email
  finisca nei destinatari quando rispondo ad una mail in cui sono stato
  messo in CC o tra i destinatari;
- :span:`set query_command|code` permette di aprire `goobook`_ per cercare gli
  indirizzi nella copia in locale della mia rubrica di Gmail;
- :span:`set print_command|code` rende accattivante la stampa delle mail
  utilizzando :span:`a2ps|code`;
- :span:`set my_pass1|code` è un comando che lancia awk su un file nella mia
  home criptata, contenente le password degli account (utile quando si
  intende conservare il proprio muttrc in una cartella non cifrata: le
  password sono al sicuro);
- :span:`imaps://francesco.devirgilio@inventati.org@mail.autistici.org|code` le
  impostazioni dell'account imap per Austistici/Inventati; ci ho messo
  un bel po' a trovare la retta via, considerato che le indicazioni
  sull'accesso ad IMAP tramite Mutt sul sito di A/I sono molto
  generiche;
- :span:`macro index y|code` e seguenti, permettono di cambiare rapidamente
  account con la semplice pressione in successione di alcuni tasti;
- :span:`macro pager G|code` è un comando studiato per copiare la mail cifrata
  in una certa cartella, la decifra con la propria chiave privata, la
  apre ed all'uscita dal visualizzatore elimina il file decifrato;
- :span:`macro index Z|code` e seguente, permette di scaricare in blocco tutti
  gli allegati da una mail;
- :span:`macro index .r|code` permette di segnare come lette tutte le mail nella
  cartella corrente.

Ci sono tante altre funzioni integrate in questo muttrc, ma niente che
non si trovi anche altrove sulla rete.

.. _questo: {filename}/2012/03/muttrc-take-2.rst
.. _www.autistici.org: http://www.autistici.org
.. _goobook: https://code.google.com/p/goobook
