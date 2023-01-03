# name=input("Введите имя ")
# name_start=name[0].upper()
# name_end=name[1:].lower()
# res=name_start+name_end
# print(res)

# name='Ivan'
# for i in name:
#     print (i)


# exm = 'Привет мир'
# count = 0
# for i in exm:
#      if i == 'и':
#         count = count + 1
# print (count, 'буквы "и" в данной строке ')

# проверка на вхождения
# in - not in
# a='hello'
# b='hello world'
# print (a in b)

# format
# {}
# string = "{}, {}, {}".format('Петя', 'Ваня', 'Катя')
# print(string)

# порядок с позиционными аргументами
# string = "{1}, {0}, {2}".format('Петя', 'Ваня', 'Катя')
# print(string)
# порядок по ключевым словам
# string = "{s}, {b}, {j}".format(j='Петя', b='Ваня', s='Катя')
# print(string)

# f- строки (передача динамически внутри строки переменной)
# a = 'Ivan'
# res = f'{a}, hello'
# print(res)

# List - [], list()
# people = ['Ivan', 'Tom', 'Kate']
# for person in people^
#     prit(person) # перебор элементов
# numbers_1 = list()
# print(numbers [5] * 6) #6 раз по 5

# Methods list
# append(item)
# people = ['Ivan', 'Tom', 'Kate']
# new_person = people.append ('Bob')
# print(people)

# insert (item) добавляет элемент в список по индексу
# people = ['Ivan', 'Tom', 'Kate']
# new_person = people.append ('Bob')
# print(people.insert(1,'Bill'))
# print(people)

# remove(item) удаление первого найденного элемента
# print(people.remove('Bill'))
# print(people)

# in
# people = ['Ivan', 'Tom', 'Kate']
# if 'Tom' in people:
#     people.remove('Tom')
# print(people)

# count()
# people = ['Ivan', 'Tom', 'Kate', 'Tom']
# people_count = people.count('Tom')
# print(people_count)

# список в списке
# people = [
#     ['Ivan', 29],
#     ['Kate', 27],
#     ['Bob', 32]
#
# ]
# print(people[0][1]) # обращение к первому элементу 0 списка
# for person in people:
#     for item in person:
#         print(item) # элеметы вложенного списка


# tuple () кортеж, неизменяемый
# Словари {keys:value}
# dict() функция для преобразования в словарь
# users = {1: 'Tom', 2: 'Bob', 3: 'Kate'}
# # users[1] = 'Tom2'
# # print(users)
# key = 2
# if key in users:
#     user = users [key]
#     print(user)
# else:
#     print('Результат не найден')

# get()
# users = {1: 'Tom', 2: 'Bob', 3: 'Kate'}
# users_1 = users.get(3)
# print(users_1)

# items()
# users = {1: 'Tom', 2: 'Bob', 3: 'Kate'}
# for key, value in users.items():
#     print (key,value) # ркасиво вытащить пару ключ-значение

# множества set() (можно вытаскивать дубликаты)
# users = {'Tom','Bob', 'Kate'}
# # print(len(users))
# users.add('Sam')
# print(users)

# union() объединяет 2 множества и возвращает новое множество
# users_1 = {'Tom','Bob', 'Kate'}
# users_2 = {'Sam','Kate', 'Bob'}
# users_3 = users_1.union(users_2)
# # intersection() пересечение возвращает новое множество
# users_4= users_1.intersection(users_2)
# users_5 = users_1.difference(users_2) #разность
# users_6 = users_1.symmetric_difference(users_2)
# print(users_4)

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада '))
deposit = []
for key in per_cent: deposit.append(per_cent[key] * money / 100)
max_deposit = max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))