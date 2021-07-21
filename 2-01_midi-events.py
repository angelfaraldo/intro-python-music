"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra

"nombre-del-archivo"
contenidos:
"""

import mido
import time

# the following line checks that there are some ports to send midi to
print(mido.get_output_names())
out_port = mido.open_output()  # opens the 1st port per default

# this would open other ports if available
out_port = mido.open_output(mido.get_output_names()[0])

# Basic Operation
# ===============

# define a midi message:
msg = mido.Message('note_on', channel=0, note=62, velocity=127)

# and then send it out via the selected port:
out_port.send(msg)

# the time object pauses the programme execution for the specified time
# IN SECONDS!
time.sleep(1)

# this is a note off message:
msg = mido.Message('note_off', note=62)
out_port.send(msg)


# podemos abreviar las dos lineas anteriores en una sola
out_port.send(mido.Message('note_on', note=48))
time.sleep(0.5)
out_port.send(mido.Message('note_on', note=55))
time.sleep(0.5)
out_port.send(mido.Message('note_on', note=64))
time.sleep(0.5)
out_port.send(mido.Message('note_on', note=72))

# y mandar valores de control
# en especial... hay uno muy interesante que es el llamado "panic" button.
# lo que hace es mandar un mensaje de note_off a todas las notas
# es el control número 123, al que hay que mandarle un valor de 0:
x
# otro elemento interesante es cambiar los "instrumentos" del sintetizador.
# en el standard general midi, se definió una "orquesta" de instrumentos,
# cada uno con su número de programa (mirad la lista adjunta.
out_port.send(mido.Message('program_change', program=40))

# en el protocolo MIDI inicial también se definió que habría 16 canales. En
# usos modernos, la asignación de canal es prácticamente arbitraria,
# sin embargo en sintetizadores con el protocolo GM (General MIDI), había un
# canal reservado a sonidos de percusión: el canal 10, aunque en mido es el
# 9, pues se empieza a contar desde 0.
out_port.send(mido.Message('note_on', channel=9, note=50))
time.sleep(0.1)
out_port.send(mido.Message('note_off', channel=9, note=50))


# It can be useful to introduce the notion of function in order to iterate
# jugar con random, y con random.choice.

# TODO: Hacer un pequeño ejercicio introductorio en compensación por la falta
#  del ejercicio 1. Es decir. Transcribir una pequeña melodía midi (1 o dos
#  compases)