import time
def calculator():
    while True:
        result = 0
        try:
            znak = input("Введите один из 4 знаков: умножение(*), вычитание(-), сложение(+) или деление(/). Если хотите выйти напишите Quit. Поле ввода: ")
            if znak == "*" :
                first_number = float(input("Первое число для умножения: "))
                second_number = float(input("Второе число для умножения: "))
                result = first_number * second_number
                print(result)
            elif znak == "-":
                first_number = float(input("Первое число для вычитания: "))
                second_number = float(input("Второе число для вычитания: "))
                result = first_number - second_number
                print(result)
            elif znak == "+":
                first_number = float(input("Первое число для сложения: "))
                second_number = float(input("Второе число для сложения: "))
                result = first_number + second_number
                print(result)
            elif znak == "/":
                first_number = float(input("Первое число для деления: "))
                second_number = float(input("Второе число для деления: "))
                result = first_number / second_number
                print(result)
            elif znak.lower() == "quit":
                print("До встречи!")
                time.sleep(0.7)
                break
            else:
                print("Неизвестная операция. Используйте *, -, + или /")
                time.sleep(1.5)
                continue
        except ValueError:
            print("Калькулятор умеет работать только с числами")
            continue
        except ZeroDivisionError:
            print("Калькулятор не может делить на ноль")
            continue
                
calculator()