#Import librerias
import mysql.connector


def drop_databse():
    try:
        #eliminar base de datos
        #Conectamos a la base de datos
        conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cespedes2003',
            database = 'escuela'
        )
        #solicitud
        cursor = conexion.cursor()
        cursor.execute('DROP DATABASE IF EXISTS escuela')
        conexion.close()
        cursor.close()

        print('Se elimino la base de datos')
    except:
        print('No se elimino la base de datos')



#Borrar tabla
def drop_table():
    try:
        #Conexion a la base de datos
        conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cespedes2003',
            database = 'escuela'
        )
        
        #SOLICITUD
        cursor = conexion.cursor()
        cursor.execute('DROP TABLE IF EXISTS estudiantes')
        conexion.close()
        cursor.close()
        
        print('Se borro la talba')
        
    except:
        print('No se pudo borrar la tabla')
        


def drop_column():
    #Eliminar columna de la base de datos
    try:
        #Conexion a la base de datos
        conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cespedes2003',
            database = 'escuela'
        )
        #INSTANCIA
        cursor = conexion.cursor()
        cursor.execute('ALTER TABLE estudiantes DROP numero_lista')
        conexion.close()
        cursor.close()
        
        print(f'Se realizo el cambio')
        
    except:
        print('No se pudo eliminar la columna')
        

#Eliminar una fila
def drop_row():
    try:
        conexion  = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cespedes2003',
            database = 'escuela'
        )
        cursor = conexion.cursor()
        #sql = ('DELETE FROM estudiantes WHERE id_estudiante = %s')
        #id_estudiante = int(input('Ingrese el id del estudiante que quiere eliminar: '))
        
        cursor.execute('DELETE FROM estudiantes WHERE id_estudiante = 2')
        conexion.commit()
        
        print(f'{cursor.rowcount} registro(s) eliminado')
        
        
    except:
        print('No se pudo borrar la fila')


if __name__ == '__main__':
    #print(drop_column())
    #print(drop_table())
    #print(drop_databse())
    #print(drop_row())
    pass