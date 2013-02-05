gacli
=====

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


Install
=======

Simple
------

1. Ensure you are using `FileVault 2`_ on Mac OS X Lion or later
2. Install ``gacli`` python module:

::

   sudo pip install https://github.com/ClockworkNet/gacli/archive/master.zip#egg=gacli

VirtualEnv and User Bin
-----------------------

The following instructions assume your shell adds ``~/bin`` to your path and that you have virtualenv_ and virtualenvwrapper_ installed.

1. Ensure you are using `FileVault 2`_ on Mac OS X Lion or later
2. Create gacli virtualenv and install ``gacli`` python module:

::

    mkvirtualenv -i https://github.com/ClockworkNet/gacli/archive/master.zip#egg=gacli gacli

3. Symlink ``ga`` to home bin:

::

    ln -s $(which ga) ~/bin/

.. _`FileVault 2`: http://support.apple.com/kb/HT4790
.. _virtualenv: http://www.virtualenv.org/
.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/


Configuration
=============

The ``ga`` script excepts your secret key (the first line in
``.google_authenticator``) to be located in ``~/.ga``.


Related
=======

* mac-ssh-confirm_: Protect against SSH Agent Hijacking on Mac OS X with the
  ability to confirm agent identities prior to each use

.. _mac-ssh-confirm: https://github.com/TimZehta/mac-ssh-confirm


Dependencies
============

- onetimepass_

.. _onetimepass: https://github.com/tadeck/onetimepass


License
=======

gacli is licensed under the `BSD 2-Clause License <http://www.opensource.org/licenses/BSD-2-Clause>`_: ::

    Copyright (c) 2013, Clockwork Active Media Systems
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    - Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    - Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.
