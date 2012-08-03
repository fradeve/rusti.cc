Install the plugin using VAM

    :InstallAddons Tagbar

Add some customizations to `.vimrc`

    let g:tagbar_left = 1                                                                                                                                                                                                             map T :TagbarOpen<CR>

To use Tagbar at top of its possibilities, we'll need both Exuberant-ctags and DoctorJS.

    sudo apt-get install exuberant-ctags

Make sure that you're running `exuberant-ctags`:

    ctags --version
    Exuberant Ctags 5.9~svn20110310, Copyright (C) 1996-2009 Darren Hiebert

DoctorJS (aka jsctags) runs on top of node.js

    sudo apt-get install nodejs
    git clone --recursive https://github.com/mozilla/doctorjs.git
    git submodule init && git submodule update

#Due to a bug, we need to roll back DoctorJS version to older one
#
#    cd doctorjs
#    git checkout 1062dd31625cc002261f15e68af77eedd63a56f6

Now compile and install DoctorJS

    sudo make install

Start VIM and press "T" to open Tagbar for the loaded JS file.

## Tagbar error, how to solve ##

if this gives and error like:

    Error: require.paths is removed.

you need to roll back the node installed on the system to a previous version.
First, we'll remove the package manager version of nodeJS

    sudo apt-get remove --purge nodejs

Install nodeJS dependencies:

    sudo apt-get install build-essential libssl-dev python

Since we're trying to stick together more pieces of software (jsctags, Tagbar, node.js) sometimes you'll need to try different previous versions of node.js to find which of them works for you. Using a node virtual machine manager, you only need to know which version number you want to install.

    git clone git://github.com/creationix/nvm.git
    cd nvm
    . nvm.sh
    nvm install v0.5.9
    nvm use v0.5.9
    nvm alias default v0.5.9

To source `nvm.sh` in every shell and make the node installed always available, insert in `~/.bashrc`

    ## nvm settings ##
    . .vim/bundle/nvm/nvm.sh

as my nvm installation is in `~/.vim/bundle`. I think the `src` folder could be removed to free some space:

    rm -r .vim/bundle/nvm/src

Now open TagBar again in Vim to be certain that the currently installed version works fine.

## Install and use JS autocompletion ##

DoctorJS can be used to help us while writing with autocompletion. Now, we'll generate `tags` file for the current project. `cd` into project's folder and

    jsctags OpenLayers.js
    jsctags map.js

Obviously, you can use some mappings in `.vimrc` to make `jsctags` command run automatically when opening a certain project's file in Vim. Now, we'll tell `.vimrc` where to take `tags` file

    set tags=./tags,./../tags,./*/tags

and which kind of completion tips Vim must show when using autocompletion (for, more informations, see `:h 'complete'`):

    set complete=.,b,u,] 

## Install Syntastic with community-driven JShint ##

In Vim:

    :InstallAddons Syntastic

Install node package manager

    sudo apt-get install npm

Install JShint globally

    sudo npm -g install jshint

now it should have been installed at `/usr/local/lib/node_modules/jshint`.

Download in `~/.jshintrc` the default JShint community rc:

    wget https://raw.github.com/jshint/node-jshint/master/example/defaults.json
    mv default.json ~/.jshintrc
