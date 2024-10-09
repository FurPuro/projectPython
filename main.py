from random import randint,choices
from time import sleep
from data import *
import os
import json
from helpers import *

if not os.path.exists("accs"):
    os.makedirs("accs")

name = input("Введите имя: ")
current_enemy = 0
accPath = "accs/"+name+".acc"
acc = open(accPath,"a+")
acc.seek(0,os.SEEK_END)
if acc.tell():
    print("Аккаунт найден, читаем...")
    acc.seek(0)
    acc.close()
    acc = open(accPath,"r")
    newPlayer = json.loads(acc.readline())
    current_enemy = int(acc.readline(2))
    acc.close
else:
    print("Аккаунт не найден, создаём...")
    acc.seek(0)
    acc.close()
    current_enemy = 0
    newPlayer = {
        "name": name,
        "armor": 0.975,
        "health": 40.0,
        "maxHealth": 40.0,
        "damage": 2.0,
        "luck": 5,
        "inventory": [],
        "equipment": 1,
        "money": 1250.0
    }
change_player(newPlayer)

enemiesCount = 0
for i in enemies:
    enemiesCount += 1

print("Добро пожаловать в игру,",newPlayer["name"]+"!")

action = 0

while True:
    if current_enemy >= enemiesCount:
        print("Поздравляю, вы прошли игру и спасли своего отца от улья!")
        os.remove(accPath)
        break
    change_player(newPlayer)
    acc = open(accPath,"w")
    acc.writelines([json.dumps(newPlayer),"\n"+str(current_enemy)])
    acc.close()
    enemy = enemies[current_enemy]
    action = int(input('''Выберите действие:
0 - В бой!
1 - В магазин
2 - В казино глупцов
3 - Статистика игрока
4 - Статистика следующего врага
5 - Тренировка
6 - Магазин экипировки
    '''))
    print()
    if action == 0:
        newPlayer = fight(enemy)
        if newPlayer["health"] > 0:
            print(f"Ты победил! {enemy['win']}")
            newPlayer["money"] += enemy["prize"]
            current_enemy += 1
        else:
            print(f"Ты проиграл! {enemy['lose']}")
            os.remove(accPath)
            break
    elif action == 1:
        action2 = int(input(f"""Добро пожаловать в магазин! Выберите что хотите приобрести:
0 - Выйти
1 - Аптечка из целебных трав (восстанавливает максимальное здоровье) - 1000Д
2 - Святая вода (добавляет 10 к максимальному здоровью) - 1500Д
3 - Зелье удачи - 2000Д
4 - Улучшить оружие - {newPlayer['damage']*501}Д
    """))
        newPlayer = shop(action2)
    elif action == 2:
        newPlayer = casino()
    elif action == 3:
        newPlayer = playerStats()
    elif action == 4:
        enemyStats(enemy)
    elif action == 5:
        action2 = int(input("""Что вы хотите тренировать?
0 - Выйти
1 - Боксирования
2 - Отжимания
    """))
        newPlayer = training(action2)
    elif action == 6:
        action2 = int(input("""Добро пожаловать в магазин экипировки! Выберите что хотите приобрести:
0 - Выйти
1 - Кожаная броня (+1%) - 1000Д
2 - Золотая броня (+1.75%) - 1500Д
3 - Кольчужная броня (2.25%) - 2000Д
    """))
        newPlayer = equipmentShop(action2)
    print("")

# Сделать экипировку