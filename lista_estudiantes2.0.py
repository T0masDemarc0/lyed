#inicialización de variables
ruta_archivo = '/Users/usuario/Documents/tomy/instituto juan pablo 2/1er año/estructura y dato/visual studio code/cursado/listado_estudiantil.txt'
estudiantes_lectura = open(ruta_archivo, 'r')
ingresos_validos = 0
ingresos_invalidos = 0
estudiantes = [] 

#lectura secuencial del archivo y carga en lista estudiantes, quitandole el enter al final de cada uno
while True:
    estudiante = estudiantes_lectura.readline()
    if not estudiante:
        break
    estudiantes.append(estudiante[:-1])
estudiantes_lectura.close()

#nueva apertura del archivo, esta vez para escribirlo
estudiantes_escritura = open(ruta_archivo, 'w')

#ciclo para cargar por teclado de nuevos estudiantes
while True:
    estudiante = input("Ingrese el apellido y nombre del estudiante: ").strip().upper()
    if not estudiante:
        break
    
    #validaciones varias: solo texto, 2 o mas palabras y no repetido
    ok = True
    for caracter in estudiante:
        if caracter.isdigit():
            ok = False
            print('Solo se permiten letras')
            break
        
    if len(estudiante.split()) == 1:
        ok = False
        print('Debería ingresar Apellido y Nombre')

    if estudiante in estudiantes:
        ok = False
        print('El estudiante ya fue ingresado')        

    if ok == True:
        estudiantes.append(estudiante)
        ingresos_validos += 1
    else:
        ingresos_invalidos += 1

print("Ingresos inválidos:", ingresos_invalidos)
print("Estudiantes ingresados:", ingresos_validos)

#ordenamiento de la lista
estudiantes.sort()

#muestra en pantalla
for alumno in estudiantes:
    print(alumno)
  
#escribe cada elemento de la lista en archivo de texto, añadiendo un enter al final de c/u
for alumno in estudiantes:
    estudiantes_escritura.write(alumno + '\n')
estudiantes_escritura.close()