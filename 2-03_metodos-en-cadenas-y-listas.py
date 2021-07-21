"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra

"nombre-del-archivo"
contenidos: manipulación de cadenas
"""

# En este programa vamos a repasar algunas nociones básicas de teoría de la música.
# En particular, sobre las notas musicales y sus nombres
# Además, veremos cómo realizar manipulaciones sencillas en cadenas.

notas_musicales = "do re mi fa sol la si"
musical_notes = "c d e f g a b"

# devuelve todas las letras en mayúsculas
notas_musicales.upper()
# 'DO RE MI FA SOL LA SI'

# devuelve todas las letras en minúsculas
notas_musicales.lower()
# 'do re mi fa sol la si'

# Mayúscula la primera letra, seguida de minúsculas
notas_musicales.capitalize()
# 'Do re mi fa sol la si'

# capitaliza la primera letra de cada 'palabra', es decir, después de cada espacio.
notas_musicales.title()
# 'Do Re Mi Fa Sol La Si'

# cuenta el número de ocurrencias de un carácter o secuencia de caracteres
notas_musicales.count("do")
# 1

notas_musicales.count("l")
# 2

notas_musicales.count(" ")
# 6

# devuelve el índice de la primera ocurrencia de la sub-cadena introducida
notas_musicales.find("mi")
# 6

notas_musicales.find("l")
# 14

# cuenta todos los caracteres de la cadena, no las notas por separado
# en este caso, si quisiéramos saber cuantas "notas" diferentes tenemos, tendríamos que usar otro método.
len(notas_musicales)
# 21

# reemplaza
notas_musicales.replace("do", "ut")
# 'ut re mi fa sol la si'

# crea una lista partiendo la cadena en subcadenas
notas_musicales.split()
# ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

# de hecho, este último método crea un nuevo tipo, "lista" que es de gran
# utilidad.
list_notas = notas_musicales.split()

# accede a la ayuda de los tipos LISTA para ver qué métodos crees que podrían
# ser útiles para manipular material musical