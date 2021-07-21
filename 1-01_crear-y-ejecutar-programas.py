"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra

"1-01_crear-y-ejecutar-programas"
contenidos: print(), comentarios, input(), variables, string concatenation
"""

# PRINT y CADENAS
print("hola, chicas y chicos!")
print("")
print('Estamos utilizando la función "print" para imprimir texto en la consola.')


# COMMENTS
# es bueno introducir comentarios para explicar vuestro código, documentar dudas, etc.
# el carácter "\n" es "newline", y crea una línea en blanco después de la cadena.
print("Espero que durante esta semana aprendáis cosas interesantes,\ny que os resulte entretenido.")


# INPUT
# aquí acabamos de concatenar dos strings ("cadenas", en castellano)
input("Hola, Cómo te llamas?")
print("Encantado")


# VARIABLES (almacenamiento)
# convenciones para llamar variables
mi_nombre = input("Hola, Cómo te llamas?")


# concatenación de cadenas
print("Mucho gusto, " + mi_nombre)


# tipos de data: int, float, strings, boolean
type(mi_nombre)

edad = 40
type(edad)

temperatura = 35.7
type(temperatura)

soltero = True
type(soltero)


# type casting
# nos sirve para convertir un tipo en otro
# esto es útil, por ejemplo para imprimir en la consola valores numéricos

edad = str(edad)
print("Hola, me llamo " + edad)

# o con una f-string
print("hola, me llamo {mi_nombre}, y tengo {edad} años.")
