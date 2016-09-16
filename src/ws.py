#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Define la capa de servicios de la aplicación

@autor Maximiliano Báez
@contact maxibaezpy@gmail.com
"""
from bottle import Bottle, route, request, abort, response
from datetime import datetime
from controller import *
from app_config import *
import json
# se configura instancia la aplicación
app = Bottle()
ctrl =  AgendaController(App.config);

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")

def json_dumps (data):
    return json.dumps(data, ensure_ascii=False, encoding="utf-8", default=json_serial)
    
@route('/agenda', method='POST')
def crear():
    try:
        data = json.load(request.body)
        response.content_type="application/json"
        result = ctrl.crear(data);
        return json_dumps(result)
    except Exception :
        return abort(500);

@route('/agenda', method='GET')
def listar():
    try:
        lista = ctrl.listar(request.query)
        response.content_type="application/json"
        return json_dumps(lista)
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
    return json_dumps(data)


@route('/agenda/<id>', method='PUT')
def actualizar(id):
    try:
        response.content_type="application/json"
        data = json.load(request.body)
        data["id"] = id
        udp = ctrl.actualizar(data);
        return json_dumps(udp)
    except Exception :
        return abort(500);

@route('/agenda/<id>', method='DELETE')
def eliminar(id):
    #try:
        response.content_type="application/json"
        ctrl.eliminar(id);
    #except Exception :
    #    return abort(500);

@app.route('/404')
def error():
    return abort(404)
