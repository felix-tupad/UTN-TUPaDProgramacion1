#1)
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


# Defino la variable edad y pido al usuario que ingrese su edad
edad = int(input("Ingrese su edad: ")) 
# Si la edad es mayor a 18, muestro el mensaje: Es mayor de edad
if edad > 18:                        
    print("Es mayor de edad.")        











#2)
# Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.


# Defino la variable nota y pido al usuario que ingrese su nota
nota = float(input("Ingrese su nota: ")) 
# Si la nota es mayor o igual a 6, mostrar el mensaje: Aprobado
if nota >= 6:                         
    print("Aprobado")
# En cualquier otro caso, mostrar el mensaje: Desaprobado
else:
    print("Desaprobado")










#3)
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.


# Defino la variable numero y pido al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
# Si el número es par, mostrar el mensaje: Ha ingresado un número par
if numero % 2 == 0:
    print("Ha ingresado un número par")
# En cualquier otro caso, mostrar el mensaje: Por favor, ingrese un número par
else:
    print("Por favor, ingrese un número par")









#4)
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.


# Defino la variable edad y pido al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))
# Si la edad es menor a 12, mostrar el mensaje: Usted es un/a niño/a
if edad < 12:
    print("Usted es un/a niño/a.")
# Si la edad es mayor o igual a 12 y menor a 18, mostrar el mensaje: Usted es un/a adolescente
elif edad >= 12 and edad < 18:
    print("Usted es un/a adolescente.")
# Si la edad es mayor o igual a 18 y menor a 30, mostrar el mensaje: Usted es un/a adulto/a joven
elif edad >= 18 and edad < 30:
    print("Usted es un/a adulto/a joven.")
# En cualquier otro caso, mostrar el mensaje: Usted es un/a adulto/a
else:
    print("Usted es un/a adulto/a.")











#5)
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.


# Defino la variable contrasenia y pido al usuario que ingrese una contraseña
contrasenia = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
# Defino la variable longitud que almacena la cantidad de caracteres de la contraseña a traves de la función len()
longitud = len(contrasenia)
# Si la longitud de la contraseña es mayor o igual a 8 y menor o igual a 14, mostrar el mensaje: Ha ingresado una contraseña correcta
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
# En cualquier otro caso, mostrar el mensaje: Por favor, ingrese una contraseña de entre 8 y 14 caracteres
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")












#6)
# El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. 
# Un ejemplo de su uso es el siguiente: 
# from statistics import mode, median, mean 
# mi_lista = [1,2,5,5,3] 
# mean(mi_lista) 
# En la documentación oficial se puede encontrar más información sobre este paquete:
#  https://docs.python.org/es/3.8/library/statistics.html. 
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir 
# la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.

# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar 
# si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma: 
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.


# Importo el módulo random para generar números aleatorios.
import random
# Importo las funciones mode, median y mean del módulo statistics para calcular la moda, mediana y media.
from statistics import mode, median, mean
# Defino la lista numeros_aleatorios con 50 números aleatorios entre 1 y 100.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Calculo la moda, mediana y media de la lista numeros_aleatorios.
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")
# Si la media es mayor que la mediana y la mediana es mayor que la moda, imprimir: Sesgo positivo o a la derecha.
if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
# Si la media es menor que la mediana y la mediana es menor que la moda, imprimir: Sesgo negativo o a la izquierda.
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
# Si la media, mediana y moda son iguales, imprimir: Sin sesgo.
elif media == mediana == moda:
    print("Sin sesgo")
# En cualquier otro caso, imprimir: No se puede determinar el sesgo con los valores obtenidos.
else:
    print("No se puede determinar el sesgo con los valores obtenidos")










#7)
# Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.


# Defino la variable frase y pido al usuario que ingrese una frase o palabra.
frase = input("Ingrese una frase o palabra: ")
# Si la última letra de la frase es una vocal (mayúscula o minúscula).
if frase[-1].lower() in 'aeiou':
    frase = frase + '!'   # Añade un signo de exclamación al final de la frase en caso de cumplirse la condición.
# Muestra la variable frase por pantalla.
print(frase)              











#8)
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.


# Defino la variable nombre y pido al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")
# Defino la variable opcion y pido al usuario que ingrese una opción (1, 2 o 3)
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: ")
# Si la opción es 1 muestro la variable nombre en mayúsculas usando la función upper()
if opcion == '1':
    print(nombre.upper())
# Si la opción es 2 muestro la variable nombre en minúsculas usando la función lower()
elif opcion == '2':
    print(nombre.lower())
# Si la opción es 3 muestro la variable nombre con la primera letra en mayúscula usando la función title()
elif opcion == '3':
    print(nombre.title())
