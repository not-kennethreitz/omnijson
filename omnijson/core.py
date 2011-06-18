# -*- coding: utf-8 -*-

engine = None
_engine = None

# ordered dict ?

from .packages import simplejson

engine_map = {



}



def loads(s):
    """Loads JSON object."""
    try:
        return simplejson.loads(s)
    except (ValueError,), why:
        raise JSONError(why)



def dumps(o):
    """Dumps JSON object."""
    try:
        return simplejson.dumps(o)
    except (ValueError,), why:
        raise JSONError(why)



class JSONError(ValueError):
    """JSON Failed."""
