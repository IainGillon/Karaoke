class Room:
    def __init__(self, number, guests, songs, capacity):
        self.number = number
        self.guests = guests
        self.songs = songs
        self.capacity = capacity
        
    def add_song_to_room(self, song):
        self.songs.append(song)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)


