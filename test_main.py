import unittest
from unittest.mock import patch
from Character import Character
from main import main

class TestCharacter(unittest.TestCase):

    def test_init(self):
        player1 = Character("Player 1")
        player2 = Character("Player 2")
        self.assertEqual(player1.name, "Player 1")
        self.assertEqual(player2.name, "Player 2")
        self.assertEqual(player1.hp, 10)
        self.assertEqual(player2.hp, 10)
        print("Test init passed 2 players with 10 HP each")
        print("A enlever pourt commit video")

    # def test_init(self):
    #     player1 = Character("Player 1")
    #     player2 = Character("Player 2")
    #     self.assertEqual(player1.name, "Player 1")
    #     self.assertEqual(player2.name, "Player 2")
    #     self.assertEqual(player1.hp, 10)
    #     self.assertEqual(player2.hp, 5)
    #     print("Test init passed 2 players with 10 HP each"
    #     print("A enlever pourt commit video")


if __name__ == "__main__":
    unittest.main()