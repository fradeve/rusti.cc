Moving contacts from Owncloud to Baikal
=======================================

:date: 2016-08-24 16:00:00
:featured: no
:lang: en
:tags: vcf, owncloud, baikal
:headline: How to move contacts from Ownclod to Baikal

Recently I got rid of my personal Owncloud instance. When I installed it, I was
simply searching for a tool to handle my contacts privately, coming from GMail.
After more than 1 year, that was the only feature I was using in Owncloud, and
there is no point in having such a complicated setup when the same result can be
achieved with a much smaller service.

I then installed Baikal_ in a `Docker container`_ and pointed it to a MySQL
database on my dedicated database machine.

Migrating the contacts has been the hardest task so far. In order:

#.  export contacts from Owncloud as a `.vcf` file using the provided button
#.  download and compile vcf2csv_ (instructions are in the readme)
#.  run the script:

    .. code-block:: bash

        ./vcf2csv -i Contacts.vcf > contacts.csv|code

#.  install Thunderbird, Lightning_, `SOGO connector`_
#.  set up a new remote addressbook connected to the Baikal instance
#.  import the contacts' CSV in a new local addressbook in Lightning; the tool
    to match Lightning contacts fields with the fields in the CSV is very
    limited; I have found much easier to reorder the columns of my CSV to
    reflect the order of the fields in the importer: this will avoid you to play
    with the buttons to sort the fields in the importer which are not very
    usable
#.  once you are happy with the imported data, just select all the entries in
    the the local addressbook and cut / paste them over into the remote
    addressbook: SOGO will syncrhonize all of them to the Baikal server

.. _Baikal: http://baikal-server.com
.. _Docker container: https://github.com/fradeve/docker-baikal
.. _vcf2csv: http://vcf2csv.sourceforge.net
.. _Lightning: https://addons.mozilla.org/en-US/thunderbird/addon/lightning
.. _SOGO connector: https://sogo.nu
