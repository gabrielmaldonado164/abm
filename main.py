#-*- coding: utf-8 -*-
try:
    import funciones
    import usuarios
    from bd import Database
    import os
    import sys
except Exception as e:
    print('Error: {0}'.format(e))

LIMPIAR = "clear " if sys.platform.startswith("linux") else "cls"

def main():
    user = usuarios.Usuario()
    while True:
        menu = funciones.menu_principal()
        if menu == 1:
            try:
                os.system(LIMPIAR)
                user.listar_usuarios()
                input('para continuar presione enter...')
            except Exception as e:
                print('Error: {0}'.format(e))    
        elif menu == 2:
            try:
                os.system(LIMPIAR)
                user.crear_registro()
            except Exception as e:
                print('Error: {0}'.format(e))
        elif menu == 3:
            try:
                os.system(LIMPIAR)
                user.actualizar_usuario()
            except Exception as e:
                print('Error: {0}'.format())
        elif menu == 4:
            try:
                user.eliminar_usuario()
            except Exception as e:
                print('Error: {0}'.format(e))  
        elif menu == 5:
            print('Hasta luego!')
            conexion = Database().conectar()
            conexion.close()
            exit()
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        print('Interrupcion del programa.')
        conexion = Database().conectar()
        conexion.close()
        exit()
        
 