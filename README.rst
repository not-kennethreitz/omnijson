JSONs.
======

The Problem
-----------

::

    # Python 2.5.4 (r254:67916, Jun 24 2010, 21:47:25)

    >>> import anyjson
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Users/kreitz/.virtualenvs/25/lib/python2.5/site-packages/anyjson/__init__.py", line 127, in <module>
        raise ImportError("No supported JSON module found")
    ImportError: No supported JSON module found


The Solution
------------

::

    # Python 2.5.4 (r254:67916, Jun 24 2010, 21:47:25)

    >>> import jsons
    # \o/


Features
--------

- Loads whichever is the fastest JSON module installed
- Falls back on built in pure-python simplejson, just in case.
- Proper API (``loads()``, ``dumps()``)
- Verndorizable