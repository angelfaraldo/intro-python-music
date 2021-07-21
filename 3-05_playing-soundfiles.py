"""
INTRODUCCIÓN A LA PROGRAMACIÓN EN PYTHON A TRAVÉS DE LA MÚSICA
Ángel Faraldo, del 19 al 23 de julio de 2021
Campus Junior, Universitat Pompeu Fabra

"playing-a-soundfile"
contenidos:
"""

# THIS IS THE SIMPLEST POSSIBLE WAY
from magicsound import magicsound

# this library can do no more
magicsound('./samples/drums.wav')


# LETS FIND A MORE ELABORATE WAY OF DOING IT
# Manipulate audio with http://pydub.com/


# Open a WAV file
import pydub

song1 = pydub.AudioSegment.from_wav("./samples/aeiou.wav")

# or an mp3 (for which we need to have FFMPEG installed...
# song2 = pydub.AudioSegment.from_mp3("./samples/3 - Regina Movement - 66bpm.mp3")


# Slice audio
# pydub does things in milliseconds
one_second = 1 * 1000

first_second = song1[:1000]
last_second = song1[-1000:]

# Make the beginning louder and the end quieter
# boost volume by 6dB
beginning = first_second + 6

# reduce volume by 3dB
end = last_second - 3

#Concatenate audio (add one file to the end of another)
without_the_middle = beginning + end

# AudioSegments are immutable, therefore original audio is not modified!
backwards = song1.reverse()

# Crossfade (again, beginning and end are not modified)
# 1.5 second crossfade
with_style = beginning.append(end, crossfade=500)

# repeat the clip twice
do_it_over = with_style * 2

# Fade (note that you can chain operations because everything returns an AudioSegment)
# 2 sec fade in, 3 sec fade out
awesome = do_it_over.fade_in(500).fade_out(500)

# Save the results (again whatever ffmpeg supports)
awesome.export("mashup.wav", format="wav")
