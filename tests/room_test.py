import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
       self.room1 = Room(1, "Bubba Ray Dudley", "X Goin Give It To Ya", 4)
       self.room2 = Room(2, "D-Von Dudley", "Candle In The Wind", 4)


    def test_room_has_guest(self):
        # room_guests = (self.room2.guests)
        self.assertEqual("D-Von Dudley", self.room2.guests)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room1.capacity)

    def test_room_has_song(self):
        self.assertEqual("X Goin Give It To Ya", self.room1.songs)