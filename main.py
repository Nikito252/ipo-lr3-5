num = int(input("Введите целое число: "))

#тернарное выражение 
absolute_value = num if num >= 0 else -1 * num
print("Абсолютное значение числа:", absolute_value)
