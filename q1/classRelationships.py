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

 
song1 = Song(101, "Taylor", 5000, 210, "Spotify, YouTube")
song2 = Song(102, "Bruno", 8200, 180, "Spotify")
song3 = Song(103, "Adele", 6400, 245, "YouTube")
playlist1 = Playlist("Study Mix", "Ana")
 
print("--- BEFORE RELATIONSHIP ---")
print("Playlist:", playlist1.name, "by", playlist1.owner)
print("Songs in playlist:", len(playlist1.songs))
song1.display_info()
song2.display_info()
song3.display_info()
print()
 
print("--- BUILDING RELATIONSHIP ---")
playlist1.add_song(song1)
playlist1.add_song(song2)
playlist1.add_song(song3)
print()
 
print("--- AFTER RELATIONSHIP ---")
print("Playlist:", playlist1.name, "by", playlist1.owner)
print("Songs in playlist:", len(playlist1.songs))
print("Related object(s):")
for song in playlist1.songs:
    print("-", song.get_id(), song.artist, song.length, "sec")
print("Total length:", playlist1.get_total_length(), "sec")
 
