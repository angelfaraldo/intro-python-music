
# este es un mecanismos para crear archivos midi.
# en vez de enviar el output midi al puerto, crea un archivo de sonido que puedas guardar,
# y reproducir más adelante

import mido
import time


hihat = "x x x x x x x x x x x x x x x x "
snare = "- - x - - - x - - - x x - - - -"
kick =  "x - - x x - - - x - - - x - - -"

hh_events = hihat.split()
sn_events = snare.split()
kk_events = kick.split()


#bpm = 120
quarter =
eight = quarter * 0.5
ticks_per_quarter = 256
step_dur_in_ticks = int(eight * ticks_per_quarter)

mid = mido.MidiFile()
track1 = mido.MidiTrack()
track2 = mido.MidiTrack()
track3 = mido.MidiTrack()
mid.tracks.append(track1)
mid.tracks.append(track2)
mid.tracks.append(track3)

for bar in range(1):
    for step in range(8):
        if hh_events[step] == "x":
            track1.append(mido.Message('note_on', channel=9, note=42, velocity=90, time=128))
        elif hh_events[step] == "-":
            track1.append(mido.Message('note_off', channel=9, note=42, velocity=90, time=128))
        if sn_events[step] == "x":
            track2.append(mido.Message('note_on', channel=9, note=38, velocity=127, time=128))
        elif sn_events[step] == "-":
            track2.append(mido.Message('note_off', channel=9, note=38, velocity=90, time=128))
        if kk_events[step] == "x":
            track3.append(mido.Message('note_on', channel=9, note=35, velocity=112, time=128))
        elif kk_events[step] == "-":
            track3.append(mido.Message('note_off', channel=9, note=35, velocity=90, time=128))
        # time.sleep(eight)

mid.save('drum-pattern.mid')
