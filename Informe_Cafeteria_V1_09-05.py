with open("ventas.txt", "r") as archivo:
    # Leemos el contenido del archivo y lo dividimos por líneas
    lineas = archivo.read().splitlines()

print(lineas)

"""ANALISIS DE VENTA DE LA CAFETERIA
1) TOTAL DE VENTAS DE CADA PRODUCTO - CHECK
2) PROMEDIO VENTAS DIARIAS - CHECK
3) IMPRIMIR ESOS RESULTADOS - CHECK

2GENERACION INFORME VENTA
1)ventas cada producto por dia
2)total ventas x dia
"""
A="pan ciabatta"
A_precio=2000
lun_A=50
mar_A=30
mier_A=20
jue_A=10

total_ventas_semana_A= (lun_A+mar_A+mier_A+jue_A)*A_precio
total_ventas_LUN_A= lun_A*A_precio
total_ventas_MAR_A= mar_A*A_precio
total_ventas_MIER_A= mier_A*A_precio
total_ventas_JUE_A= jue_A*A_precio


B="pie de limon"
B_precio=3500
lun_B=40
mar_B=25
mier_B=15
jue_B=8

total_ventas_semana_B= (lun_B+mar_B+mier_B+jue_B)*B_precio
total_ventas_LUN_B= lun_B*B_precio
total_ventas_MAR_B= mar_B*B_precio
total_ventas_MIER_B= mier_B*B_precio
total_ventas_JUE_B= jue_B*B_precio


C="café"
C_precio=2200
lun_C=60
mar_C=35
mier_C=25
jue_C=12
total_ventas_semana_C= (lun_C+mar_C+mier_C+jue_C)*C_precio
total_ventas_LUN_C= lun_C*C_precio
total_ventas_MAR_C= mar_C*C_precio
total_ventas_MIER_C= mier_C*C_precio
total_ventas_JUE_C= jue_C*C_precio

D="té"
D_precio=1600
lun_D=45
mar_D=28
mier_D=18
jue_D=9
total_ventas_semana_D= (lun_D+mar_D+mier_D+jue_D)*D_precio
total_ventas_LUN_D= lun_D*D_precio
total_ventas_MAR_D= mar_D*D_precio
total_ventas_MIER_D= mier_D*D_precio
total_ventas_JUE_D= jue_D*D_precio

E="alfajor"
E_precio=1000
lun_E=55
mar_E=32
mier_E=22
jue_E=11
total_ventas_semana_E= (lun_E+mar_E+mier_E+jue_E)*E_precio
total_ventas_LUN_E= lun_E*E_precio
total_ventas_MAR_E= mar_E*E_precio
total_ventas_MIER_E= mier_E*E_precio
total_ventas_JUE_E= jue_E*E_precio


promedio_ventasTotales_lun=(total_ventas_LUN_A+total_ventas_LUN_B+total_ventas_LUN_C+total_ventas_LUN_D+total_ventas_LUN_E)/5

promedio_ventasTotales_mar=(total_ventas_MAR_A+total_ventas_MAR_B+total_ventas_MAR_C+total_ventas_MAR_D+total_ventas_MAR_E)/5

promedio_ventasTotales_mier=(total_ventas_MIER_A+total_ventas_MIER_B+total_ventas_MIER_C+total_ventas_MIER_D+total_ventas_MIER_E)/5

promedio_ventasTotales_juev=(total_ventas_JUE_A+total_ventas_JUE_B+total_ventas_JUE_C+total_ventas_JUE_D+total_ventas_JUE_E)/5

venta_general_lunes=total_ventas_LUN_A+total_ventas_LUN_B+total_ventas_LUN_C+total_ventas_LUN_D+total_ventas_LUN_E
venta_general_martes=total_ventas_MAR_A+total_ventas_MAR_B+total_ventas_MAR_C+total_ventas_MAR_D+total_ventas_MAR_E
venta_general_miercoles=total_ventas_MIER_A+total_ventas_MIER_B+total_ventas_MIER_C+total_ventas_MIER_D+total_ventas_MIER_E
venta_general_jueves=total_ventas_JUE_A+total_ventas_JUE_B+total_ventas_JUE_C+total_ventas_JUE_D+total_ventas_JUE_E

with open("informe_ventas.txt", "w") as informe:
    # Escribimos el encabezado del informe
    informe.write(f"Informe de Ventas - Cafetería de Grano // Génesis Montero y Natalia Paredes\n\nANÁLISIS DE VENTA DE LA CAFETERÍA\n\n1) TOTAL DE VENTAS SEMANAL (Lunes-Jueves) DE CADA PRODUCTO:\nPan de ciabatta: ${total_ventas_semana_A}\nPie de limón: ${total_ventas_semana_B}\nCafé: ${total_ventas_semana_C}\nTé: ${total_ventas_semana_D}\nAlfajor: ${total_ventas_semana_E}\n\n2) PROMEDIO VENTAS DIARIAS:\nLunes: ${promedio_ventasTotales_lun}\nMartes: ${promedio_ventasTotales_mar}\nMiércoles: ${promedio_ventasTotales_mier}\nJueves: ${promedio_ventasTotales_juev}\n\nINFORME VENTA\nVENTA DE CADA PRODUCTO POR DÍA:\nCiabatta:\n  -Lunes: ${total_ventas_LUN_A}\n  -Martes: ${total_ventas_MAR_A}\n  -Miércoles: ${total_ventas_MIER_A}\n  -Jueves: ${total_ventas_JUE_A}\nPie de Limón:\n  -Lunes: ${total_ventas_LUN_B}\n  -Martes: ${total_ventas_MAR_B}\n  -Miércoles: ${total_ventas_MIER_B}\n  -Jueves: ${total_ventas_JUE_B}\nCafé:\n  -Lunes: ${total_ventas_LUN_C}\n  -Martes: ${total_ventas_MAR_C}\n  -Miércoles: ${total_ventas_MIER_C}\n  -Jueves: ${total_ventas_JUE_C}\nTé:\n  -Lunes: ${total_ventas_LUN_D}\n  -Martes: ${total_ventas_MAR_D}\n  -Miércoles: ${total_ventas_MIER_D}\n  -Jueves: ${total_ventas_JUE_D}\nAlfajor:\n  -Lunes: ${total_ventas_LUN_E}\n  -Martes: ${total_ventas_MAR_E}\n  -Miércoles: ${total_ventas_MIER_E}\n  -Jueves: ${total_ventas_JUE_E}\n\nTOTAL VENTAS POR DÍA:\nLunes: ${venta_general_lunes}\nMartes: ${venta_general_martes}\nMiércoles: ${venta_general_miercoles}\nJueves: ${venta_general_jueves}")