#Creamos la clase Nodo para almacenar los datos
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

#Creamos la clase ArbolBinario para almacenar los nodos, e implementamos varios métodos:
class ArbolBinario:
    #Método constructor para inicializar el árbol
    def __init__(self):
            self.raiz = None

    #Método para insertar nuevos nodos
    def Insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        
        # Si el árbol está vacío, el nuevo nodo será la raíz
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return
        
        # Si el árbol no está vacío, encontrar la posición adecuada para insertar el nuevo nodo
        nodo_actual = self.raiz
        while True:
            if valor < nodo_actual.valor:
                if nodo_actual.izquierda is None:
                    nodo_actual.izquierda = nuevo_nodo
                    return
                nodo_actual = nodo_actual.izquierda
            else:
                if nodo_actual.derecha is None:
                    nodo_actual.derecha = nuevo_nodo
                    return
                nodo_actual = nodo_actual.derecha
    
    #Recorremos el árbol hasta encontar el valor deseado
    def BuscarNodo(self, valor):
        nodo_actual = self.raiz
        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                return True
            elif valor < nodo_actual.valor:
                nodo_actual_padre = nodo_actual
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual_padre = nodo_actual
                nodo_actual = nodo_actual.derecha
        return False
    
    #Recorremos el árbol para encontar el nodo deseado, lo eliminamos y reorganizamos el árbol
    def EliminarNodo(self, valor):
        nodo_actual = self.raiz
        nodo_a_eliminar_padre = None
        encontrado = False
        while nodo_actual and not encontrado:
            if valor == nodo_actual.valor:
                encontrado = True
            elif valor < nodo_actual.valor:
                nodo_a_eliminar_padre = nodo_actual
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_a_eliminar_padre = nodo_actual
                nodo_actual = nodo_actual.derecha
        if not encontrado:
            return "El valor a eliminar no se encuentra en el árbol"
        if nodo_actual.izquierda is None and nodo_actual.derecha is None:
            if nodo_actual.valor < nodo_a_eliminar_padre.valor:
                nodo_a_eliminar_padre.izquierda = None
            else:
                nodo_a_eliminar_padre.derecha = None
        elif nodo_actual.izquierda is None:
            if nodo_actual.valor < nodo_a_eliminar_padre.valor:
                nodo_a_eliminar_padre.izquierda = nodo_actual.derecha
            else:
                nodo_a_eliminar_padre.derecha = nodo_actual.derecha
        elif nodo_actual.derecha is None:
            if nodo_actual.valor < nodo_a_eliminar_padre.valor:
                nodo_a_eliminar_padre.izquierda = nodo_actual.izquierda
            else:
                nodo_a_eliminar_padre.derecha = nodo_actual.izquierda
        else:
            padre_reemplazo = nodo_actual
            reemplazo = nodo_actual.izquierda
            while reemplazo.derecha:
                padre_reemplazo = reemplazo
                reemplazo = reemplazo.derecha
            nodo_actual.valor = reemplazo.valor
            if reemplazo.izquierda:
                if padre_reemplazo.valor > reemplazo.valor:
                    padre_reemplazo.izquierda = reemplazo.izquierda
                else:
                    padre_reemplazo.derecha = reemplazo.izquierda
            else:
                if padre_reemplazo.valor > reemplazo.valor:
                    padre_reemplazo.izquierda = None
                else:
                    padre_reemplazo.derecha = None

    #Utilizamos recursividad para recorrer el árbol e ir imprimiéndolo
    def mostrar_arbol_inorden(self, nodo):
        if nodo:
            self.mostrar_arbol_inorden(nodo.izquierda)
            print(nodo.valor)
            self.mostrar_arbol_inorden(nodo.derecha)

    #Imprimimos el árbol pero diferenciando entre hijos
    def imprimir_arbol(self, nodo):
        cadena = str(nodo.valor)
        
        # Determina si el nodo actual tiene hijos
        if nodo.izquierda is not None or nodo.derecha is not None:
            cadena += '('
            if nodo.izquierda is not None:
                cadena += self.imprimir_arbol(nodo.izquierda)
            
            # Agrega una coma solo si el nodo tiene ambos hijos
            if nodo.izquierda is not None and nodo.derecha is not None:
                cadena += ','
            
            if nodo.derecha is not None:
                cadena += self.imprimir_arbol(nodo.derecha)
            
            cadena += ')'
        
        return cadena

#Insertamos unos cuantos nodos
def insertarinicio(arbol):
    arbol.Insertar(int(5))
    arbol.Insertar(int(4))
    arbol.Insertar(int(9))
    arbol.Insertar(int(3))
    arbol.Insertar(int(7))
    arbol.Insertar(int(2))
    arbol.Insertar(int(8))
    arbol.Insertar(int(1))
    arbol.Insertar(int(6))
    arbol.Insertar(int(0))
    return arbol


#Inicio del programa
nuevoarbol = ArbolBinario()
nuevoarbol = insertarinicio(nuevoarbol)
exit = False
#Menú para seleccionar opciones
while(exit!=True):
    print("------------------------------------")
    print("---------Menú-recursividad----------")
    print("------------------------------------")
    print("\n1- Insertar nodo")
    print("2- Buscar nodo")
    print("3- Eliminar nodo")
    print("4- Mostrar árbol")
    print("5- Mostrar árbol diferenciando hijos")
    print("6- Vaciar árbol")
    print("7- Salir.")
    opcion=int(input("Por favor, introduzca la opción deseada: "))

    if(opcion==1):
        nuevonodo=int(input("Qué valor desea que tenga el nuevo nodo?: "))
        nuevoarbol.Insertar(nuevonodo)
    elif(opcion==2):
        nodobuscado=int(input("Qué nodo desea buscar?: "))
        if(nuevoarbol.BuscarNodo(nodobuscado)==True):
            print("El nodo buscado existe")
        else:
            print("El nodo buscado no existe")
    elif(opcion==3):
        nodobuscado=int(input("Qué nodo desea eliminar?: "))
        nuevoarbol.EliminarNodo(nodobuscado)
    elif(opcion==4):
        print(nuevoarbol.mostrar_arbol_inorden(nuevoarbol.raiz))
    elif(opcion==5):
        print(nuevoarbol.imprimir_arbol(nuevoarbol.raiz))
    elif(opcion==6):
        nuevoarbol= ArbolBinario()
    elif(opcion==7):
        exit=True
    else: 
        print("Introduzca una opción válida.")