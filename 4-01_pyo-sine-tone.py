"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra

"nombre-del-archivo"
contenidos:
"""


from pyo import *

# Creates and boots the server.
# The user should send the "start" command from the GUI.
s = Server().boot()
# Drops the gain by 20 dB.
s.amp = 0.01

# Creates a sine wave player.
# The out() method starts the processing
# and sends the signal to the output.
a = Sine(440).out()

# Opens the server graphical interface.
s.gui(locals())