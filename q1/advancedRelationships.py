class Song:
    def __init__(self, song_id, artist, views, length, platforms):
        self.__id = song_id
        self.artist = artist
        self.views = views
        self.length = length
        self.platforms = platforms
 
    def get_id(self):
        return self.__id
 
    def describe(self):
        return self.artist + " - " + str(self.length) + " sec, " + str(self.views) + " views, " + self.platforms
 
 
class RemixSong(Song):
    def __init__(self, song_id, artist, views, length, platforms, remixer):
        super().__init__(song_id, artist, views, length, platforms)
        self.remixer = remixer
 
    def describe(self):
        return super().describe() + ", remix by " + self.remixer
 
 
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
 
    def add_song(self, song):
        self.songs.append(song)
 
 
class Listener:
    def __init__(self, name):
        self.name = name
 
    def listen(self, song):
        song.views += 1
        print(self.name + " listened to " + song.artist)
 
 
song1 = Song(101, "Taylor", 5000, 210, "Spotify")
remix1 = RemixSong(102, "Taylor", 1200, 195, "YouTube", "DJ Mark")
 
print("TEST 1: INHERITANCE")
print("Artist:", remix1.artist)
print("ID:", remix1.get_id())
print(song1.describe())
print(remix1.describe())
print()
 
print("TEST 2: AGGREGATION")
playlist = Playlist("Study Mix")
playlist.add_song(song1)
playlist.add_song(remix1)
print(playlist.name, "contains:")
for song in playlist.songs:
    print("-", song.describe())
del playlist
print("Playlist deleted, song still exists:", song1.artist)
print()
 
print("TEST 3: DEPENDE")
ana = Listener("Ana")
ana.listen(song1)
print("Views now:", song1.views)
