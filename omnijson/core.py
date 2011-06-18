# -*- coding: utf-8 -*-

from .packages import simplejson as internal_json

engine = None
_engine = None


# ordered dict ?

# from .packages import simplejson

def _import(engine, from_mod=False):
    try:
        if from_mod:
            # from from_mod import engine
            __import__(engine)
        else:
            __import__(engine)

        eval('return simplejson')
    except ImportError:
        return False


# print _import('simplejson')
# from .packages import simplejson


def loads(s):
    """Loads JSON object."""
    try:
        return internal_json.loads(s)
    except (ValueError,), why:
        raise JSONError(why)



def dumps(o):
    """Dumps JSON object."""
    try:
        return internal_json.dumps(o)
    except (ValueError,), why:
        raise JSONError(why)



class JSONError(ValueError):
    """JSON Failed."""
