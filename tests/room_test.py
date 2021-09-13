import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song1 = Song(1, "X Goin Give It To Ya", "DMX", 3.36)
        self.song2 = Song(2, "Candle In The Wind", "Elton John", 3.50)
        self.guest1 = Guest("Bubba Ray Dudley", self.song2)
        self.guest2 = Guest("D-Von Dudley", self.song2)
        self.room1 = Room(1, [self.guest1], [self.song1], 4)
        self.room2 = Room(2, [self.guest2], [self.song2], 4)

    def test_room_has_number(self):
        self.assertEqual(1, self.room1.number)

    def test_room_has_guest(self):
        # room_guests = (self.room2.guests)
        # self.assertEqual("D-Von Dudley", self.room2.guests[0].name)
        self.assertEqual("Candle In The Wind", self.room2.guests[0].song.title)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room1.capacity)

    def test_room_has_song(self):
        self.assertEqual("X Goin Give It To Ya", self.room1.songs[0].title)

    def test_add_song_to_room(self):
        self.assertEqual(1, len(self.room1.songs))
        self.room1.add_song_to_room(self.song2)
        self.assertEqual(2, len(self.room1.songs))
    
    def test_check_in_guest(self):
        self.assertEqual(1, len(self.room1.guests))
        self.room1.check_in_guest(self.guest2)
        self.assertEqual(2, len(self.room1.guests))
        
    def test_check_out_guest(self):
        self.assertEqual(1, len(self.room1.guests))
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(0, len(self.room1.guests))

    
