
from datetime import date
from typing import List


from .data_entries import Meal, Activity 

class Balance:
    def __init__(self, date_obj: date, target_calories: int):
        self.date = date_obj
        self.target_calories = target_calories
        self.meals: List[Meal] = []
        self.activities: List[Activity] = []

    def add_meal(self, meal: Meal):
        self.meals.append(meal)

    def add_activity(self, activity: Activity):
        self.activities.append(activity)

    def get_consumed_calories(self) -> float:
        return sum(m.calculate_total_calories() for m in self.meals)

    def get_burned_calories(self) -> float:
        return sum(a.calculate_calories_burned() for a in self.activities)

    def calculate_net_balance(self) -> float:
        return self.get_consumed_calories() - self.get_burned_calories()