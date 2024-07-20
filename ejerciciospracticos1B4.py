'''Cree un programa que pida el nombre, el número de comisión, asignatura,
docente y si el usuario estuvo presente, luego que muestre los datos 
por consola con las leyendas pertinentes'''

nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
comision= input("Ingrese el numero de su comision: ")
asignatura= input("Ingrese la materia que esta cursando: ")
docente= input("Cual es el nombre de su docente?: ")
asistencia= input("El alumno estuvo presente?: ")
print("El alumno cuyo nombre es " , nombre , apellido , "de la comision " , comision , "de " , asignatura , "del profesor " , docente , asistencia , "asistio a clases")