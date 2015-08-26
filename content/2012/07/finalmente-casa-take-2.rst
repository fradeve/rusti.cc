Finalmente a casa: take 2
=========================

:date: 2012-07-22 13:30:00
:tags: blog

Il titolo probabilmente ricorda `qualcosa di già sentito`_
ma fa niente. Questo post è una comunicazione di servizio: da oggi si
"blogga come un hacker".

Il blog è stato completamente riscritto, e portato da
`Ikiwiki`_ (wiki engine in Perl) ad `Hyde`_ (generatore di pagine statiche /
blogging engine in Python/Django); la possibilità di estendere il
proprio *blogging engine* in un linguaggio conosciuto è un vantaggio non
trascurabile (non imparerò certo Perl per sistemare il mio blog). Il
codice di base è stato forkato da quello scritto da `Fernando Paolo`_ 
ed a lui vanno anche tutti i crediti per il layout. Al suo codice ho 
aggiunto, invece:

- supporto ai tag
- la possibilità di evidenziare i *featured articles* nella lista dei
  post
- il feed atom dei post pubblicati
- un template Jinja2 per inserire immagini ridimensionate con link
  all'immagine nel formato originale
- un template Jinja2 per inserire grafici realizzati con la libreria
  `g.raphael library`_
- l'integrazione con i commenti su Disqus

Tutto il codice è rilasciato in licenza GNU GPL v3, mentre le librerie
javascript ovviamente conservano la licenza originaria. Per ulteriori
informazioni, consultare il file :span:`README.md|code` `qui`_.

Inoltre, tutto il mio codice pubblico è stato trasferito su GitHub, per
una serie di motivi:

- l'aspetto "social" di GitHub è molto più pronunciato rispetto a
  Launchpad
- è di gran lunga più semplice gestire progetti con GitHub piuttosto
  che con Launchpad (basti pensare al fatto che autonomamente l'utente
  non può eliminare un progetto da Launchpad, anche se ne è egli stesso
  il creatore/manutentore)
- vedo Launchpad sempre più come una piattaforma per pacchettizzare
  software e distribuirlo su Ubuntu/Debian piuttosto che un sistema per
  gestire celermente codice e progetti
- to abbandonando progressivamente Bazaar a favore dello
  *standard-compliant*, *uberdocumented* `GIT`_;
  la possibilità di Launchpad di *mirrorare* codice in repository GIT
  di terze parti e pacchettizzarlo in automatico rimane comunque una
  caratteristica interessante che tornerà sicuramente utile

Rimangono comunque al loro posto i cardini della gestione del blog/sito:
Ubuntu server, VIM per le modifiche al progetto, Lighttpd come
webserver.

.. _Fork me!: https://github.com/fradeve/fradeve.org
.. _qualcosa di già sentito: http://blog.fradeve.org/log/2007/09/finalmente-a-casa.html
.. _Ikiwiki: http://www.ikiwiki.info
.. _Hyde: https://github.com/hyde/hyde
.. _Fernando Paolo: https://github.com/fspaolo
.. _g.raphael library: http://g.raphaeljs.com
.. _qui: https://github.com/fradeve/fradeve.org/blob/master/README.md
.. _GIT: http://git-scm.com
