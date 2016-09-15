#! /usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2

class BaseDao (object):
    """
    DAO base, implementa la conexión a la base de datos y los metodos CRUD base
    para las entidades.

    @autor Maximiliano Báez
    @contact maxibaezpy@gmail.com
    """
    @property
    def conn(self):
        """
        Referencia a la conexión a la base de datos
        """
        return self.__conn

    @conn.setter
    def conn(self, value):
        """
        Seter del conector de la base de datos
        """
        self.__conn = value


    def __init__(self, config):
        """
        Constructor del dao base.
        """
        self.__conn = psycopg2.connect(database=config.get("db.name"),\
                                       user=config.get("db.user"),\
                                       password=config.get("db.password"),\
                                       host=config.get("db.host"), \
                                       port=config.get("db.port"));

        self.conn.autocommit = True

    def query(self, query_string, args={}, is_many=False):
        """
        Este método se encarga de construir la consulta sql definida en
        `query_string`, establce la conexión en la base de datos y
        ejecuta la consulta.

            SELECT * FROM tabla WHERE id = :id

        @type query_string : String
        @param query_string: La referencia al cursor de la consulta.

        @type args : Dictionaries
        @param args: Un diccionario con los parametros del query.

        @type insert_many : Boolean
        @param insert_many: True para activar el executemany.

        @rtype  Cursor
        @return La referencia al cursor de la consulta.
        """

        cursor = self.conn.cursor()
        if not is_many:
            cursor.execute(query_string, args)
        else:
            cursor.executemany(query_string, args)
        return cursor

    def to_array(self, dbcursor):
        """
        Se encarga de procesar el cusor y generar un array de  diccionarios 
        con los datos obtenidos del cursor. Las columnas de los campos del 
        cursor son utilizadas como claves de diccionario.

        @type dbcursor : Cursor
        @param dbcursor : La referencia al cursor de la consulta.

        @rtype  Dictionaries
        @return Un diccionario con los datos del cursor.
        """
        return self.__to_dict(dbcursor);
    
    def to_dict(self, dbcursor):
        """
        Se encarga de procesar el cusor y generar un diccionario con los
        datos obtenidos del cursor. Las columnas de los campos del cursor
        son utilizadas como claves de diccionario.

        @type dbcursor : Cursor
        @param dbcursor : La referencia al cursor de la consulta.

        @rtype  Dictionaries
        @return Un diccionario con los datos del cursor.
        """
        d = self.to_array(dbcursor);
        if len(d) == 0:
            return None;
        return d[0];
        
    def __to_dict(self, dbcursor):
        """
        Se encarga de procesar el cusor y generar un diccionario con los
        datos obtenidos del cursor. Las columnas de los campos del cursor
        son utilizadas como claves de diccionario.

        @type dbcursor : Cursor
        @param dbcursor : La referencia al cursor de la consulta.

        @rtype  Dictionaries
        @return Un diccionario con los datos del cursor.
        """
        # se obtienen todos los datos
        results = dbcursor.fetchall()
        if len(results) < 1:
            return results

        # se genera el array de resultados a partir de cursor
        rownum = 0
        for row in results:
            dictrow = {}
            dictnum = 0
            for col in dbcursor.description:
                dictrow[col[0]] = row[dictnum]
                dictnum += 1
            results[rownum] = dictrow
            rownum += 1

        dbcursor.close()
        # se retorna la lista de resultados
        return results

    
