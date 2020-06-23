# encoding: UTF-8 
# Autores: Irma Gómez, Victor Curiel, Francisco Arenas 
# Introduction to graph theory (Binary Tree implementation)

class Nodo():
    #Constructor
    def __init__(self, valor):
        self.valor = valor
        self.nodoIzquierda = None
        self.nodoDerecha = None

class BinaryTree():
    #Constructor
    def __init__(self):
        self.root = None

    #Metodo para añadir elementos. Se complementa con un metodo recursivo 
    def agregarNodo(self, valor):
        if (self.root is None):
            self.root = Nodo(valor)
        else: 
            self.adicionRecursiva(valor, self.root)
    
    def adicionRecursiva(self, valor, nodoActual):
        if (valor < nodoActual.valor):
            if (nodoActual.nodoIzquierda is None):
                nodoActual.nodoIzquierda = Nodo(valor)
            else: 
                self.adicionRecursiva(valor, nodoActual.nodoIzquierda)
        elif (valor > nodoActual.valor):   
            if (nodoActual.nodoDerecha is None):
                nodoActual.nodoDerecha = Nodo(valor)
            else:
                self.adicionRecursiva(valor, nodoActual.nodoDerecha)
        else:
            print("El valor: ", valor," ya se encuentra dentro del árbol:) ")
        

    #Impresión basada en el código de J.V sacado de la página:
    #https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/34013268#34013268 
    def printTree(self):
        if (self.root != None):
            lineas, *_ = self._printTree(self.root)
            for linea in lineas:
                print(linea)

    def _printTree(self, nodo_Actual):
        #No hay nodos a la izquierda y a la derecha
        if (nodo_Actual.nodoDerecha is None and nodo_Actual.nodoIzquierda is None):
            linea = '%s' % nodo_Actual.valor
            ancho = len(linea)
            altura = 1
            centro = ancho // 2
            return [linea], ancho, altura, centro
        
        #Nodo a la izquierda
        #Las variables x,y,z reemplazan a las variables n,p,x del código original
        #Las variables i,j reemplazan a la variables s,u del código original
        if (nodo_Actual.nodoDerecha is None):
            lineas, x, y, z = self._printTree(nodo_Actual.nodoIzquierda)
            i = '%s' % nodo_Actual.valor
            j = len(i)
            primeraLinea = (z + 1) * ' ' + (x - z - 1) * '_' + i
            segundaLinea = z * ' ' + '/' + (x - z - 1 + j) * ' '
            desplazoLinea = [linea + j * ' ' for linea in lineas]
            return [primeraLinea, segundaLinea] + desplazoLinea, x + j, y + 2, x + j // 2

        #Nodo a la derecha 
        #Las variables x,y,z reemplazan a las variables n,p,x del código original
        #Las variables i,j reemplazan a la variables s,u del código original
        if (nodo_Actual.nodoIzquierda is None):
            lineas, x, y, z =  self._printTree(nodo_Actual.nodoDerecha)
            i = '%s' % nodo_Actual.valor
            j = len(i)
            primeraLinea = i + z * '_' + (x - z) * ' '
            segundaLinea = (j + z) * ' ' + '\\' + (x - z - 1) * ' '
            desplazoLinea = [j * ' ' + linea for linea in lineas]
            return [primeraLinea, segundaLinea] + desplazoLinea, x + j, y + 2, j // 2

        #Nodos en ambos extremos (Izq. y Der.) 
        #Las variables x,y,z reemplazan a las variables n,p,x del código original
        #Las varaibles a,b,c reemplazan a las variables m,q,y del código original 
        #Las variables i,j reemplazan a las variables s,u del código original
        #Las variables q,r reemplazan a las variables a,b del código original
        izquierda, x, y, z =  self._printTree(nodo_Actual.nodoIzquierda)
        derecha, a, b, c =  self._printTree(nodo_Actual.nodoDerecha)
        i = '%s' % nodo_Actual.valor
        j = len(i)
        primeraLinea = (z + 1) * ' ' + (x - z- 1) * '_' + i + c * '_' + (a - c) * ' '
        segundaLinea = z * ' ' + '/' + (x - z - 1 + j + c) * ' ' + '\\' + (a - c - 1) * ' '
        if (y < b):
            izquierda += [x * ' '] * (b - y)
        elif (b < y):
            derecha += [a * ' '] * (y - b)

        lineasComprimidas = zip(izquierda, derecha)
        lineas = [primeraLinea, segundaLinea] + [q + j * ' ' + r for q, r in lineasComprimidas]
        return lineas, x + a + j, max(y, b) + 2, x + j // 2

#Se salen de las clases y se crean funciones con las que se podrán ejecutar el programa
def userInput():
    print('''
    ----------------------------------------------
    IMPLEMENTACIÓN DE BINARY TREE:
        1. Probar Binary Tree
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

def creacionLista(archivo):
    lectura = open(archivo, 'r')
    contenido = lectura.read()
    contenido = contenido.replace("{","")
    contenido = contenido.replace("\n","")
    contenido = contenido.replace("}","")
    lista=contenido.split(",")
    lista=list(map(int,lista))
    return lista

def binaryTree(inputList):
    arbolBinario = BinaryTree()

    for valor in inputList:
        arbolBinario.agregarNodo(valor)

    arbolBinario.printTree()

def main():
    opcion = userInput()
    while opcion != 0:
        if opcion == 1:
            archivo = input("Escriba el nombre del archivo con extensión .txt: ")
            lista = creacionLista(archivo)
            binaryTree(lista)
            opcion = userInput()
        elif opcion == 2:
            autores()
            opcion = userInput()
        else: 
            print("Opción no disponible!")
            opcion = userInput()
  
main()


        


