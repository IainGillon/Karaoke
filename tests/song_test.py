import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("X Goin Give It To Ya", "DMX", 3.36)
        self.song2 = Song("Candle In The Wind", "Elton John", 3.50)
    def test_song_has_name(self):
        self.assertEqual("X Goin Give It To Ya", self.song1.title)
    def test_song_has_artist(self):
        self.assertEqual("Elton John", self.song2.artist)
    def test_song_has_legnth(self):
        self.assertEqual(3.36, self.song1.legnth)
