# -*- coding: utf-8 -*-

engine  = None
_engine = None

options = [
    ['ujson', 'loads', 'dumps', ValueError],
    ['yajl', 'loads', 'dumps', (TypeError, ValueError)],
    ['jsonlib2', 'read', 'write', ValueError],
    ['jsonlib', 'read', 'write', ValueError],
    ['simplejson',\/// 'loads', 'dumps', (TypeError, ValueError)],
    ['json', 'loads', 'dumps', (TypeError, ValueError)],
    ['simplejson_from_packages', 'loads', 'dumps', ValueError],
]

def _import(engine):
    try:
        if '_from_' in engine:
            engine, package = engine.split('_from_')
            m = __import__(package, globals(), locals(), [engine], -1)
            return getattr(m, engine)

        return __import__(engine)

    except ImportError:
        return False


def loads(s):
    """Loads JSON object."""

    try:
        try:
            return _engine[0](s, **kwargs)
        except TypeError:
            return _engine[0](s)

    except _engine[2] as why:
        raise JSONError(why)



def dumps(o, **kwargs):
    """Dumps JSON object."""

    try:
        try:
            return _engine[1](o, **kwargs)
        except TypeError:
            return _engine[1](o)

    except _engine[2] as why:
        raise JSONError(why)



class JSONError(ValueError):
    """JSON Failed."""


for e in options:

    __engine = _import(e[0])

    if __engine:
        engine, _engine = e[0], e[1:4]

        for i in (0, 1):
            _engine[i] = getattr(__engine, _engine[i])

        break
