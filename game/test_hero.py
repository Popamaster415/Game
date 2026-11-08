name1 = "Человек паук"
name2 = "Железный человек"
hp = 3

def greet():
    print(f"Привет! Я герой {name1}")
    print(f"Привет! Я герой {name2}")

def damage():
    global hp
    hp -= 1
    print(f"{name1} получил урон! Осталось жизней: {hp}")
    print(f"{name2} получил урон! Осталось жизней: {hp}")

greet()

damage()
damage()


