archivo = open(input('ingrese un archivo: '), 'rt')
datos = archivo.read()
palabras = datos.split()
cantidad_de_letras = len(datos)-datos.count(" ")
parrafos = datos.split("\n")
cantidad_de_parrafos = 1
oraciones = datos.split(".")
cantidad_de_oraciones = 1

print('la cantidad de palabras son: ', len(palabras))
print("la cantidad de letras que tiene son: ", cantidad_de_letras )

palabra_mas_larga=0
parrafo_mas_largo_tamaño = 0
comprovador=0
palabra_mas_larga_tamanio=0
parrafo_mas_largo=0
cantidad_de_letras_en_oraciones = 0
oracion_mas_larga = 0
oracion_mas_larga_tamaño = 0
i=0
e=0
o=0

for e in range(len(oraciones)): 
    comprobador2 = len(oraciones[i])
    if comprobador2 > oracion_mas_larga_tamaño :
        oracion_mas_larga = oraciones[i]
        palabras_en_oraciones = oracion_mas_larga.split()
        oracion_mas_larga_tamaño = len(palabras_en_oraciones)
    if e: 
        cantidad_de_oraciones += 1
    e =+1

for o in range(len(parrafos)): 
    comprobador3 = len(parrafos[i])
    if comprobador3 > parrafo_mas_largo_tamaño :
        parrafo_mas_largo = parrafos[i]
        palabras_en_parrafos = parrafo_mas_largo.split(".")
        palabras_por_parrrafo = parrafo_mas_largo.split()
        parrafo_mas_largo_tamaño = len(palabras_en_parrafos)
        palabras_por_parrafos_mas = len(palabras_por_parrrafo)
    if o: 
        cantidad_de_parrafos += 1
    o =+1

for i in range(len(palabras)) :      

    comprobador = len(palabras[i])          
  
    if comprobador > palabra_mas_larga_tamanio : 
        palabra_mas_larga= palabras[i]                      
        palabra_mas_larga_tamanio=len(palabra_mas_larga)

    i +=1

print("la palabra mas larga es: ", palabra_mas_larga)
print(f"tiene {palabra_mas_larga_tamanio} letras")
print(f"el documento tiene {cantidad_de_oraciones} oraciones")
print("la oracion mas grande es:", oracion_mas_larga)
print(f"la oracion consiste de  {oracion_mas_larga_tamaño} palabras ")
print(f"el documento tiene {cantidad_de_parrafos} parrafos")    
print("el parrafo mas grande es: ",parrafo_mas_largo)
print(f"tiene {parrafo_mas_largo_tamaño} oraciones dentro")
print(f"tiene {palabras_por_parrafos_mas} palabras dentro")

"C:/Users/usuario/Documents/tomy/instituto juan pablo 2/1er año/estructura y dato/visual studio code/cursado/texto.txt"
#C:/Users/usuario/Documents/tomy/instituto juan pablo 2/1er año/estructura y dato/visual studio code/cursado/prueba de textpo.txt