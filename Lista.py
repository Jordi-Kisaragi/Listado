'''
Created on 30 nov. 2016
Programa que se utiliza para formar una lista para trabajar en el programa principal.
@author: usuario
'''
def Crear_lista(lista):
        '''Insertaremos 5 valores que utilizaremos posteriormente en una lista vacia para realizar el programa'''
        pregunta=input("Pon usted un valor: ") #Introduce cualquier valor aqui#
        lista.append(pregunta) #Almacena el valor en una lista#
        elemento=input("Si quiere otro valor, escribe si, sino, escribe no: ") #Ponga usted si o no para que se ejecute#
        while elemento=="Si" or elemento=="si": #Si usted escribe si, el programa continua. Cualquier otro valor hara que el programa pare#
            elementos=input("Introduce otro valor: ") #Introduce otro valor aqui#
            lista.append(elementos) #Almacena otro valor en la lista#
            print (lista) #Muestra los valores ingresados de la lista#
            elemento=input("Si quiere otro valor, escribe si, sino, escribe no: ")  #Ponga usted si o no para que se ejecute#
        return lista #devuelve el valor para que se ejecute el programa de nuevo#
    
def Separar_lista(lista):
    '''Ahora vamos a dividir la lista en paciente, fase y temperatura.
    
    '''
    Id_paciente=lista[0]
    Fase_ensayo=lista[1]
    Serie_temperatura=lista[2:]
    return Id_paciente,Fase_ensayo,Serie_temperatura

def flotante(lista):
    
    '''
    Aqui el programa hace colocar las temperaturas en un numero flotante,
    separando el numero en .0
    '''
    lista=[37.1,39.3,38.1]
    for n in range(2,len(lista)):
        lista[n]=float(lista[n])
    for n in range(3,len(lista)):
        lista[n]=float(lista[n])
    for n in range(4,len(lista)):
        lista[n]=float(lista[n])
        return lista
    
def ordenar(lista):
    '''
    Aqui ordenamos los elementos de la lista, referido a las temperaturas.
    '''
    lista=[37.1,39.3,38.1] 
    for indice1 in range(len(lista)):    
        for indice2 in range (indice1+1, len(lista)): 
            print(lista[indice1],lista[indice2])
            if lista[indice1]>lista[indice2]:             
                lista[indice1],lista[indice2]=lista[indice2],lista[indice1]
    print(lista)
    
if __name__ =="__main__":
    lista=[]
    print (Crear_lista(lista))
    Id_paciente,Fase_ensayo,Serie_temperatura=Separar_lista(lista)