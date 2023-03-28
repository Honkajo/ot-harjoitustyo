import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_rahamaara_on_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_myytyjen_lounaiden_maara_on_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullisesti(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(vaihtoraha, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_maukkaasti(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kassan_rahamaara_ei_muutu_kun_edullinen_maksu_ei_riitä(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassan_rahamaara_ei_muutu_kun_maukas_maksu_ei_riitä(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_ruoka_kortilla(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(onnistui), "True")
        self.assertEqual(kortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_ruoka_kortilla(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(onnistui), "True")
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortin_rahamaara_ei_muutu_jos_edullinen_maksu_ei_ole_riittävä(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(onnistui), "False")
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortin_rahamaara_ei_muutu_jos_maukas_maksu_ei_ole_riittävä(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(onnistui), "False")
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)    

    def test_rahan_lataaminen_kortille(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 400)
        self.assertEqual(kortti.saldo, 400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(kortti, -100), None)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)







    
    
