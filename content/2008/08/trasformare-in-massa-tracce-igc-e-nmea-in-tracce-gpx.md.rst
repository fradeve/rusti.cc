Title: Trasformare in massa tracce igc e nmea in tracce gpx Date:
2008-08-18 16:42:55 tags: python, openstreetmap

Questo è un post scritto da `Sdonk <http://www.sdonk.org/>`__, ospitato
qui sul mio blog :)

Durante
l'\ `openstreecamping2008 <http://blog.sdonk.org/2008/08/trasformare-in-massa-tracce-igc-e-nmea-in-tracce-gpx/>`__
abbiamo avuto la necessità di trasformare, con gpsbabel, le decine di
tracce igc, il formato di tracking che utilizza il cellulare di
`Fradeve <http://www.fradeve.org>`__, raccolte durante i giri in bici in
formato GPX che e il formato utilizzato da JOSM. Dopo qualche giorno ci
siamo resi conto che era noioso ridigitare ogni volta il comando dal
terminale (ovviamente non tutto, ma modificando semplicemente il nome
del file nel comando precedente) e potevamo perdere tempo prezioso in
questo modo?

Ovviamente no! Mentre Fradeve leggeva la biografia di Torvalds (ve la
consiglio) e il caldo era insopportabile, ho scritto un piccolo script
in python per convertire in massa file igc e nmea in file GPX. Credo sia
possibile farlo anche in Bash, ma non conoscendo il Bash ho preferito
usare il python e in particolare il modulo os, contenuto nella libreria
standard, che permette al programma di interfacciarsi con il sistema
operativo. `Clic qui per scaricare lo
script <http://www.blog.sdonk.org/wp-content/uploads/trasforma.py>`__

Qualche commento al codice:

::

    :::python
    if formato in ListaFormati:
        ListaFile = CercaFile(os.listdir('.') , formato)
        else : print "Formato inesistente o non ancora implementato, esco dal programma."
    exit()

Controlla il formato passato come argomento al programma e, se corretto
(i formati accettati sono igc e nmea), restituisce una lista, attraverso
la funzione os.listdir(cartella), con **tutti** i file contenuti nella
cartella passata come argomento.

::

    :::python
    def CercaFile(lista, flag):
    for i in lista:
        if flag in i:
            gpx.append(i)
            return gpx

La funzione CercaFile restituisce una nuova lista contenente soltanto i
file con l'estensione interessata (igc o nmea), eliminando tutti gli
altri file inutili.

::

    :::python
    if ListaFile != []:
        c = 0
        for i in ListaFile:
            stringa = "gpsbabel -i " + formato + " -f '" + i + "' -o gpx -F '" + i[0:-3] + "'gpx"
            os.system(stringa)
            c = c + 1 print "Ho trasformato " + str(c) + " file in gpx ed ho cancellato i file " + formato + ""
    else:
    print "Non ci sono file da convertire, ciao!" [/sourcecode]

Controlla che ci siano file da convertire, in caso positivo passa al
sistema, attraverso il la funzione os.system, il comando gpsbabel
necessario alla conversione dei file. La stringa che può sembrare
complicata serve a trasformare i file mantenendo il nome originale. Per
eseguire lo script basta copiare i file da trasformare nella stessa
cartella dove è presente lo script e poi da terminale digitare:

::

    :::bash
    python trasforma.py formato

dove ``formato`` deve essere sostituito con igc o con nmea a seconda del
formato di partenza dei file.

Semplice, veloce ed efficace a patto di aver gpsbabel installato,
ovviamente!