class AgendaDao(BaseDao):
    """
    DAO Author, implementa las operaciones CRUD sobre la tabla de agenda.

    @autor Maximiliano Báez
    @contact maxibaezpy@gmail.com
    """
    def fetch(self, args):
        """
        Se encarga de obtener todos los authores de la base de datos.

        @rtype  Dictionaries
        @return Un diccionario con el resultado de la consulta
        """
        sql_string="""
        SELECT id                   AS id, 
               nombre               AS nombre, 
               apellido             AS apellido, 
               alias                AS alias, 
               telefono             AS telefono, 
               email                AS email, 
               direccion            AS direccion, 
               fecha_creacion       AS fechaCreacion, 
               fecha_modificacion   AS fechaCreacion
        FROM   PUBLIC.agenda 
        WHERE  nombre                    LIKE  %(filtro)s OR 
               apellido                  LIKE  %(filtro)s OR 
               alias                     LIKE  %(filtro)s OR 
               CAST(telefono AS VARCHAR) LIKE  %(filtro)s OR 
               email                     LIKE  %(filtro)s OR 
               direccion                 LIKE  %(filtro)s 
        ORDER BY id 
        LIMIT  %(cantidad)s 
        OFFSET %(inicio)s 
        """
        cursor = self.query(sql_string, args)
        return self.to_array(cursor)
    
    def count(self, args):
        """
        Se encarga de obtener la cantidad de registros que cumplen con los
        criterios de filtrado.
        
        @rtype  Dictionaries
        @return Un diccionario con el resultado de la consulta
        """
        sql_string="""
        SELECT COUNT(*) AS total
        FROM   PUBLIC.agenda 
        WHERE  nombre                    LIKE  %(filtro)s OR 
               apellido                  LIKE  %(filtro)s OR 
               alias                     LIKE  %(filtro)s OR 
               CAST(telefono AS VARCHAR) LIKE  %(filtro)s OR 
               email                     LIKE  %(filtro)s OR 
               direccion                 LIKE  %(filtro)s 
        """
        cursor = self.query(sql_string, args)
        return self.to_dict(cursor)
    
    def get(self, id):
        """
        Se encarga de obtener los datos de un author especifico.

        @rtype  Dictionaries
        @return Un diccionario con el resultado de la consulta
        """
        sql_string="""
        SELECT id                   AS id, 
               nombre               AS nombre, 
               apellido             AS apellido, 
               alias                AS alias, 
               telefono             AS telefono, 
               email                AS email, 
               direccion            AS direccion, 
               fecha_creacion       AS fechaCreacion, 
               fecha_modificacion   AS fechaCreacion
        FROM   PUBLIC.agenda 
        WHERE id= %(id)s
        """
        args = {"id" : id}
        cursor = self.query(sql_string, args)
        return self.to_dict(cursor)

    def insert(self, args={}):
        """
        Se encarga de persitir el author

        @type args : Dictionaries
        @param args: Un diccionario con los datos del author.

        """
        # se definie el query de la consulta.
        sql_string = """
        INSERT INTO PUBLIC.agenda  (
            nombre, 
            apellido, 
            alias, 
            telefono, 
            email, 
            direccion
        ) VALUES (
            %(nombre)s, 
            %(apellido)s, 
            %(alias)s, 
            %(telefono)s, 
            %(email)s, 
            %(direccion)s
        )
        RETURNING id
        """

        cursor = self.query(sql_string, args)
        return self.to_dict(cursor)

    def update(self, args={}):
        """
        Se encarga de actualizar los datos de un author

        @type args : Dictionaries
        @param args: Un diccionario con los datos del author.

        @rtype  Cursor
        @return Un cursor con el estado de la operación
        """
        # se definie el query de la consulta.
        sql_string = """
        UPDATE PUBLIC.agenda 
        SET    nombre=               %(nombre)s, 
               apellido=             %(apellido)s, 
               alias=                %(alias)s, 
               telefono=             %(telefono)s, 
               email=                %(email)s, 
               direccion=            %(direccions)s, 
               fecha_modificacion=   now()
        WHERE id= %(id)s
        """
        cursor = self.query(sql_string, args)
        return cursor

    def delete(self, args={}):
        """
        Se encarga de borrar un author

        @type args : Dictionaries
        @param args: Un diccionario con los datos del author.

        @rtype  Cursor
        @return Un cursor con el estado de la operación
        """
        # se definie el query de la consulta.
        sql_string = """
        DELETE FROM agenda WHERE id= %(id)s
        """
        cursor = self.query(sql_string, args)
        return cursor
