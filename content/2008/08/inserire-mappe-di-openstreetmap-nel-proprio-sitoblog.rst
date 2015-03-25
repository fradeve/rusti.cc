Inserire mappe di OpenStreetMap nel proprio sito/blog
=====================================================

:date: 2008-08-19 08:20:35
:tags: openstreetmap, webgis

Qual'è la più grande soddisfazione per un mapper se non quella di
mostrare i risultati del proprio lavoro sul sito o sul blog personale?
Spulciando il `wiki di OpenStreetMap`_ mi sono
imbattuto nella pagina `OpenLayers Simple Example`_
in cui è descritta la procedura più semplice per inserire una *slippy
map* standard in una pagina web attraverso uno script in Java. Essendo
*pythonista* convinto, di Java non capisco molto, ma il codice mi è
sembrato molto intuitivo, vediamo insieme il codice della pagina html:

.. _wiki di OpenStreetMap: http://wiki.openstreetmap.org/wiki/Main_Page
.. _OpenLayers Simple Example: http://wiki.openstreetmap.org/wiki/OpenLayers_Simple_Example

.. code-block:: html

    <html>
        <head>
            <title>Slippy map di Terlizzi</title>

            <!-- bring in the OpenLayers javascript library
            (here we bring it from the remote site, but you could
            easily serve up this javascript yourself) -->
            <script src="http://www.openlayers.org/api/OpenLayers.js"></script>

            <!-- bring in the OpenStreetMap OpenLayers layers.
            Using this hosted file will make sure we are kept up
            to date with any necessary changes -->
            <script src="http://www.openstreetmap.org/openlayers/OpenStreetMap.js"></script>

            <script type="text/javascript">
                // Start position for the map (hardcoded here for simplicity,
                // but maybe you want to get from URL params)
                var lat=41.12925
                var lon=16.5449
                var zoom=15

                var map; //complex object of type OpenLayers.Map

                //Initialise the 'map' object
                function init() {

                map = new OpenLayers.Map ("map", {
                controls:[
                new OpenLayers.Control.Navigation(),
                new OpenLayers.Control.PanZoomBar(),
                new OpenLayers.Control.Attribution()],
                maxExtent: new OpenLayers.Bounds(-20037508.34,-20037508.34,20037508.34,20037508.34),
                maxResolution: 156543.0399,
                numZoomLevels: 19,
                units: 'm',
                projection: new OpenLayers.Projection("EPSG:900913"),
                displayProjection: new OpenLayers.Projection("EPSG:4326")
                } );

                // Define the map layer
                // Note that we use a predefined layer that will be
                // kept up to date with URL changes
                // Here we define just one layer, but providing a choice
                // of several layers is also quite simple
                // Other defined layers are OpenLayers.Layer.OSM.Mapnik, OpenLayers.Layer.OSM.Maplint and OpenLayers.Layer.OSM.CycleMap
                layerTilesAtHome = new OpenLayers.Layer.OSM.Osmarender("Osmarender");
                map.addLayer(layerTilesAtHome);

                var lonLat = new OpenLayers.LonLat(lon, lat).transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());

                map.setCenter (lonLat, zoom);
                }

            </script>
        </head>

        <!-- body.onload is called once the page is loaded (call the 'init' function) -->
        <body onload="init();">
            <!-- define a DIV into which the map will appear. Make it take up the whole window -->
            <div style="width:100%; height:100%" id="map"></div>
        </body>

    </html>

Questa è una pagina html completa che integra una slippy map delle
stesse dimensioni della pagina html, nel caso vogliate personalizzare il
titolo della pagina (quello che compare nella finestra del browser)
dovete modificare ciò che e compreso nel tag

.. code-block:: html

   <title>Modificare questo testo</title>

Il passo successivo consiste nel modificare le coordinate di origine
della mappa e lo zoom di default, dal [sito][3], cliccando su
"permalink" in basso a destra dopo aver cercato la città o la regione di
interesse e lo zoom gradito e copiando il nuovo indirizzo che nel
frattempo sarà comparso nella barra del browser. Le coordinate e lo zoom
vanno inserite in questo punto del file html:

.. code-block:: html

   <script type="text/javascript">
   var lat=41.12925
   var lon=16.5449
   var zoom=15

Se intendiamo utilizzare un solo tipo di layer (vedi punto successivo)
possiamo lasciare invariata la porzione di script che inizializza gli
oggetti della mappa, in caso contrario dobbiamo aggiungere il
LayerSwitcher alla mappa per permettere agli utenti di cambiare layer al
volo, modificando il codice che inizializza i controlli da così:

.. code-block:: html

   new OpenLayers.Control.Navigation(),
   new OpenLayers.Control.PanZoomBar(),
   new OpenLayers.Control.Attribution()],

a così:

.. code-block:: html

   new OpenLayers.Control.Navigation(),
   new OpenLayers.Control.PanZoomBar(),
   new OpenLayers.Control.LayerSwitcher(),
   new OpenLayers.Control.Attribution()],

In questo script è implementato solo il layer di Osmarender (il software
di rendering open source nato in casa OpenStreetMap e utilizzato dal
progetto di rendering distribuito tiles@home):

.. code-block:: html

   layerTilesAtHome = new OpenLayers.Layer.OSM.Osmarender("Osmarender");
   map.addLayer(layerTilesAtHome);

Volendo ottenere una mappa più interattiva è possibile aggiungere anche
gli altri due layer standard usati da OpenStreetMap nelle mappe del
sito:

-  Mapnik layer (lo standard di rendering di OpenStreetMap)
-  CycleMap (la mappa con le isoipse utili ai ciclisti)

Per aggiungere gli altri due layer è necessario modificare il codice
precedente in questo modo:

.. code-block:: html

   layerTilesAtHome = new OpenLayers.Layer.OSM.Osmarender("Osmarender");
   map.addLayer(layerTilesAtHome);
   layerMapnik = new OpenLayers.Layer.OSM.Mapnik("Mapnik");
   map.addLayer(layerMapnik);
   layerCycleMap = new OpenLayers.Layer.OSM.CycleMap("CycleMap");
   map.addLayer(layerCycleMap);

Infine dobbiamo decidere soltanto le dimensioni di visualizzazione della
mappa in modo da adattarla al contesto del nostro sito o blog, per fare
ciò basta modificare le dimensioni proporzionali della mappa rispetto al
``<div>`` in cui è contenuta, in questo caso, essendo su di un file html
a parte, ho deciso di lasciare le dimensioni della mappa grandi quanto
la pagina html.

.. code-block:: html

   <div style="width:100%; height:100%" id="map"></div>

