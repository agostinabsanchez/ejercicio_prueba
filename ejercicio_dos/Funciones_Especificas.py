from Paquete_utilidades.Input import *
from Paquete_utilidades.Validaciones import *
from Paquete_utilidades.Menu import *


def cargar_planilla(coches_por_linea, legajos) -> None: ##Ver si dividir legajo de carga de recaudacion
    legajo_existe = False
    while legajo_existe == False:
        legajo = pedir_numero_entero("Ingrese su número de legajo: ")
        legajo_existe = validar_existe_en_lista(legajos,legajo)

    n = len(coches_por_linea[0])
    lista_coches = [""] * n

    cargar_otra_recaudacion = "Si"
    while cargar_otra_recaudacion == "Si" or cargar_otra_recaudacion == "si" :
        for i in range(len(lista_coches)):
            coche = coches_por_linea[0][i]
            linea = coches_por_linea[1][i]

            lista_coches[i]= f"Coche: {coche} Linea: {linea}"
        
        opcion_coche = imprimir_menu("Cargar recaudación al coche: ", lista_coches, False)

        indice_coche = opcion_coche - 1

        recaudación = pedir_numero_entero("Ingrese la recaudación en pesos: ")

        coches_por_linea[2][indice_coche] = coches_por_linea[2][indice_coche] + recaudación 


        cargar_otra_recaudacion = input("Desea cargar otra recaudación? (Si/No): ")


def mostrar_matriz(coches_por_linea : list[list]) -> None:
    for i in range(len(coches_por_linea[0])):
        print(f"Coche: {coches_por_linea[0][i]} Linea: {coches_por_linea[1][i]} Recaudación: {coches_por_linea[2][i]}")


def calcular_recaudacion_linea(lineas : list, matriz : list[list])-> None:
    
    for i in range(len(lineas)):
        linea_actual = lineas[i]
        print(f"Linea {linea_actual}: ")
        recaudacion_linea = 0 

        for j in range(len(matriz[0])):
            if matriz[1][j] == linea_actual:
                recaudacion = matriz[2][j]
                recaudacion_linea += recaudacion
        print(f"Recaudación: {recaudacion_linea}") 


def calcular_recaudacion_total(matriz : list[list]) -> int:
    recaudacion_total = 0
    for i in range(len(matriz[2])):
        recaudacion =  matriz[2][i]
        recaudacion_total += recaudacion

    return recaudacion_total


def calcular_mayor_menor_recaudacion_linea(lineas: list, matriz: list[list]):
    for i in range(len(lineas)):
        linea_actual = lineas[i]
        print(f"Linea {linea_actual}: ")

        minimo_coche = 0
        maximo_coche = 0 
        indice_minimo = None
        indice_maximo = None
        for j in range(len(matriz[0])):

            if matriz[1][j] == linea_actual:
                recaudacion_coche = matriz[2][j]
                if indice_minimo == None or recaudacion_coche < minimo_coche:
                    minimo_coche = recaudacion_coche
                    indice_minimo = j

                if indice_maximo == None or recaudacion_coche > maximo_coche:
                    maximo_coche = recaudacion_coche
                    indice_maximo = j

        if indice_maximo == None or indice_minimo == None:
            print("No hay coches con recaudación para esta línea.")
        else:
            print(f"Máxima recaudación: {maximo_coche} del coche {matriz[0][indice_maximo]}")
            print(f"Mínimo recaudación: {minimo_coche} del coche {matriz[0][indice_minimo]}")


def calcular_promedio_linea(lineas :list, matriz : list[list]):
    for i in range(len(lineas)):
        linea_actual = lineas[i]
        print(f"Linea: {linea_actual}: ")

        recaudacion_linea = 0
        contador_coche = 0
        for j in range(len(matriz[0])):
            if matriz[1][j] == linea_actual:
                recaudacion_coche = matriz[2][j]
                recaudacion_linea += recaudacion_coche
                contador_coche += 1
                
        promedio_linea = recaudacion_linea / contador_coche
        print(f"Promedio: {promedio_linea}")

def calcular_recaudacion_mas_5000_linea(lineas : list, matriz : list[list]):
    for i in range(len(lineas)):
        linea_actual = lineas[i]
        print(f"Coches con recaudación mayor a $5000 en la línea: {linea_actual}: ")

        contador_recaudacion_mayor = 0
        for j in range(len(matriz[0])):
            if matriz[1][j] == linea_actual:
                recaudacion_coche = matriz[2][j]
                if recaudacion_coche > 5000:
                    print(f"Coche: {matriz[0][j]} Recaudacion ${recaudacion_coche}")
                    contador_recaudacion_mayor += 1
        if contador_recaudacion_mayor == 0:
            print("No hay coches.")