import game

if __name__ == "__main__":
    loc1 = game.Location("Козельницька")
    loc1.set_description("вул. Козельницька")
    students = game.Character("студенти", "Ви бачите студентів")
    students.set_conversation("Не відволікайте, ми вчимось")
    loc1.set_character(students)
    branch = game.Weapon("гілка", 5)
    loc1.set_item(branch)
    branch.set_description("Також стежці в Стрийському парку ви бачите гілку")
    loc2 = game.Location("Стрийська")
    loc2.set_description("вул. Стрийська")
    bandit = game.Enemy("Лотр", "Ви бачите Лотра", 1)
    bandit.set_conversation("Ану стоять!")
    loc2.set_character(bandit)
    rock = game.Weapon("rock", 10)
    rock.set_description("На землі лежить камінь")
    loc2.set_item(rock)
    loc3 = game.Location("Франка")
    loc3.set_description("вул. І.Франка")
    kavaler = game.Character('K', "Попереду йде кавалер")
    kavaler.set_conversation("Вітаю, як ся маєте?")
    loc3.set_character(kavaler)
    coin = game.Item("coin")
    coin.set_description("На землі лежить монетка")
    loc3.set_item(coin)
    loc4 = game.Location("Шевченка")
    loc4.set_description("пр.Т.Шевченка")
    batar = game.Enemy("name", "Ви бачите п'яного батаяра", 7)
    batar.set_conversation("Чого ти так на мене дивишся?")
    loc4.set_character(batar)
    loc5 = game.Location("Краківська")
    laydak = game.Character("лайадк", "На землі сидить лайдак")
    laydak.set_conversation("Кинь мені монетку!")
    loc5.set_character(laydak)

    loc5.set_description("вул. Краківська")
    loc1.link_room(loc2, "forward")
    loc2.link_room(loc3, "forward")
    loc3.link_room(loc4, "forward")
    loc4.link_room(loc5, "forward")
    loc2.link_room(loc1, "back")
    loc3.link_room(loc2, "back")
    loc4.link_room(loc3, "back")
    loc5.link_room(loc4, "back")

    dead = False

    current_room = loc1
    backpack = []
    been_to_final = False

    while not dead:

        print("\n")
        if current_room == loc5:
            been_to_final = True
        if been_to_final and current_room == loc1:
            print("You won!!!")
            break
        current_room.get_details()

        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()

        item = current_room.get_item()
        if item is not None:
            item.describe()

        command = input("> ")

        if command in ["forward", "back"]:
            # Move in the given direction
            try:
                current_room = current_room.move(command)
            except game.WrongDirectionError:
                print("The room in that direction doesn`t exist")
        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            if current_room == loc5:
                if coin in [i[0]for i in backpack]:
                    print("Дякую!")
            if inhabitant is not None:
                inhabitant.talk()
        elif command == "fight":
            if inhabitant is not None:
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                fight_with = input()

                # Do I have this item?
                if fight_with in [i[0]for i in backpack]:
                    if inhabitant.fight(backpack[[i[0]for i in backpack].index(fight_with)][1]):
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_room.character = None
                    else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("You don't have a " + fight_with)
            else:
                print("There is no one here to fight with")
        elif command == "take":
            if item is not None:
                print("You put the " + item.get_name() + " in your backpack")
                backpack.append((item.get_name(), item))
                current_room.set_item(None)
            else:
                print("There's nothing here to take!")
        elif command == "backpack":
            [print(i[0]) for i in backpack]
        elif command == "help":
            print("""Availible commands is:
                    forward
                    back
                    take
                    fight
                    take 
                    backpack
                  """)
        else:
            print("I don't know how to " + command)
