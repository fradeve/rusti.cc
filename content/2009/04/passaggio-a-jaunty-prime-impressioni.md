Title: Passaggio a Jaunty: prime impressioni
Date:  2009-04-28 09:15:14
tags: gnulinux, ubuntu, dell

Sono passati due anni da quando ho comprato il
mio primo portatile un Dell Inspiron 640m (14''), che dopo l'uscita dei
netbook è diventato il mio "PC fisso" da tenere sulla scrivania (visto che per
prendere appunti all'università uso direttamente l'EEE 901).


Dopo l'acquisto due anni fa, la prima cosa che feci fu ovviamente installare
l'ultima Ubuntu (all'epoca era appena uscita la Feisty e Gutsy era ancora in
lavorazione). Da allora, di aggiornamento in aggiornamento sono passato fino
ad Intrepid senza troppi problemi (e passato anche da KDE a GNOME a metà
strada); ho installato e testato software (soprattutto [giochi per il Wiki][1]
di Ubuntu-it), creato e formattato partizioni, ma lo "zoccolo duro" di Ubuntu
è rimasto li.


Adesso, con l'uscita di Jaunty, e per la frammentazione delle partizioni, e
per la quantità interessante di dati, file di configurazione, residui di
installazioni, ecc, ho deciso di radere al suolo tutte le partizioni presenti
sull'hard disk e fare un'installazione pulita di Ubuntu 9.04 Jaunty Jackalope
(che solo per scriverlo ci vuole una laurea).


Purtroppo, ho trovato subito una spiacevole sorpresa: pensavo che i driver
Intel (ho una scheda grafica integrata Intel 945GM) fossero stabili ed
inattaccabili, ma dopo l'installazione, sebbene l'accelerazione grafica fosse
abilitata, gli FPS erano ad un livello talmente basso da rasentare lo
scandalo. Su [consiglio][2] del Forum ho inserito una riga per l'"uxa" nel mio
xorg.conf:


	Section "Device"
		Identifier      "Configured Video Device"
		Option          "AccelMethod" "uxa"
	EndSection


L'accelerazione grafica è tornata ad essere prestante, ma l'opzione ha dato
luogo ad un memory leak che nel giro di 20 minuti riempie swap/ram, piantando
il sistema. Ci ho messo 2 giorni per capire cosa stesse succedendo (e li la
mia fiducia in Ubuntu ha seriamente vacillato). Ancora una volta il [forum][3]
e [Launchpad][4] mi son venuti in aiuto, ed alla fine ho dovuto disabilitare
l'accelerazione grafica e Compiz, passando a Metacity, almeno fin quando le
cose non si risolveranno. Qualcuno ha consigliato di passare da "uxa" ad
"exa",


	Section "Device"
		Identifier      "Configured Video Device"
		Option          "AccelMethod" "exa"
	EndSection


ma a questo punto, tant'è, mi accontento di [Metacity][5]. Per abilitare
Metacity:

    :::basH
	gconftool-2 -s '/apps/metacity/general/compositing_manager' --type bool true


Nota positiva: disattivando Compiz e attivando Metacity, ho riscoperto una
freschezza e una prontezza del sistema che avevo dimenticato dalla Gutsy in
poi: gli effetti grafici sono modesti ma equilibrati, la velocità del sistema
è eccellente... tutto sommato: chi si accontenta, gode ;)

   [1]: http://wiki.ubuntu-it.org/Giochi

   [2]: http://forum.ubuntu-it.org/index.php/topic,250190.msg2017461.html#msg2017461

   [3]: http://forum.ubuntu-it.org/index.php/topic,282239.msg2038277.html#msg2038277

   [4]: https://bugs.launchpad.net/ubuntu/+source/compiz/+bug/328232

   [5]: http://it.wikipedia.org/wiki/Metacity
