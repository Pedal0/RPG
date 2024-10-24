import unittest
from unittest.mock import patch
from main import Character
from main import main

class TestCharacter(unittest.TestCase):
    def test_attaque(self):
        player1 = Character("Player 1")
        player2 = Character("Player 2")
        player1.attack(player2)
        self.assertEqual(player2.hp, 9)
   
if __name__ == "__main__":
    unittest.main()