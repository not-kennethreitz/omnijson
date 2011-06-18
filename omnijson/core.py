# -*- coding: utf-8 -*-

from .packages import simplejson as internal_json
from .packages.simplejson.ordered_dict import OrderedDict

engine = None
_engine = None

# ujson, dumps, loads

json_map = OrderedDict()
json_map['simplejson_from_packages'] = ['loads', 'dumps', ValueError]

json_map['ujson'] = ['loads', 'dumps', ValueError]
json_map['yajl'] = ['loads', 'dumps', (TypeError, ValueError)]
json_map['jsonlib2'] = ['read', 'write', ValueError]
json_map['jsonlib'] = ['read', 'write', ValueError]
json_map['simplejson'] = ['loads', 'dumps', (TypeError, ValueError)]
json_map['json'] = ['loads', 'dumps', (TypeError, ValueError)]

json_map['simplejson_from_packages'] = ['loads', 'dumps', ValueError]
# json_map['packages.simplejson'] = ['simplejson.loads', 'simplejson.dumps', ValueError]


# from .packages import simplejson

def _import(engine):
    try:
        if '_from_' in engine:
            engine, package = engine.split('_from_')
            # print package
            # print engine
            # print '\o/'
            # __import__(engine, fromlist=package)
            m = __import__(package, globals(), locals(), [engine], -1)
            return getattr(m, engine)

        return __import__(engine)

    except ImportError:
        return False



for k, v in json_map.items():
    # print k
    __engine = _import(k)
    if __engine:
        engine, _engine = k, v

        for i in (0, 1):
            # print __engine
            _engine[i] = getattr(__engine, _engine[i])

        break




def loads(s):
    """Loads JSON object."""
    try:
        return _engine[0](s)

    except  _engine[2], why:
        raise JSONError(why)



def dumps(o):
    """Dumps JSON object."""
    try:
        return _engine[1](o)
    except _engine[2], why:
        raise JSONError(why)



class JSONError(ValueError):
    """JSON Failed."""
