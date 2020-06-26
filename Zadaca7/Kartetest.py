import unittest
from Karte import Karte

class KarteTestCase(unittest.TestCase):
    def test_size_of_deck(self):
        game_test = Karte()
        deck = game_test.create_deck()
        self.assertEqual(len(deck), 52, "Deck ima 52 karte")
    def test_shuffle_randomizes_deck(self):
        game_test = Karte()
        deck_one = game_test.create_deck()
        deck_one = game_test.shuffle_deck(deck_one)
        deck_two = game_test.create_deck()
        deck_two = game_test.shuffle_deck(deck_two)
        self.assertNotEqual(str(deck_one), str(deck_two), "Karte su promiješanje")
    def test_deal_removes_a_card(self):
        game_test = Karte()
        deck = game_test.create_deck()
        inital_deck_num = len(deck)
        card = game_test.deal_card(deck)
        after_deal_deck_num = len(deck)
        self.assertEqual(inital_deck_num, after_deal_deck_num + 1, "Miče se jedna karata iz decka")
    
        
    def test_value_of_cards_in_ranks(self):
        game_test = Karte()
        card = game_test.rank['Dama']
        self.assertEqual(card, 12, "Vrijednost Dame je 12")
        card = game_test.rank['Kralj']
        self.assertEqual(card, 13, "Vrijednost Kralja je 13")
        card = game_test.rank['Kec']
        self.assertEqual(card, 1, "Vrijednost Keca je 1")
        
    def test_card_kec_value(self):
        game_test = Karte()
        kec = list(game_test.rank.keys())[list(game_test.rank.values()).index(1)]
        self.assertEqual(kec, "Kec", "Kec ima vrijednost 1")
    
    
    
    
    
    

if __name__ == "__main__":
    unittest.main()