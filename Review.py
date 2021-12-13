"""La función de reseña en un listado para productos con las mejores reseñas y otro para las peores, 
considerando los productos con devolución. Reutilizando codigo de funciónes anteriores.

by Lucia Cárdenas Borunda
"""
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

## Definici+on de la funcion para hacer la función
def review(opc = 'worse' and 'better'):
    ## Hacer un directorio para el conteo del total de productos vendidos. 
    dictionary = {}
    #Una lista que recabara la lista de productos
    product = []

    for sale in lifestore_sales:
        if sale[1] in dictionary.keys():
            #Crear un diccionario de cada procducto # pero ahora es una lista con el total de las reseñas y total del producto vendido se complementa con la operación 24 
            (dictionary[sale[1]])[0] += sale[2] 
            (dictionary[sale[1]])[1] += 1 ## siendo quien suma 
        else:
            ## Aqui se asigna por primera vez, si, no solo sumaria el contador
            dictionary[sale[1]] = [sale[2], 1]
    #Se sobreescribira el diccionario ya existente, remplazando la lista por el promedio de las reseñas con la misma llave(siendo el numero del producto)
    dictionary = {x:dictionary[x][0]/ dictionary[x][1] for x in dictionary} 
    if opc == 'better': ## Validacndo la función del mejor reutilizando el codigo mayor de @Sort
        for five in range(5):
            better = max(dictionary, key=dictionary.get)
            for name in lifestore_products: ##Solamente que este ahora llamara las reseñas
                if better == name[0]: 
                    product.append([dictionary[better], name[1]])
                    break
            del dictionary[better]
        
    if opc == 'worse': ## Validacndo la función del mejor reutilizando el codigo menor de @Sort
        for five in range(5):
            worse = min(dictionary, key=dictionary.get)
            for name in lifestore_products:
                if worse == name[0]: 
                    product.append([dictionary[worse], name[1]])
                    break
            del dictionary[worse]
    
    for value in product:
        print(str(value[0]) + " , "  + value[1] )

##Dedinición de las funcion para el menu de reseñas.
def score():

    ##Definición de las variables tipo texto que solo se utilizaran para el formato del menú imprimido despues de la creación.
    title = "Reseñas de Productos"
    print ("\n", title.center (60), "\n")

    ##Variable input en cual se agregara la opción que accederas de los servicios
    score = int(input("""
    1. Mejores reseñas
    2. Peores reseñas
    0. Salir \n
        Ingresa una opción: """))

    #Se define un ciclo while que declara que mientras menu sea diferente a 0 se realizaria una acción ya que si es igual saldria del programa.
    while score != 0:
        ##Aqui se mostrara los accesos a las funciones conforme los selecciones nos enviara a la función requerida
        if score == 1:
            print("\n \n \n \n", "Las 5 mejores reseñas".center (60), "\n \n" )
            review('better')
            break
        elif score == 2:
            print("\n \n \n \n", "Los 5 peores reseñass".center (60), "\n \n" )
            review('worse')
            break
        #Si llegara a ingresar un numero de los que no estan admitidos, mostrara el mensaje de error.
        else:
            print("\n")
            print("¡Error!".center (60))
            print("Seleccione una opcion valida".center(60))
            break   
