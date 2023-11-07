while True:
    try:
        number = int(input("введите трёхзначное число"))  # ввод данных
    except ValueError:
        print("что-то пошло не так")
        continue
    break

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

new_number = tens * 100 + hundreds * 10 + ones

print("Ответ", new_number)