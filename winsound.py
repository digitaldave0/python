import winsound

def play_happy_birthday():
    # The notes for the song "Happy Birthday" in the key of C
    notes = ['C', 'C', 'D', 'C', 'F', 'E', 'C', 'C', 'D', 'C', 'G', 'F', 'C', 'C', 'C', 'C', 'G', 'F', 'E', 'D']
    durations = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2]

    # Set the tempo of the song
    tempo = 200  # number of milliseconds per quarter note

    # Play the song
    for note, duration in zip(notes, durations):
        frequency = 0
        if note == 'C':
            frequency = 262
        elif note == 'D':
            frequency = 294
        elif note == 'E':
            frequency = 330
        elif note == 'F':
            frequency = 349
        elif note == 'G':
            frequency = 392
        elif note == 'A':
            frequency = 440
        elif note == 'B':
            frequency = 494
        if frequency > 0:
            winsound.Beep(frequency, duration * tempo)
        else:
            winsound.Beep(600, duration * tempo)
        time.sleep(tempo / 1000)

play_happy_birthday()