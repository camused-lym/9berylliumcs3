class Song:
    def __init__(self, song_id, artist, views, length, platforms):
        self.__id = song_id
        self.artist = artist
        self.views = views
        self.length = length
        self.platforms = platforms
 
    def get_id(self):
        return self.__id
 
    def display_info(self):
        print(self.artist + " - " + str(self.length) + " sec, " + str(self.views) + " views, " + self.platforms)
 
 
class Playlist:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.songs = []
 
    def add_song(self, song):
        self.songs.append(song)
        print("Added song by " + song.artist + " to " + self.name)
 
    def get_total_length(self):
        total = 0
        for song in self.songs:
            total += song.length
        return total
