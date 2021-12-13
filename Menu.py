"""" Menú de opciones multiples para seleccionar una de los servicios que solicito el cliente

by Lucia Cárdenas Borunda
"""
from Category import category
from Review import score
from Total import total
from Sort import sort

##Dedinición de las funcion para el menu de selección.
def menu():

    ##Definición de las variables tipo texto que solo se utilizaran para el formato del menú imprimido despues de la creación.
    title = "Clasificación de Datos"
    print ("\n", title.center (60), "\n")

    ##Variable input en cual se agregara la opción que accederas de los servicios
    menu = int(input("""
    1. Orden de Productos 
    2. Categorias de Productos 
    3. Reseñas de Servicios
    4. Total de Ventas
    0. Salir \n
        Ingresa una opción: """))

    #Se define un ciclo while que declara que mientras menu sea diferente a 0 se realizaria una acción ya que si es igual saldria del programa.
    while menu != 0:
        ##Aqui se mostrara los accesos a las funciones conforme los selecciones nos enviara a la función requerida
        if menu == 1:
            sort()
        elif menu == 2:
            category()
        elif menu == 3:
            score()
        elif menu == 4:
            total()
            break
        #Si llegara a ingresar un numero de los que no estan admitidos, mostrara el mensaje de error.
        else:
            print("\n")
            print("¡Error!".center (60))
            print("Seleccione una opcion valida".center(60))
            break   
