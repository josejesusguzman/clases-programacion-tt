import mysql.connector 
from mysql.connector import errorcode
import random

try:
    conexion = mysql.connector.connect(
        host = "clase-python.mysql.database.azure.com",
        user = "josejesusguzman@clase-python",
        password = "5f6g7h8j9k0l.",
        database = "doxeos"
    )
    print("Conexión exitosa")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR :
        print("Usuario on contraseña incorrectos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR :
        print("La base de datos no existe")
    else :
        print(err)
    exit()


try :
    cursor = conexion.cursor()
    consulta_sql = "INSERT INTO usuarios_doxeados (id, correo, pass, direccion, telefono) VALUE (%s, %s, %s, %s, %s);"
    cursor.execute(consulta_sql, (random.randint(0, 1000), "correotest@12345.com", "sdakjhdasjkhdkjas", "sadasda", str(random.randint(10000, 1000000))))
    conexion.commit()
    print ("Dato almacenado")
except Exception as err :
    print(err)

basedatos = conexion.cursor()
sql_statement = "SELECT * FROM usuarios_doxeados"

basedatos.execute(sql_statement)
result = basedatos.fetchall()

print (basedatos.rowcount)

for x in result :
    print(x)

conexion.close()

