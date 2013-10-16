Title: Network Manager + Ubuntu 8.10 + Asus 901
Date:  2008-11-11 22:31:02
tags: gnulinux, python, ubuntu

Uno dei problemi più interessanti in cui mi sono
imbattuto dopo l'installazione di Ubuntu 8.10 "Intrepid Ibex" su Asus 901 è
stato sicuramente quello relativo a Network Manager.

In realtà, ho sempre usato Wicd, perché e più veloce nel connettere, più
intuitivo da gestire, perché è sviluppato in Python ed è più leggero di
Network Manager, senza parlare del fatto che si installa tranquillamente con
un unico pacchetto valido per tutte le architetture, mentre NM e strutturato
in 2 pacchetti più un paio di dipendenze.


Unico problema: Wicd non è in grado di gestire la connessione alla rete
wireless degli studenti all'Università di Bari, motivo per cui sono stato
costretto a tornare a Network Manager, che nelle ultime due versioni di Ubuntu
devo ammettere è decisamente migliorato.


Ma, sorpresa: all'avvio di Ubuntu 8.10 sul mio Asus 901, l'applet di Network
Manager non si avvia in automatico, anzi a dir la verità non si avvia proprio,
restituendomi un simpatico errore da terminale a proposito di una connessione
mancante.


Girando un po' per la rete, scopro che il bug è già stato segnalato e che è in
attesa d'essere risolto. Nel frattempo, sono state elaborate due soluzioni
artigianali, che dovrebbero funzionare distintamente l'una dall'altra, ma che
in realtà ho applicato contemporaneamente. Se avete il mio stesso problema,
provateci.


La prima cosa da fare è installare sul proprio sistema i pacchetti aggiornati
da SVN di NetworkManager, disponibili nel seguente repository su Launchpad,
aggiungetelo al vostro source.list:

    :::bash
	deb http://ppa.launchpad.net/network-manager/ubuntu intrepid main

Dopo aver dato un bel

    :::bash
	sudo apt-get update
	sudo apt-get upgrade

avrete aggiornato i pacchetti.

Adesso, dobbiamo commentare le seguenti righe (ammesso che le abbiate) nel
file _/etc/network/interfaces_:

    :::bash
	sudo nano /etc/network/interfaces
	#auto eth0
	#iface eth0 inet manual

Salvate e chiudete il file. Ora, dopo un bel riavvio del sistema, provate a
dare

    :::bash
	sudo killall NetworkManager
	sudo killall nm-applet
	NetworkManager
	nm-applet

Quindi, dovreste assistere al magico avvio dell'applet di NetworkManager nella
vostra traybar, e connettervi senza troppi problemi.
