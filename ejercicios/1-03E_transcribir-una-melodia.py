"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra

RETO - Día 1
======
TRANSCRIBE UNA MELODÍA SENCILLA EN FORMATO PARTITURA O MIDI A CÓDIGO DE PYTHON CON LOS MATERIALES VISTOS,
DE MODO QUE CUANDO EJECUTES EL PROGRAMA LA MELODÍA SUENE.

Hasta ahora hemos visto parámetros del sonido como la altura, el timbre o la duración. En este ejercicio
te pido además que incorpores la INTENSIDAD.

La intensidad es la fuerza o el volumen al cual un sonido es percibido. Hay muchas maneras de referirnos
al volumen según el contexto. Por ejemplo, en ingeniería de sonido se utiliza la medida relativa del "decibelio"
En música, se suelen utilizar escalas más subjetivas, como piano (suave), mezzopiano, mezzoforte, o forte.
En computación, el volumen o intensidad está ligado a un factor de escalado, típicamente una multiplicación
por un valor entre 0 (silencio) y 1 (máximo permitido). Podríamos establecer algunas correlaciones: Por ejemplo:

silencio = 0
piano = 0.05
mezzopiano = 0.05
mezzoforte = 0.1
forte = 0.2

La función sine tone, recibe como tercer argumento la INTENSIDAD, así, por ejemplo:

sine_tone(la4, negra, forte)

produciría una nota la4 a duración de negra en dinámica forte.

- Antes de nada, experimenta y encuentra una escala de intensidad que te parezca que tenga sentido
  entre estos cuatro valores. ¿son los valores equidistantes?
- Recuerda que los argumentos de sine_tone, son, en orden: ALTURA, DURACIÓN, INTENSIDAD
- Utiliza con todos los elementos usados hasta ahora: variables, strings, aritmética, etc.
- En programación, es muy habitual REUTILIZAR código, así que utiliza fragmentos de código vistos hasta ahora.
- Por ejemplo, además de la melodía, puedes introducir un tempo en bpm que se acomode con la melodía elegida.
- Cuando ejecutes el programa, la melodía transcrita ha de sonar por el altavoz de tu ordenador.

# BONUS: la música está llena no solo de sonidos, sino también de silencios, aunque aún no hemos visto un
modo apropiado de implementarlo. Con los elementos que hemos visto hasta ahora, ¿se te ocurre alguna manera
de introducir silencios en tu transcripción

"""
