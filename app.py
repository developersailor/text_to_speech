import numpy as np
from scipy.io.wavfile import write
from gtts import gTTS
import tempfile
import os
import pydub

def create_cig_kofte_song():
	"""
	Creates a song by combining a melody and lyrics converted to speech.

	Returns:
		str: The path of the output audio file.
	"""
	# Define the melody notes (frequencies in Hz)
	melody_freqs = [161.63, 193.66, 229.63, 249.23, 292.00, 340.00, 393.88, 423.25]  # C4 to C5 in Hz (pop music)
	melody_duration = 1  # Duration of each note in seconds

	# Create the melody sound
	sample_rate = 29100
	melody = []

	for freq in melody_freqs:
		t = np.linspace(0, melody_duration, int(sample_rate * melody_duration), endpoint=False)
		wave = 0.5 * np.sin(2 * np.pi * freq * t)  # Sine wave
		melody.extend(wave)

	melody = np.array(melody)

	# Convert the lyrics to speech
	lyrics = "Çiğ köfte, lezzeti bol, Tadını al, sen de gel, Acı mı acı, yeme de yanında yat, Bu lezzet, başka bir tat. Çiğ köfte, çiğ köfte, Haydi gel, tat bu lezzeti."

	tts = gTTS(lyrics, lang='tr')
	with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
		tts.save(fp.name)
		tts_path = fp.name

	# Convert the speech to a waveform
	speech = pydub.AudioSegment.from_file(tts_path)
	speech = np.array(speech.get_array_of_samples())

	# Ensure both melody and speech have the same length
	if len(melody) > len(speech):
		speech = np.pad(speech, (0, len(melody) - len(speech)), 'constant')
	elif len(melody) < len(speech):
		melody = np.pad(melody, (0, len(speech) - len(melody)), 'constant')

	# Combine melody and speech
	combined = melody + speech / np.max(np.abs(speech)) * np.max(np.abs(melody))

	# Save the combined sound
	output_path = 'ciğ_köfte_song.wav'
	write(output_path, sample_rate, combined.astype(np.float32))

	return output_path

output_path = create_cig_kofte_song()
output_path