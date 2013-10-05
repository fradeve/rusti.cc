Title: Debian + Xfce4 su NeoFreerunner
Date:  2008-09-22 22:06:27
featured: yes
tags: freerunner, gnulinux, openmoko, pygtk, python, ubuntu,
---

Dopo l'arrivo del Neo FreeRunner, non ho resistito alla tentazione
di installarci, in ordine, Qtopia, Openmoko 2008.08-update e poi Debian. Tra
le tre distro, solo la prima e l'ultima sono state in grado di farmi
ricevere/effettuare telefonate (uso una vecchia SIM Omnitel). Gli SMS vengono
gestiti perfettamente da tutte le distribuzioni. Tuttavia, nell'ottica di
avere un cellulare/palmare con cui poter fare qualsiasi cosa, rimangono in
ballo solo Qtopia e Debian. Su Qtopia le uniche librerie di sviluppo
supportate sono le Qt, e considerato che mi diverto con il PyGtk, anche Qtopia
viene scartata.


In questa guida vedremo come installare Debian con Xfce4 sul
Neo. In generale, il primo impatto è stato veramente molto positivo. Il
processore da 400 MHz del Neo ha la potenza di calcolo necessaria per ospitare
il desktop enviroment, che risponde molto velocemente alle richieste
dell'utente. Debian + Xfce4 per l'avvio impiega 1 minuto e 40 secondi, contro
gli almeno 3 minuti e 30 secondi di Openmoko. Piccolo neo: i caratteri del
desktop sono un po' piccoli, ma con un po di pazienza tutto si può ingrandire.


Veniamo al dunque: occorre prima di tutto partire da un'installazione di un
"qualsiasi" sistema operativo GNU/Linux nella memoria flash del Neo (che è di
256 Mib). La distribuzione Openmoko 2007.02 che trovate di default all'acquisto
va benissimo, anche se io sono partito dalla Openmoko 2008.08. Durante
l'installazione Debian si auto scaricherà completamente dalla rete, quindi c'è
la necessità di connettere il Neo ad internet. Consiglio vivamente di farlo
via USB, quindi occorre avere accesso al palmare via SSH. Per farlo, è
sufficiente seguire le [istruzioni presenti nel Wiki italiano][1]. Appena
finito, potremo testare la connessione con un semplice

	ping www.google.it 


Debian verrà installato
nella microSD (quella da 512 Mib in dotazione con il Neo, al termine
dell'installazione, avrà disponibili solo 30 Mib circa, quindi è consigliato
dotarsi di microSD di dimensioni pari o superiori ad 1 Gib). Si presume che la
scheda sia inserita nel Neo; se non lo fosse, spegnetelo, inserite la scheda e
riaccendetelo entrando in Openmoko. Fate il login via SSH nell'Openmoko,
solitamente

	ssh root@192.168.0.202

Dovreste essere posizionati nella home del sistema operativo.
Adesso, scarichiamo lo script che ci permetterà di installare Debian, con il
comando da SSH

	wget http://pkg-fso.alioth.debian.org/freerunner/install.sh

Rendiamo eseguibile
lo script con

	chmod +x install.sh

A questo punto non ci resta che eseguire lo script per installare Debian. Lo
script scaricherà direttamente sulla microSD tutti i pacchetti necessari
all'installazione di Debian, quindi **qualsiasi dato sulla scheda verrà
cancellato**, è bene che lo sappiate. Tuttavia, Qtopia o Openmoko (il secondo
si basa comunque sul primo) potrebbero avere ancora accesso alla scheda,
quindi "uccidiamo" il processo di Qtopia, con

	killall qpe

Quindi finalmente eseguiamo lo script

	SD_PART1_FS=vfat ./install.sh all

Specificando questa opzione, lo script creerà automaticamente la partizione
Vfat per l'avvio, che altrimenti avremmo dovuto creare manualmente. Durante
l'esecuzione dello script potremmo ricevere errori che fanno riferimento al
fatto che la partizione _/dev/mmcblk0p1_ contiene un filesystem montato. In
questo caso, possiamo smontarlo con

	umount /media/mmcblk0p1

Oppure possiamo controllare qual'è il PID dei
processi che usano quella partizione con il comando

	fuser -m /media/mmcblk0p1

e quindi ucciderli tutti con il comando

fuser -m /media/mmcblk0p1 | grep killall

Attenzione: questi comandi non sempre funzionano,
ma possono sicuramente tornare utili.


Adesso, andiamo a prenderci un bel
cappuccino, un cornetto, ed una fetta di torta. Forse sarebbe meglio anche
fare una passeggiata per digerire, perché l'installazione dura più di un'ora.
Al termine, dovremmo trovare nel terminale un messaggio del tipo "_Done.
Reboot and enjoy!_" Non ci resta che spegnere il Neo con il comando

	shutdown now

