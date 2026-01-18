import random
import time


def generate_shells():
    length = random.randint(2, 8)  # количество патронов (от 2 до 8)
    
    while True:
        shells = [random.choice([True, False]) for _ in range(length)]
        
        if not (all(shells) or not any(shells)): # Проверяем, чтобы не было только True или только False
            break
    
    global storms
    global blanks

    storms = 0
    blanks = 0

    for i in shells:
        if i == True:
            storms += 1
    
        else:
            blanks += 1
    
    print("Холостые:", blanks)
    time.sleep(2)
    print("Боевые:", storms)
    time.sleep(2)
    
    return shells

def players_turn():
    global player_lives
    global dealer_lives
    global storms
    global blanks

    while True:
        if player_lives > 0 and dealer_lives > 0 and len(shells) > 0:    
            print("Твой ход! В кого стреляем? 1: в себя, 2: в дилера:")
            players_choice = input()
            time.sleep(2)

            if players_choice == "1":
                    print("Ты стреляешь в себя!")
                    time.sleep(2)
                    current_shell = shells.pop()
                    
                    if current_shell == True:
                        player_lives -= 1
                        storms -= 1
                        print("Патрон был боевым! Теперь у тебя", player_lives, "hp.")
                        time.sleep(2)
                        break
                    
                    else:
                        blanks -= 1
                        print("Патрон был холостым!")
                        time.sleep(2)
                
            elif players_choice == "2":
                    print("Ты стреляешь в дилера!")
                    time.sleep(2)
                    current_shell = shells.pop()

                    if current_shell == True:
                        dealer_lives -= 1
                        storms -= 1
                        print("Патрон был боевым! У дилера осталось", dealer_lives, "hp.")
                        time.sleep(2)
                        break

                    else:
                        blanks -= 1
                        print("Патрон холостой!")
                        time.sleep(2)
                        break

            else:
                print("Введи 1 или 2!")

        else:
            break


def dealers_turn():
    global player_lives
    global dealer_lives
    global storms
    global blanks

    while True:
        if player_lives > 0 and dealer_lives > 0 and len(shells) > 0:
            print("Ход дилера!")
            time.sleep(2)
            if storms > blanks:
                print("Дилер стреляет в тебя!")
                time.sleep(2)
                current_shell = shells.pop()

                if current_shell == True:
                    storms -= 1
                    player_lives -= 1
                    print("Патрон был боевым! Теперь у тебя", player_lives, "hp.")
                    time.sleep(2)
                    break

                else:
                    blanks -= 1
                    print("Повезло, патрон холостой!")
                    time.sleep(2)
                    break
            
            else:
                print("Дилер стреляет в себя!")
                time.sleep(2)
                current_shell = shells.pop()

                if current_shell == True:
                    storms -= 1
                    dealer_lives -= 1
                    print("Патрон был боевым! Теперь у дилера", dealer_lives, "hp.")
                    time.sleep(2)
                    break

                else:
                    blanks -= 1
                    print("Патрон был холостым!")
                    time.sleep(2)

        else:
            break

shells = generate_shells()

player_lives = 5
dealer_lives = 5

while player_lives > 0 and dealer_lives > 0:
    players_turn()

    if len(shells) == 0:
        print("Патроны закончились! Новый раунд!")
        time.sleep(2)
        shells = generate_shells()

    dealers_turn()

    if len(shells) == 0:
        print("Патроны закончились! Новый раунд!")
        time.sleep(2)
        shells = generate_shells()

if player_lives == 0:
    print("Ты умер! ИГРА ОКОНЧЕНА.")

else:
    print("Дилер умер! Ты победил!")
