"""Hacer dos funciones 1  solicitando mis datos personales
, definir 2 variables numericas que sean de parametros de entrada de otra funcion que realice
las 4 operaciones aritmeticas +-*/ haciendo uso de los operadores logicos == < >  != 
retornar e invocar ambas funciones"""
"""Este es un juego entre la maquina y quien ejecuta el codigo
primero pide datos de la persona
segundo pide un numero
tercero realiza una operacion matematica dependiendo del numero ingresado
cuarto depende si ingreso numero , retorna un numero  y le manda un mensaje
cuarto si no ingreso numero , retorna mensaje
"""
#declarando variables principales
datos_solicitados = ["Nombre", "Apellido","Edad","Direccion"]
datos_respuesta = []
numero_solicitado = 0
numero_respuesta = []
juego = "Adivina que operación matematica +,-,* o / realice?"
solicita_operacion = ""

def solicita_datos_persona(array_datos):
    print('Dime tu: ')
    for i in array_datos:
        #datos_respuesta.append(input(array_datos[i]))
        datos_respuesta.append(input(i))
        #print()
    return datos_respuesta

def juego_matematico(numero):
    #if type(numero) == 'int' and numero >= 0: #tambien puede ser otro tipo de numero ideal es preguntar esnumero()
    if int(numero): #tambien puede ser otro tipo de numero ideal es preguntar esnumero()
        if numero > 100:
            numero_respuesta.append(numero - 75)
            numero_respuesta.append("Resta")
        elif numero > 75:
            numero_respuesta.append(numero + 3333)
            numero_respuesta.append("Suma")
        elif numero > 50:
            numero_respuesta.append(numero / 5)
            numero_respuesta.append("Division")
        elif numero >25:
            numero_respuesta.append(numero * 3)
            numero_respuesta.append("Multiplicación")
        else:
            numero_respuesta.append(numero)
            numero_respuesta.append("Ninguna")
    else:
        print("No ingresaste un numero")    
        numero_respuesta.append("")
        #break()

#inicia ejecucion
print("Hola, ¿Quién eres?")
solicita_datos_persona(datos_solicitados)
print(f'Tu datos son : {datos_respuesta} ') #imprime todos los datos ingresados
numero_solicitado = input("Juega conmigo, Escribe un número mayor a 0 : ")
#como controlo el error si escribe una letra
if int(numero_solicitado):
    juego_matematico(int(numero_solicitado))
    print(f' {datos_respuesta[0]} ingresaste {numero_solicitado}')
    solicita_operacion = input(print (f' te retorno {numero_respuesta[0]} {juego}')) 
    #se puede hacer un if comparando lo que ingreso  y decirle si esta ok o no
    print (f'Ja Ja Te dejare con la duda. Chao {datos_respuesta[0]}')
else:
    print('No quieres jugar. Para la otra será.')