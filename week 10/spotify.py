class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        mins = self.duration // 60
        secs = self.duration % 60
        return f"{self.title} by {self.artist} ({mins}:{secs:02d})"
    

class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = [] 
    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, song_title):
        for song in self.songs:
            if song.title == song_title:
                self.songs.remove(song)
                return
        print(f"Song '{song_title}' not found in playlist")
    
    def reorder_song(self, song_title, new_position):
        for i, song in enumerate(self.songs):
            if song.title == song_title:
                song_to_move = self.songs.pop(i)
                self.songs.insert(new_position, song_to_move)
                return
        print(f"Song '{song_title}' not found in playlist")
    
    def get_total_duration(self):
        total_secs = sum(song.duration for song in self.songs)
        return total_secs
    
    def __str__(self):
        output = f"Playlist: {self.name}\n"
        output += "=" * 40 + "\n"
        
        for i, song in enumerate(self.songs, 1):
            output += f"{i}. {song}\n"
        
        total_secs = self.get_total_duration()
        mins = total_secs // 60
        secs = total_secs % 60
        output += "=" * 40 + "\n"
        output += f"Total Duration: {mins}:{secs:02d}"
        
        return output


# Test function
def test_spotify():
    # Create some songs
    song1 = Song("Vitamin C", "CAN", 212)
    song2 = Song("Train in Vain(Stand by ME)", "The Clash", 194)
    song3 = Song("Femme Fatale", "The velvet Underground, Nico", 159)
    song4 = Song("This Charming Man - 2011", "The Smiths", 162)
    
    # Create a playlist
    my_playlist = Playlist("Early Alternative")
    
    # Add songs
    my_playlist.add_song(song1)
    my_playlist.add_song(song2)
    my_playlist.add_song(song3)
    my_playlist.add_song(song4)
    
    print(my_playlist)
    print("\n" + "=" * 40 + "\n")
    
    # Remove a song
    my_playlist.remove_song("Imagine")
    
    # Reorder - move "Hotel California" to position 0 (first)
    my_playlist.reorder_song("Hotel California", 0)
    
    print("After modifications:")
    print(my_playlist)


test_spotify()
