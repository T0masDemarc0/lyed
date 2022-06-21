nombre1 = []
nombre2 = []
nombre3 = []
nombre = input('ingrese su nombre:')
appelido = input('ingrese su apellido: ')
nombre1.append(nombre)
nombre1.append(appelido)
nombre =  input('ingrese otro nombre: ')
appelido = input('ingrese otro apellido: ')
nombre2.append(nombre)
nombre2.append(appelido)
nombre =  input('ingrese otro nombre: ')
appelido = input('ingrese otro apellido: ')
print(nombre1)
print(nombre2)
nombre3.append(nombre)
nombre3.append(appelido)
dni1 = float(input('ingrese el dni del primer nombre: '))
dni2 = float(input('ingrese el dni del segundo nombre: '))
dni3 = float(input('ingrese el dni del tercer nombre: '))
'''
variables = input('ingrese una clave: ')

print(lista_de_nombres[variables])
'''
lista_de_nombres = {dni1:nombre1,dni2:nombre2,dni3:nombre3}
print('Los alumnos ingresados son: ', lista_de_nombres)
