class Goals:
    ACTIVITY_FACTORS = {
        "sedentary": 1.2,       # Сидячий спосіб життя
        "light": 1.375,         # Легка активність
        "moderate": 1.55,       # Помірна активність
        "high": 1.725,          
    }

    def calculateDailyCalories(self, user_data):
        
        # 1. Визначення базового метаболізму (BMR)
        bmr = (10 * user_data['weight']) + (6.25 * user_data['height']) - (5 * user_data['age'])
        
        if user_data['gender'].lower() == 'male':
            bmr += 5
        else: 
            bmr -= 161
            
        # 2. Застосування коефіцієнта активності
        activity_factor = self.ACTIVITY_FACTORS.get(user_data['activityLevel'].lower(), 1.2)
        tdce = bmr * activity_factor 

        # 3. Коригування під ціль (-15% для втрати, +15% для набору)
        if user_data['goal'].lower() == 'loss':
            tdce *= 0.85
        elif user_data['goal'].lower() == 'gain':
            tdce *= 1.15
            
        return round(tdce)


class User:
    
    def __init__(self, name, age, gender, height, weight, activityLevel, goal):
        self.name = name
        self.age = age 
        self.gender = gender 
        self.height = height 
        self.weight = weight 
        self.activityLevel = activityLevel
        self.goal = goal
        self.daily_calories_target = Goals().calculateDailyCalories(self.__dict__)
        self.meal_history = []
        self.activity_history = []


user1 = User("Богдан", 25, "Male", 178, 80, "moderate", "loss")
print(f"Ціль калорій для {user1.name}: {user1.daily_calories_target} ккал")