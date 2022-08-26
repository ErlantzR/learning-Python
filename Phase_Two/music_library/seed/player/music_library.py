from dataclasses import dataclass

class MusicLibrary:
    def __init__(self):
        self.songs_list = []

    def all(self):
        return self.songs_list

    def add(self, song_name):
        self.songs_list.append(song_name)

    def remove(self, song_index):
        if song_index + 1 <= len(self.songs_list):
            self.songs_list.pop(song_index)
            return True
        
        return False

@dataclass
class Track:
    title: str
    artist: str
    file: str

    def __str__(self):
        return f"{self.title} by {self.artist}"
