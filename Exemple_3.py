"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
например декодирование
"""
print("Введите код\n")
code = input()

decode = ""

for i in range(len(code)):
    try:
        lenght = int(code[i])
        for j in range(lenght - 1):
            decode = decode + code[i + 1]
    except:
        decode = decode + code[i]

print(decode)