OmniJSON
========

The Problem
-----------

::

    # Python 2.5.4 (r254:67916, Jun 24 2010, 21:47:25)
    >>> import anyjson
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        raise ImportError("No supported JSON module found")
    ImportError: No supported JSON module found


The Solution
------------

::

    >>> import omnijson as json
    # \o/


Features
--------

- Loads whichever is the fastest JSON module installed
- Falls back on built in pure-python simplejson, just in case.
- Proper API (``loads()``, ``dumps()``)
- Verndorizable
- Supports Python 2.5-3.2 out of the box


Usage
-----

Load the best JSON available::

    import omnijson as json

Dump some objects::

    >>> json.loads('{"yo": "dawg"}')
    {'yo': 'dawg'}

Load some objects::

    >>> json.dumps({'yo': 'dawg'})
    '{"yo": "dawg"}'

Check JSON Engine::

    >>> json.engine
    'ujson'

Install
-------

Installing OmniJSON is easy::

    $ pip install omnijson

Of, if you must::

    $ easy_install omnijson

But, you `really shouldn't do that
<http://www.pip-installer.org/en/latest/index.html#pip-compared-to-easy-install>`_.


License
-------

The MIT License::

    Copyright (c) 2011 Kenneth Reitz

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.