Rusti.cc
========

Just a rustic boy.

Hello, this is Francesco de Virgilio's blog, originally forked from Fernando 
Paolo's `website`_ (in the abandoned ``old_hyde`` branch), and subsequently 
moved to `Pelican`_ I've added some enhancements to the theme created by 
`andrewseidl`_:

* featured articles in post list support (``andrewseidl-theme/templates/index.html``); 
  it reads ``featured: yes`` in metadata
* "last updated" added in articles headings (``andrewseidl-theme/templates/article.html``); 
  it reads ``Modified`` in metadata
* switched code CSS to the excellent `Solarized`_
* comments are hidden by default and can be toggled; comments count for each 
  post are fetched using Disqus APIs and showed next to the "Comments" menu; 
  if comments count is 0, "Comments" menu is greyed out (new variable 
  ``DISQUS_PUBLICKEY`` in ``pelicanconf.py`` needed);
* a Jinja2 template working with `g.raphael library`_) to quickly insert graphs

All the code is released under GNU GPL v3 licence, see LICENSE; all the 
javascript libraries are released in full respect of theire own licences.

Feel free to fork and enhance this work under the therms of GPL.

.. _website: https://github.com/fspaolo/fspaolo.github.com
.. _Pelican: http://github.com/getpelican/pelican
.. _andrewseidl: https://github.com/andrewseidl
.. _Solarized: https://github.com/altercation/solarized
.. _g.raphael library: http://g.raphaeljs.com
