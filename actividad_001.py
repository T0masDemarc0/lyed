nombres_alumnos = []
nombre_apellido = input("ingrse un nombre y apellido: ")
if nombre_apellido.isnumeric() :
   print("no se permiten numeros")
   nombre_apellido = input("ingrse un nombre y apellido: ")
   nombres_alumnos.append(nombre_apellido.upper())
nombres_alumnos.append(nombre_apellido.upper())
alumnos_presentes = 1
   
while alumnos_presentes < 5 :
    if alumnos_presentes < 5 :
       nombre_apellido = input("ingrse un nombre y apellido: ")
       if nombre_apellido.isnumeric() :
          print("no se permiten numeros")
          nombre_apellido = input("ingrse un nombre y apellido: ")
          if not nombre_apellido  :
           print("estos alumnos estan presentes:", alumnos_presentes)
           nombres_alumnos.sort()
           for alumno in nombres_alumnos:
               print(alumno)
           break
          nombres_alumnos.append(nombre_apellido.upper())
       if not nombre_apellido :
           print("estos alumnos estan presentes:", alumnos_presentes)
           nombres_alumnos.sort()
           for alumno in nombres_alumnos:
               print(alumno)
           break
       nombres_alumnos.append(nombre_apellido.upper())
       alumnos_presentes += 1
       
   

print("estos alumnos estan presentes:", alumnos_presentes)
nombres_alumnos.sort()
for alumno in nombres_alumnos:
   print(alumno)

   continue