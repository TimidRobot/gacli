gacli
=====

``gacli`` was created for used with google-authenticator_. Thankfully, TOTP_ is
an open standard so ``gacli`` may have additional applications.

The ``ga`` command line utility provides convenient access to TOTP verification
codes: ::

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


Install
=======

Choose *either* Simple *or* VirtualEnv and User Bin installation:

Simple
------

1. Install the pip python module, if you have not already done so.

   - `Installation -- pip documentation`

2. Install the gacli python module: ::

        sudo pip install https://github.com/ClockworkNet/gacli/archive/master.zip#egg=gacli

VirtualEnv and User Bin
-----------------------

The following instructions assume your shell adds ``~/bin`` to your path and
that you have virtualenv_ and virtualenvwrapper_ installed.

1. Create a new gacli virtualenv and install the gacli python module: ::

        mkvirtualenv -i https://github.com/ClockworkNet/gacli/archive/master.zip#egg=gacli gacli

2. Symlink ``ga`` to home bin: ::

        ln -s $(which ga) ~/bin/

.. _`Installation -- pip documentation`: http://www.pip-installer.org/en/latest/installing.html
.. _virtualenv: http://www.virtualenv.org/
.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/


Configuration
=============

1. Ensure you are using disk encryption (ex. `FileVault 2`_ on Mac OS X Lion or
   later)
2. Copy the secret key from the first line of your ``.google_authenticator``
   and put in ``~/.ga``
3. ``chmod 0400 ~/.ga``

.. _`FileVault 2`: http://support.apple.com/kb/HT4790


Related
=======

* mac-ssh-confirm_: Protect against SSH Agent Hijacking on Mac OS X with the
  ability to confirm agent identities prior to each use

.. _mac-ssh-confirm: https://github.com/TimZehta/mac-ssh-confirm


Requirements
============

- Mac OS X Lion or Mountain Lion
- onetimepass_

.. _onetimepass: https://github.com/tadeck/onetimepass


License
=======

- LICENSE_ (`BSD 2-Clause License`_)

.. _LICENSE: LICENSE
.. _`BSD 2-Clause License`: http://www.opensource.org/licenses/BSD-2-Clause
