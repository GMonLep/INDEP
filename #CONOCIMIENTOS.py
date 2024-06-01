#CONOCIMIENTOS

nomcomp=input("Escriba su nombre y apellido por favor: ")
rut=input("Escriba su RUT con punto y dígito verificador: ")
correo=input("Escriba su correo: ")
celular=int(input("Escriba su número de teléfono: "))
oracion= (f"NOMBRE: {nomcomp}",f"RUT: {rut},"f"CORREO: {correo}",f"FONO: {celular}") #f"cadena texto {aqui_la_variable}"
separa="  "
JUANCHO = separa.join(oracion)

print(JUANCHO)
print('-'*6)
espacio='\n' #se salta hacia abajo
a=5
b=6
valorSinIVA=float(a*b) #float es para aceptar decimales
altura=float(input("Ingrese su altura (kg), si desea usar una coma, reemplacela por un punto: "))

#==: The 'equal to' operator.
#!=: The 'not equal to' operator.
#<: The 'less than' operator.
#>: The 'greater than' operator.
#<=: The 'less than or equal to' operator.
#>=: The 'greater than or equal to' operator.