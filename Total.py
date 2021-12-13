"""Creación de la función para sacar el resultado total anual y mensual de las ventas, junto con el promedio de ventas.

by Lucia Cárdenas Borunda
"""

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
  
## Definici+on de la funcion para hacer la función
def total():
    ## Hacer un directorio para el conteo del total de productos vendidos. 
    dictionary = {} #directorio
    product = [] #creación de lista vacia
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10','11','12'] ##Variable de meses creado
    total = 0 #Asignar una variable al total

    #Bucle para revisar la lista de datos de venta
    for sale in lifestore_sales:
        #valor temporal que asigna un rango para sacar la fecha de la lista de ventas
        temp = sale[3][3:5] 
        #Revisara si el mes fue asignado como una llave unica, si, no se asigna
        if temp in dictionary.keys():
            ## Si ya existe la llave guardada, solo se agregaria la nueva tienda a la lista
            dictionary[temp].append(sale[1])
        else:
            ## Aqui se asigna por primera vez, si, no solo sumaria el contador
            dictionary[temp] = [sale[1]]

    for check in dictionary: ##Checara todo el diccionario
        product.append([check, 0, 0]) ##Esta declarando una lista del mes, arrancando con cero ganancias.
        for item in dictionary[check]:#Repasar la lista que se encuentra dentro del diccionario.
            for price in lifestore_products: #Asignara el precio al producto
                if item == price[0]: #Estamos comparando cual es el producto contra el preciuo
                    for revise in product: #Como es una lista de lista se tiende que revisar nuevamente la lista
                        if revise[0] == check: #Al hacerse la revision se checa que los valores este
                            revise[1] += price[2] #Un incremento del precio por venta en el mes
                            revise[2] += 1 #Contara solamente los productos del mes
                            break
                    break

    for date in product: #se realiza una revisión para sacar el mes de la lista producto
        date[2] = date[1] / date[2] # Calculando el promedio mensual
        total += date[1] #Calcula el total de ingresos 
    
    product.sort(key=lambda x:x[1], reverse=True) #Se ordenan las ventas con mayores ganancias la mes en la lista
    print("\n","Ventas Mensuales".center(60)) #Etiqueta
    print(" ","Orden de Meses con más Ventas".center(60), "\n")
    print("Meses" + " | " + "Total de Ingresos" + " | " + "\t Promedio") #Etiqueta
    print("----------------------------------------------") #Etiqueta

    for value in product:#Impresión de resultados.
        print(value[0] + " | ".rjust(6) + str(value[1]).ljust(17) + " | " +str(value[2]))
    
    print("\n") 
    print("Total Anual: ", total) #Impresión total
