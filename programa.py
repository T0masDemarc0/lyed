estudiantes = []
ingresos_validos = 0
ingresos_invalidos = 0
archivo_de_estudiantes = open('/home/willy/Dropbox/ISPI-4038/TSenDS/LyEEDD/2022/listado_estudiantil.txt', 'w')

while True:
    estudiante = input("Ingrese el apellido y nombre del estudiante: ").strip().upper()
    if not estudiante:
        break
    
    ok = True
    
    #validaciones varias
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

estudiantes.sort()
for alumno in estudiantes:
    print(alumno)
    archivo_de_estudiantes.write(alumno + '\n')

archivo_de_estudiantes.close()