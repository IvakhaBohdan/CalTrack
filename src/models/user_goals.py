from typing import List
from datetime import date

from .stats_recs import Balance 

class Goals:
    
    ACTIVITY_FACTORS = {
        "sedentary": 1.2,       
        "light": 1.375,         
        "moderate": 1.55,       
        "high": 1.725,          
    }

    def calculateDailyCalories(self, user_data: dict) -> int:
        
        bmr = (10 * user_data['weight']) + (6.25 * user_data['height']) - (5 * user_data['age'])
        
        if user_data['gender'].lower() == 'male':
            bmr += 5
        else:
            bmr -= 161
            
        activity_factor = self.ACTIVITY_FACTORS.get(user_data['activityLevel'].lower(), 1.2)
        tdce = bmr * activity_factor 

        if user_data['goal'].lower() == 'loss':
            tdce *= 0.85
        elif user_data['goal'].lower() == 'gain':
            tdce *= 1.15
            
        return round(tdce)


class User:
    
    def __init__(self, name: str, age: int, gender: str, height: float, weight: float, activityLevel: str, goal: str):
        self.name = name
        self.age = age          
        self.gender = gender    
        self.height = height    
        self.weight = weight    
        self.activityLevel = activityLevel
        self.goal = goal
        
        user_data = self.__dict__.copy()
        self.daily_calories_target: int = Goals().calculateDailyCalories(user_data) 
        
        self.history: List[Balance] = [] 
        self.custom_products = [] 

    def get_today_balance(self) -> Balance:
        today = date.today()
        return Balance(today, self.daily_calories_target)

    def add_custom_product(self, product):
        self.custom_products.append(product)
        return f"Продукт '{product.name}' додано до власних."