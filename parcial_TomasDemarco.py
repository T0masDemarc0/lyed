from pickle import TRUE
import random
archivo = open(input('ingrese un archivo: '), 'rt')
datos = archivo.read()
palabras = datos.split()
palabra_mas_larga_tamanio = 0
cantidad_de_palabras = len(palabras)
si = 1
no = 20
i = 0
e = 0
o = 0
tester = 0
suma_de_letras = 0
letras = []
letras_random = []
random_letras = []
tester2 = 0
random_letras_e =''

for i in range(len(palabras)) :      

    tester = len(palabras[i])          
  
    if tester > palabra_mas_larga_tamanio : 
        palabra_mas_larga= palabras[i]                      
        palabra_mas_larga_tamanio=len(palabra_mas_larga)

    i +=1   

for e in range(len(palabras)) : 
    cantidad_de_letras = len(palabras[e])
    letras.append(cantidad_de_letras)
    e +=1

for o in range(len(letras)) :
    
    if suma_de_letras == 0 :
        suma_de_letras = letras[o]
    else :
        suma_de_letras += letras[o]
    
    o +=1
    
promedio = suma_de_letras / cantidad_de_palabras

palabra_mas_larga_en_mayusculas = palabra_mas_larga.upper()

print("\nLa cantidad de palabras que tiene el archivo es", cantidad_de_palabras)
print(f"\nLa palabra mas larga es", palabra_mas_larga_en_mayusculas, 'y esta mide', palabra_mas_larga_tamanio)
print(f"\nEl promedio de letras es", "{0:.2f}".format(float(promedio)), "por palabra")

letras_pedidas = float(input("\nIngrese una cantidad de letras: "))
while TRUE :
    if letras_pedidas > 21 :
        print('\nNo hay palabras de ese tamaño')
        letras_pedidas = float(input("\nIngrese una cantidad, menor o igual a 21 ,de letras: "))
    if letras_pedidas <= 21 :
        break

for a in range(len(palabras)) :
    tester2 = len(palabras[a])
    if tester2 == letras_pedidas :
        letras_random.append(palabras[a])
    if letras_pedidas == 0 :
        break


while si < no :
    random_letras_e = random.choice(letras_random)
    random_letras_e = random_letras_e.upper()
    random_letras.append(random_letras_e)

    si += 1

print(f"\nAlgunas palabras con esa cantidad de letras son: {random_letras}")   