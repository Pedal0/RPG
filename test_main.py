import unittest
from unittest.mock import patch
from main import Character
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
    
    def test_attaque_player1(self):
        player1 = Character("Player 1")
        player2 = Character("Player 2")
        for i in range(player1.hp):
            player1.attack(player2)
            self.assertEqual(player2.hp, player1.hp - i - 1)
            print(f"Test attaque passed player 2 has {player1.hp - i - 1} HP after attack")
   
    def test_attaque_player2(self):
        player1 = Character("Player 1")
        player2 = Character("Player 2")
        for i in range(player2.hp):
            player2.attack(player1)
            self.assertEqual(player1.hp, player2.hp - i - 1)
            print(f"Test attaque passed player 1 has {player2.hp - i - 1} HP after attack")

    def test_attaque_player1_dead(self):
        player1 = Character("Player 1")
        player2 = Character("Player 2")
        player1.hp = 0
        player2.attack(player1)
    
    def test_attaque_player2_dead(self):
        player1 = Character("Player 1")
        player2 = Character("Player 2")
        player2.hp = 0
        player1.attack(player2)


if __name__ == "__main__":
    unittest.main()