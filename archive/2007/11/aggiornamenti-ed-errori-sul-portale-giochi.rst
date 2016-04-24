Aggiornamenti (ed errori) sul Portale Giochi
============================================

:date: 2007-11-11 22:13:29
:tags: ubuntu

Considerando che nessuno è perfetto, mi devo scusare per alcune
"imperfezioni" (chiamiamole così) in alcuni precedenti post: i giochi
che avrei voluto introdurre nel Portale Giochi li ho esposti 2 post fa,
e tra questi ho incluso **FreeCol**, che è già `presente nel wiki`_
(l'ho tradotto io stesso dal portoghese, chissà come ho fatto a
dimenticarmene!). Altra imperfezione: nel mio `precedente post`_
ho accennato al fatto che Ubuntu su Asus EEE non riesce a riconoscere il
wireless. Non è del tutto corretto: tramite ndiswrapper, è possibile, ed
in particolare lo si può fare importando i driver da Windows XP (non mi
chiedete come). Queste informazioni sono riportate in una risposta al
post che ho citato in quell'articolo. Ringrazio chi me l'ha fatto notare
;)

.. _presente nel wiki: http://wiki.ubuntu-it.org/Giochi/Strategia/FreeCol

Detto questo... oggi mi sono apprestato a provare ad installare
Bridge Construction Set, uno dei giochi citati nel
`Full Circle Magazine n°5`_, e del quale vorrei
scrivere la wiki. Dopo aver fatto partire l'installer ed eseguito lo
script per patchare la libreria Openal (il file e :span:`bcs-linux-openal-fixer.sh|code`),
l'unica cosa che ottengo è questa:

.. code-block:: bash

    fradeve@dhcppc2:~/BridgeConstructionSetDemo$ ./bcs fcntl: Operation not
    permitted fcntl: Operation not permitted

Non so veramente come uscirne... se qualcuno ha idee o viene a capo di
qualcosa, me lo faccia sapere, che buttiamo giù questa wiki. Sul forum
internazionale non ho trovato niente. Sapete dove `trovarmi`_ :D

.. _Construction Set: http://www.garagegames.com/products/17
.. _Full Circle Magazine n°5: http://fullcirclemagazine.org/issue-5
.. _trovarmi: http://wiki.ubuntu-it.org/FrancescoDeVirgilio
.. _precedente post: http://dl.dropbox.com/u/369614/blog/public_html/FradeveOpenblog/posts/2007/11/ubuntu-710-su-asus-eee-pc.html
