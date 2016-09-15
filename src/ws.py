#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Define la capa de servicios de la aplicación

@autor Maximiliano Báez
@contact maxibaezpy@gmail.com
"""
from bottle import Bottle, route, request, abort, response
from controller import *
from app_config import *
import json
# se configura instancia la aplicación
app = Bottle()
ctrl =  AgendaController(App.config);

@route('/agenda', method='POST')
def crear():
    try:
        response.content_type="application/json"
        data = json.load(request.body)
        return ctrl.crear(data);
    except Exception :
        return abort(500);

@route('/agenda', method='GET')
def listar():
    try:
        lista = ctrl.listar(request.query)
        response.content_type="application/json"
        return json.dumps(lista);
    except Exception :
        return abort(500);

@route('/agenda/<id>', method='GET')
def obtener(id):
    
    try:
        data = ctrl.obtener(id);
        response.content_type="application/json"
    except Exception :
            return abort(500);
    if data is None:
        return abort(404);
    
    return  json.dumps(data)

@route('/agenda/<id>', method='PUT')
def actualizar(id):
    try:
        response.content_type="application/json"
        data = json.load(request.body)
        udp = ctrl.actualizar(data);
        return json.dumps.data();
    except Exception :
        return abort(500);

    

@route('/agenda/<id>', method='DELETE')
def actualizar(id):
    try:
        response.content_type="application/json"
        ctrl.eliminar(id);
    except Exception :
        return abort(500);

@app.route('/404')
def error():
    return abort(404)
