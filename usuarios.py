#-*- coding: utf-8 -*-
from bd import Database
import funciones
import os
import sys

class Usuario():
    conexion = Database().conectar()
    cursor = conexion.cursor()
    
    def crear_registro(self):
        self.conexion.ping(reconnect=True)
        if self.conexion.open:
            while True:
                try:
                    datos = funciones.pedir_datos() 
                    listado = self.listar_usuarios()
                    self.conexion.ping(reconnect=True)
                    if listado != False:
                        if funciones.buscar_email(listado,datos):
                            print('Lo siento, no se pudo crear el registro ya que hay un email existente en la base.\n')
                            break
                        else:
                            sql = 'INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)'
                            self.cursor.execute(sql,(datos['nombre'], datos['apellido'],datos['email'],datos['password']))
                            self.conexion.commit()
                            print('\nRegistrado correctamente!!! \n')
                            break
                    else:
                        sql = 'INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)'
                        self.cursor.execute(sql,(datos['nombre'], datos['apellido'],datos['email'],datos['password']))
                        self.conexion.commit()
                        print('\nRegistrado correctamente el nuevo usuario!!! \n')
                        break
                except Exception as e:
                    print('Error: {0}'.format(e))
                finally:
                    self.conexion.close()                 
        else:
            print('Al parecer hay  problemas de conexion...')
    
    def listar_usuarios(self):
        self.conexion.ping(reconnect=True)
        if self.conexion.open:
            try:
                self.cursor.execute('SELECT * FROM usuarios ORDER BY id ASC')
                resultados = self.cursor.fetchall() 
                if len(resultados) >= 1:
                    funciones.mostrar_usuarios(resultados)
                    return resultados
                else:
                    print('No hay usuarios anteriores registrados en el sistema para mostrar.\n')
                    return False
            except Exception as e:
                print('Error use: {0}'.format(e))
            finally:
                self.conexion.close()
        else:
            print('Al parecer hay  problemas de conexion...')
    
    def eliminar_usuario(self):
        self.conexion.ping(reconnect=True)
        if self.conexion.open:
            try:
                listado = self.listar_usuarios()
                self.conexion.ping(reconnect=True)
                if listado != False:
                    ids = funciones.get_numero('Ingrese ID del usuario a eliminar: ')
                    if funciones.buscar_usuario(listado,ids):
                        self.cursor.execute('DELETE FROM usuarios WHERE id = {0}'.format(ids))
                        self.conexion.commit()
                        print('Usuarios eliminado correctamente!\n')
                    else:
                        print('Lo siento, no hay usuarios con ese id, volviendo al menu principal...\n')
            except Exception as e:
                print('Error:{0}'.format(e))
            finally:
                self.conexion.close()
        else:
            print('Al parecer hay  problemas de conexion...')
        
    def actualizar_usuario(self):
        self.conexion.ping(reconnect=True)
        if self.conexion.open:
            try:
                listado = self.listar_usuarios()
                self.conexion.ping(reconnect=True)
                if listado != False:
                    ids = funciones.get_numero('Ingrese ID del usuario a actualizar: ')
                    if  funciones.buscar_usuario(listado,ids):
                        while True:
                            menu = funciones.menu_modificaciones()
                            opciones = funciones.switch(menu)
                            if 'nombre' in opciones:
                                self.cursor.execute('UPDATE usuarios SET nombre = "{0}" WHERE id = {1}'.format(opciones['nombre'],ids))
                                self.conexion.commit()
                                print('Usuario actualizado!!\n')
                            elif 'apellido' in opciones:
                                self.cursor.execute('UPDATE usuarios SET apellido = "{}" WHERE id = {}'.format(opciones['apellido'],ids))
                                self.conexion.commit()
                                print('Usuario actualizado!!\n')
                            elif 'email' in opciones:
                                if funciones.buscar_email(listado,opciones):
                                    print('Lo siento, no se puede agregar el email ya que se encuentra registrado en base.\n')
                                else:
                                    self.cursor.execute('UPDATE usuarios SET email = "{}" WHERE id = {}'.format(opciones['email'],ids))
                                    self.conexion.commit()
                            elif opciones.values() == None:
                                continue
                            elif 'false' in opciones:
                                print('Volviendo al menu principal...')
                                break
                    else:
                        print('Lo siento, no se encontro un usuario con ese id')   
            except Exception as e:
                print('Error:{0}'.format(e))
            finally:
                self.conexion.close()
        else:
            print('Al parecer hay  problemas de conexion...')