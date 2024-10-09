from random import randint,choices
from time import sleep
from data import *

def fight(enemy):
    round = randint(1,2)
    enemy_hp = enemy["health"]

    print(f"Вы дерётесь с {enemy['name']}")
    print(f"{enemy['script']}")
    input("Нажмите Enter чтобы продолжить")
    print("")

    while player["health"] > 0 and enemy_hp > 0:
        if round == 1:
            print(f"{player['name']} атакует {enemy['name']}")
            if randint(1,100) <= player["luck"]:
                enemy_hp -= player['damage']*2.5
            else:
                enemy_hp -= player['damage']
            sleep(.5)
            print(f"У {enemy['name']} осталось {enemy_hp} жизней осталось!")
            print("")
            sleep(.5)
            round = 2
        else:
            print(f"{enemy['name']} атакует {player['name']}")
            player['health'] -= enemy['damage'][randint(0,enemy['damage'].index(max(enemy['damage'])))]*(player["armor"]+player["equipment"])
            sleep(.5)
            print(f"У {player['name']} осталось {player['health']} жизней осталось!")
            print("")
            sleep(.5)
            round = 1
    return player

def training(trainingType):
    if trainingType == 1 or trainingType == 2:
        for i in range(99):
            print("Тренировка завершена на",str(i+1)+"%")
            sleep(0.1)
        print("Тренировка завершена!")
    if trainingType == 1:
        player["damage"] += 1.5
        print("+1.5 к урону")
    elif trainingType == 2:
        player["armor"] -= 0.025
        print("+2.5% к защите")
    return player

def enemyStats(enemy):
    print("Имя:",enemy["name"])
    print("Жизни:",enemy["health"])
    print("Урон:",enemy["damage"])
    print("Приз: "+str(enemy["prize"])+"Д")

def playerStats():
    print("Имя:",player["name"])
    print("Защита защищает на:",(1-player['armor'])*100,"% + броня:",(1-player['equipment'])*100,"% = ",(1-player['armor'])*100+(1-player['equipment'])*100,"%")
    print("Максимальное здоровье:",player["maxHealth"])
    print("Здоровье:",player["health"])
    print("Урон:",player["damage"])
    print("Критический урон:",player["damage"]*2.5)
    print(f"Шанс на критический урон: {player['luck']}%")
    print(f"Баланс: {player['money']}Д")
    print("Инвентарь:")
    for i in player["inventory"]:
        print(player["inventory"].index(i)+1,"-",i)
    if "Аптечка" in player["inventory"]:
        use1 = int(input("""Использовать Аптечку?
0 - Нет    1 - Да
    """))
        if use1 == 1:
            player["health"] = player["maxHealth"]
            player["inventory"].remove("Аптечка")
            print("Использовано!")
    if "Святая вода" in player["inventory"]:
        use2 = int(input("""Использовать Святую воду?
0 - Нет    1 - Да
    """))
        if use2 == 1:
            player["maxHealth"] += 10
            player["health"] += 10
            player["inventory"].remove("Святая вода")
            print("Использовано!")
    if "Зелье удачи" in player["inventory"]:
        use3 = int(input("""Использовать Зелье удачи?
0 - Нет    1 - Да
    """))
        if use3 == 1:
            player["luck"] += 3
            player["inventory"].remove("Зелье удачи")
            print("Использовано!")
    return player

def casino():
    action = int(input(f"""Добро пожаловать в казино глупцов! Здесь вы можете выиграть 400Д с шансом 55%, но проиграть 400Д с шансом 45%, вы будете играть? (Сейчас у вас {player['money']})
0 - Нет    1 - Да
    """))
    if action == 1:
        if player['money'] >= 400:
            if randint(1,100) <= 90:
                player["money"] += choices([400,-400],weights=[55,45],k=1)[0]
            else:
                print("Джекпот!")
                player["money"] += 800
            print("Теперь у вас",player["money"])
        else:
            print("Недостаточно средств!")
    return player

def shop(action):
    if action == 1:
        if player['money'] >= 1000:
            player['inventory'].append("Аптечка")
            print("Приобретено")
            player["money"] -= 1000
        else:
            print("Недостаточно средств!")
    if action == 2:
        if player['money'] >= 1500:
            player['inventory'].append("Святая вода")
            print("Приобретено")
            player["money"] -= 1500
        else:
            print("Недостаточно средств!")
    if action == 3:
        if player['money'] >= 2000:
            player['inventory'].append("Зелье удачи")
            print("Приобретено")
            player["money"] -= 2000
        else:
            print("Недостаточно средств!")
    if action == 4:
        if player['money'] >= player['damage']*501:
            print("Приобретено")
            player["money"] -= player['damage']*501
            player['damage'] += 5
        else:
            print("Недостаточно средств!")
    return player
def equipmentShop(action):
    if action == 1:
        if player['money'] >= 1000:
            player['equipment'] = 0.99
            print("Приобретено и экипировано")
            player["money"] -= 1000
        else:
            print("Недостаточно средств!")
    if action == 2:
        if player['money'] >= 2000:
            player['equipment'] = 0.9725
            print("Приобретено и экипировано")
            player["money"] -= 1500
        else:
            print("Недостаточно средств!")
    if action == 3:
        if player['money'] >= 4000:
            player['equipment'] = 0.9775
            print("Приобретено и экипировано")
            player["money"] -= 2000
        else:
            print("Недостаточно средств!")
    return player