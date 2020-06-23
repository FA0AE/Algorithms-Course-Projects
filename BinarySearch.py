# encoding: UTF-8 
# Autores: Irma Gómez, Victor Curiel, Francisco Arenas 
# Implementación de Binary Search

def userInput():
    print('''
    ----------------------------------------------
    IMPLEMENTACIÓN DE BINARY SEARCH:
        1. Probar Binary Search
        2. Conocer quienes hicieron el programa
        0. Salir
    ----------------------------------------------
    ''')
    opcion = int(input('¿Qué desea hacer? '))
    return opcion

def autores():
    print('''
    Autor:            Carrera:   Matrícula:
    Irma Gómez        (ITI)      A01747743
    Victor Curiel     (ISC)      A01747245
    Francisco Arenas  (ISC)      A01369122
    ''')

def lecturaArchvo(archivo):
    lectura = open(archivo, 'r')
    contenido = lectura.read()
    contenido = contenido.replace("(","")
    contenido = contenido.replace("\n","")
    x = contenido.split(")")
    return x

def creacionLista(archivo):
    x = lecturaArchvo(archivo)
    lista=x[0].split(",")
    lista=list(map(int,lista))
    return lista

def obtencionValor(archivo):
    x = lecturaArchvo(archivo)
    valor = int(x[1])
    return valor

def compararValor(valorBuscado, valorMitad):
    if (valorBuscado == valorMitad):
        return 0                        #El valor búscado está en la mitad
    elif (valorBuscado < valorMitad):   
        return -1                       #El valor está de lado izquierdo del array
    elif (valorBuscado > valorMitad):
        return 1                        #El valor está de lado derecho del array

def binarySearch(lista, valorBuscado):
    indiceMitad = int(len(lista) / 2)
    valorMitad = int(lista[indiceMitad])
    listaNum = list(range(1, len(lista) + 1))
    iteraciones = 0
    while(True):
        iteraciones += 1
        print("Comparando con: ", valorMitad)
        if (compararValor(valorBuscado, valorMitad) == -1):
            lista = lista[:indiceMitad]
            listaNum = listaNum[:indiceMitad]

        elif (compararValor(valorBuscado, valorMitad) == 1):
            lista = lista[indiceMitad:]
            listaNum = listaNum[indiceMitad:]

        elif (compararValor(valorBuscado, valorMitad) == 0):
            if (len(lista) == 2):
                if (lista[1] == valorBuscado):
                    lista = lista[1]
                    listaNum = listaNum[1]
                elif (lista[0] == valorBuscado):
                    lista = lista[0]
                    listaNum = listaNum[1]
            else:
                listaNum = listaNum[valorMitad]
            print("Las iteraciones necesarias fueron: ", iteraciones)
            return listaNum
            break;

        if (len(lista) != 0):
            indiceMitad = int(len(lista) / 2)
            valorMitad = lista[indiceMitad]
        else:
            False
            return -1
            break;

# Función main() con implementación de menú
def main():
    opcion = userInput()
    while opcion != 0:
        if opcion == 1:
            archivo = input("Escriba el nombre del archivo con extensión .txt: ")
            lista = creacionLista(archivo)
            valorBuscado = obtencionValor(archivo)
            print("El valor buscado es: ", valorBuscado)
            print("El valor fue encontrado en el índice: ", binarySearch(lista, valorBuscado))
            opcion = userInput()
        elif opcion == 2:
            autores()
            opcion = userInput()
        else: 
            print("Opción no disponible!")
            opcion = userInput()

# Llamada al main        
main()