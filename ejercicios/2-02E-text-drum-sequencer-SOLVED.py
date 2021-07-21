import mido
import time

out_port = mido.open_output()  # opens the 1st port per default

hihat = "x x x x x x x x x x x x x x x x "
snare = "- - x - - - x - - - x x - - - -"
kick =  "x - - x x - - - x - - - x - - -"

bpm = 120
quarter = 60 / bpm
eight = quarter * 0.5

hh_events = hihat.split()
sn_events = snare.split()
kk_events = kick.split()

for bar in range(8):
    for step in range(8):
        if hh_events[step] == "x":
            out_port.send(mido.Message('note_off', channel=9, note=42, velocity=0))
            out_port.send(mido.Message('note_on', channel=9, note=42, velocity=90))
        if sn_events[step] == "x":
            out_port.send(mido.Message('note_off', channel=9, note=38, velocity=0))
            out_port.send(mido.Message('note_on', channel=9, note=38, velocity=127))
        if kk_events[step] == "x":
            out_port.send(mido.Message('note_off', channel=9, note=35, velocity=0))
            out_port.send(mido.Message('note_on', channel=9, note=35, velocity=112))
        time.sleep(eight)

