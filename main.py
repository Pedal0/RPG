from Character import Character

     

player1 = Character("Player 1")
player2 = Character("Player 2")
    
while player1.hp > 0 and player2.hp > 0:
      
      player1.attack(player2)

      if player2.hp <= 0:
        print('Player 1 has won')
        break
      print(f'Player 2 HP: {player2.hp}')

      player2.attack(player1)

      if player1.hp <= 0:
        print('Player 2 has won')
        break
      print(f'Player 1 HP: {player1.hp}')

