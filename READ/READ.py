#----IMPORT_LIBRERIAS
import mysql.connector


def read_table():
    #read_table
    try:
        #CONECT
        conexion = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            password = 'Cespedes2003',
            database = 'escuela'
        )
        #SELECCIONAR DATOS
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM estudiantes')
        #cursor.execute('SELECT COUNT(*) FROM estudiantes')
        #cursor.execute('SELECT * FROM estudiantes')
        #cursor.excecute('SELECT * FROM estudiantes WHERE numero_lista > 10 AND numero_lista < 1' )
        result = cursor.fetchall()
        print(result)
        
    except:
        print('sorry, no fue posible mostrar los datos')

if __name__ == '__main__':
    print(read_table())