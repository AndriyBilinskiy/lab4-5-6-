"""Module for classes for main.py"""


class WrongDirectionError(Exception):
    """Special exception for determining wrong direction """
    pass


class Location:
    def __init__(self, name):
        self.name = name
        self.__neighboring_rooms = {"forward": None, "back": None}
        self.__description = None
        self.__character = None
        self.__item = None

    def set_description(self, description):
        self.__description = description

    def set_character(self, character):
        self.__character = character

    def set_item(self, item):
        self.__item = item

    def get_details(self):
        print("You entered", self.__description)

    def get_character(self):
        return self.__character

    def get_item(self):
        return self.__item

    def link_room(self, room, direction):
        if direction not in ["forward", "back"]:
            return False
        self.__neighboring_rooms[direction] = room

    def move(self, direction):
        room = self.__neighboring_rooms[direction]
        if not room:
            raise WrongDirectionError
        return room


class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__conversation = None

    def set_conversation(self, conversation):
        self.__conversation = conversation

    def describe(self):
        print(self.description)

    def talk(self):
        print(self.__conversation)

    def fight(self):
        print("Can`t fight peacefull character")


class Enemy(Character):
    def __init__(self, name, description, health):
        super().__init__(name, description)
        self.__weakness = None
        self.health = health

    def set_weakness(self, weakness):
        self.__weakness = weakness

    def fight(self, weapon):
        return weapon == self.__weakness or (isinstance(weapon, Weapon) and weapon.damage >= self.health)

    def describe(self):
        print("Ви бачите", self.description)


class Item:
    def __init__(self, name):
        self.__name = name
        self.__description = None

    def set_description(self, description):
        self.__description = description

    def describe(self):
        print(self.__description)

    def get_name(self):
        return self.__name


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
