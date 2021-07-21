# READ THE DOCUMENTATION
# https://mido.readthedocs.io/en/latest/midi_files.html


import mido

mimidi = mido.MidiFile('midi/testmid.MID')

#print("ticks", mi_midi.ticks_per_beat)
# print(mi_midi)



#for msg in mi_midi.play():
#    # with the play() method, time values are in secs
#    if not msg.is_meta:
#        print(msg)#
#        #out_port.send(msg)

for msg in mimidi.tracks[0]:
    if msg.note > 60:
        msg = Message(note=100, channel=msg.channel, velocity=msg.velocity)