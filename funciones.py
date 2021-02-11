#-*- coding: utf-8 -*-
import re
import hashlib
import bd
import string
import os
import sys

def menu_principal():
    while True:
        try:
            print("\n\t\t    ----- Menu Principal -----\n")
            print("1) Listar usuarios")
            print("2) Registrar usuario")
            print("3) Actualizar usuario")
            print("4) Eliminar usuario")
            print("5) Salir\n")
            opcion = int(input('Ingrese una opcion correspondiente: '))

            if opcion < 1 or opcion > 5:
                os.system('clear')
                print("Opcion incorrecta, por favor ingrese una opcion del menu...")
                print("---------------------------------------------------------\n")
            else:
                break     
        except Exception as e:
            os.system('clear')
            print("Lo siento, no es un dato correcto, por favor ingrese un numero positivo.\n")
            continue
    return opcion

def menu_modificaciones():
    while True:
        try:
            print("\n\t\t      ----- Menu de modificaciones -----\n")
            print("1) Modificar nombre")
            print("2) Modificar apellido")
            print("3) Modificar email")
            print("4) Salir\n")
            opcion = int(input('Ingrese una opcion correspondiente: '))
            if opcion < 1 or opcion > 4:
                print("Opcion incorrecta, por favor ingrese una opcion del menu...")
                print("---------------------------------------------------------\n")
            else:
                break
        except Exception as e:
            print('Lo siento, no es un dato correcto, por favor ingrese un numero del menu.\n')
            continue
    return opcion 
 
def validar_string(string):
    nuevo = string.split()
    aprobed = None
    for i in nuevo:
        if i.isalpha() and i != '':
            aprobed = True
        else:
            aprobed = False
            break
    return aprobed

def get_string(text,error):
    flag = False
    while not flag:
        dato = input(text)
        if validar_string(dato):
            flag = True
        else:
            print(error)
    return dato.capitalize()

def validar_email(email):
    expresion = "^[a-zA-Z0-9._~-]+@[a-zA-Z0-9.-]+(?:\.[a-zA-Z0-9-]+)$"
    if re.search(expresion, email):
        return True
    else:
        return False

def get_email(text):
    flag = False
    while not flag:
        email = input(text)
        if validar_email(email):
            flag = True
        else:
            print('Lo siento, no es un correo valido.') 
    return email

def get_numero(text):
    flag = False
    while not flag:
        try:
            numero = int(input(text))
            if type(numero) is int and numero >= 1:
                flag = True
            else:
                print('Lo siento, debe ser un numero positivo.\n')
        except ValueError:
            print('Lo siento, debe ingresar un numero.\n')
    return numero

def get_password(text): 
    password = input(text)
    cifrado = hashlib.sha256(password.encode('utf-8'))
    return cifrado.hexdigest()

def pedir_datos():
    nombre =  get_string('Ingrese su nombre: ', 'Error, no es un nombre valido, no puede tener caracteres especiales ni numeros')
    apellido = get_string('Ingrese su apellido: ','Error, no es un apellido valido, no puede tener caracteres especiales ni numeros')
    email = get_email('Ingrese su email: ')
    password = get_password('Ingrese su contraseña: ')

    datos = {
        'nombre':nombre,
        'apellido':apellido,
        'email':email,
        'password':password
    }
    return datos
    
def mostrar_usuarios(usuarios):
    print('\t\t----- Listado de  Usuarios en base  ----- \n')
    for datos in usuarios:
        print(
            'ID: {0} \nNombre:{1} \nApellido:{2} \nEmail:{3} \nPassword:{4} \nFecha de Creacion:{5}\n'.format(
                datos['id'],datos['nombre'],datos['apellido'],datos['email'],datos['password'],datos['fecha']
            )
        )
    
def buscar_usuario(usuarios, id):
    for match in usuarios:
        if match['id'] == id:
            return True
            break

def buscar_email(usuarios, email):
    for match in usuarios:
        if match['email'] in email.values():
            return True 
            break        

def switch(opcion):
    final = {'none': None}
    while True:
        if opcion == 1:
            dato = {'nombre':get_string('Ingrese nombre nuevo: ','Error, no es un nombre valido, no puede contener caracteres especiales ni numeros')}    
        elif opcion == 2:
            dato = {'apellido':get_string('Ingrese apellido: ','Error, no es un nombre valido, no puede contener caracteres especiales ni numeros')}
        elif opcion == 3:
            dato = {'email':get_email('Ingrese email nuevo: ')}
        elif opcion == 4:
            final = {'false':False}
            break
        while  True:
            confirmarcion = get_string('Desea confirmar el cambio(s/n)','Error debe ser una letra.')
            if confirmarcion.lower() == 's':
                final = dato 
                break
            elif  confirmarcion.lower() == 'n':
                print('El cambio no se realizo.')
                break
            else:
                print('Letra invalida.')
                continue
        break
    return final

