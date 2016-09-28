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
    """
    Genera el json string que se retorna al cliente
    """
    return json.dumps(data, ensure_ascii=False, encoding="utf-8", default=json_serial)


def cross_domains(fn):
    """
    Decorator que habilita el cross domain para los request
    """
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


@route('/<:re:.*>', method='OPTIONS')
def enableCORSGenericRoute():
    print 'Generic regex route'

@route('/agenda', method='POST')
@cross_domains
def crear():
    #try:
        data = json.load(request.body)
        response.content_type="application/json"
        result = ctrl.crear(data);
        return json_dumps(result)
    #except Exception :
    #    return abort(500);
    
@route('/agenda', method='GET')
@cross_domains
def listar():
    try:
        lista = ctrl.listar(request.query)
        response.content_type="application/json"
        return json_dumps(lista)
    except Exception :
        return abort(500);

@route('/agenda/<id>', method='GET')
@cross_domains
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
@cross_domains
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
@cross_domains
def eliminar(id):
    #try:
        response.content_type="application/json"
        ctrl.eliminar(id);
    #except Exception :
    #    return abort(500);

@app.route('/404')
@cross_domains
def error():
    return abort(404)
