from abc import *


class Weapon(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass


class Sward(Weapon):
    def attack(self):
        print("검 공격")


class Knife(Weapon):
    def attack(self):
        print("칼 공격")


class GameCharacter:

    def __init__(self):
        self.weapon = None

    def setWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon is None:
            print("맨손 공격")
            return
        self.weapon.attack()


character = GameCharacter()
sward = Sward()
knift = Knife()
character.attack()
character.setWeapon(sward)
character.attack()
character.setWeapon(knift)
character.attack()
