Title: Project management in fradeve's setup Date: 2013-10-07 02:29:00
Status: draft tags: fabric, python

Automated setup
---------------

::

    cd
    fab setup:newproject

    cd ~/git/newproject
    vagrant init [name in vagrantfile]

    fab load:newproject

Manual setup
------------

GIT clone the project
~~~~~~~~~~~~~~~~~~~~~

::

    cd /home/fradeve/git
    git clone http://repo.git

Vagrantize the project
~~~~~~~~~~~~~~~~~~~~~~

Assuming a Vagrant box has been previously added (e.g. named ``myvps``),
let's init a new WM for the project

::

    cd /home/fradeve/git/newproject
    vagrant init oiavps

define WM settings

::

    vim Vagrantfile

    config.vm.box = "oiavps"
    config.vm.network :forwarded_port, guest: 80, host: 4567
    config.ssh.username = "vagrant"
    config.vm.synced_folder "/home/host/git/newproject", "/home/oia/public_html/newproject", :owner => "oia", :group => "www-data"
    config.vm.synced_folder "/home/host/.dotfiles", "/home/vagrant/.dotfiles"

Tmuxize your WM
~~~~~~~~~~~~~~~

::

    cp .tmuxifier/template.window.sh .tmuxifier/newproject.window.sh
    vim .tmuxifier/newproject.window.sh    

Define a BASH alias for tmuxified project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    vim .bash_profile
    alias muxnewproject='tmux rename-window newproject && tmuxifier load-window newproject'

Define WM dotfiles
~~~~~~~~~~~~~~~~~~

::

    vagrant ssh

Symlink files as in ``.dotfiles/vagrant/README.md``

::

    cp .tmuxifier/template.window.sh .tmuxifier/newprojectlog.window.sh

    vim .bash_aliases
    alias logproject='tmuxifier load-window newprojectlog.windows.sh'

Celebrate
~~~~~~~~~

::

    muxnewproject

