import ast

# condicionales

datosIngresados = input("digita operacion a realizar ej: 2+2 ")

if datosIngresados.find('+')>0: 
            datos= datosIngresados.split('+')
            print(str(datos[0])+'+'+str(datos[1]) +' = ',str(ast.literal_eval(datos[0])+ast.literal_eval(datos[1])))
if datosIngresados.find('-')>0: 
            datos= datosIngresados.split('-')
            print(str(datos[0])+'-'+str(datos[1]) +' = ',str(ast.literal_eval(datos[0])-ast.literal_eval(datos[1])))
if datosIngresados.find('*')>0: 
            datos= datosIngresados.split('*')
            print(str(datos[0])+'*'+str(datos[1]) +' = ',str(ast.literal_eval(datos[0])*ast.literal_eval(datos[1])))
if datosIngresados.find('/')>0: 
            datos= datosIngresados.split('/')
            print(str(datos[0])+'/'+str(datos[1]) +' = ',str(ast.literal_eval(datos[0])/ast.literal_eval(datos[1])))

