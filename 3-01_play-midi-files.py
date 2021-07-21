import mido
import time

# READ THE DOCUMENTATION
# https://mido.readthedocs.io/en/latest/midi_files.html

# play it back straight into the midi port.
out_port = mido.open_output(mido.get_output_names()[0])

mimidi = mido.MidiFile('midi/Bach - Flute allemande.mid')

print("ticks", mimidi.ticks_per_beat)
print(mimidi)

for i, track in enumerate(mimidi.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)


# A METHOD COMPARABLE TO WHAT WE HAVE BEEN DOING WITH STREAMS!!!
for msg in mimidi:
    time.sleep(msg.time)
    if not msg.is_meta:
        out_port.send(msg)


# A FASTER AND MORE RELIABLE METHOD
for msg in mimidi.play():
    out_port.send(msg)