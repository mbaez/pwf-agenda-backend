#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
# Change working directory so relative paths (and template lookup) work again
#sys.path.append(os.chdir(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(__file__))
import bottle
from ws import *

application = bottle.default_app()
