lista_multiplicada = []
listado_numeros = []
numeros_escritos = 0

#pedido y sumado de numero

cantidad_de_numeros = int(input("cantidad de numeros a ingresar: "))
while cantidad_de_numeros < 0 :
        cantidad_de_numeros = int(input("ingrese un numero valido: "))

while cantidad_de_numeros > numeros_escritos:
    numero = input("ingrese un numero aleatorio: ")
    esnumero = numero.isdigit()
    numeros_escritos += 1
    if not(numero) :
        print('solo se permiten numeros')
        numeros_escritos -=1 
    if esnumero :
        numeros = float(numero)
        listado_numeros.append(numeros)
    if numeros_escritos >= cantidad_de_numeros :
        break
    if cantidad_de_numeros < 1 :
        print('ingrese un numero valido')
        cantidad_de_numeros = int(input("cantidad de numeros que desea ingresar: "))

#suma

suma_lista = sum(listado_numeros)
print('la lista sumada es: ', suma_lista)


#multiplicacion

largo = len(listado_numeros)

for i in range(largo):
    valor= float(listado_numeros[i]) 
    if i == 0 : 
        resultado = valor
    else:
        resultado *= valor


#mayor y menor

print(f'el mayor es {max(listado_numeros)}')
print(f'el menor es {min(listado_numeros)}')
print(' el total multiplicado es :' , resultado)
print('los numeros ingresados son: ', listado_numeros)  

''' 
una forma de sacar el mayor y el menor

for numero in listado_numeros :
    if mayor==NONE and menor==NONE : 
        menor = numero
        mayor = numero
    else:
        if numero<menor:
            menor = numero
        if numero > mayor :
            mayor = numero

print(f'El numero mayor es {mayor}')
print(f'El numero menor es {menor}')
'''