#!/usr/bin/env python
# -*- coding: utf-8 -*-

import omnijson as json

a = json.loads('{"yo":"dawg"}')
print a

print json.dumps(a)



json.loads('{"yo": dawg"}')