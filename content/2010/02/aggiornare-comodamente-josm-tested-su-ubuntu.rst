Aggiornare comodamente JOSM-tested su Ubuntu
============================================

:date: 2010-02-22 16:20:29
:tags: ubuntu, openstreetmap, josm, gnulinux

Per chi non lo sapesse, `JOSM`_ è l'editor più importante tra tutti 
quelli disponibili per contribuire al progetto OpenStreetMap. È scritto 
in Java ed è `distribuito`_ in due versioni, josm-tested è l'ultima 
versione "perfettamente funzionante", mentre josm-latest è l'ultima 
versione disponibile in assoluto, stabile ma comunque in continuo 
sviluppo. Tutti i mapper di OpenStreetMap che
non abbiano sufficiente dimestichezza con i linguaggi di programmazione
da automatizzare il processo, hanno sempre provveduto da se a scaricare
(ogni tanto, quando capita) l'ultima versione disponibile di JOSM dal
sito ufficiale, considerato che quella che c'è nei repository di Ubuntu
viene aggiornata molto molto raramente. La soluzione? Il mapper pugliese
Paki ha creato un PPA per gli utenti Ubuntu/Debian in cui distribuisce
le due versioni di JOSM, entrambe aggiornate all'ultima disponibile, che
verranno rese disponibili velocissimamente non appena rilasciate sul
sito ufficiale. Per partire con l'installazione, è sufficiente
aggiungere il repository di Paki e installare i pacchetti ``josm-tested`` o
``josm-latest``. Più comodo di così :) Adesso non resta che far rockeggiare
OpenStreetMap nella vostra città :D

Incollo di seguito la sua mail:

    Mi presento, sono Pasquale Ambrosini e faccio attualmente parte
    della comunità pugliese di OpenStreetMap. Grazie all'ausilio di
    launchpad, ho aperto un repository contenente le ultime versioni di
    josm-tested e josm- latest.

    Vi spiego in breve la politica che ho adottato.

    Vi sarete sicuramente resi conto che nei repository Ubuntu, josm non
    è aggiornato molto spesso, anzi, per dirla tutta gli aggiornamenti
    sono più unici che rari. Quindi ho aperto un repository che contiene
    il pacchetto josm- tested che, verrà aggiornato non appena
    aggiorneranno il software. Convenzionalmente si potrà aggiornare dal
    gestore di pacchetti, come sempre.

    Per josm-latest invece ho adottato una politica diversa, infatti la
    versione unstable è soggetta a molti aggiornamenti nell'arco della
    settimana e sarebbe impossibile "starci dietro", così ho scritto uno
    script in python con librerie grafiche gtk che provvederà a
    verificare se, all'avvio ci sono aggiornamenti e in caso positivo,
    vi comunicherà l'aggiornamento. Quindi sarete voi stessi ad
    aggiornare, senza l'ausilio del gestore pacchetti, in maniera rapida
    e veloce. Ci tengo a precisare che i due pacchetti "josm-tested" e
    "josm-latest" non intaccano minimamente il pacchetto josm ma,
    useranno le vostre preferenze che usate normalmente.

Per installare il repository su Ubuntu 9.10 (da terminale):

.. code-block:: bash

    sudo add-apt-repository ppa:pasquale-ambrosini/josm && sudo apt-get update

Fatto ciò vi troverete i due pacchetti nel gestore pacchetti.

Vi lascio uno screenshot del downloader/installer:

.. figure:: {filename}/images/spqr2.png


.. _JOSM: http://josm.openstreetmap.de
.. _distribuito: http://wiki.openstreetmap.org/wiki/IT:JOSM
