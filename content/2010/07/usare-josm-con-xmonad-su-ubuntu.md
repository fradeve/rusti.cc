Title: Usare JOSM con Xmonad su Ubuntu
Date:  2010-07-03 19:04:51
tags: xmonad, ubuntu, openstreetmap, josm, gnome,

Come molti di voi sapranno, JOSM è un programma in Java
che viene utilizzato dai "mappatori liberi" per contribuire ad OpenStreetMap,
la "Wikipedia delle mappe". Da qualche tempo sto usando Xmonad come gestore di
finestre  (con grandissima soddisfazione, peraltro) ed ho scoperto che sulla
rosa c'è anche qualche spina: oggi, quando ho aperto JOSM, la finestra è
apparsa, ma il suo contenuto era completamente grigio. Come si può agevolmente
leggere nelle [note di installazione][1] sul wiki di JOSM, il problema è tutto
tra Java e Xmonad, ed è facilmente risolvibile.

Su Debian/Ubuntu, è sufficiente installare il pacchetto [dwm-tools][2], e poi dare da terminale:

	wmname LG3D

ogni volta prima di aprire JOSM.
Alternativamente, si potrebbe anche creare un [alias nel proprio .bashrc][3],
per eseguire il comando ogni volta che si desidera aprire JOSM:

	alias josm='wmname LG3D && josm'

Per ulteriori informazioni, si può anche consultare il [wiki di Awesome][4] (progetto simile
ad Xmonad) per quel che riguarda la compatibilità con Java. Proprio lì si
legge che i problemi dovrebbero essere risolti con l'introduzione di Java JVM
e OpenJDK 1.7. Speriamo bene :)


**AGGIORNAMENTO --- 14/07/10**

Come mi han suggerito nel canale IRC del LUGBari, una soluzione alternativa è quella di
aggiungere la seguente riga nel proprio .bashrc (almeno su Ubuntu/Debian):

	_JAVA_AWT_WM_NONREPARENTING=1; export
	_JAVA_AWT_WM_NONREPARENTING

Quindi salvare il file e aggiornare bashrc con il comando

	source .bashrc


   [1]: http://josm.openstreetmap.de/wiki/InstallNotes

   [2]: http://packages.ubuntu.com/lucid/dwm-tools

   [3]: http://news.softpedia.com/news/How-to-Customize-the-Shell-Prompt-40033.shtml

   [4]: http://awesome.naquadah.org/wiki/Problems_with_Java
