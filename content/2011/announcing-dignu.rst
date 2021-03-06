Announcing diGNU
================

:date: 2011-06-16 19:50:00
:lang: en
:tags: webgis, server, archaeology, oia
:headline: A new open source software for archaeologists is coming

As posted on archeos@lists.linux.it and open-archaeology@lists.okfn.org:

Hi all, This appears to be, more or less, a quick presentation of the
startup and of our main project, so if you know a better way to spend
your time today, simply ignore this.

Who runs what?
--------------

OIA (Open Ideas for Archaeology) has been started in the past months
after a funding we received from the Apulia Region government ("Principi
Attivi 2010"), focused on innovative ideas from new young entrepreneurs.
We are a team of 4 archaeologists with different backgrounds
(osteoarchaeology, ceramics, survey, etc) and a conservation scientist
(hey, that's me) interested in open source GIS, FLOSS and GNU/Linux
applied in the archaeological field.

What's the mission?
-------------------

Create and offer open source tools to archaeologists through the web, to
easily manage on-field and post-processing works and elaborations.

Be more specific, please!
-------------------------

Our main project is called *diGNU*, GNU licensed, GeoDjango
spatially-enabled server-side archaeological management tool, to easily
access, organize, modify and communicate archaeological data during and
after the excavation. Follows a quick list of the main features; diGNU
will:

- organize and query all geographic and survey data using PostGIS
- offer a (hope for) rocking integration with an open source GIS system
  GUI locally installed (QGIS?), accessible from remote server
- export all catalogue data using LaTeX, with specific templating
  support and a near real-time map rendering integration for small
  areas
- support the archiving of single objects 3D meshes in the database,
  and integrate them in the LaTeX generated printed version of
  catalogue data
- integrate an easy install process using the Ubuntu/Debian package
  system (apt, PPA)
- export cartographic data using Mapnik, in various formats (PDF, SVG,
  JPG/PNG) and customization possibilities
- automate matrix creation using GraphViz

Other features we will likely introduce:

- full support for osteoarchaeology and paleopathology data,
  comprehensive of detailed data sheets exportation, using LaTeX
- support real-time collaboration between field and office connecting
  databases with mobile GIS (gvSIG mobile?)
- a full-featured quantitative archaeology analysis system, based on a
  KISS web interface to R and using PostGIS data
- here we are: a plugin system to easily add features to the whole
  product

Where we are now?
-----------------

At the starting point. I'm writing the django basis on which diGNU will
run. Yeah, it sounds like a glue-project taking the best of open source
tools and offering them to archaeologists on a silver plate, like the
"Wordpress" for archaeologists.

Do you have any deadline?
-------------------------

The main features must be completed and rocking in 16 months starting
from today.

OK,show us the code...
----------------------

We will bring out the first public release in December, hopefully.

Why are you writing here?
-------------------------

Because diGNU is a gift to the entire FLOSS-powered archaeological
community, and we need your help to define some concepts, starting, for
example, from the database model. We need your experience, needs and
requests to create a product modelled on the user base, on the concrete
needs and on the dreams of every archeo-geek.

I've already read some discussions on the database model, starting from
iadb `iadb`_. We need to know your approach,
assuming that nearly we don't have any standard, today.

OK, give us contacts
--------------------

At now, we don't have a website, will be up in some weeks, but we're
already working on django, database and PostGIS issues. If you're
interested in the project or have any suggestion, please append it to
the discussions that will take place in this ML, or simply mail me at
`francesco.devirgilio@inventati.org`.

Cheers

.. _iadb: http://www.iadb.org.uk
