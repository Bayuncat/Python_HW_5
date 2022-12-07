import random
from random import randint

# Функция выбора игроков из консоли (человек-Бот или человек-человек)
def whoPlays():
   while True:
        try:
            wp = int(input(f'Как будем играть:\n1 - с умным ботом,\n2 - с другом\n:'))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        else:
            if wp==1: 
                players = ["Кеша", "Bot"]
                return players
            elif wp==2: 
                players = ["Кеша", "Амредин"]
                return players
            print("Попробуйте еще раз ввести: один или два")

# Определились с выбором игроков
players = whoPlays()
print(f'Играют 2 игрока: {players}\n')

# Разыгрываем чей ход будет первым 
whoFirst = random.choice([True, False])
player1 = players[int(whoFirst)]
player2 = players[int(not whoFirst)]

# Здесь можно вручную задать общее число конфет и каким будет максимальный ход
bonbon = 2021
stepLimit = 28

# Разделяю код программы на варианты игры, в порядке первого хода (бот-человек, человек-бот, человек-человек)
if (player1 == "Bot"): variant = 1
elif (player2 == "Bot"): variant = 2
else: variant = 3

# Метод проверки значения вводимого человеком
def checkConditions(total, player):
   while True:
        try:
            a = int(input(f'Твой ход {player}, конфет осталось {total}: '))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        else:
            if ((a <= stepLimit) and (a >= 1) and (a <= total)):
                return a
            print("Столько конфет взять невозможно по правилам игры, попробуйте еще раз")

# Стратегия выигрыша Бота (botStrategy): 
# 1. Если остается конфет меньше или равно лимиту, то забирай все что есть
# 2. При условии не выполнения п.1 на любом ходе при делении числа оставшихся конфет на (лимит+1) остаток = 0, то выбирай рандомно,
# может человек ошибется и тогда сработает п.3.
# 3. При условии не выполнения п.1 и п.2 на любом ходе при делении числа оставшихся конфет на (лимит+1) остаток > 0, бери остаток.

def botStrategy(total):
    if total <= stepLimit:
        b = total
    elif total%(stepLimit+1) == 0:
        b = randint(1, stepLimit)
    elif (total%(stepLimit+1) >= 1):
        b = total%(stepLimit+1)
    return b

print(f'У нас есть {bonbon} конфет.\nЗа один ход можно брать не менее 1 конфеты и не более {stepLimit} конфет.\nПервым ходит: {player1}\nВторым ходит: {player2}\n')

# Здесь я разделяю игры на 3 варианта, нарушая принцип DRY. Но пока не понимаю как сократить его в данной ситуации:

match variant:
# Игра: бот-человек: 
    case 1:
        while bonbon > 0:
              
              b = botStrategy(bonbon)
              bonbon -= b
              print(f'{player1} взял в сумме конфет: {b}. Их осталось: {bonbon}')
              if bonbon == 0: 
                    print(f'{player1} выиргал')
                    break

              a = checkConditions(bonbon, player2)
              bonbon -= a
              print(f'Ты взял в сумме конфет: {a}. Их осталось: {bonbon}')
              
              if bonbon == 0: 
                    print(f'{player2} выиргал')
                    break
                
    case 2:

# Игра: человек-бот:              
        while bonbon > 0:
              a = checkConditions(bonbon, player1)
              bonbon -= a
              print(f'Ты взял в сумме конфет: {a}. Их осталось: {bonbon}')
              if bonbon == 0: 
                    print(f'{player1} выиргал')
                    break

              b = botStrategy(bonbon)
              bonbon -= b
              print(f'{player2} взял в сумме конфет: {b}. Их осталось: {bonbon}')
              if bonbon == 0: 
                    print(f'{player2} выиргал')
                    break

    case 3:
# Игра: человек-человек:                
        while bonbon > 0:
              a = checkConditions(bonbon, player1)
              bonbon -= a
              print(f'Ты взял в сумме конфет: {a}. Их осталось: {bonbon}')
              if bonbon == 0: 
                    print(f'{player1} выиргал')
                    break

              b = checkConditions(bonbon, player2)
              bonbon -= b
              print(f'Ты взял в сумме конфет: {b}. Их осталось: {bonbon}')
              if bonbon == 0: 
                    print(f'{player2} выиргал')
                    break

    case _:
        print("Ничего не получается")