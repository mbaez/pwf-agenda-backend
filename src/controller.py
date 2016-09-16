#! /usr/bin/env python
# -*- coding: utf-8 -*-
from dao import *
class AgendaController (object):
    """
    Capa encargada de abstraer la lógica de negocios para la capa de servicios.

    @autor Maximiliano Báez
    @contact maxibaezpy@gmail.com
    """
    @property
    def dao(self):
        """
        Referencia al DAO
        """
        return self.__dao
    
    def __init__(self, config):
        """
        Constructor de la clase, se encarga de inicializar el controller
        """
        self.__dao = AgendaDao(config)

    def crear(self, args):
        """
        Encargada de crear un nuevo recurso, realizando un insert en la
        BD con los datos.
        """
        result = self.dao.insert(args);
        return self.obtener(result.get("id"));

    def listar(self, query):
        """
        Obtiene la lista de los recursos.
        """
        args ={}
        args['inicio'] =  query.get('inicio',0);
        args['cantidad'] =  query.get('cantidad', 20)
        args['filtro'] = query.get('filtro', '');
        args['filtro'] =  '%'+ str(args['filtro'])+ '%';
        print args;
        result =  self.dao.count(args);
        result['lista'] = self.dao.fetch(args);
        return result;

    def obtener(self, id):
        """
        Obtiene un recurso por su id
        """
        return self.dao.get(id);

    def eliminar(self, id):
        """
        Se encarga de eliminar un recurso por su id
        """
        return self.dao.delete(id);

    def actualizar(self, args):
        """
        Actualiza los datos de un recurso
        """
        self.dao.update(args);
        return self.obtener(args.get("id"));
