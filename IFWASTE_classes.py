import random


class Food:
    def __init__(self, foodType, amount_kg):
        self.type = foodType
        self.amount_kg = amount_kg
        self.expirationTime = random.uniform(1,5)

    def __str__(self): 
        return(f"Food: {self.type}, Amount: {self.amount_kg} kg")


class Waste:
    def __init__(self, food: Food):
        self.type = food.type
        self.amount_kg = food.amount_kg

    def __str__(self):
        return f"Waste category: {self.type}, Amount: {self.amount_kg}"


class House:
    def __init__(self):
        self.members_adult = random.randint(1, 3)
        self.members_dependent = random.randint(0, 3)
        self.kcal = (self.members_adult*random.gauss(2144, 1308) + self.members_dependent*random.gauss(1800,1434))/3
        self.menu = []
        self.waste_bin = []

    def __str__(self):
        return(f"Adults: {self.members_adult}, Dependents: {self.members_dependent}, kilocalories per day: {self.kcal}")

    def shop(self):
        FLW_categories = [
            "Meat & Fish",
            "Dairy & Eggs",
            "Fruits and Vegetables",
            "Baked Goods",
            "Dry Foods",
            "Snacks, Condiments, & Other",
            "Liquids/Oils/Grease", 
            "Cooked/Prepared Items/Leftovers", 
        ]
        # Randomly add some items to their menu
        for i in range(self.members_adult):
            food_type = random.choice(FLW_categories)
            amount_kg = round(random.uniform(1, 5), 2)
            food = Food(food_type, amount_kg)
            self.menu.append(food)
    
    def waste(self, food):
        waste_item = Waste(food)
        self.waste_bin.append(waste_item)
        del food

    def print_menu(self):
        for food in self.menu:
            print(food)

    def print__bin(self):
        for waste in self.waste_bin:
            print(waste)