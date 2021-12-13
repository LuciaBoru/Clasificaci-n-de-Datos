"""Crear un archivo que realice una validación sobre los productos mas vendidos y buscados, tanto los productos que 
al contrario cuentan con las menores busquedas y ventas.

by Lucia Cárdenas Borunda
"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

## Definici+on de la funcion para hacer el orden de las ventas
def sold(opc = 'less' and 'high'): ## Funcion, con una opción menor y mayor
    ## Hacer un directorio para el conteo del total de productos vendidos. 
    dictionary = {}
    #Generar una lista donde se guardaran los datos que se extraigan del archivo
    product = []

    for sale in lifestore_sales:## Bucle que recorrera la lista de ventas
        if sale[1] in dictionary.keys(): # Revisara si el mes fue asignado como una llave unica, si, no se asigna
            dictionary[sale[1]] += 1 #Se realizara el conteo de ventas
        else:
            dictionary[sale[1]] = 1 #Si la venta no se encuentra se comparara
    if opc == 'high': #La opcion de venta mayor 
        for five in range(5): #Sacar el rango de 5
            high = max(dictionary, key=dictionary.get) #Se sacara la llave del diccionario con la mayor venta
            for name in lifestore_products: #Se revisara la lista de productos
                if high == name[0]: #Evaluando el mayor producto
                    product.append([dictionary[high], name[1]]) #Sacando el valor maximo sumado 
                    break
            del dictionary[high] #Delimitando solo al mayor
        
    if opc == 'less': ##Opcion del menor 
        for five in range(5): #Asignación de rango 
            less = min(dictionary, key=dictionary.get) #Cambiando a la función de los datos menores.
            #Similar a la primera función solo con un rango menor.
            for name in lifestore_products:
                if less == name[0]: 
                    product.append([dictionary[less], name[1]])
                    break
            del dictionary[less]
    
    for value in product: #Sacando los valores de los productos
        print(str(value[0]) + " , " + value[1]) ##Impresión de los resultados.

## Definici+on de la funcion para hacer las busquedas, solo cambiando el directorio y similar al codigo de arriba
def search(opc = 'high' and 'less'):
    dictionary = {}
    product = []

    for sale in lifestore_searches: ##modificar el archivo para extraer la cantidad de busquedas
        if sale[1] in dictionary.keys():
            dictionary[sale[1]] += 1
        else:
            dictionary[sale[1]] = 1
    if opc == 'high':
        for five in range(10):
            high = max(dictionary, key=dictionary.get)
            for name in lifestore_products:
                if high == name[0]: 
                    product.append([dictionary[high], name[1]])
                    break
            del dictionary[high]
        
    if opc == 'less':
        for five in range(10):
            less = min(dictionary, key=dictionary.get)
            for name in lifestore_products:
                if less == name[0]: 
                    product.append([dictionary[less], name[1]])
                    break
            del dictionary[less]
    
    for value in product:
        print(str(value[0]) + " , " + value[1])
    
##Dedinición de las funcion para el menu de orden.
def sort():

    ##Definición de las variables tipo texto que solo se utilizaran para el formato del menú imprimido despues de la creación.
    title = "Orden de Datos"
    print ("\n", title.center (60), "\n")

    ##Variable input en cual se agregara la opción que accederas de los servicios
    sort = int(input("""
    1. Productos mas vendidos
    2. Productos mas buscados
    3. Productos menos vendidos
    4. Productos menos buscandos
    0. Salir \n
        Ingresa una opción: """))

    #Se define un ciclo while que declara que mientras menu sea diferente a 0 se realizaria una acción ya que si es igual saldria del programa.
    while sort != 0:
        ##Aqui se mostrara los accesos a las funciones conforme los selecciones nos enviara a la función requerida
        if sort == 1:
            print("\n \n \n \n", "Los 5 productos con mayores ventas".center (60), "\n \n" )
            sold('high')
            break
        elif sort == 2:
            print("\n \n \n \n", "Los 10 productos con mayor búsquedas".center (60), "\n \n" )
            search('high')
            break
        elif sort == 3:
            print("\n \n \n \n", "Los 5 productos con menores ventas".center (60), "\n \n" )
            sold('less')
            break
        elif sort == 4:
            print("\n \n \n \n", "Los 10 productos con menor búsquedas".center (60), "\n \n" )
            search('less')
            break
        #Si llegara a ingresar un numero de los que no estan admitidos, mostrara el mensaje de error.
        else:
            print("\n")
            print("¡Error!".center (60))
            print("Seleccione una opcion valida".center(60))
            break   
