import music21 as m21
import os

kern_dataset_path = "deutschl/test"
acceptable_duration = [
    0.25,
    0.5,  # 8th note
    0.75,  # dotted note
    1.0,  # quarter note
    1.5,  # dotted quarter note
    2,
    3,
    4  # whole note
]


def load_songs_in_kern(dataset_path):
    songs = []
    # go through all the files in the dataset, loaded in with music21
    for path, subdir, files in os.walk(dataset_path):
        for file in files:
            if file[-3:] == 'krn':
                song = m21.converter.parse(os.path.join(path, file))
                songs.append(song)
    return songs


def has_acceptable_durations(song, acceptable_durations):
    for note in song.flat.notesAndRests:
        if note.duration.quarterLength not in acceptable_durations:
            return False
    return True 

def preprocess(dataset_path):
    pass
    # load the songs
    print("Loading Songs")
    songs = load_songs_in_kern(dataset_path)
    print(f"Loaded {len(songs)} songs.")

    for song in songs:
    # filter out songs that have non-acceptable lengths
        if not has_acceptable_durations(song, acceptable_duration):
         continue
    # transpose songs to Cmaj/amin

    # save songs to text file


if __name__ == "__main__":
    m21.configure.run()
    songs = load_songs_in_kern(kern_dataset_path)
    print(f"Loaded {len(songs)} songs.")
    song = songs[0]

    print(f"Has acceptable duration? {has_acceptable_durations(song, acceptable_duration)}")
    song.show()
