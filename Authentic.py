"""Archivo de autentificacion donde se contiene la función que realizara el registro de usuario y contraseña.

Se guardara sobre archivos para almacenar los usuarios y nombraremos el archivo database, en el cual sera llamado en ambas funciones
ademas de abrirlos y poder leerlos.

by Lucia Cárdenas Borunda
"""

from Menu import menu
from os import write #Importa archivos de escritura
import getpass #Importa para protección de contraseñas

#Definiremos la función para el registro de usuarios y contraseñas
def register():
    #Se abrira el archivo "database" y se leera el archivo 
    db = open ("database.txt", "r")

    print("\n \n \n", "Registro de Usuario".center (60), "\n \n") #Salto de linea

    #Se agregara el 'input' para la entrada de datos en el registro.
    Username = input("Crear un nombre de usuario: ")
    print("\n")
    Password = getpass.getpass("Crear una contraseña: ")
    print("\n")
    Password1 = getpass.getpass("Confirmar contraseña: ")
    print("\n")
    #Como el archivo no puede ser leido de manera interna en python se debe de realizar una interpretación.
    u = [] #Se creara una variable vacia tipo lista para almacenar el usuario
    p = [] #Se aplicara lo mismo pero con la contraseña

    #Usando un bucle for para dividir el texto de nuestra database
    for i in db:
        a, b = i.split(", ") #Con esto se dividira el texto con una coma.
        b = b.strip() #Este proceso eliminara lo que se escribe en automatico despues del usuario al generar en el archivo.
        u.append(a) #Almacenara el nombre de usuario
        p.append(b) #Almacenara la contraseña
    #Los datos que son iguales quedaran ellos en un dictado que se revisara para comprimir la información    
    data = dict(zip(u, p))

    #Se validara la contraseña que ingrese el usuario tanto como la confirmación, haciendo una comparación de caracteres.
    if Password != Password1:
        print("Las contraseñas no coinciden, reintente nuevamente")
        register()
    else:
        #Para mas seguridad se solicitara que la contraseña tenga un minimo de 6 caracteres de ser lo contrario se solicitara que lo vuelva a intentar.
        if len(Password) <= 6:
            print("La contraseña es demasiado corta, reintente nuevamente:")
            register()
        #Aparte agregaremos una condición que valide si el usuario registrado ya se encuentra en el archivo de texto.
        elif Username in u:
            print("El usuario " + Username + " ya existe")
            register()
        #Por este lado se realizara la escritura en el archivo de texto, mandando a llamar el archivo y solicitando abrirlo para escribir la información recaudada.
        else:
            db = open("database.txt", "a")
            #Se generara una estructura en el archivo para que no se lleguen a generar confuciones en la lectura, dividiendo por comas y dando un salto de linea al final.
            db.write(Username + ", " + Password + "\n")
            print("¡Registrado de manera exitosa!")

#    os.system("CLS")

#Definiendo tambien la función en la cual se realizara el inicio de sesión
def access():
    #Se replicara la lectura del archivo
    db = open("database.txt", "r")

    print("\n \n \n", "Inicio de Sesión".center (60), "\n \n") ##Titulo de la acción a realizar

    #Se volveran a solicitar los 'input' para la entrada de datos para el inicio de sesión.
    Username = input("Ingresa tú usuario: ")
    print("\n")
    Password = getpass.getpass("Ingresa tú contraseña: ")

    #Se copiara la manera de interpretación del archivo que se utilizo en el registro
    if not len(Username or Password) < 1:
        #Como el archivo no puede ser leido de manera interna en python se debe de realizar una interpretación.
        u = [] #Se creara una variable vacia tipo lista para almacenar el usuario
        p = [] #Se aplicara lo mismo pero con la contraseña

    #Usando un bucle for para dividir el texto de nuestra database
        for i in db:
            a, b = i.split(", ") #Con esto se dividira el texto con una coma.
            b = b.strip() #Este proceso eliminara lo que se escribe en automatico despues del usuario al generar en el archivo.
            u.append(a) #Almacenara el nombre de usuario
            p.append(b) #Almacenara la contraseña
        #Los datos que son iguales quedaran ellos en un dictado que se revisara para comprimir la información    
        data = dict(zip(u, p))

        #Se agregaron try para lograr agregar excepciones en el programa
        try:
            #Con este se validara la lectura del archivo si se encuentra en la database
            if data[Username]:
                try:
                    #Solicitud y validación de la contraseña que esta este en la misma linea que la contraseña
                    if Password == data[Username]:
                        #Si esto resulta exitoso se redirigira al menú
                        print("\n","Inicio de sesión, ¡Exitoso!".center (60), "\n \n")
                        welcome = "Bienvenido " + Username
                        print("\n",welcome.center (60))
                        menu()
                    else:
                        #Se ralizan 2 verificaciones al no llegar a tener coincidencia con el nombre se lanzarara un mensaje de error
                        print("Nombre de usuario o contraseña incorrectos")
                #En la segunda validacion dara una revisión al archivo para comprobar si, se encuentran los datos o se enviara el mensaje
                except:
                    print("Contraseña o nombre de usuario incorrecto")
            #Al verificar si el usuario se encuentra en la base de datos se mandara un mensaje para que verifique 
            else:
                print("El nombre de usuario no existe")
        #Esta excepcion aparecera si todo lo contrario no pudo ser verificado se mostrara el siguiente mensaje
        except:
            print("Inicio de sesión, Erroneo")
    else:
        print("Ingrese un valor")

#Definiremos un menú de autentificación
def home(option=None):
    title = "Bienvenido Gerencia LifeStore"
    print ("\n \n \n",title.center (60), "\n")
    print("Inicio | Registro".center (60), "\n \n \n")#Impresión de las opciones
    option = input ("¿Donde desea ingresar? ")# Seleccionar una opción
    if option == "Inicio" or option == "inicio": ##Comparación de opciones
        access() ##Ingresa al acceso
    elif option == "Registro" or option == "registro":
        register()#Ingresa al registro
    else:##Si no llega a ser una opción de las siguientes despliega un mensaje de error
        print("¡Opción no valida!")

if __name__== "__main__":
    home()#Muestra la información del home
