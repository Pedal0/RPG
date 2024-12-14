class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 10

    def attack(self, other):
        if other.hp > 0:

            other.hp -= 1

            if other.hp <= 0:

                print(f"{other.name} is dead")