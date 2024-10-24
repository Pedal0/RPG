class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 10

    def attack(self, other):
        other.hp -= 1
        
def main():
    player1 = Character("Player 1")
    player2 = Character("Player 2")
    player1.attack(player2)
    print(player2.hp)

if __name__ == "__main__":
    main()