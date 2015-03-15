Youtube-dl: interfaccia per il programma da repo
================================================

:date: 2007-10-25 16:45:19
:tags: ubuntu

Oggi vorrei parlarvi di un piccolo ma utilissimo software creato da un
amico, `Davide Contalbo`_. Si
chiama Youtube-dl e, come avrete intuito, serve a scaricare i filmati
dal nostro sito di videostreaming flash preferito. Notare che Youtube-dl
e anche il nome del pacchetto che svolge la stessa funzione, presente
nei repository di Ubuntu. La differenza tra questo pacchetto e lo script
scritto da Davide è che quest'ultimo aggiunge (tramite Zenity) una
amichevole ma intuitiva interfaccia grafica al programma vero e proprio.
Il programma, terminato il download, permette anche di convertire il
video in vari formati (mpeg, avi, 3gp, Wmv).

.. _Davide Contalbo: http://contalbodavide.blogspot.com

Ok, credo di aver parlato anche troppo, passiamo alla pratica.
Installiamo le dipendenze (ovvero i pacchetti ``youtube-dl``, ``zenity``
ed ``ffmpeg``). Da terminale, diamo un bel

::

    sudo nano /usr/bin/youtube-dl

Incolliamo lo script vero e proprio

::

    #!/bin/bash
    # Funzione che configura il terminale da usare
    function config {
    cd ~/Desktop
    msg=`zenity --title="XBackup" --list --text="Ridurre le notifiche e i messaggi di informazioni?" --radiolist  --column="Scegli" --column="Abilita" false "Si" false "No"`
    if [[ $msg = "Si" ]];
    then
    msg=1;
    elif [[ $msg = "No" ]];
    then
    msg=0;
    else
    zenity --error --title="XBackup - Errore" --text="Nessuna scelta effettuata - Uscita inattesa"
    exit 1;
    fi

    de=`zenity --title="Youtube-DL" --text="Quale DE utilizzate tra questi sottostanti?" --list --radiolist  --column="Scegli" --column="Desktop Environment" false "Gnome" false "Kde" false "Xfce"`
    if [[ $de = "Gnome" ]]
    then
    if [[ $msg -eq 0 ]]
    then
    zenity --info --title="Youtube-DL - Informazioni" --text="Ambiente Grafico Gnome"
    else
    sleep 1;
    fi
    terminal="gnome-terminal -x"
    elif [[ $de = "Kde" ]];
    then
    if [[ $msg -eq 0 ]]
    then
    zenity --info --title="Youtube-DL - Informazioni" --text="Ambiente Grafico Kde"
    else
    sleep 1;
    fi
    terminal="konsole -e"
    elif [[ $de = "Xfce" ]];
    then
    if [[ $msg -eq 0 ]]
    then
    zenity --info --title="Youtube-DL - Informazioni" --text="Ambiente Grafico Xfce"
    else
    sleep 1;
    fi
    terminal="xfce-terminal -x"
    else
    zenity --error --title="Youtube-DL - Errore" --text="Nessuna scelta effettuata - Uscita inattesa"
    exit 1;
    fi
    }

    # Funzione che permette di convertire i file flv nei formati richiesti
    function trasform {
    formato=`zenity --width=300 --height=300  --title="Youtube-DL" --list --radiolist  --text="In quale formato deve essere trasformato il tuo video?" --column="Scegli" --column="Formati" false "3gp"  false "Wmv" false "Mpeg" false "Avi" false "Ogg"`
    zenity  --info ---title="Youtube-DL - Informazioni" --text="Adesso verrà aperto un terminale che serve al programma per trasformare il file nel formato desiderato"
    if [[ $formato = "3gp" ]]
    then
    $terminal ffmpeg -i tmp_file.flv -s 176x144 -r 15.0 -b 80k -vcodec h263 -ar 8000 -ac 1 -acodec amr_nb -y ${video_name}.3gp
    if [[ $msg -eq 0 ]]
    then
    zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="File ${video_name}.3gp creato - Rilanciare il software per trasformarlo in un altro formato"
    zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="Grazie per aver usato il software"
    else
    sleep 1;
    fi
    elif [[ $formato = "Wmv" ]];
    then
    if [[ $msg -eq 0 ]]
    then
    $terminal ffmpeg -i tmp_file.flv ${video_name}.wmv
    zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="File ${video_name}.wmv creato - Rilanciare il software per trasformarlo in un altro formato"
    zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="Grazie per aver usato il software"
    else
    sleep 1;
    fi
    elif [[ $formato = "Avi" ]];
    then
    $terminal ffmpeg -i tmp_file.flv ${video_name}.avi
    if [[ $msg -eq 0 ]]
    then
    zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="File ${video_name}.avi creato - Rilanciare il software per trasformarlo in un altro formato"
    $terminal zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="Grazie per aver usato il software"
    else
    sleep 1;
    fi
    elif [[ $formato = "Mpeg" ]];
    then
    if [[ $msg -eq 0 ]]
    then
    ffmpeg -i tmp_file.flv ${video_name}.mpg
    zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="File ${video_name}.mpg creato - Rilanciare il software per trasformarlo in un altro formato"
    zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="Grazie per aver usato il software"
    else
    sleep 1;
    fi
    elif [[ $formato = "Ogg" ]];
    then
    if [[ $msg -eq 0 ]]
    then
    ffmpeg -i tmp_file.flv ${video_name}.ogg
    zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="File ${video_name}.ogg creato - Rilanciare il software per trasformarlo in un altro formato"
    zenity --info  --width=300 --title="Youtube-DL - Informazioni" --text="Grazie per aver usato il software"
    else
    sleep 1;
    fi
    else
    zenity --error --width=300  --title="Youtube-DL - Errore" --text="Nessuna scelta effettuata - Uscita inattesa"
    exit 1;
    fi
    }


    # MENU PRINCIPALE e cuore del programma
    zenity --info --width=300 --title="Youtube-DL" --text "Programma per scaricare i video da YouTube e trasformarli vari formati"
    config
    find tmp_file.flv
    if [[ $? -eq 0 ]];
    then
       zenity --info --width=300 --title="Youtube-DL - Informazioni" --text "File già scaricato                 "
    video_name=`zenity --entry --title="Youtube-DL" --text "Inserisci il nome che vuoi dargli (senza estensione)"`
    else

      video_url=`zenity --entry --title="Youtube-DL" --text "Inserisci l'url del video da YouTube"`
    video_name=`zenity --entry --title="Youtube-DL" --text "Inserisci il nome che vuoi dargli (senza estensione)"`
    zenity  --info ---title="Youtube-DL - Informazioni" --text="Adesso verrà aperto un terminale che serve al programma per scaricare il file nel formato flv"
    $terminal youtube-dl -o tmp_file.flv  $video_url
    fi
    trasform
    rm tmp_file.flv

Sempre da terminale, eseguire il comando

::

    sudo chmod a+x /usr/bin/youtube-d

Si potrà eseguire il programma con il comando da terminale youtube-dl

Osservazioni
------------

Purtroppo, qualche perfezionamento andrebbe inserito: non sarebbe una
cattiva idea affiancare quei formati video proprietari con un sano .ogg,
e forse si potrebbero ridurre al minimo le conferme sulle azioni svolte.
Comunque, rimane uno script molto efficace, che va dritto all'obiettivo
;) Una nota di merito: al contrario di Gentube (altro famoso programma
che svolge la stessa funzione), tutti i file di configurazione e
temporanei necessari all'esecuzione di questo script (presenti in Home)
vengono cancellati al termine del programma. Buon divertimento!
