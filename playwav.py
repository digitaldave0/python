import pyaudio
import wave

def play_sound(filename):
    # Open the wave file
    wf = wave.open(filename, 'rb')

    # Open a PyAudio object
    p = pyaudio.PyAudio()

    # Open a stream to play the wave file
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Read the wave file and play it
    data = wf.readframes(1024)
    while data:
        stream.write(data)
        data = wf.readframes(1024)

    # Close the stream and PyAudio object
    stream.stop_stream()
    stream.close()
    p.terminate()

# Play a sound file
play_sound('song.wav')
