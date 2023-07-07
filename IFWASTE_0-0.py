import random


class Food:
    def __init__(self, food_type, amount_kg):
        self.type = food_type
        self.amount_kg = amount_kg


class House:
    def __init__(self):
        self.members_adult = random.randint(1, 3)
        self.members_dependent = random.randint(0, 3)
        self.menu = []

    def generate_menu(self):
        for i in range(self.members_adult):
            food_type = random.choice(foods)
            amount_kg = round(random.uniform(1, 5), 2)
            food = Food(food_type, amount_kg)
            self.menu.append(food)

    def print_menu(self):
        for food in self.menu:
            print(f"Food: {food.type}, Amount: {food.amount_kg} kg")


# Usage example
house = House()
house.generate_menu()
house.print_menu()
