Title: Usare il pacchetto LaTeX xfrac su Ubuntu Lucid
Date:  2010-07-26 22:10:48
tags: ubuntu, latex, gnulinux

Questo è un post per smaliziati utenti LaTeX.
Capita spesso di dover inserire nei propri documenti delle frazioni, e sarebbe
bello ed esteticamente gradevole farlo usando non solo la solita piatta linea
orizzontale di frazione, ma una bella sbarra obliqua. Il pacchetto che
permette ciò e xfrac, ed ha un'altra importante caratteristica: riesce
agevolmente a gestire tutti i tipi di font usati per il testo, senza generare
fastidiose incongruenze. Purtroppo xfrac non è compreso in TeXLive, la
distribuzione LaTeX pacchettizzata per Debian ed Ubuntu, e tocca installarlo
manualmente. Ma anche dopo averlo installato, si avrà un errore. Vediamo come
procedere.


Scarichiamo il pacchetto da CTAN:

    :::bash
	wget http://mirror.ctan.org/macros/latex/contrib/mh.zip

Spostiamolo nella cartella di sistema di LaTeX, estraiamo l'archivio e cancelliamo lo zip:

    :::bash
	sudo mv mh.zip /usr/share/texmf/tex/latex
	sudo unzip /usr/share/texmf/tex/latex/mh.zip
	sudo rm mh.zip

Entriamo nella cartella e compiliamo il pacchetto

    :::bash
	cd mh
	sudo tex *.dtx

In questo momento, il pacchetto avrebbe dovuto funzionare, ma ci darà
errore perché, come è stato [segnalato][1] nel bug tracker di Debian, xfrac
dipende da alcuni file di stile (_template.sty_) che sono presenti nella nuova
distribuzione di LaTeX (LaTeX3). Quindi, adesso sarà sufficiente installare
l'apposito pacchetto e rigenerare la cache dei file di stile:

    :::bash
	sudo apt-get install texlive-latex3
	sudo texhash


   [1]: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=425591
