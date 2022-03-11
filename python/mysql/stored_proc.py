from matplotlib.style import context
import mysql.connector 
from mysql.connector import errorcode

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
    cursor.callproc('doxeados')

    for result in cursor.stored_results() :
        print(result.fetchall())

    print("Ejecución exitosa")
except Exception as ex :
    print (ex) 