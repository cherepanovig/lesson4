my_string = input("Напишите страну Вашего рождения: ")
print(my_string)
print('Количество символов: ', len(my_string))
print(my_string.upper())
# Так как название страны негоже писать в нижнем регистре, то первую букву оставим заглавной
print(my_string.lower().capitalize())
# Команда для удаления пробелов
print('Россия - великая страна'.replace(' ', ''))
# Первый символ
print(my_string[0])
# Последний символ
print(my_string[len(my_string)-1])
