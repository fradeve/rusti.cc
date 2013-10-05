Title: GRUB e l'opzione VGA in Ubuntu Natty
Date:  2011-05-03 14:30:00
tags: ubuntu,

Dopo l'upgrade a Natty Narwal, a fasi alterne, GRUB sembrava non voler avviare la mia installazione. In sostanza, dopo l'avvio di tutti i processi di sistema, il server X sembrava _freezare_ e non volersi avviare più. Per puro caso ho scorto un messaggio di errore di una frazione di secondo tra la scomparsa di GRUB e l'avvio del sistema, che parlava di un problema legato alla voce `vga`.

Uno dei grandissimi vantaggi di GRUB è la possibilità di modificare in tempo reale le opzioni della voce di avvio con la pressione del tasto `e`, per cui mi è sembrato ragionevole eliminare la voce `vga=775` e tentare un avvio, cosa che ha funzionato.

[Indagando oltre][1], è venuto fuori che l'opzione _vga_ è quella che permette di modificare la risoluzione e profondità di colore durante l'avvio del sistema operativo. Per qualche arcano motivo la mia scheda grafica (nVidia Corporation G80 GeForce 8800 GTS rev a2) o i driver in uso (proprietari, purtroppo) non supporta la modalità 775 e quindi eliminando o modificando la voce `vga` quantomeno il sistema si avvia. Che fare, procedere per tentativi, o qualcuno conosce una maniera più coerente di affrontare la situazione?

   [1]: http://pierre.baudu.in/other/grub.vga.modes.html

