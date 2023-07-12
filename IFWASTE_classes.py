import random

class Food:

    def __init__(self, foodType, amount_kg):
        self.type = foodType
        self.amount_kg = amount_kg
        # Determine the kcal_per_kg and expiration_time of a food
        if self.type == "Dairy & Eggs":
            self.kcal_per_kg = random.gauss(1814, 1098)
            self.expiration_time = 7*random.uniform(1, 4)
        elif self.type == "Meat & Fish":
            self.kcal_per_kg = random.gauss(2240, 980)
            self.expiration_time = random.uniform(3, 11)
        elif self.type == "Dry Foods & Baked Goods":
            self.kcal_per_kg = random.gauss(3361,1233) 
            self.expiration_time = 7*random.uniform(1, 8)
        elif self.type == "Fruits and Vegetables":
            self.kcal_per_kg = random.gauss(787.5, 736)
            self.expiration_time = random.uniform(5.5, 14.5) 
        elif self.type == "Snacks, Condiments, Liquids, Oils, Grease, and Other":
            self.kcal_per_kg = random.gauss(2793, 1990) 
            self.expiration_time = 30*random.uniform(3,18)
        elif self.type == "Cooked/Prepared Items/Leftovers":
            self.kcal_per_kg = random.gauss(1300, 200) #assumed ready to eat or frozen from the store
            self.expiration_time = random.uniform(4,11)
        else :
            raise ValueError("Not a listed Food Class")

    def decay(self):
        self.expiration_time -= 1 # decays one day at a time

    def __str__(self): 
        return(f"Food: {self.type}, Amount: {self.amount_kg} kg")


class Waste:
    def __init__(self, food: Food):
        self.type = food.type # stores the FW category
        self.amount_kg = food.amount_kg # amount in kilograms

    def __str__(self):
        return f"Waste category: {self.type}, Amount: {self.amount_kg}"


class House:
    def __init__(self):
        self.members_adult = random.randint(1, 3) # income earning/providing members
        self.members_dependent = random.randint(0, 3) # Children and elderly
        # kcal per meal based on members
        self.kcal = (self.members_adult*random.gauss(2144, 1308) + self.members_dependent*random.gauss(1800,1434))/3
        self.menu = [] # stores all of a households foods
        self.waste_bin = [] # the house trashcan
        self.shopping_frequency = random.randint(1,7) # how many days between shoppig trips

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
        for i in range(self.members_adult + self.members_dependent):
            food_type = random.choice(FLW_categories)
            amount_kg = round(random.uniform(1, 5), 2)
            food = Food(food_type, amount_kg)
            self.menu.append(food)
    
    def eat(self) :
        random.shuffle(self.menu)
        meal = self.kcal 
        for food in self.menu:
            if food.expiration_time >= 0 :
                self.waste(food)
            if meal > 0:
                if food.kcal_per_kg*food.amount_kg > meal:
                    food.amount_kg -= meal/food.kcal_per_kg
                else:
                    meal -= food.kcal_per_kg*food.amount_kg
                    self.menu.remove(food)
                    del food
            else:
                break

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
