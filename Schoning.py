# encoding: UTF-8 
# Autores: Irma Gómez, Victor Curiel, Francisco Arenas 
# Proyecto Final
import requests
key=1

def numerosAleatorios(n,alMin,alMax):
    global key
    if(key==1):
        clave="001228cd-a88c-42ec-8053-f7e179d2c624"
        idRand=17793
    elif(key==2):
        clave="908d1b49-ce43-4c95-b303-381bb6767e0c"
        idRand=32290
    elif(key==3):
        clave="ab0f0ca4-1cce-4b22-be1a-5d1f04361d03"
        idRand=10981
    elif(key==4):
        clave="fc7fd996-9bdb-471e-b842-bfec79ac1906"
        idRand=27002
    elif(key==5):
        clave="086083f1-1c1f-4039-af90-fc27b5ebefe8"
        idRand=4413
    elif(key==6):
        clave="5ac9a946-ee8d-459c-b681-2bf5b3c0fa94"
        idRand=25746
    elif(key==7):
        clave="8f247f1f-ab3a-497f-afee-41694d2e1242"
        idRand=4574
    elif(key==8):
        clave="498cf376-7d05-46fd-80e7-f534589a2d65"
        idRand=8198
    elif(key==9):
        clave="85458730-2b83-4cc4-805e-ee117d770381"
        idRand=19837
    elif(key==10):
        clave="1989b68b-970a-4888-a286-97a54e76e094"
        idRand=3671
    
    reqData= {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": clave,
            "n": n,
            "min": alMin,
            "max": alMax,
            "replacement": True,
            "base": 10
        },
        "id": idRand
    }
        
    response=requests.post('https://api.random.org/json-rpc/2/invoke',json=reqData)
    response.raise_for_status
    
    json=response.json()
 
    if(json['result']['requestsLeft']<50):
        key=key+1
    data=json['result']['random']['data']
    
    return data

def escribirArchivo(archivo,string):
    f = open (archivo, "a")
    f.write(string)
    f.close()

def crearDiccionario(num):
    cont=1
    diccionario={}
    listaAl=numerosAleatorios(num,0,1)
    for i in range (num):
        diccionario[i+1]=listaAl[i]
        cont+=1
    return diccionario
    

def read(archivo):
    lectura = open(archivo, 'r')
    info=lectura.readlines(1)
    info=lectura.readlines(2)
    
    num=info[0].split(" ")
    diccionario=crearDiccionario(int(num[2]))
    
    contenido = lectura.read()

    lista=contenido.split(" 0\n")
    
    valores=[]
    
    for x in lista:
        if(x!=''):
            y=x.split(" ")
            valores.append(y)

    return valores,diccionario


def evaluating(valores,diccionario,archivoEscribir):
    
    satisfiedC=[] #Lista con claúsulas True
    NoSatisfiedC=[] #Lista con claúsulas False
    
    print("\nValores de variables: \n",diccionario)
    escribirArchivo(archivoEscribir,("\nValores de variables: \n"+str(diccionario)))
    
    for i in range(len(valores)):
        flagO=0
        
        for j in range (len(valores[i])):
            #Valor j de la clausula i 
            num=valores[i][j]
            
            if(num[0]=='-'):
                #Quitando el menos
                num=num[1:] 
                
                sustitucion=diccionario.get(int(num))
                
                #Aplicando NOT
                if(sustitucion==0):
                    sustitucion =1
                else:
                    sustitucion=0
            
            else:
                sustitucion=diccionario.get(int(num))
            if(flagO==1 or int(sustitucion)==1):
                flagO=1
            else:
                flagO=0
                
        if(flagO==0):
            #La evaluación de una clausula dio False
            NoSatisfiedC.append(i)
        else:
            satisfiedC.append(i)
    
    return satisfiedC, NoSatisfiedC



def schonning(archivo,archivoEscribir):
    valores,diccionario=read(archivo)
    print(diccionario)
    escribirArchivo(archivoEscribir,(str(diccionario)+"\n"))
    satisfiedC=[] #Lista con claúsulas True
    NoSatisfiedC=[] #Lista con claúsulas False
    print("\nClausulas: \n",valores)
    escribirArchivo(archivoEscribir,("\nClausulas: \n"+str(valores)+"\n"))
    itera=0
    for j in range(3*len(valores)):
    
        satisfiedC,NoSatisfiedC=evaluating(valores,diccionario,archivoEscribir)
        
        if(len(NoSatisfiedC)==0):
            print("\n\nLa instancia fue satisfecha\n")
            escribirArchivo(archivoEscribir,"\nLa instancia fue satisfecha")
            break
        else:
            itera=itera+1
            print("\nIteración: ",itera,"\n")
            escribirArchivo(archivoEscribir,("Iteración: "+str(itera)+"\n"))
            
            clausula=0
            variable=0
            print("Clausulas satisfechas: ",satisfiedC,"\n")
            escribirArchivo(archivoEscribir,("Clausulas satisfechas: "+str(satisfiedC)+"\n"))
            print("Clausulas insatisfechas: ",NoSatisfiedC,"\n")
            escribirArchivo(archivoEscribir,("Clausulas insatisfechas: "+str(NoSatisfiedC)+"\n"))
            
            
            
            if(len(NoSatisfiedC)!=1):
                clausula=NoSatisfiedC[numerosAleatorios(1,0,len(NoSatisfiedC)-1)[0]]
            else:
                clausula=NoSatisfiedC[0]
                
            variable=valores[clausula][numerosAleatorios(1,0,2)[0]]
            
            print("\nClaúsula a cambiar: ", clausula,"\n")
            escribirArchivo(archivoEscribir,("Claúsula a cambiar: "+ str(clausula)+"\n"))
            print("Variable a cambiar: ", variable,"\n")
            escribirArchivo(archivoEscribir,("Variable a cambiar: "+ str(variable)+"\n"))
            
            if(diccionario[abs(int(variable))]==0):
                diccionario[abs(int(variable))]=1
            else:
                diccionario[abs(int(variable))]=0
    if(len(NoSatisfiedC)!=0):
        print("\n\nProbablemente no se puede satisfacer la instancia\n\n")
        escribirArchivo(archivoEscribir,"Probablemente no se puede satisfacer la instancia")
            

def userInput():
    print('''
    ---------------------------------------------------
    PROYECTO FINAL:
        1. Probar Algoritmo de Schöning
        2. Conocer a los autores del proyecto
        0. Salir
    ---------------------------------------------------
    ''')
    opcion = int(input('¿Qué desea hacer? '))
    return opcion

def autores():
    print('''
    Autor:            Carrera:   Matrí­cula:
    Irma Gómez        (ITI)      A01747743
    Victor Curiel     (ISC)      A01747245
    Francisco Arenas  (ISC)      A01369122
    ''')


def main():
    opcion = userInput()
    while opcion != 0:
        if opcion == 1:
            archivo = input("Escriba el nombre del archivo que desea leer con extensión .txt: ")
            archivoEscribir = input("Escriba el nombre del archivo en donde desea guardar el procedimiento con extensión .txt: ")
            schonning(archivo,archivoEscribir) 
            opcion = userInput()
        elif opcion == 2:
            autores()
            opcion = userInput()
        else: 
            print("Opción no disponible!")
            opcion = userInput()
            

# Llamada al main        
main()