print("Калькулятор v0.1 (alpha).")

def first_number():
    while True:
        first_digit = input("Введите первое число: ")

        if first_digit.isdigit():
            break
        else:
            print("Ошибка ввода, введите число.")
    
    return int(first_digit)

def second_number():
    while True:
        second_digit = input("Введите второе число: ")

        if second_digit.isdigit():
            break
        else:
            print("Ошибка ввода, введите число.")
    
    return int(second_digit)

def execution():
    while True:
        a = first_number()
        b = second_number()

        while True:
            operator = input("Введите оператор (+, -, *, /, ^): ")

            if operator == "+":
                print(a, "+", b, "=", a + b)
                break

            elif operator == "-":
                print(a, "-", b, "=", a - b)
                break

            elif operator == "*":
                print(a, "*", b, "=", a * b)
                break

            elif operator == "/":
                print(a, "/", b, "=", a / b)
                break

            elif operator == "^":
                print(a, "^", b, "=", a ** b)
                break

            else:
                print("Ошибка ввода, введите действительный оператор.")
                continue

        
        r = input("Заново? 1-да 2-нет: ")

        if r == "1":
            continue

        else:
            print("До свидания!")
            break


execution()
