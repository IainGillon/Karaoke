import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("X Goin Give It To Ya", "DMX", 3.36)
        self.song2 = Song("Candle In The Wind", "Elton John", 3.50)
        self.guest1 = Guest("Bubba Ray Dudley", self.song2)
        self.guest2 = Guest("D-Von Dudley", self.song1)

    def test_guest_has_name(self):
        self.assertEqual("Bubba Ray Dudley", self.guest1.name)

    def test_guest_has_song(self):
        self.assertEqual("X Goin Give It To Ya", self.guest2.song.title)