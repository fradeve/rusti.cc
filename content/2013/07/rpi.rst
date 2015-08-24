RaspberryPi, my tips
====================

:date: 2013-07-17 16:00:00
:featured: yes
:lang: en
:modified: 2013-07-23
:tags: raspberrypi, cloud

This is nothing more than few quick notes about setting up Raspberry Pi
as a personal cloud server with sync functions. It will be updated as my
setup will change. I'm sharing it here in the hope it will be useful to
someone.

This guide is intented for those who have a single monitor and want to
quickly configure the RPi to be an headless device over wifi network.
This guide is not complete nor exaustive: see it more as a collection of
notes.

Flash Raspbian
--------------

#Download Raspbian zip, extract it. Using Disk utility erase an SD card.
Flash the ``img`` file using

.. code::

   dd bs=1M if=archlinux-hf-2013-02-11.img of=/dev/sdc

Configure boot from USB
-----------------------

Flash an USB stick with the same raspbian as above, changing from
``sdc`` to ``sdd`` (probably). Mount the ``boot`` partition of the SD
card and substitute the following contents with the file ``cmdline.txt``
in it:

.. code::

   dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/sda2 rootfstype=ext4 rootwait text

Where ``/dev/sda2`` is device pointer of the USB stick on RPi (if it not
works, try changing to ``/dev/sda1``.

Configure clock values
----------------------

To avoid FS corruption issues, add a ``config.txt`` file with the
following contents in the same dir of the SD card containing the file
above (``cmdline.txt``)

.. code::

   core_freq 240
   arm_freq 650
   sdram_freq 350
   over_voltage=2

This will underclock RPi to assure stability. Values taken from `this thread`_.

.. _this thread: http://raspberrypi.stackexchange.com/questions/2069/filesystem-corruption-on-the-sd-card

Boot, configure base system
---------------------------

Put in the USB stick and the SD card, power on RPi. Raspbian will boot
in a configuration tool. It is strongly recommended to use the tool to
expand the FS to fill the space on the device containing the OS.

Configure SSH to start automatically.

Boot in X and use the graphical interface.

Configure wicd-curses
---------------------

When on the Raspbian desktop, start the wifi tool and connect to a wifi
net. Issue the followin commands:

.. code::

   sudo apt-get update
   sudo apt-get install wicd-curses

   wicd-curses

Now, configure the current wifi net to autoconnect on boot, assigning a
static IP.

Configure wired static IP
-------------------------

Configure RPi to boot directly in TTY:

.. code::

   sudo raspi-config
   Start X-server after boot? -> no

Halt the RPi

.. code::

   sudo halt

Detach it from monitor, attach it to a wired router and connect to it
using ssh

.. code::

   ssh rpi@192.168.1.100

assuming that IP as the one assigned by default from the router. Using
wicd-curses a wired static IP can be configured. We'll assume it as
``192.168.1.124``.

Put RPi over the internet
-------------------------

Change default user password:

.. code::

   passwd

Change default SSH port in ``/etc/ssh/sshd_config`` (``Port 6724``).

Sign in at www.no-ip.com, install the client and start it. The guide is
`here`_.

Autostart No-ip on every boot

.. code::

   sudo vim /etc/rc.local
   /usr/local/bin/noip2

Start service

.. code::

   sudo /usr/local/bin/noip2

Open router administration interface, in NAT -> Virtual Servers, forward
ports as follows:

.. code::

   # Rule  # Service   # Protocol  # Starting port     # Final port    # Local IP
   1       Rpi SSH     All         6724                6724            192.168.1.124
   2       Rpi WWW     All         80                  80              192.168.1.124

Clean the image
---------------

.. code::

   sudo apt-get remove midori python3 python3-minimal omxplayer gcc-4.4-base:armhf gcc-4.5-base:armhf gcc-4.6-base:armhf fonts-freefont-ttf
   sudo apt-get autoremove

Backup the image
----------------

.. code::

   sudo dd if=/dev/sdd2 of=/home/user/raspbian-fradeve-20130518.img bs=1M

Install encrypted partition
---------------------------

-  Using GParted, create a separate storage partition. We'll use

   .. code::

      /           /dev/sda2
      rpidata     /dev/sda3

-  Connect to RPi, boot. Create encrypted partition:

   .. code::

      cryptsetup -y -v luksFormat /dev/sda3
      cryptsetup luksOpen /dev/sda3 rpidata

-  Format newly created encrypted partition

   .. code::

      sudo dd if=/dev/zero of=/dev/mapper/rpidata
      sudo mkfs.ext4 /dev/mapper/rpidata

-  Mount it

   .. code::

      mkdir /home/user/crypt
      sudo mount /dev/mapper/rpidata /home/user/crypt

To unmount

.. code::

   sudo umount /home/user/crypt
   sudo cryptsetup luksClose rpidata

To mount after boot

.. code::

   cryptsetup luksOpen /dev/sda3 rpidata
   sudo mount /dev/mapper/rpidata /home/user/crypt

To save LUKS headers (disaster recovery)

.. code::

   cryptsetup luksHeaderBackup --header-backup-file luks_headers /dev/sda3

Configure Bit Torrent Sync
--------------------------

- add repos, update and install ``btsync``
- create config file; ``user`` and ``group`` BTSync will use are
  written directly in the filename

  .. code::

     cp /etc/btsync/samples/simple.conf /etc/btsync/config.pi.www-data.conf


  .. code-block:: json

       {
           "device_name": "rpi",
           "listening_port" : 0,
           "storage_path" : "/home/pi/crypt/.btsync",
           "check_for_updates" : false, 
           "use_upnp" : false,
           "webui" :
           {
                   "listen" : "0.0.0.0:8888",
                   "login" : "user",
                   "password" : "passw"
           }
       }

- start BTSync service

  .. code::

       sudo service btsync start

Configure ownCloud storage with BTSync
--------------------------------------

Remember that ownCloud sets

-  *folder* permissions to ``u=rwx,g=rx,o=rx``
-  *files* permissions to ``u=rw,g=r,o=r``

That said,

- set ``datadirectory`` as ``/home/pi/crypt/owncloud`` in
  ``/var/www/owncloud/config/config.php``
- change owner to ``.btsync`` folder

  .. code::

     sudo chown -R www-data:www-data /home/pi/crypt/.btsync

-  change owner and permissions to ownCloud data dir

  .. code::

     sudo chown -R www-data:www-data /home/pi/crypt/owncloud/fradeve/files/*
     sudo chmod -R u=rwx,g=rx,o=rx /home/pi/crypt/owncloud/fradeve/files/*

Configure Rsnaphost backup compatible with ownCloud + BTSync
------------------------------------------------------------

Since ``owncloud/user/files`` needs permissions ``u=rwx,g=rx``, to
Rsnapshot to this dir we have two ways:

0. run Rsnaphost as ``www-data``, but this way ssh will fail
1. run Rsnapshot as ``pi`` in another dir (e.g. ``crypt/backup``) and
   later chmod and move files to ``owncloud/user/files``

   .. code::

      vim /home/pi/.bin/post_backup.sh

      ---
      #!/bin/bash

      TEMPDIR=$HOME/crypt/rsnap_temp/daily.0
      DEST=$HOME/crypt/owncloud/fradeve/files/dev

      # change folders ownership
      sudo chown -R www-data:www-data $HOME/crypt/rsnap_temp/daily.0

      # change permissions on folders, apply some compatible with ownCloud
      sudo find $HOME/crypt/rsnap_temp/daily.0 -type f -exec sudo chmod u=rwx,g=rx,o=rx {} \;

      # change permissions on files, apply some compatible with ownCloud
      sudo find $HOME/crypt/rsnap_temp/daily.0 -type d -exec sudo chmod u=rwx,g=rx,o=rx {} \;

      for D in $TEMPDIR/*; do
          if [ -d "${D}" ]; then
              sudo rm -r $DEST/${D##*/}                       # remove old dir in dest
              sudo mv $TEMPDIR/${D##*/} $DEST/${D##*/}        # move new dir to dest
          fi
      done

      # delete rsnapshot root
      sudo rm -r $TEMPDIR 
      ---

      chmod +x .bin/movetoowncloud.sh

Install Ajenti
--------------

Add the Debian repo as from instructions on the site.

.. code::

   sudo apt-get install python-pip python-dev libevent-dev
   sudo pip install -U gevent
   sudo pip install greenlet==dev
   sudo service ajenti restart

Install Mozilla Weave
---------------------

.. code::

   cd /var/www
   sudo git clone https://github.com/balu-/FSyncMS.git
   sudo mv FSyncMS weave
   sudo chown -R www-data:www-data

With browser, connect to

::

   http://yourserver.org/weave/setup.php

Select Sqlite.

.. code::

   sudo mv /var/www/weave/setup.php /home/pi/setup.php.old

Connect to ``http://yourserver.org/weave/index.php/``, if the following
message will show up, everything works as expected.

::

    "Invalid request, this was not a firefox sync request!"

Setup FF Sync from Firefox using the following custom server address

::

    http://yourserver.org/weave/index.php/

After configuring, if the window freezes or nothing happens, simply
wait. URL validation process on a custom server could take up to 10
minutes. When the ``Next`` button will be available (after several
minutes) click it.

.. code::

   rm /home/pi/setup.php.old

WARNING: from personal experience, changing machine name from Firefox
Sync settings simply breaks the whole sync system. Once things work,
leave them as they are.

Install Deluge
--------------

Installation
~~~~~~~~~~~~

.. code::

   mkdir /home/pi/crypt/deluge
   mkdir /home/pi/crypt/deluge/complete
   mkdir /home/pi/crypt/deluge/incomplete

   sudo apt-get install deluged deluge-console

Start Deluge for the 1st time and kill it

.. code::

   deluged
   sudo pkill deluged
   cp ~/.config/deluge/auth ~/.config/deluge/auth.old
   vim ~/.config/deluge/auth

   ---
   user:pw:level
   ---

E.g. ``pi:testpassw:10``. Next, start Deluge console and enable remote
connections to daemon:

.. code::

   deluged
   deluge-console

   config -s allow_remote True
   config allow_remote
   exit


.. code::

   sudo pkill deluged
   deluged

Web interface:
~~~~~~~~~~~~~~

.. code::

   sudo apt-get install deluged python-mako deluge-web
   deluge-web

Remember to:

-  open port 8112 on iptables ``sudo iptables -A INPUT -p tcp -m tcp --dport 8112 -j ACCEPT``
-  forward port 8112 to local ip on router

Connect to ``serverip:8112`` and access with defined credentials.

Autostart at boot
~~~~~~~~~~~~~~~~~

.. code::

   sudo vim /etc/rc.local

   ---
   [some other code]

   su pi -c deluged
   su pi -c deluge-web

   exit 0
   ---

.. _here: http://www.lucavallongo.com/blog/2012/11/raspberrypi-configurazione-no-ip
