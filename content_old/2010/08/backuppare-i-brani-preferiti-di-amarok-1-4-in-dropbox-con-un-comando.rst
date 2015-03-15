Backuppare i brani preferiti di Amarok 1.4 in Dropbox, con un comando
=====================================================================

:date: 2010-08-10 23:07:46
:tags: ubuntu, gnulinux, dropbox, amarok

Dropbox dà dipendenza, inutile negarlo. Da quando la uso mi è venuta
pian piano la mania di sincronizzare tutti i file di sistema vitali
(bashrc, vimrc), un po' perché uso molte macchine in diversi momenti o
luoghi durante la giornata, un po' perché mi dà la sicurezza di avere
almeno 3 copie dei miei file più importanti (tante sono le mie
macchine). Ed oggi ho aggiunto un tassello al puzzle: la playlist dei
miei brani preferiti in Amarok.

Sarà capitato anche a voi... di voler avere una lista backuppata dei
vostri brani preferiti. Bene, solitamente quando un brano mi piace, gli
assegno 5 stelle su Amarok (uso Amarok 1.4, il 2 non mi convince per
niente). In questo post vedremo proprio come creare una scorciatoia da
terminale per ordinare ad Amarok di salvare in un file .m3u, in una
cartella a nostro piacimento, ad esempio... Dropbox! Il gioco sta tutto
in `dcop`__, componente sul quale Amarok 1.4 basa molte delle sue 
funzioni relative alla gestione della musica (dcop è stato sostituito 
da d-bus in Amarok 2, per una migliore integrazione con KDE4).

La prima cosa da fare è impostare una "playlist veloce" in Amarok,
inserendo come condizione da verificare per l'inclusione nella playlist
che la valutazione sia massima (o comunque superiore ad una soglia di
vostro gradimento). Diamo un nome alla playlist che si possa ricordare,
ad esempio "bellissime".

Possiamo quindi passare ad Amarok, dopo averlo aperto, i seguenti
comandi tramite dcop:

::

    :::bash
    dcop amarok playlistbrowser loadPlaylist bellissime

Permette di caricare la playlist "bellissime" nel player;

::

    :::bash
    dcop amarok playlist saveM3u bellissime.m3u /home/user

Permette di esportare la playlist appena caricata nella propria home,
sostituendo ovviamente "user" con il proprio nome utente.

Possiamo quindi provare a concatenare i comandi, in un'unica stringa da
aggiungere ai nostri alias di .bashrc, ad esempio:

::

    :::bash
    dcop amarok playlistbrowser loadPlaylist bellissime && dcop amarok playlist saveM3u bellissime.m3u /home/user && mv /home/user/bellissime.m3u ~/Dropbox/bellissime.m3u

So che si poteva tranquillamente evitare l'ultimo comando, ma ho
preferito aggiungere un passaggio per rendere le cose più semplici. Il
nostro alias da aggiungere al file ~/.bashrc, quindi sarebbe:

::

    :::bash
    alias amarok-backup='dcop amarok playlistbrowser loadPlaylist bellissime && dcop amarok playlist saveM3u bellissime.m3u /home/user && mv /home/user/bellissime.m3u ~/Dropbox/bellissime.m3u'

Infine, aggiorniamo il nostro bashrc con

::

    :::bash
    source ~/.bashrc

Dovremo solamente stare attenti a seguire bene la procedura prima di
eseguire il comando "amarok-backup" da terminale, altrimenti potremmo
incorrere in un crash (non chiedetemi perché):

-  aprire amarok
-  cancellare dalla voce "playlist" del menù omonimo le vecchie playlist
   salvate in home e poi trasferite, altrimenti il nuovo backup non
   funzionerà
-  dare il comando "amarok-backup" da terminale
-  chiudere amarok

A ben pensarci, questo giochetto delle playlist si potrebbe fare anche
con una query sul database SQLite di Amarok 1.4... ma oggi non ne avevo
voglia :) Suggerimenti per rendere il tutto ancora più veloce?

.. _dcop: http://amarok.kde.org/wiki/DCOP_Functions
