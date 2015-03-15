Getting Things GNOME + Tomboy = todo + note
===========================================

:date: 2010-02-01 21:55:23
:tags: gtd, gnulinuX

.. raw:: html

   <center>

|image0|

.. raw:: html

   </center>

Recentemente ho scoperto un programma che stavo cercando da tempo:
`Getting Things GNOME`__, alias GTG. I todo,
le liste delle cose da fare, fanno allegramente parte della mia giornata
da qualche anno ormai, complice un po' la deformazione scientifica a
catalogare, ordinare, compartimentalizzare tutto il lavoro :D

GTG è un programma che sebbene relativamente giovane (siamo ancora alla
versione 0.2) promette veramente bene. Si presenta all'utente con
un'interfaccia molto semplice, costituita dalla barra dei pulsanti in
alto, la lista delle cose da fare sulla destra e quella dei tag sulla
sinistra.

Per ogni cosa da fare è possibile definire una data di inizio ed una
data di fine, oltre che un tag. Ad ogni tag può essere associato un
colore, chiaramente visibile accanto al tag nella lista dei tag o sullo
sfondo della voce nella lista delle cose da fare. In base alla data di
scadenza di ogni impegno è possibile ordinare la lista dei todo, e
accanto ad ogni voce verranno visualizzati quanti giorni mancano alla
scadenza. È possibile ordinare la lista delle cose da fare per tag, per
priorità o semplicemente in ordine alfabetico :D

Penso che il grande punto di forza di GTG sia la possibilità di
aggiungere plugins, che come Firefox ha dimostrato, è una caratteristica
essenziale di un programma realizzato in maniera collaborativa. Essendo
GTG completamente scritto in Python, anche i plugin vengono scritti con
tale linguaggio, e questo costituisce probabilmente un vantaggio: Python
è un linguaggio di programmazione molto popolare. I plugin attualmente
disponibili non sono molti: oltre a quello per sincronizzare il proprio
todo di Remember the Milk, c'è un plugin di integrazione con Tomboy.

A questo proposito, Tomboy sembra essere proprio il punto di partenza
per lo sviluppo dell'editor dei todo in GTG: quando si va ad editare o a
creare un impegno, la finestra di editing è quasi identica a quella di
Tomboy, con la sola differenza che le parole *StileWiki* non vengono
collegate automaticamente alle omonime note. L'integrazione con Tomboy,
invece, è semplice quanto accattivante: in fase di editing è sufficiente
premere il pulsante "aggiungi nota Tomboy" per far apparire una casella
di testo in cui digitando le prime lettere della nota di Tomboy che si
sta cercando, parte una ricerca dinamica che screma in tempo reale i
risultati. Una volta confermato, la simpatica nota di Tomboy compare
sulla nota, e cliccandoci sopra si aprirà direttamente la nota del
famoso programma con i post-it gialli.

Qualcuno sta sviluppando in questo periodo un plugin per l'integrazione
con Tomboy. Insomma, a Getting Things GNOME manca solo la
sincronizzazione con Google Calendar, e poi dichiarerei il programma
molto vicino all'essere realmente completo.

L'integrazione tra GTG e Tomboy mi rende particolarmente entusiasta,
perché - almeno per quanto mi riguarda - non riesco a fare a meno di
Tomboy per i piccoli appunti e le piccole note, ma non è utile per
definire scadenze e pianificare le cose da fare; al contrario, non
affiderei mai a GTG le mie singole note. L'integrazione tra i due è
l'ideale ;)

Adesso, non vi resta che provarlo: GTG è già nei repository di Karmic;
per Jaunty lo potete trovare in `questo PPA`__; GTG non supporta 
versioni di Ubuntu precedenti a Jaunty :)

.. |image0| image:: http://dl.dropbox.com/u/369614/blog/img_red/gtg-0.2-all-shad.png
.. _Getting Things GNOME: http://gtg.fritalk.com
.. _questo PPA: https://edge.launchpad.net/%7Egtg/+archive/ppa
