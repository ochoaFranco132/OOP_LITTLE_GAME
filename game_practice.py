from utilities import *


class Person:
    # Class attribute
    attack = True
    # Instances attribute
    def __init__(self, nickname, age) -> None:
        self.nickname = nickname
        self.age = age
        self.health = 100
        self.food = 100

    # Getters
    def get_health(self):
        return self.health

    def get_food(self):
        return self.food

    # Display attributes Method
    def display_attributes(self):
        print("*ATTRIBUTES*")
        print(f"NAME:   {self.nickname}")
        print(f"AGE:    {self.age}")
        print(f"ATTACK: {self.attack}")
        print(f"HEALTH: {self.health}")
        print(f"FOOD:   {self.food}")
        print("\n")

    def running(self):
        """Decrease food value in 20 points."""
        self.food -= 20

    def eating(self):
        """Increase food value in 30 points."""
        self.food += 30


class Zombie:
    def __init__(self, attack: bool, health_recov: bool) -> None:
        self.damage = 150
        self.health = 200
        self.tired = 100
        self.attack = attack
        self.health_recov = health_recov

    def start_attack(self, person):
        """Take a person as parameter and attack it decreasing their health in N damage points and the zombie get tired decreasing tired value in 20 points."""

        if (self.attack) and (self.tired + 20 > 0):
            person.health -= self.damage
            print("GGGGRRRRRRRRRR!")
            self.tired -= 20


def main():
    """Driver code"""
    # Players
    player_1 = Person("Bkendev", 18)
    zombie_1 = Zombie(True, True)
    run = True
    # Main logic.
    while run:
        # Display options letter
        menu.user_options()
        # Input validation
        usr_op = menu.input_validation(3)

        if usr_op == 1:
            # Check food.
            food.decrease_food(player_1)

        elif usr_op == 2:
            # Check food.
            food.increase_food(player_1)

        elif usr_op == 3:
            display_attr(player_1)
        else:
            run = False
            print("Good Bye!")
            screen_cleaner()


if __name__ == "__main__":
    main()
