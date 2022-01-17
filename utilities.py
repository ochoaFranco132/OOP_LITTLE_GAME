import os


def screen_cleaner():
    if os.name == "posix":
        print()
        input("Press enter to continue..")
        os.system("clear")

    if os.name == "nt":
        print()
        input("Press enter to continue..")
        os.system("cls")


class Menu:
    @staticmethod
    def general():
        """Display a general Menu"""
        print("1- Person")
        print("2- Zombie")
        print("0- Exit")

    @staticmethod
    def person():
        """Display a menu"""
        print("1- Run")
        print("2- Eat")
        print("3- Display attributes")
        print("0- Exit")

    @staticmethod
    def zombie():
        print("1- Scream")
        print("2- Display attributes")
        print("0- Exit")

    def input_validation(nro, menu_type):
        op = int(input("Pick an option: "))
        screen_cleaner()
        while op < 0 or op > nro:
            print("Wrong Option, try again")
            screen_cleaner()
            assert menu_type <= 0 or menu_type > 3, "Wrong parameter value."
            if menu_type == 1:
                Menu.general()
            elif menu_type == 2:
                Menu.person()
            else:
                Menu.zombie()

            op = int(input("Pick an option: "))
            screen_cleaner()
        return op


class food:
    @staticmethod
    def increase_food(player):
        """Take a player as parameter and check if there's enough food, in that case increase food value, otherwise display a letter saying that is no enough food."""
        if player.food + 30 > 100:
            print("You've been eaten to much!")
            screen_cleaner()
        else:
            player.eating()
            print("You just eat something!")
            screen_cleaner()

    @staticmethod
    def decrease_food(player):
        """Take a player as parameter and check if there's enough food, in that case decrease food value, otherwise display a letter saying that is no enough food."""
        if player.food - 20 < 0:
            print("You cannot run now!")
            screen_cleaner()
        else:
            player.running()
            print("You're running!")
            screen_cleaner()


def display_attr(player):
    """Take a player as parameter and display their attributes."""
    player.display_attributes()
    screen_cleaner()
