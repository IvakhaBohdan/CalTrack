import sys
import os
import pygame
from datetime import date

from models.user_goals import User
from models.data_entries import Product, Meal, Activity
from models.stats_recs import Balance, Recs

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CalTrack: Демонстрація Повної Моделі (15/15 Карток)")
font = pygame.font.Font(None, 30)
text_color = (255, 255, 255) 
background_color = (0, 50, 100)
line_spacing = 30


# Створення користувача (Картка #2, #3)
test_user = User(
    name="Богдан", 
    age=25, 
    gender="Male", 
    height=178, 
    weight=80, 
    activityLevel="moderate", 
    goal="loss"
)
target_cal = test_user.daily_calories_target

# Створення продуктів (Картка #4)
p_chicken = Product("Куряче філе", 165, 31, 3.6, 0)
p_rice = Product("Рис", 130, 2.7, 0.3, 28.6)
p_apple = Product("Яблуко", 95, 0.5, 0.3, 25)

# Створення прийому їжі (Картка #5)
lunch = Meal("Обід", "13:00", [p_chicken, p_rice])
consumed_cal = lunch.calculate_total_calories()

# Створення активності (Картка #6)
run = Activity("running", 30) # 30 хвилин бігу
burned_cal = run.calculate_calories_burned()

# Створення балансу за день (Картка #7, #8)
today_balance = test_user.get_today_balance()
today_balance.add_meal(lunch)
today_balance.add_activity(run)
today_balance.add_meal(Meal("Перекус", "16:00", [p_apple]))

net_balance = today_balance.calculate_net_balance()

# Генерація рекомендації (Картка #10)
recommender = Recs(today_balance)
recommendation = recommender.get_daily_recommendation()



y_pos = 50
def render_text(surface, text, x, y, font, color):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))
    return y + line_spacing

y_pos = render_text(screen, "--- CalTrack: Демонстрація Логіки Моделі ---", 50, y_pos, font, (255, 255, 0))
y_pos = render_text(screen, f"Користувач: {test_user.name} ({test_user.age} р.), Ціль: {test_user.goal.upper()}", 50, y_pos, font, text_color)
y_pos = render_text(screen, f"Цільова норма (TDEE): {target_cal} ККАЛ", 50, y_pos, font, (0, 255, 0))
y_pos = render_text(screen, "-" * 50, 50, y_pos, font, text_color)

y_pos = render_text(screen, f"1. Дані (Meal, Activity):", 50, y_pos, font, (255, 150, 0))
y_pos = render_text(screen, f"   Обід: {lunch.meal_type} - {lunch.calculate_total_calories()} ккал (Картка #5)", 50, y_pos, font, text_color)
y_pos = render_text(screen, f"   Активність: {run.activity_type} - Спалено {burned_cal} ккал (Картка #6)", 50, y_pos, font, text_color)
y_pos += line_spacing / 2

y_pos = render_text(screen, f"2. Аналіз (Balance, Recs):", 50, y_pos, font, (255, 150, 0))
y_pos = render_text(screen, f"   Спожито за день: {today_balance.get_consumed_calories()} ккал", 50, y_pos, font, text_color)
y_pos = render_text(screen, f"   Спалено за день: {today_balance.get_burned_calories()} ккал", 50, y_pos, font, text_color)
y_pos = render_text(screen, f"   Чистий Баланс: {round(net_balance)} ккал (Картка #7)", 50, y_pos, font, text_color)
y_pos += line_spacing / 2

y_pos = render_text(screen, f"3. Рекомендація:", 50, y_pos, font, (255, 150, 0))
y_pos = render_text(screen, f"   -> {recommendation}", 50, y_pos, font, (255, 255, 255))
y_pos += line_spacing * 2


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background_color)
    
    y_pos_reset = 50
    render_text(screen, "CalTrack: Демонстрація Моделі ", 50, y_pos_reset, font, (255, 255, 0))
    y_pos_reset = render_text(screen, f"Користувач: {test_user.name} ({test_user.age} р.), Ціль: {test_user.goal.upper()}", 50, y_pos_reset + line_spacing, font, text_color)
    y_pos_reset = render_text(screen, f"Цільова норма (TDEE): {target_cal} ККАЛ", 50, y_pos_reset + line_spacing, font, (0, 255, 0))
    y_pos_reset = render_text(screen, "-" * 50, 50, y_pos_reset + line_spacing, font, text_color)
    
    y_pos_reset = render_text(screen, f"1. Дані (Meal, Activity):", 50, y_pos_reset + line_spacing, font, (255, 150, 0))
    y_pos_reset = render_text(screen, f"   Обід: {lunch.meal_type} - {lunch.calculate_total_calories()} ккал", 50, y_pos_reset + line_spacing, font, text_color)
    y_pos_reset = render_text(screen, f"   Активність: {run.activity_type} - Спалено {burned_cal} ккал ", 50, y_pos_reset + line_spacing, font, text_color)
    
    y_pos_reset = render_text(screen, f"2. Аналіз (Balance, Recs):", 50, y_pos_reset + line_spacing + 15, font, (255, 150, 0))
    y_pos_reset = render_text(screen, f"   Спожито за день: {today_balance.get_consumed_calories()} ккал", 50, y_pos_reset + line_spacing, font, text_color)
    y_pos_reset = render_text(screen, f"   Спалено за день: {today_balance.get_burned_calories()} ккал", 50, y_pos_reset + line_spacing, font, text_color)
    y_pos_reset = render_text(screen, f"   Чистий Баланс: {round(net_balance)} ккал", 50, y_pos_reset + line_spacing, font, text_color)

    y_pos_reset = render_text(screen, f"3. Рекомендація :", 50, y_pos_reset + line_spacing + 15, font, (255, 150, 0))
    render_text(screen, f"   -> {recommendation}", 50, y_pos_reset + line_spacing, font, (255, 255, 255))
    
    pygame.display.flip()

pygame.quit()
sys.exit()