import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room
from src.venue import Venue

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("Moe's Tavern", [1, 2], 1000)

    def test_venue_has_name(self):
        self.assertEqual("Moe's Tavern", self.venue.name)
    
    def test_venue_has_room_numbers(self):
        self.assertEqual([1, 2], self.venue.room_numbers)

    def venue_has_till(self):
        self.assertEqual(1000, self.venue.till)
    