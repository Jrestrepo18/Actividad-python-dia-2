numero=int(input("Ingrese un numero: "))
mi_lista=[1,2,3,4,5]
if numero in mi_lista:
    print("el numero esta en la lista.")
else:
    print("El numero no esta en la lista.")
print(mi_lista)

print(mi_lista[0])

mi_lista[3]=25
print(mi_lista[3])
print(mi_lista)

mi_lista.append(23)
print(mi_lista)
