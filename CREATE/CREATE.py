#-------IMPORT_LIBRERIE----#
import mysql.connector

#-----------CREACION_DATABASE-----#

def crear_database():
    try:    
        #CREACION DATABASE
        conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cespedes2003',
            database = 'mysql'
        )

        cursor = conexion.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS escuela')
        conexion.close()
        cursor.close()
        
        print('Se creo la base de datos')
    except:
        print('No se pudo crear la base de datos')



def crear_tabla():
    #CREACION TABLA
    try:
        conexion = mysql.connector.connect(
            host = 'localhost', 
            user = 'root',
            password = 'Cespedes2003',
            database = 'escuela'
        )

        cursor = conexion.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS estudiantes(id_estudiante INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(45) NOT NULL, materia VARCHAR(45) NOT NULL, seccion ENUM("A","B","C") DEFAULT("A"), numero_lista TINYINT(2) CHECK(numero_lista >= 1 AND numero_lista <= 45))')
        conexion.close()
        cursor.close()

        print('Se creo la tabla correctamente')
        
    except:
        print('No se pudo crear la tabla')



if __name__ == '__main__':
    print(crear_database())
    print(crear_tabla())

