class Product:
    def __init__(self, name: str, calories: float, proteins: float, fats: float, carbs: float):
        self.name = name
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbs = carbs

    def get_nutrients(self):
        return {
            'calories': self.calories,
            'proteins': self.proteins,
            'fats': self.fats,
            'carbs': self.carbs
        }
    
class Meal:
    def __init__(self, meal_type: str, time: str, products: list):
        self.meal_type = meal_type 
        self.time = time
        self.products = products  

    def calculate_total_calories(self) -> float:
        total_cal = sum(p.calories for p in self.products)
        return total_cal

    def calculate_total_nutrients(self) -> dict:
        total = {'proteins': 0, 'fats': 0, 'carbs': 0}
        for p in self.products:
            total['proteins'] += p.proteins
            total['fats'] += p.fats
            total['carbs'] += p.carbs
        return total