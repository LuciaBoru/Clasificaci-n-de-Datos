"""Se realizara la validación de ventas y busquedas por categoria para lograr indentificar que productos fueron los que tuvieron menos
ventas y busquedas en la plataforma.

by Lucia Cardenas Borunda
"""
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

## Definici+on de la funcion para la categoria de ventas
def categorySold():
    ## Hacer una lista para el conteo del total de productos vendidos. 
    nameCate = []
    product = []  #Hacer una lista donde se almacenaran los productos.
    temp = [] ## Realizar una lista temporral

    for sale in lifestore_sales: #Un ciclo que validara las categorias dentro de la lista ventas
        validation =  True #Se validara si el valor es verdadero
        for id in temp:  #Creando la llave en un ciclo para utilizar la llave temporal
            if sale[1] == id[0]: ## Comparando la venta con la llave
                id[1] += 1 #Se contara la llave
                validation = False # Se validara el caso que llegue a ser falso
        if validation: #Si la validacion agregara los datos en la lista temporal.
            temp.append([sale[1],1])

    #Se ordenaran los datos 
    temp.sort(key=lambda x:x[1])

    for value in temp: ##Se evaluaran los valores en la lista temporal
        for category in lifestore_products: #Trayendo la categoria desde la lista productos
            if value[0] == category[0]: ##Comparando si el valor es igual a la categoria
                product.append([category[3],category[1], value[1]]) #Ingresando los valores en la lista producto
                if category[3] not in nameCate: ## Comparando la categoria para agregar los valores en la lista del nomebre de categoria, si no estan dentro
                    nameCate.append(category[3])#Introducir los valores de la categoria en la nueva lista

    for name in nameCate: #Asignar un nombre en la categoria
        print("\n", name)    #Impresión de la categoria
        limit = 5    #Asignar un limite a mostrar
        for value in product: #Sacar el valor de la lista producto
            if value[0] == name and limit != 0: #Si el valor es igual o diferente al limite 
                print(" " + str(value[1]) + ", " + str(value[2])) #se imprimira la información
                limit -= 1 #Solamente que el valor sea menor o igual que 

#Funcion categoria por busqueda, se reutilizo el codigo de la función anterior solo haciendo un cambio.
def categorySearch():
    ## Hacer un directorio para el conteo del total de productos vendidos. 
    nameCate = []
    product = []
    temp = []

    for sale in lifestore_searches:
        validation =  True
        for id in temp:            
            if sale[1] == id[0]:
                id[1] += 1
                validation = False
        if validation:
            temp.append([sale[1],1])

    temp.sort(key=lambda x:x[1])

    for value in temp:
        for category in lifestore_products:
            if value[0] == category[0]:
                product.append([category[3],category[1], value[1]])
                if category[3] not in nameCate:
                    nameCate.append(category[3])

    for name in nameCate:
        print("\n", name)    
        limit = 10    ##SOlo se le cambiara el limite de muestra
        for value in product:
            if value[0] == name and limit != 0:
                print(" " + str(value[1]) + ", " + str(value[2]))
                limit -= 1

##Dedinición de las funcion para el menu de categoria.
def category():

    ##Definición de las variables tipo texto que solo se utilizaran para el formato del menú imprimido despues de la creación.
    title = "Categoria de Productos"
    print ("\n", title.center (60), "\n")

    ##Variable input en cual se agregara la opción que accederas de los servicios
    category = int(input("""
    1. Productos menos vendidos
    2. Productos menos buscandos
    0. Salir \n
        Ingresa una opción: """))

    #Se define un ciclo while que declara que mientras menu sea diferente a 0 se realizaria una acción ya que si es igual saldria del programa.
    while category != 0:
        ##Aqui se mostrara los accesos a las funciones conforme los selecciones nos enviara a la función requerida
        if category == 1:
            print("\n \n \n \n", "Los 5 productos con menores ventas".center (60), "\n \n" )
            categorySold()
            break
        elif category == 2:
            print("\n \n \n \n", "Los 10 productos con menores búsquedas".center (60), "\n \n" )
            categorySearch()
            break
        #Si llegara a ingresar un numero de los que no estan admitidos, mostrara el mensaje de error.
        else:
            print("\n")
            print("¡Error!".center (60))
            print("Seleccione una opcion valida".center(60))
            break   
