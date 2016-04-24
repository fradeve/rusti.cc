Anonimato in IRC
================

:date: 2012-04-05 11:00:00
:featured: yes
:tags: irc, privacy
:headline: Come tutelare la propria privacy in IRC

Nonostante IRC possa sembrare un posto "sicuro" dal punto di vista della
privacy, sarebbe meglio non farsi troppe illusioni, è un servizio che
(come tutti gli altri) viene hostato su server e molto dipende dalla
fiducia che riponiamo in chi li gestisce. Per precauzione, potremmo
seguire alcuni di questi passi.

Mascherare l'IP
---------------

Insostituibile, `i2p`_. Installiamolo seguendo le `istruzioni`_ riportate 
nel sito ufficiale, poi avviamolo con il comando

.. code-block:: bash

   sudo /etc/init.d/i2p start

Si aprirà in automatico una pagina nel nostro browser predefinito, che
punta all'indirizzo :span:`http://127.0.0.1:7657|code`. La pagina per impostare i
tunnel IRC è raggiungibile all'indirizzo
:span:`http://127.0.0.1:7657/i2ptunnel/list|code`. Modificando la voce "IRC
Proxy", inserire come porta la 6667. Occorrerebbe anche assicurarsi che
le porte del router siano aperte. Queste accortezze dovrebbero fare in
modo che i2p riporti "OK" nella voce "stato della rete" presente nella
pagina principale.

Usare un vhost su IRC
---------------------

I `vhost`_ sono
servizi per mascherare alcuni dati visibili agli utenti connessi sul
server IRC che stiamo usando. Nel caso un server IRC offra il servizio
di vhost, ecco come utilizzarlo. I comandi riportati vengono utilizzati
su `IRSSI`_.

Collegarsi al server

.. code-block:: bash

   /connect irc.nomeserver.net 6667

assegnarsi un nickname fittizio

.. code-block:: bash

   /nick fakenick

registrare la propria email (dopo essersene creata una ad-hoc,
consigliatissimo il servizio di `Autistici/Inventati`_

.. code-block:: bash

   /msg NickServ register <password> fake@mail.com

fare join nel canale del vhost e richiederne un servizio

.. code-block:: bash

   /join #vhost
   !vhost fakenick@qualsiasicosa

identificarsi finalmente con il nuovo nick fittizio, la mail fittizia e
la password precedentemente registrata

.. code-block:: bash

   /msg NickServ IDENTIFY <password>

Bloccare il CTCP
----------------

`CTCP`_ è il 
protocollo per scambiare file e informazioni tra due client IRC; tra i
comandi integrati in questo protocollo, quasi tutti (tranne ACTION)
hanno dei lati negativi dal punto di vista della privacy e possono
permettere a persone connesse allo stesso server di `ottenere informazioni`_ l'uno
dell'altro. In IRSSI è possibile ignorare i CTCP inserendo i seguenti
comandi nel file :span:`.irssi/config|code`

.. code-block:: bash

   /ignore * CTCPS
   /ignore * DCC

Altro
-----

I livelli aggiuntivi per la tutela della privacy non mancano. Tra
questi:

- usare la porta SSL per la connessione al server IRC se non si dispone
  di i2p
- usare una cartella criptata con `EncFS`_ o `Tomb`_ per le impostazioni 
  di IRSSI (:span:`.irssi|code`), così da mettere al sicuro i log, le password e le 
  email delle nostre attività di chat
- usare il plugin `OTR`_ di IRSSI 
  per cifrare le nostre comunicazioni sul server e fare in modo che non
  ne rimanga traccia neanche lì (le comunicazioni rimarranno comunque
  in chiaro nella nostra cartella dei log)

.. _i2p: http://www.i2p2.de
.. _istruzioni: http://www.i2p2.de/debian.html
.. _vhost: http://en.wikipedia.org/wiki/Vhost_(IRC)#Hostmasks
.. _IRSSI: http://www.irssi.org
.. _Autistici/Inventati: http://www.autistici.org/it/index.html
.. _CTCP: http://en.wikipedia.org/wiki/Client-To-Client_Protocol
.. _ottenere informazioni: http://ugha.i2p.to/HowTo/IrcAnonymityGuide
.. _EncFS: http://www.arg0.net/encfs
.. _Tomb: http://tomb.dyne.org
.. _OTR: http://irssi-otr.tuxfamily.org
