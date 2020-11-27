import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Singy McSingface", 36, 50)

    def test_guest_has_name(self):
        self.assertEqual("Singy McSingface", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(36, self.guest.age)

    def test_guest_has_cash(self):
        self.assertEqual(50, self.guest.cash)

    def test_remove_cash(self):
        self.guest.remove_cash(5)
        self.assertEqual(45, self.guest.cash)

    
