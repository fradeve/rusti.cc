Title: Backup strategies
Date:  2012-04-14 15:15:00
featured: yes
lastupdated: 2013-05-19
tags: backup

Non ho molto tempo per spiegare l'immagine. In soldoni, è uno schema riassuntivo di come sono organizzati i miei dati ed i miei backup, realizzato anche per approfondire un po' la conoscenza di Graphviz. Il codice è in fondo al post.

<center>![][1]<br>_Storie di ordinario backup_</center>

_Legenda_

* in verde le cartelle cifrate
* sono state usate forme e frecce differenti per distinguere i processi
* le linee tratteggiate indicano le componenti che devono ancora essere implementate

Il codice dell'immagine:

    digraph G {
        // TODO
        // * legend
        graph [ dpi = 500 ];
        size ="4,6";	// table size
        compound=true;
        ranksep="1.5"
        rankdir="LR"

        subgraph cluster_edgar {
            style=filled;
            color=lightgrey;
            label = <<b>edgar</b>>;

            // boxes

            subgraph cluster_hd1 {
                style=filled;
                color="#008000";
                label="sda2";

                immagini_hd1 [label="img",shape=folder]
                musica_hd1 [label="music",shape=folder]
                books_hd1 [label="books",shape=folder]
                mail_hd1 [label="mail",shape=folder]
                video_hd1 [label="video",shape=folder]
                dev_hd1 [label="dev",shape=folder]
            }
            
            subgraph cluster_ssd {
                style=filled;
                color="#008000";
                label="ssd";

                irssi [label="~/.irssi",shape=folder]
            }

            // scripts and programs
            offlineimap [label="offlineimap",shape=component]
            btsync_edgar [label="BTSync",shape=component]
            rsnap_edgar [label="rsnapshot",shape=component]
            firefox_desktop [label="Firefox\ndesktop",shape=component]
            
            // folders
            filesystem_edgar [label="filesystem",shape=folder]
        }

        subgraph cluster_mail {
            style=filled;
            color=lightblue;
            label = <<b>Mail services</b>>;

            ai [label="A/I \nmail",shape=box3d,style=filled,fillcolor="#808000"]
            gmail [label="Gmail",shape=box3d]
            riseup [label="Riseup \nmail",shape=box3d,style=filled,fillcolor="#808000"]
        }

        subgraph cluster_services {
            style=filled;
            color=lightblue;
            label = <<b>Internet services</b>>;

            github [label="GitHub",shape=component]
            librefm [label="Libre.fm",shape=component]
            facebook [label="Facebook",shape=component]
            twitter [label="Twitter",shape=component]
            foursquare [label="Foursquare",shape=component]
            identica [label="Identi.ca",shape=component]
        }

        subgraph cluster_paranoia {
            style=filled;
            color=yellow;
            label = <<b>server 1</b> paranoia>;

            rsync_paranoia [label="rsync",shape=component]

            filesystem_paranoia [label="filesystem",shape=folder]
            
            subgraph cluster_pubwww_paranoia {
                style=filled;
                color=lightblue;
                label = "Public www";
                
                blog_pubwww [label="blog|site",shape=folder]
                others_pubwww_paranoia [label="others",shape=folder]
            }

            filesystem_paranoia -> rsync_paranoia
            others_pubwww_paranoia -> rsync_paranoia
        }

        subgraph cluster_sgagliozza {
            style=filled;
            color=cyan;
            label = <<b>server4</b> sgagliozza>;

            rsync_sgagliozza [label="rsync",shape=component]

            filesystem_sgagliozza [label="filesystem",shape=folder]

            subgraph cluster_pubwww_sgagliozza {
                style=filled;
                color=lightblue;
                label = "Public www";

                thblog_pubwww [label="th blog",shape=folder]
            }

            filesystem_sgagliozza -> rsync_sgagliozza
            thblog_pubwww -> rsync_sgagliozza
        }

        subgraph cluster_ovh {
            style=filled;
            color=orange;
            label = <<b>server2</b> ovh>;

            rsync_ovh[label="rsync",shape=component]
            filesystem_ovh [label="filesystem",shape=folder]
            
            subgraph cluster_pubwww_ovh {
                style=filled;
                color=lightblue;
                label = "Public www";

                others_pubwww_ovh [label="others",shape=folder]
            }

            filesystem_ovh -> rsync_ovh
            //others_pubwww_ovh -> html_back [ltail=cluster_pubwww_ovh]


            // other backups
            subgraph cluster_backup {
                style=filled;
                fillcolor=white;
                label = "backups";

                html_back [label="html\nbackups",shape=folder]
                db_back [label="db\nbackups",shape=folder]
            }
        }

        subgraph cluster_rpi{
            style=filled;
            color=brown;
            label = <<b>server 3</b> RPi>;

            owncloud [color=blue]
            lastexport [label="lastexport.py",shape=component]
            btsync_rpi [label="BTSync",shape=component]
            rsnap_rpi [label="rsnapshot",shape=component]
            mbsync [label="mbysnc",shape=component]

            filesystem_rpi [label="filesystem",shape=folder]

            subgraph cluster_pubwww_rpi {
                style=filled;
                color=lightblue;
                label = "Public www";

                owncloud [label="owncloud",shape=component]
                ttrss [label="TT-RSS",shape=component]
                videodb [label="VideoDB",shape=component]
                thinkup [label="ThinkUp",shape=component]
                fsyncms [label="FSyncMS",shape=component]
            }

            // owncloud backups
            subgraph cluster_owncloud_backup {
                style=filled;
                fillcolor=green;
                label = "RPi storage";

                immagini_back [label="img",shape=folder]
                video_back [label="video",shape=folder]
                musica_back [label="music",shape=folder]
                books_back [label="books",shape=folder]
                mail_back [label="mail",shape=folder]
                data_back [label="data\nbackups",shape=folder]
                dev_back [label="dev",shape=folder]
                firefox_back [label="Firefox",shape=folder]
                irssi_back [label="~/.irssi",shape=folder]
            }
        }

        subgraph cluster_android {
            style=filled;
            color=pink;
            label = <<b>Android</b>>;

            sms [label="Android \nSMS",shape=box3d]
            calendar [label="calendar",shape=component]
            contacts [label="contacts",shape=component]
            chatmobile [label="Gtalk\nmobile",shape=egg]
            ttrssmobile [label="TT-RSS\nmobile",shape=component]
            webdav [label="webDAV",shape=component]
            firefox_android [label="Firefox",shape=component]
        }

        chat [label="Gtalk\ndesktop|web\nlogs",shape=egg]
        
        // ## bindings ##

        // browser
        firefox_desktop -> fsyncms -> firefox_back -> firefox_android

        // chat
        irssi -> btsync_edgar
        irssi_back -> btsync_rpi
        chat -> gmail
        chatmobile -> gmail

        // android
        owncloud -> calendar [dir=both,style=dashed]
        owncloud -> contacts [dir=both,style=dashed]
        ttrss -> ttrssmobile
        webdav -> owncloud

        // server backups
        btsync_edgar -> btsync_rpi [color=forestgreen,dir=both]
        filesystem_edgar -> rsnap_edgar -> dev_hd1 -> btsync_edgar[color=forestgreen]
        //owncloud -> dev_hd1 [label="dd",ltail="cluster_rpi"]
        rsync_paranoia -> rsnap_rpi
        rsync_ovh -> rsnap_rpi
        rsync_sgagliozza -> rsnap_rpi
        rsnap_rpi -> dev_back
        filesystem_rpi -> rsnap_rpi
        btsync_rpi -> dev_back

        // service backups
        github -> data_back [style=dashed]
        librefm -> lastexport -> data_back [style=dashed]
        facebook -> thinkup
        twitter -> thinkup
        foursquare -> thinkup
        html_back -> rsync_ovh
        db_back -> rsync_ovh
        btsync_rpi -> data_back [style=dashed]

        // mail - sms
        sms -> gmail
        gmail -> offlineimap [dir=both]
        ai -> offlineimap [dir=both]
        riseup -> offlineimap [dir=both]
        offlineimap -> mail_hd1
        gmail -> mbsync [dir=both]
        ai -> mbsync [dir=both]
        riseup -> mbsync [dir=both]
        mbsync -> mail_back
        
        // immagini
        immagini_hd1 -> btsync_edgar
        immagini_back -> owncloud
        btsync_rpi -> immagini_back

        // video
        video_hd1 -> btsync_edgar 
        video_back -> owncloud
        btsync_rpi -> video_back

        // musica
        musica_hd1 -> btsync_edgar [style=dashed]
        musica_back -> owncloud
        btsync_rpi -> musica_back [style=dashed]

        // libri
        books_hd1 -> btsync_edgar 
        books_back -> owncloud
        btsync_rpi -> books_back
    }

   [1]: http://dl.dropbox.com/u/369614/blog/img_red/backup.png
