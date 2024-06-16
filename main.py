import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            # Игрок атакует
            self.player.attack(self.computer)
            if self.computer.is_alive():
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            else:
                print(f"{self.computer.name} побежден!")
                break

            # Компьютер атакует
            self.computer.attack(self.player)
            if self.player.is_alive():
                print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            else:
                print(f"{self.player.name} побежден!")
                break

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