Attenzione: ora che abbiamo un Neo in dual boot, per poter avviare uno dei due sistemi, dovremo
**per forza accenderlo accedendo alla NOR**; per farlo, tenere premuto il
pulsante AUX, quindi premere contemporaneamente POWER e dopo che AUX ha emesso
un lampeggìo, lasciare POWER. Da questo menù, sarà possibile selezionare
l'opzione _boot_ per avviare Openmoko o Qtopia e l'opzione _Boot from SD
(FAT+ext2) _per avviare Debian. Scorrere il menù con il tasto AUX e
selezionare la seconda voce con POWER. Debian non ci metterà molto ad avviarsi
(meno di Openmoko 2008.08). Rimarremo delusi, forse ci aspettiamo un bel
desktop con lo _swirl_, in realtà troveremo solo l'essenziale interfaccia
grafica di Zhone, il programma di base per le telefonate, che purtroppo fa
solo quello.


Dobbiamo installare Xfce4. Per farlo quindi e necessario usare il
potere della Supermucca di APT :) Logghiamoci via SSH. Probabilmente avremo
problemi perché il Neo, pur avendo mantenuto il proprio indirizzo
192.168.0.202, ha cambiato sistema operativo. Sul terminale uscirà un
messaggio d'errore che potremo facilmente aggirare editando il file
_~/.ssh./known_hosts_ e cancellando tutto ciò che contiene:

	nano ~/.ssh./known_hosts

Quindi, riproviamo:

	ssh root@192.168.0.202

siamo in Debian! Installiamo un po di pacchetti utili:

	apt-get install xfce4 nano

Al termine, sarà meglio editare il file _/etc/fstab_ per evitare 
il filesystem check che rallenta di molto l'avvio di Debian: 

	nano /etc/fstab

e trasformiamolo da così

	rootfs  /
	ext2    defaults,errors=remount-ro,noatime      0 1 /dev/mmcblk0p1  /boot
	vfat    defaults,noatime                        0 2 /dev/mtdblock6  /mnt/flash
	jffs2   defaults,noatime,noauto         0 2 proc    /proc           proc
	defaults                                0 0 tmpfs   /tmp            tmpfs
	defaults,noatime                        0 0 tmpfs   /var/lock       tmpfs
	defaults,noatime                        0 0 tmpfs   /var/run        tmpfs
	defaults,noatime                        0 0 tmpfs   /var/tmp        tmpfs
	defaults,noatime                        0 0 

a così:

	rootfs  /               ext2    defaults,errors=remount-
	ro,noatime      0 0 /dev/mmcblk0p1  /boot   vfat    defaults,noatime
	0 0 /dev/mtdblock6  /mnt/flash      jffs2   defaults,noatime,noauto         0
	0 proc    /proc           proc    defaults                                0 0
	tmpfs   /tmp            tmpfs   defaults,noatime                        0 0
	tmpfs   /var/lock       tmpfs   defaults,noatime                        0 0
	tmpfs   /var/run        tmpfs   defaults,noatime                        0 0
	tmpfs   /var/tmp        tmpfs   defaults,noatime                        0 0

Adesso, dobbiamo fare in modo che Debian all'avvio non carichi
Zhone, ma Xfce come desktop environment predefinito.

	nano /etc/init.d/zhone-session

e modifichiamo la riga 17 da così:

	PROG_FSO=/usr/bin/zhone-session

a così:

	PROG_FSO=/usr/bin/startxfce4

Adesso possiamo riavviare e goderci il nostro Xfce :D Per liberare un po'
 di spazio nella partizione root di Debian possiamo dare un bel
	
	apt-get clean apt-get autoclean

Di default, c'è un piccolo inconveniente: non esiste
il click con il tasto destro. Per ovviare a questo fastidiosa carenza, i
passaggi seguenti ci permetteranno di installare un pacchetto che farà 
percepire ad X una pressione prolungata del touchscreen come un click destro,
correggendo una sfasatura della posizione del puntatore che si verifica a
causa di un bug del pacchetto.

	wget http://www.ohli.de/download/xserver-xorg-input-tslib_0.0.4-5+fso2_armel.deb
	wget http://pkg-fso.alioth.debian.org/freerunner/pointercal dpkg -i xserver-
	xorg-input-tslib_0.0.4-5+fso2_armel.deb
	mv pointercal /etc/pointercal
	shutdown now

Al riavvio, tutto sarà sistemato. Per facilitarci la vita
nelle prossime connessioni via SSH, possiamo modificare il file _/etc/hosts_
ed inserire l'IP del nostro PC collegato al Neo via USB:

	nano /etc/hosts 192.168.0.200 pc

In questo modo potremo inviare file dal Debian al PC semplicemente scrivendo _scp
file.est nomeutente@pc_:~.


E adesso, la parte più importante: telefonare. Potremo avviare Zhone da
**Menù -> Office -> Zhone**. Appena avviato, il software riconoscerà automaticamente la nostra SIM, ci chiederà il PIN e ci permetterà di effettuare/ricevere chiamate, SMS, oltre
che di sfogliare la rubrica. Personalmente, mi sono premurato di mantenere su
Xfce solo 2 desktop, uno solo per Zhone e l'altro per tutti gli altri
programmi in esecuzione (Iceweasel, Liferea, XMMS). In questo modo è facile
switchare dal desktop "PC" a quello "telefono" senza troppi problemi.

Buon divertimento!

   [1]: http://wiki.openmoko.org/wiki/Getting_Started_with_your_Neo_FreeRunner/it#Connettere_il_Neo_FreeRunner_alla_Rete_via_USB
