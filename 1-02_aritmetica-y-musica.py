"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra

"1-03_aritmetica-y-parametros-del-sonido"
contenidos: modo interactivo, operadores aritméticos, precedencia, frecuencia,
altura, octava, semitono, duración, intensidad, timbre
"""

# modo interactivo para usar python como una calculadora extendida!
# operadores aritméticos, suma, resta, multiplicación, división, exponentes, paréntesis

# parámetros del sonido: ALTURA, DURACIÓN, INTENSIDAD, TIMBRE

# ============================================================
# ALTURA
# frecuencia, altura, octava, semitono

# la nota de referencia es la llamada "La4" (o La5, dependiendo de la región).
# convencionalmente, es el resultado de una oscilación periódica a 440 Hz.
# es decir, 440 oscilaciones por segundo.
la = 440

# sine_tone es una conveniencia para reproducir tonos de manera sencilla
from sine_tone import *  # esto es un módulo de python. Más sobre esto en otra sesión.

sine_tone(la, 2)

# pero en gramática musical, hay muchos "la's" diferentes,
# con "alturas" más graves y más agudas, referenciadas por índices: la4, la5, etc.
la2 = 110
la3 = 220
la4 = 440
la5 = 880
la6 = 1760

# fijaros en las relaciones numéricas entre las notas. hay algún patrón reconocible?
# y escuchando las notas, os resulta más fácil percibir algún patrón? cómo lo explicaríais
sine_tone(la2)
sine_tone(la3)
sine_tone(la4)
sine_tone(la5)
sine_tone(la6)

# las relaciones consecutivas entre las notas del mismo nombre, se llaman "octavas"
# ¿sabéis por qué?
la4 = la
la5 = la * 2
la6 = la * 4  # o la5 * 2, si preferís

la3 = la / 2

# en programación, la multiplicación es una operación mucho más rápida que la división
# por esa razón, en casos donde sea razonable, es preferible multiplicar que dividir.
la2 = la * 0.25

# para calcular octavas desde una sola nota de referencia hemos de tener en cuenta que
# octavas sucesivas siempre responden a una relación de dobles o mitades con la octava anterior
# Esto quiere decir que nuestra percepción de las alturas musicales es LOGARÍTMICA
# pues escuchamos como equidistantes relaciones cuya distancia cambia de manera exponencial.

# dada una nota de referencia "la" a 440. Utilizando "potencias" cómo podríamos
# calcular de manera programática la frecuencia de todas las octavas superiores o inferiores?
# atención a la precedencia (orden de ejecución de los operadores matemáticos)
la4 = 440 * 2 ** 0
la5 = 440 * 2 ** 1
la6 = 440 * 2 ** 2
la3 = 440 * 2 ** -1
la2 = 440 * 2 ** -2

# esto funciona estupendamente en relación a la misma frecuencia de referencia, pero
# ¿Y SI QUISIÉRAMOS INTRODUCIR LOS DATOS DE UNA MANERA CONSISTENTE CON EL ÍNDICE DE CADA OCTAVA?

# observad la necesidad de incluir paréntesis para la prioridad del ejecución
la2 = 440 * 2 ** (2 - 4)
la4 = 440 * 2 ** (4 - 4)
la5 = 440 * 2 ** (5 - 4)

# para que resulte más fácil podemos utilizar variables en vez de números
# esto hace el código mucho más legible

frecuencia_de_referencia = 440
octava = 4

la4 = frecuencia_de_referencia * 2 ** (octava - 4)


# SEMITONOS
# en música occidental, la octava se divide en 12 partes perceptualmente equivalentes
# llamadas "semitonos". Es otro ejemplo de una división LOGARITMICA, ya que está directamente
# relacionada con la octava, que funciona en ratios de dobles.

# para calcular el ratio del semitono, calculamos la raíz 12 de 2... (dividimos logarítmicamente
# la octava en doce partes:
ratio_semitono = 1.059463094359295

# una vez tenemos este ratio, podemos conseguir todas las notas necesarias aplicando la transposición
# deseada, con operaciones aritméticas sencillas. La fórmula es la siguiente:

do4 = la4 * ratio_semitono ** -9
re4 = la4 * ratio_semitono ** -7
mi4 = la4 * ratio_semitono ** -5
fa4 = la4 * ratio_semitono ** -4
sol4 = la4 * ratio_semitono ** -2
la4 = la4
si4 = la4 * ratio_semitono ** 2
do5 = la4 * ratio_semitono ** 3

sine_tone(do4)
sine_tone(re4)
sine_tone(mi4)
sine_tone(fa4)
sine_tone(sol4)
sine_tone(la4)
sine_tone(si4)
sine_tone(do5)
