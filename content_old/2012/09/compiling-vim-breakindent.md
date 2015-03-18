Title: Compiling VIM with Breakindent patch
Date:  2012-09-10 10:00:00
featured: yes
lang: en
tags: vim

[VIM Breakindent patch][1]'s story is quite frustrating, since it is a nice piece of code (really useful when you work with tag-like structured coding languages, e.g. LaTeX) but it has been [never integrated in standard VIM][2] due to some instability issues. In 2012, you always have to patch and compile VIM manually to get it working. This guide has been tested on Ubuntu 12.04 (many thanks to [ephemient][5] for pointing out the correct procedure, as a result of a [discussion][6] on Stackexchange).

Get the sources:

    :::bash
	sudo apt-get sources vim

Download VIM breakindent patch file:

    :::bash
	wget

Set permissions on the sources and move the patch into the set of Debian patches:

    :::bash
	cd vim-7.3.429
	sudo chmod u=rw,g=r,o=r ../vim-breakindent.patch
	sudo cp ../vim-breakindent.patch debian/patches/debian/.

Add one new entry in `debian/changelog`, bumping version from `vim_7.3.429-2ubuntu2.1` to `vim_7.3.429-2ubuntu2.2`.

Add `debian/vim-breakindent.patch` at the end of `debian/patches/series`

Generate new source package

    :::bash
	sudo pdebuild

Compile the new `.dsc`:

    :::bash
	sudo pbuilder build vim_7.3.429-2ubuntu2.2.dsc

Install new debs:

    :::bash
	sudo dpkg -i /var/cache/pbuilder/result/*.deb

### Debian package ###
As I write, [Eudoxos][3] is maintaining a [Launchpad repository][4] with Vim breakindent-patched compiled `.deb` packages.

   [1]: https://retracile.net/wiki/VimBreakIndent
   [2]: https://groups.google.com/forum/#!msg/vim_dev/VdMLVy_ZS2I/KsRNkREcBhgJ
   [3]: http://stackoverflow.com/users/761090/eudoxos
   [4]: https://launchpad.net/~eudoxos/+archive/ppa
   [5]: http://stackoverflow.com/users/20713/ephemient
   [6]: http://stackoverflow.com/questions/10998516/compiling-vim-with-breakindent-patch