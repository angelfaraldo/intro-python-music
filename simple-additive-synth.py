"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra
"""

from pyo import *

# Creates and boots the server.
# The user should send the "start" command from the GUI.
s = Server().boot()
# Drops the gain by 20 dB.
s.amp = 0.1

# Init Values
freq = 100
n_harmonics = 10


def aggregate_tones(fundamental=100, n_harmonics=10):
    return [fundamental * i for i in range(1, n_harmonics + 1)]


synth = Sine(aggregate_tones(100, n_harmonics), mul=[1 / vol for vol in range(1, n_harmonics + 1)]).out()
synth.ctrl(map_list=[SLMapMul([1 / vol for vol in range(1, n_harmonics + 1)])], title="Additive Synth")

# graph the signal as a waveform and spectrogram
show_waveform = Scope(sum(synth))
show_spectrum = Spectrum(synth)

# Opens the server graphical interface
s.gui(locals())
