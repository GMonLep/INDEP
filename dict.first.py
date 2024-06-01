#Estos son simplemente una guia para saber que estamos asignando.
A="pan ciabatta"
A_precio=2000
lun_A=50
mar_A=30
mier_A=20
jue_A=10


"""The dictionary is made up of two parts: keys and values.
Keys must be made up of only one element.
Values can be of any type, including list, tuple, integer, and so on."""
#Se le asigna un valor a cada palabra puesta, en este caso cada dia tiene su valor 
pan_ciabatta={50:'Lunes','Martes':30,'Miércoles':20,'Jueves':10};

print(pan_ciabatta['Martes']); #--> se le puede pedir imprimir el valor mediante la llamada de su "Nombre" asignado
print(pan_ciabatta[50])
print()
print("Ventas semanales Pan Ciabatta", list(pan_ciabatta.items()));
print()
print("Ventillas del pancillo:" + str(pan_ciabatta))
print()
print(pan_ciabatta)



with open("prueba_dict.txt", "w") as prueba:
    prueba.write("Ventillas del pancillo juasjuas:" + str(pan_ciabatta))
