gacli
=====

``gacli`` was created for used with google-authenticator_. Thankfully, TOTP_ is
an open standard so ``gacli`` may have additional applications.

The ``ga`` command line utility provides convenient access to TOTP verification
codes::

    usage: ga [-h] [-d] [-f FILE]

    Copy newline terminated TOTP verification code to Mac OS X clipboard.

    optional arguments:
      -h, --help            show this help message and exit
      -d, --debug           print debug information
      -f FILE, --file FILE  Secret file

    The debug option continually prints verification codes instead of copying a
    single code to the clipboard.

.. _google-authenticator: https://code.google.com/p/google-authenticator/
.. _TOTP: http://en.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm


Security
========

This application assumes you have secured your local computer disk or
filesystem encryption. ``gacli`` is only safe **with encryption**:

- `OS X: About FileVault 2`_
- `EncryptedFilesystems - Community Ubuntu Documentation`_
- `GnuPG`_
- `GPGSuite`_ (GnuPG for Mac OS X)

.. _`OS X: About FileVault 2`: https://support.apple.com/kb/ht4790
.. _`EncryptedFilesystems - Community Ubuntu Documentation`:
   https://help.ubuntu.com/community/EncryptedFilesystems
.. _`GnuPG`: http://www.gnupg.org/
.. _`GPGSuite`: https://gpgtools.org/gpgsuite.html


Install
=======

Choose *either* of the following installation methods:

1. `Simple Global`_
2. `VirtualEnv and User Bin`_ (recommended)


Simple Global
-------------

1. Please consider, again, using the `VirtualEnv and User Bin`_ method
2. Install the pip python module, if you have not already done so.

   - `Installation -- pip documentation`_

3. Install the gacli python module::

        sudo pip install gacli


VirtualEnv and User Bin
-----------------------

This installation method has the following requirements:

- Your ``PATH`` includes ``~/bin``
- virtualenv_ Python module is installed
- virtualenvwrapper_ Python module is installed

Installation:

1. Create a new gacli virtualenv and install the gacli python module::

        mkvirtualenv -i gacli gacli

2. Symlink ``ga`` to home bin::

        ln -s $(which ga) ~/bin/

.. _`Installation -- pip documentation`: http://www.pip-installer.org/en/latest/installing.html
.. _virtualenv: http://www.virtualenv.org/
.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/


Configuration
=============

1. See `Security`_
2. Copy the secret key from the first line of your ``.google_authenticator``
   and put in ``~/.ga``
3. Change permissions::

    chmod 0400 ~/.ga


GnuPG Protection
----------------

1. Encrypt secret file::

    cat ~/.ga | gpg -aes -r EMAIL > .ga.gpg

2. Delete unencrypted secret file::

    rm ~/.ga

3. Add an alias to your ``.bashrc``::

    alias gad='gpg -qd ~/.ga.gpg | ga -f -'


Related
=======

- mac-ssh-confirm_: Protect against SSH Agent Hijacking on Mac OS X with the
  ability to confirm agent identities prior to each use

.. _mac-ssh-confirm: https://github.com/TimidRobot/mac-ssh-confirm


Requirements
============

- Linux or Mac OS X

  - Linux utilizes ``xclip`` or ``xsel``.
  - Mac OS X utilizes ``pbcopy``

- onetimepass_

.. _onetimepass: https://github.com/tadeck/onetimepass


License
=======

- `LICENSE`_ (Expat License/`MIT License`_)

.. _`LICENSE`: LICENSE
.. _`MIT License`: http://www.opensource.org/licenses/MIT
