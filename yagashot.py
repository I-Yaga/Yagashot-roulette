import random


def generate_shells():
    length = random.randint(2, 8)  # количество патронов (от 1 до 8)
    
    while True:
        shells = [random.choice([True, False]) for _ in range(length)]
        
        # Проверяем, чтобы не было только True или только False
        if not (all(shells) or not any(shells)):
            return shells


shells = generate_shells()
print(shells)

storms = 0
blanks = 0

for i in shells:
    if i == True:
        storms += 1
    
    else:
        blanks += 1


print("Холостые:", blanks)
print("Боевые:", storms)

player_lives = 5
dealer_lives = 5


def game():


    print("Твои жизни:", player_lives)
    print("Жизни дилера:", dealer_lives)

    def players_turn():
        if player_lives > 0 and dealer_lives > 0 and len(shells) > 0:
            print("Твой ход! В кого стреляем? 1: в себя, 2: в дилера:")

            while True:
                players_choice = input()

                if players_choice == "1":
                    current_shell = shells.pop()
                    
                    if current_shell == True:
                        player_lives -= 1
                        print("Патрон оказался боевым! Теперь у тебя", player_lives, "hp. Теперь ход дилера!")
                        break
                    
                    else:
                        print("Патрон был холостым! В кого стреляем дальше?")
                
                elif players_choice == "2":
                    current_shell = shells.pop()

                    if current_shell == True:
                        dealer_lives -= 1
                        print("Патрон был боевым! У дилера осталось", dealer_lives, "hp. Теперь ход дилера!")
                        break

                    else:
                        print("Патрон холостой! Теперь ход дилера!")
                        break

                else:
                    print("Введи 1 или 2!")
            
        elif player_lives == 0:
            print("Ты умер! ИГРА ОКОНЧЕНА.")

        elif dealer_lives == 0:
            print("Дилер умер! Ты победил!")

        elif len(shells) == 0:
            print("Патроны закончились! Новый раунд!")

    players_turn()


game()
