"""
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств
"""

def check_input(massege):

    num = input(massege)

    is_correct = False
    while(is_correct == False):
        if (num.isdigit()):
            if(0 < int(num)):
                is_correct = True
            else:
                print('Похоже вы ввели не число\n')
                num = input(massege)
        else:
            print('Упс :(\n Вы ввели не число, а что-то другое\n')
            num = input(massege)
    return num

n = int(check_input("Введите количество чисел первого множества\n"))

listn = list()

for i in range(n):
    x = int(check_input(f"Введите число {i + 1} первого множества\n"))
    listn.append(x)

m = int(check_input("Введите количество чисел второго множества\n"))

listm = list()

for i in range(m):
    x = int(check_input(f"Введите число {i + 1} второго множества\n"))
    listm.append(x)
    

listres = list(filter(lambda x:x in listn, listm))

listres.sort

print(listres)
