import os
import music21 as m21

kern_dataset_path = "deutschl/test"

def load_songs_in_kern(dataset_path):
    songs = []
    
    #go through all the files in the dataset, loaded in with music21
    for path, subdir, files in os.walk(dataset_path):
        for file in files:
            if file[-3:] == 'krn':
                song = m21.converter.parse(os.path.join(path,file))
                songs.append(song)
    return songs


def has_accetpable_duration(song, acceptable_durations):
    pass

def preprocess(dataset_path):
    pass

    #load the songs 
    print("Loading Songs")
    songs = load_songs_in_kern(dataset_path)
    print(f"Loaded {len(songs)} songs.")
    #filter out songs that have non-acceptable lengths 

    #transpose songs to Cmaj/amin

    #save songs to text file


if __name__== "__main__":
    songs = load_songs_in_kern(kern_dataset_path)
    print(f"Loaded {len(songs)} songs.")
    song = songs[0]
    song.show()