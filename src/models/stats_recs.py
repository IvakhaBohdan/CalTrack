
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
    
class Stats:
    def __init__(self, history: List[Balance]):
        self.history = history

    def get_average_daily_intake(self) -> float:
        if not self.history:
            return 0
        total_intake = sum(day.get_consumed_calories() for day in self.history)
        return round(total_intake / len(self.history))

    def check_goal_progress(self) -> dict:
        days_met_target = sum(1 for day in self.history if day.calculate_net_balance() <= day.target_calories)
        return {
            'total_days': len(self.history),
            'met_target_days': days_met_target
        }

    def get_reports(self) -> str:
        avg = self.get_average_daily_intake()
        progress = self.check_goal_progress()

        report = f"Звіт за {progress['total_days']} днів:\n"
        report += f"  Середнє споживання: {avg} ккал/день.\n"
        report += f"  Днів досягнення цілі: {progress['met_target_days']}."
        return report