# En cualquier otro caso, muestro el mensaje: Opción no válida.
else:
    print("Opción no válida.")









#9)
# Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


# Defino la variable magnitud y pido al usuario que ingrese la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# si la magnitud es menor a 3 muestro el mensaje: Muy leve (imperceptible).
if magnitud < 3:
    print("Muy leve (imperceptible).")
# si la magnitud es mayor o igual a 3 y menor a 4 muestro el mensaje: Leve (ligeramente perceptible).
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
# si la magnitud es mayor o igual a 4 y menor a 5 muestro el mensaje: Moderado (sentido por personas, pero generalmente no causa daños).
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
# si la magnitud es mayor o igual a 5 y menor a 6 muestro el mensaje: Fuerte (puede causar daños en estructuras débiles).
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
# si la magnitud es mayor o igual a 6 y menor a 7 muestro el mensaje: Muy Fuerte (puede causar daños significativos).
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
# en cualquier otro caso muestro el mensaje: (magnitud mayor o igual a 7)
else:
    print("Extremo (puede causar graves daños a gran escala).")









#10)
# Utilizando la información aportada en la siguiente tabla sobre las estaciones del año Periodo del año.

# Periodo del año                                                     Hemisferio Norte          Hemisferio Sur
# Desde el 21 de diciembre hasta el 20 de marzo (incluidos)           Invierno                  Verano
# Desde el 21 de marzo hasta el 20 de junio (incluidos)               Primavera                 Otoño
# Desde el 21 de junio hasta el 20 de septiembre (incluidos)          Verano                    Invierno
# Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)      Otoño                     Primavera

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

#Defino la variable hemisferio y pido al usuario que ingrese en cuál hemisferio se encuentra (norte/sur).
#Uso .lower() para convertir la entrada a minúsculas y evitar errores de comparación.
hemisferio = input("Ingrese el hemisferio en el que se encuentra (norte/sur): ").lower()
#Defino la variable mes y pido al usuario que ingrese el mes del año como un número entero entre 1 y 12.
mes = int(input("Ingrese el mes (1-12): "))
#Defino la variable dia y pido al usuario que ingrese el día del mes como un número entero entre 1 y 31.
dia = int(input("Ingrese el día (1-31): "))
#Defino la variable estacion como una cadena vacía para almacenar la estación del año correspondiente.
estacion = ""
#Verifico que el hemisferio sea norte y que el mes y día estén en rangos válidos.
if (hemisferio == "norte") and (mes >= 1 and mes <= 12) and (dia >= 1 and dia <= 31): 
    #Verifico si el mes es marzo y el día es mayor o igual a 21, o si el mes es abril o mayo, o si el mes es junio y el día es menor o igual a 20.
    if (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20): #Uso "mes in [4, 5]" para verificar si el mes es abril o mayo.
        estacion = "primavera"
    #Verifico si el mes es junio y el día es mayor o igual a 21, o si el mes es julio o agosto, o si el mes es septiembre y el día es menor o igual a 20.
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20): #Uso "mes in [7, 8]" para verificar si el mes es julio o agosto.
        estacion = "verano"
    #Verifico si el mes es septiembre y el día es mayor o igual a 21, o si el mes es octubre o noviembre, o si el mes es diciembre y el día es menor o igual a 20.
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20): #Uso "mes in [10, 11]" para verificar si el mes es octubre o noviembre.
        estacion = "otoño"
    #Si ninguna de las condiciones anteriores se cumple, entonces la estación es invierno.
    else:
        estacion = "invierno"
#Verifico si el hemisferio es sur y que el mes y día estén en rangos válidos.
elif hemisferio == "sur" and (mes >= 1 and mes <= 12) and (dia >= 1 and dia <= 31):
    #Verifico si el mes es marzo y el día es mayor o igual a 21, o si el mes es abril o mayo, o si el mes es junio y el día es menor o igual a 20.
    if (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "otoño"
    #Verifico si el mes es junio y el día es mayor o igual a 21, o si el mes es julio o agosto, o si el mes es septiembre y el día es menor o igual a 20.
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "invierno"
    #Verifico si el mes es septiembre y el día es mayor o igual a 21, o si el mes es octubre o noviembre, o si el mes es diciembre y el día es menor o igual a 20.
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "primavera"
    #Si ninguna de las condiciones anteriores se cumple, entonces la estación es verano.
    else:
        estacion = "verano"
#Si el hemisferio no es ni norte ni sur y/o el mes y/o el día no están en rangos váñidos, muestro un mensaje de error.
else:
    print("Datos ingresados no válidos.")
#Si la estación no es una cadena vacía, imprimo la estación del año correspondiente.
if estacion:
    print(f"Usted se encuentra en {estacion}.")