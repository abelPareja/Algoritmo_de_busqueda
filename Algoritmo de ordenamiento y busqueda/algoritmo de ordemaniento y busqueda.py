# -*- coding: utf-8 -*-
"""
Apellidos y Nombres: Pareja Ramos Abel 
"""

def ordenamiento(lista):
    longitud = len(lista)-1
    
    for i in range(0,longitud):
        print(f"pasada #{i + 1}")
        for j in range(0, longitud):
            print(f"comparacion: {lista[j]} > {lista[j + 1]} ")
            if lista[j] > lista[j+1]:
                print(f"intercambiar: {lista[j]} x {lista[j + 1]}")
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
        print(f"lista: {lista}")        
    return lista


cadena= [70,90,0,80,60,85]

print("antes de ordenar: ")
print(cadena)
print("despues de ordenar: ")
print(ordenamiento(cadena))