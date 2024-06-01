"""ANALISIS DE VENTA DE LA CAFETERIA
1) TOTAL DE VENTAS DE CADA PRODUCTO - CHECK
2) PROMEDIO VENTAS DIARIAS - CHECK
3) IMPRIMIR ESOS RESULTADOS - CHECK

2GENERACION INFORME VENTA
1)ventas cada producto por dia
2)total ventas x dia
----------------------------------------------------------------------

for key in pan_ciabatta:    
    pan_ciabatta[key]*=precio_pan_ciabatta   
    
    ---> this method only allows for the dictionary to be updated, meaning when you write the dictionary "pan_ciabatta" in the document, it will no longer show the original values and will ONLY show the values multiplied by precio_pan_ciabatta
    
-----------------------------------------------------------------------

what we want is to preserve the original dictionary, print it and only after that print a version with each value multiplied by precio_pan_ciabatta:

we first assign a name to the new variable
venta_dinero_pan_ciabatta = dict(zip(pan_ciabatta.keys(), map(lambda x: x*precio_pan_ciabatta, pan_ciabatta.values())));

"""
precio_pan_ciabatta=2000
pan_ciabatta=dict({'Lunes':50,'Martes':30,'Miércoles':20,'Jueves':10});

venta_diaria_pan_ciabatta = dict(zip(pan_ciabatta.keys(), map(lambda x: x*precio_pan_ciabatta, pan_ciabatta.values())));

venta_semanal_pan_ciabatta=(pan_ciabatta.get('Lunes')+pan_ciabatta.get('Martes')+pan_ciabatta.get('Miércoles')+pan_ciabatta.get('Jueves'))*precio_pan_ciabatta;



with open("probando_diccionario.txt", "w") as documento:
    documento.write("TOTAL VENTAS SEMANALES CADA PRODUCTO\n[Lunes-Jueves]\n\n");
    #str() is a built-in function in the Python programming language that is used to convert the specified value into a string datatype:
    documento.write(f"PAN CIABATTA\n")
    documento.write(f"Venta por unidad: {str(pan_ciabatta)}\n");
    documento.write(f"Dinero recaudado por día: {str(venta_diaria_pan_ciabatta)}");
    documento.write(f"Dinero total de la semana: {str(venta_semanal_pan_ciabatta)}");