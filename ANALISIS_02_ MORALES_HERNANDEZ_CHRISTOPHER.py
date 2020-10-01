# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:17:10 2020

@author: OMEN
"""
import csv

lista_datos = []
lista_rutas = []
total1=[]


with open("synergy_logistics_database.csv","r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
        lista_datos.append(linea)
        
def rutas(direccion):
    cont=0
    rutas_contadas = []
    conteo = []
    suma = 0
    corg = 0
    org = []
    index = []
    saldo = []
    total=[]
    
    lista_datos.pop(0)
    for ruta in lista_datos:
        if ruta[1] == direccion:
            suma = []
            ruta_actual = [ruta[2],ruta[3],ruta[4],ruta[6],ruta[8]]     
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[2],movimiento[3],movimiento[4],movimiento[6],movimiento[8]]:
                        cont+=1
                        suma.append(int(movimiento[9]))
                rutas_contadas.append(ruta_actual)
                conteo.append([[ruta[2],ruta[3]],ruta[4],ruta[6],ruta[8],cont,sum(suma)])
                cont=0

    conteo.sort(reverse = True, key = lambda x:x[0])
    
    cont = 0
    index = []
    for ruta in conteo:
        if ruta[0] not in index:
            org.append(ruta[0])
            index.append(ruta[0])
            
    cont=0
    index = []
    for r in org:
        corg+=1
        cont = 0 
        for p in conteo:
            if r == p[0]:
                cont = cont + p[5]
                formato_ideal = (p[0])   
        index.append([formato_ideal,cont])
    index.sort(reverse=True, key = lambda x:x[1])

    if direccion == "Imports":
        with open("RUTAS_I","w") as archivo:
            escritor = csv.writer(archivo, delimiter = ",")
            escritor.writerows(index)
    else:
        with open("RUTAS_E","w") as archivo:
            escritor = csv.writer(archivo, delimiter = ",")
            escritor.writerows(index)
    
    
    print("\n Las rutas con mayor ingresos son: ")
    
    for ru in range(10):
        print(index[ru])
        saldo.append(index[ru][1])
    
    for pi in lista_datos:
        if pi[1] == direccion:
            total.append(int(pi[9]))
    
    print("\n El numero de rutas son: ",corg)
    print("\n El top 5 de rutas con mas ingresos genera un tota de ingresos de: ",sum(saldo))
    print("\n Es equivalente a un porcentaje de: ",((sum(saldo)/sum(total))*100))
      
    return conteo  
        
op = int(input("Elige una opcion:\n 1.-Importaciones\n 2.-Exportaciones\n op ->"))

if op == 1:
    
    for pi in lista_datos:
        if pi[1] == "Imports":
            total1.append(int(pi[9]))
            
    print("\n Importaciones con un total de: ",sum(total1))
    
    lista_rutas = rutas("Imports")
    
    for pe in lista_rutas:
        print(pe)
    
elif op == 2:
    
    for pi in lista_datos:
        if pi[1] == "Exports":
            total1.append(int(pi[9]))
            
    print("Exportaciones con un total de: ",sum(total1))
    
    lista_rutas = rutas("Exports")
    
    for pe in lista_rutas:
        print(pe)

else:
    print("Ingresa otra opcion")
    