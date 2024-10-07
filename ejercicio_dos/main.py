""" 
Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total 
tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).

Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:

Cargar planilla. El chofer se debe identificar (el legajo debe existir 
dentro de una lista de legajos). Si el chofer existe cargará la recaudación 
del viaje indicando línea y coche (no necesariamente un chofer está 
asignado a una única línea y coche), estos datos deben estar validados. 
Un chofer puede cargar más de una recaudación por día (para distintas líneas 
y distintos coches). Cada coche de cada línea puede tener varias recaudaciones 
diarias.

Mostrar la recaudación de cada coche y línea (mostrar la matriz).

Calcular y mostrar recaudación por línea.

Calcular y mostrar recaudación por coche. ?

Calcular y mostrar la recaudación total.

Ordenar la matriz de vehiculos por recaudacion de forma descendente

Mostrar el vehiculo con mayor y menor recaudacion por cada linea

Calcular la recaudacion promedio por vehiculo de cada linea

De cada linea, mostrar los vehiculos que superen los 5000 de recaudacion

Salir.

Todo el desarrollo tiene que estar modularizado: ingreso de datos, 
validaciones de líneas y coches, generación y verificación de existencia de 
legajo, cálculos, etc.
"""
from Paquete_utilidades.Menu import *
from Paquete_utilidades.Validaciones import *
from Paquete_utilidades.Matrices import *
from Funciones_Especificas import *
import os

#Genero listas/ matrices con las que voy a trabajar
coches_por_linea = [["A01","A02","A03","A04","A05","B01","B02","B03","B04","B05","C01","C02","C03","C04","C05"],
                    ["A","A","A","A","A","B","B","B","B","B","C","C","C","C","C"],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]

lineas = ["A","B","C"]
legajos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] #RANDOMIZAR!!!

opciones_principal = ["Cargar planilla.","Recaudación de cada coche y linea al momento.", "Recaudación por línea.", "Recaudación por coche.","Recaudación total","Ordenar vehículos de menor a mayor por recaudación.","Vehiculo con mayor y menor recaudacion por cada linea.","Recaudacion promedio de cada linea.","Vehiculos que superen los 5000 de recaudacion por línea"]


while True:
    opcion = imprimir_menu("\nBienvenido/a al Sistema de Cargas de Recaudación de Choferes!\nMenu principal: ",opciones_principal,True)

    if opcion == 0: #Salir
        break
    elif opcion == 1: #Cargar planilla
        cargar_planilla(coches_por_linea, legajos)

    elif opcion == 2: #Recaudación de cada coche y linea
        mostrar_matriz(coches_por_linea)

    elif opcion == 3: #Recaudación por línea
        calcular_recaudacion_linea(lineas,coches_por_linea)

    elif opcion == 4: #Recaudación por coche
        pass #La recaudacion por coche no se obtiene al mostrar la matriz?

    elif opcion == 5: #Recaudación total
        recaudacion_total = calcular_recaudacion_total(coches_por_linea)
        print(f"Recaudación total: {recaudacion_total}")

    elif opcion == 6: #Ordenar vehículos de menor a mayor por recaudación
        bubble_sort_vertical_descendente(coches_por_linea,2)
        for i in range(len(coches_por_linea[0])):
            print(f"Coche {coches_por_linea[0][i]} Linea {coches_por_linea[1][i]} Recaudacion {coches_por_linea[2][i]}")
        
    elif opcion == 7: #Vehiculo con mayor y menor recaudacion por cada linea
        calcular_mayor_menor_recaudacion_linea(lineas,coches_por_linea)

    elif opcion == 8: #Recaudacion promedio de cada linea
        calcular_promedio_linea(lineas,coches_por_linea)
    elif opcion == 9: #Vehiculos que superen los 5000 de recaudacion por línea
        calcular_recaudacion_mas_5000_linea(lineas,coches_por_linea)

    input("Presione Enter para continuar...")
    os.system("cls")

