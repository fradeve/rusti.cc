Title: Installare pymedia su Ubuntu 8.10 Intrepid Ibex
Date:  2008-12-11 14:31:13
tags: openstreetmap, python, ubuntu, gnulinux

Recentemente, ho avuto necessità di utilizzare la
libreria [PyMedia][1], per renderizzare alcune tracce raccolte durante il
primo Archaeologic Mapping Party di OpenStreetMap in Italia (e nel mondo) a
Pompei.


PyMedia è una libreria che permette a Python di manipolare file
multimediali (audio/video/immagini). Il problema è che PyMedia non esiste nei
repository di Ubuntu 8.10 Intrepid Ibex, e l'unico pacchetto _.deb_ disponibile
in rete è adatto a Python 2.4 e ad una vecchia versione di Ubuntu. Per questo,
ho compilato e pacchettizzato con [checkinstall][2] PyMedia per Ubuntu 8.10
Intrepid Ibex. Il pacchetto potete scaricarlo da [qui][3], oppure potete
compilarvelo come segue.

## Passo 1. Ottenere pymedia ##

    :::bash
	wget http://internap.dl.sourceforge.net/sourceforge/pymedia/pymedia-1.3.7.3.tar.gz
	tar xzvf pymedia-1.3.7.3.tar.gz cd pymedia-*

## Passo 2. Installare le dipendenze ##

    :::bash
	sudo apt-get install python-dev libogg-dev libvorbis-dev liblame-dev libfaad-dev libasound2-dev python-pygame

## Passo 3. Installare GCC 3.4 ##
(PyMedia non si compilerà con GCC 4.0)

    :::bash
	sudo apt-get install gcc-3.4 g++-3.4 export CC=gcc-3.4

## Passo 4. Fare alcune modifiche al codice C ##
Prima di compilare, in `<audio/acodec/acodec.c>`, alla
linea 31, inserire quanto segue:

    :::bash
	#define HAVE_LRINTF

In maniera tale da ottenere:

    :::bash
	#include avcodec.h
	#define HAVE_LRINTF
	#include "libavcodecdsputil.h"
	#include "version.h"

## Passo 5. Costruire e compilare pymedia ##

    :::bash
	sudo python setup.py build

## Passo 6. Essere bravi utenti Ubuntu e installare PyMedia con checkinstall ##

    :::bash
	sudo apt-get install checkinstall
	sudo checkinstall python setup.py install

_Nota: Se si vuole essere dei cattivi utenti Ubuntu, è possibile installare
PyMmedia senza creare il .deb, sostituendo il comando precedente con "sudo
python setup.py install"._

## Passo 7. Controlliamo se funziona ##
in un terminare digitare "python" e poi
`import pymedia`; se non otteniamo errori, siamo a cavallo :D

    :::bash
	python >>> import pymedia

   [1]: http://pymedia.org/

   [2]: http://asic-linux.com.mx/%7Eizto/checkinstall/

   [3]: http://dl.dropbox.com/u/369614/software/pymedia_1.3.7.3-1_i386.deb 
