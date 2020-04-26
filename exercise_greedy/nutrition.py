
class Food:
    def __init__(self, name, protein, fat, carbs, calories):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.calories = calories
        self.set_fraction(1.0)
        
    def set_fraction(self, fraction):
        self.fraction = fraction
        self.protein_calories = 4 * fraction * self.protein
        self.carbs_calories = 4 * fraction * self.carbs
        self.fat_calories = 9 * fraction * self.fat
        self.calories = fraction * self.calories
        
    def __str__(self):
        return "[%0.4f] %s (P=%s,C=%s,F=%s,E=%s)" % (self.fraction, self.name, self.protein, self.carbs, self.fat, self.calories)
        

class MealPlan:
    def __init__(self):
        self.foods = []
        self.total_calories = 0.0
        self.total_protein_calories = 0.0
        self.total_carbs_calories = 0.0
        self.total_fat_calories = 0.0
        
    def add_food(self, food):
        self.foods.append(food)
        self.total_protein_calories += food.protein_calories
        self.total_carbs_calories += food.carbs_calories
        self.total_fat_calories += food.fat_calories
        self.total_calories += food.calories

    def percent_nutrient(self, nutrient): 
        """Returns the current percent value of given nutrient in current meal plan."""
        if self.total_calories > 0.0:
            return getattr(self, f"total_{nutrient}_calories") / self.total_calories
        else:
            return 0.0
    
    def calories_with_food(self, food):
        """Returns the total calories with food if the given food were added."""
        return self.total_calories + food.calories
        
    def percent_nutrient_with_food(self, food, nutrient):
        """Returns the percent nutrient value if the given food were added."""
        if self.total_calories + food.calories > 0.0:
            return (getattr(self, f"total_{nutrient}_calories") + getattr(food, f"{nutrient}_calories")) / (self.total_calories + food.calories)
        else:
            return 0.0

    def fraction_to_fit_calories_limit(self, food, calorie_limit):
        """Returns the fraction (0.0-1.0) of the food required to get to the calorie limit."""
        if self.calories_with_food(food) <= calorie_limit:
            return 1.0
        fraction = 1.0
        calories = food.calories
        f = Food(food.name, food.protein, food.fat, food.carbs, food.calories)
        while self.calories_with_food(f) > calorie_limit and fraction > 0.05:
            fraction -= 0.01
            fraction = round(fraction, 4)
            f = Food(food.name, food.protein, food.fat, food.carbs, food.calories)
            f.set_fraction(fraction)
        return fraction
        
    def fraction_to_fit_nutrient_goal(self, food, nutrient, goal):
        """Returns the fraction (0.0-1.0) of the food required to get to the nutrient goal."""
        percent_n = self.percent_nutrient_with_food(food, nutrient)

        if percent_n <= goal:
            return 1.0
        
        fraction = 1.0
        while percent_n > goal and fraction > 0.05:
            fraction -= 0.001
            f = Food(food.name, food.protein, food.fat, food.carbs, food.calories)
            f.set_fraction(fraction)
            percent_n = self.percent_nutrient_with_food(f, nutrient)
        return round(fraction, 5)

    def meets_calorie_limit(self, calorie_limit, threshold):
        """
        Returns True if the total calories of the current meal plan
        is within the specified threshold of the given calorie limit.
        """
        diff = abs(calorie_limit - self.total_calories)
        return round(diff, 3) <= threshold
        
    def meets_nutrient_goal(self, nutrient, goal, threshold):
        """
        Returns True if the total calorie contribution (by percent) of the
        given nutrient ('protein', 'carbs' or 'fat') for the current
        meal plan is within the specified threshold of the given goal.
        """
        diff = abs(goal - self.percent_nutrient(nutrient))
        diff = round(diff, 3)
        return diff <= threshold

    def __str__(self):
        s = ""
        if len(self.foods) == 0: return "Empty Plan"
        item = 1
        for food in self.foods:
            s += "%d: %s\n" % (item, food)
            item += 1
        
        s += "Total Calories: %s\n" % self.total_calories
        s += "\tProtein: %s\n" % self.percent_nutrient("protein")
        s += "\tCarbs: %s\n" % self.percent_nutrient("carbs")
        s += "\tFat: %s" % self.percent_nutrient("fat")

        return s
