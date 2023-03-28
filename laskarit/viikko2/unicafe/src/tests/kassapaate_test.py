import unittest
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def kassan_rahamaara_on_oikea(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)