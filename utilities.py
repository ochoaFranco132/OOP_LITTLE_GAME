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


class menu:
    @staticmethod
    def user_options():
        """Display a menu"""
        print("1- Run")
        print("2- Eat")
        print("3- Display attributes")
        print("0- Exit")

    @staticmethod
    def input_validation(nro):
        """Take a number of options as parameter, validate input and return it."""
        op = int(input("Pick an option: "))
        screen_cleaner()
        while op < 0 or op > nro:
            print("Wrong Option, try again")
            menu.user_options()
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
