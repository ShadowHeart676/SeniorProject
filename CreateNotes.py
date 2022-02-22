from pprint import pprint
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
from pydub.playback import play

#GOOD TEST CODE CAN IMPLEMENT FOR RECORDING SOUND LATER
#:)

samplerate = 44100

def get_wave(freq, duration=0.5):
    '''
    Function takes the "frequecy" and "time_duration" for a wave 
    as the input and returns a "numpy array" of values at all points 
    in time
    '''
    
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

def get_piano_notes():
    '''
    Returns a dict object for all the piano 
    note's frequencies
    '''
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['LC', 'LcS', 'LD', 'LdS', 'LE', 'LF', 'LfS', 'LG', 'LgS', 'LA', 'LaS', 'LB','C', 'cS', 'D', 'dS', 'E', 'F', 'fS', 'G', 'gS', 'A', 'aS', 'B','HC', 'HcS', 'HD', 'HdS', 'HE', 'HF', 'HfS', 'HG', 'HgS', 'HA', 'HaS', 'HB'] 
    base_freq = 130.81 #Low C frequency
    
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0 # silent note
    
    return note_freqs
  
  # To get the piano note's frequencies
note_freqs = get_piano_notes()


def get_song_data(music_notes):
    '''
    Function to concatenate all the waves (notes)
    '''
    note_freqs = get_piano_notes() # Function that we made earlier
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song

#createNotesforPiano
music_notes = 'LC'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LC.wav',samplerate,data.astype(np.int16))
music_notes = 'LcS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LcS.wav',samplerate,data.astype(np.int16))
music_notes = 'LD'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LD.wav',samplerate,data.astype(np.int16))
music_notes = 'LdS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LdS.wav',samplerate,data.astype(np.int16))
music_notes = 'LE'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LE.wav',samplerate,data.astype(np.int16))
music_notes = 'LF'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LF.wav',samplerate,data.astype(np.int16))
music_notes = 'LfS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LfS.wav',samplerate,data.astype(np.int16))
music_notes = 'LG'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LG.wav',samplerate,data.astype(np.int16))
music_notes = 'LgS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LgS.wav',samplerate,data.astype(np.int16))
music_notes = 'LA'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LA.wav',samplerate,data.astype(np.int16))
music_notes = 'LaS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LaS.wav',samplerate,data.astype(np.int16))
music_notes = 'LB'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/LB.wav',samplerate,data.astype(np.int16))
music_notes = 'C'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/C.wav',samplerate,data.astype(np.int16))
music_notes = 'cS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/cS.wav',samplerate,data.astype(np.int16))
music_notes = 'D'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/D.wav',samplerate,data.astype(np.int16))
music_notes = 'dS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/dS.wav',samplerate,data.astype(np.int16))
music_notes = 'E'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/E.wav',samplerate,data.astype(np.int16))
music_notes = 'F'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/F.wav',samplerate,data.astype(np.int16))
music_notes = 'fS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/fS.wav',samplerate,data.astype(np.int16))
music_notes = 'G'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/G.wav',samplerate,data.astype(np.int16))
music_notes = 'gS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/gS.wav',samplerate,data.astype(np.int16))
music_notes = 'A'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/A.wav',samplerate,data.astype(np.int16))
music_notes = 'aS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/aS.wav',samplerate,data.astype(np.int16))
music_notes = 'B'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/B.wav',samplerate,data.astype(np.int16))
music_notes = 'HC'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HC.wav',samplerate,data.astype(np.int16))
music_notes = 'HcS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HcS.wav',samplerate,data.astype(np.int16))
music_notes = 'HD'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HD.wav',samplerate,data.astype(np.int16))
music_notes = 'HdS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HdS.wav',samplerate,data.astype(np.int16))
music_notes = 'HE'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HE.wav',samplerate,data.astype(np.int16))
music_notes = 'HF'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HF.wav',samplerate,data.astype(np.int16))
music_notes = 'HfS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HfS.wav',samplerate,data.astype(np.int16))
music_notes = 'HG'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HG.wav',samplerate,data.astype(np.int16))
music_notes = 'HgS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HgS.wav',samplerate,data.astype(np.int16))
music_notes = 'HA'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HA.wav',samplerate,data.astype(np.int16))
music_notes = 'HaS'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HaS.wav',samplerate,data.astype(np.int16))
music_notes = 'HB'
data = get_song_data(music_notes)
data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
write('CodeCreatedSounds/HB.wav',samplerate,data.astype(np.int16))


#playnote
# song = AudioSegment.from_wav("CodeCreatedSounds/C.wav")
# play(song)