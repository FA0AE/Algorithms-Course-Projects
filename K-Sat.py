# -*- coding: utf-8 -*-
# Autores: Irma Gómez, Victor Curiel, Francisco Arenas 
# Implementación de K-SAT

def userInput():
    print('''
    ----------------------------------------------
    IMPLEMENTACIÓN DE ALGORITMO K-SAT:
        1. Probar Algoritmo K-SAT
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

def crearDiccionario(stringBit):
    cont=1
    diccionario={}
    for i in stringBit:
        diccionario[cont]=i
        cont+=1
        
    return diccionario
    

def read(archivo):
    lectura = open(archivo, 'r')
    info=lectura.readlines(1)
    info=lectura.readlines(2)
    
    bitString=lectura.readlines(3)
    bitString=bitString[0].replace("\n","")
    diccionario=crearDiccionario(bitString)
    
    contenido = lectura.read()

    lista=contenido.split(" 0\n")

    return lista,diccionario

def evaluating(archivo):
    lista,diccionario=read(archivo)
    print("\nValores de variables: \n",diccionario)

    valores=[]
    
    for x in lista:
        if(x!=''):
            y=x.split(" ")

            valores.append(y)
        
    print("\nClausulas: \n",valores)
    
    for i in valores:
        flag=0
        
        for j in range (len(i)):
            num=i[j]
            
            if(num[0]=='-'):
                num=num[1:] 
                
                sustitucion=diccionario.get(int(num))
                
                if(sustitucion== "0"):
                    sustitucion ="1"
                else:
                    sustitucion="0"
 
                if(flag==1 or int(sustitucion)==1):
                    flag=1
                else:
                    flag=0
            
            else:
                sustitucion=diccionario.get(int(num))

                if(int(flag)==1 or int(sustitucion)==1):
                    flag=1
                else:
                    flag=0
                
        if(flag==0):
            print("\nSolución: False")
            break
        
    
    if(flag==1):
        print("\nSolución: True")

# Función main() con implementación de menú
def main():
    opcion = userInput()
    while opcion != 0:
        if opcion == 1:
            archivo = input("Escriba el nombre del archivo con extensión .txt: ")
            print("Ejecutando programa... ")
            evaluating(archivo)
            opcion = userInput()
        elif opcion == 2:
            autores()
            opcion = userInput()
        else: 
            print("Opción no disponible!")
            opcion = userInput()

# Llamada al main        
main()
