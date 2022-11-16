#IMPORT LIBRERIAS
import mysql.connector


#INSERT DATA
conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Cespedes2003',
    database = 'escuela'
)

def insert_data():
    try:
        while True:
            # DATOS A AGREGAR
            nombre = input('Ingrese el nombre: ')
            materia = input('Ingrese la materia: ')
            seccion = input('ingrese la seccion: ').upper()
            numero_lista = int(input('ingrese numero se lista: '))
            
            #SOLICITUD
            cursor = conexion.cursor()
            sql = ('INSERT INTO estudiantes(nombre, materia, seccion, numero_lista) VALUES(%s,%s,%s,%s)')
            values =(nombre, materia, seccion, numero_lista)
            cursor.execute(sql, values)
            conexion.commit()
            print(f'se agregaron {cursor.rowcount} filas')
            
            #CICLO
            pregunta = input('Quiere agregar otro dato? ').lower()
            if pregunta == 'si':
                continue
            else:
                print('Se agragaron todos los datos correctamente')
                break
    except:
        print('No se pudo agregar el nuevo dato')





#MODIFICAR FILA
def modify_row():
    #MODIFICAR FILA
    try:
        #CONECT
        conexion = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            password = 'Cespedes2003',
            database = 'escuela'
        )
        
        #-----FORMULARIO------#
        nombre = str(input('Nombre que desea modificar: '))
        id_ = int(input('id que desea modificar: '))
        
        #-------SOLICITUD-------#
        cursor = conexion.cursor()
        sql =('UPDATE estudiantes SET nombre = %s WHERE id_estudiante = "%s"')
        values = (nombre,id_)
        cursor.execute(sql,values)
        conexion.commit()
        print('Se modifico la fila correctamente')
        
    except:
        print('No se pudo modificar la fila')
        

#AGREGAR COLUMNA
def add_column():
    try:
        #Conecion con la base de datos
        conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Cespedes2003',
            database = 'escuela'
        )
        #Solicitud
        cursor = conexion.cursor()
        cursor.execute('ALTER TABLE estudiantes ADD numero_listaa TINYINT(2) CHECK(numero_listaa >= 1 AND numero_listaa <= 45)')

        conexion.close()
        cursor.close()
        print(f'Se realizo el cambio')
        
    except:
        print('No se pudo agregar la fila')


if __name__ == '__main__':
    #print(modify_row())
    #print(insert_data())
    #print(add_column())
    pass