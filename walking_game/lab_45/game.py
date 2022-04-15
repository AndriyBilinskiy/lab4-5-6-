"""Module for classes for main.py"""


class WrongDirectionError(Exception):
    """Special exception for determining wrong direction """
    pass


defeated = 0


class Room:
    def __init__(self, name):
        self.name = name
        self.__neighboring_rooms = {"south": None, "north": None, "west": None, "east": None}
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
        print("You enetered", self.__description)

    def get_character(self):
        return self.__character

    def get_item(self):
        return self.__item

    def link_room(self, room, direction):
        if direction not in ["north", "south", "east", "west"]:
            return False
        self.__neighboring_rooms[direction] = room

    def move(self, direction):
        room = self.__neighboring_rooms[direction]
        if not room:
            raise WrongDirectionError
        return room


class Enemy:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__conversation = None
        self.__weakness = None

    def set_conversation(self, conversation):
        self.__conversation = conversation

    def set_weakness(self, weakness):
        self.__weakness = weakness

    def describe(self):
        print(f"You see the creature in the room, here is the description:\n\t{self.description}\n\tweakness: {self.__weakness}")

    def talk(self):
        print(self.__conversation)

    def fight(self, weapon):
        if weapon == self.__weakness:
            global defeated
            defeated += 1
        return weapon == self.__weakness

    def get_defeated(self):
        return defeated


class Item:
    def __init__(self, name):
        self.__name = name
        self.__description = None

    def set_description(self, description):
        self.__description = description

    def describe(self):
        print("There is", self.__description)

    def get_name(self):
        return self.__name
