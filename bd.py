#-*- coding: utf-8 -*-
import pymysql

class Database():
    conexion = None
    def conectar(self):
        try:
            self.conexion = pymysql.connect(host='ca8.toservers.com',
                            user='gabrielh',
                            password='gabi42020715',
                            database='gabrielh_abm',
                            cursorclass=pymysql.cursors.DictCursor)
            
            return self.conexion 
        except Exception as e:
            print('Lo siento, hubo un error en la conexion:{0}'.format(e))
            

    
    