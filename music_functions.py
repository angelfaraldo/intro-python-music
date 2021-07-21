"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra
"""

import mido
import time

MIDI_OUT_PORT = 0

def midi_out_port(MIDI_OUT_PORT=0):
    return mido.open_output(mido.get_output_names()[MIDI_OUT_PORT])


def bpm_to_secs(tempo_in_bpm):
    return tempo_in_bpm / 60


def play_note(note=60, dur_in_secs=1, velocity=100, channel=0, port=midi_out_port(MIDI_OUT_PORT)):
    port.send(mido.Message("note_on", note=note, velocity=velocity, channel=channel))
    time.sleep(dur_in_secs)
    port.send(mido.Message("note_off", note=note, velocity=velocity, channel=channel))


def midi_panic(port=midi_out_port(MIDI_OUT_PORT)):
    port.send(mido.Message('control_change', control=123, value=0))
