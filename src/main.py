#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Define la capa de servicios de la aplicación

@autor Maximiliano Báez
@contact maximiliano.baez@konecta.com.py
"""
from bottle import Bottle, run
from ws import *

if __name__ =="__main__" :
    run(host=App.config.get("app.host"), port=App.config.get("app.port"), debug=True)
