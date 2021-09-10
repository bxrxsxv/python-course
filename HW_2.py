import random

# 1) Создал 2 переменных типа String с разными значениями
str1 = 'str1'
str2 = 'str2'

# 2) Создал 4 переменных типа Integer с разными значениями
int1 = 1
int2 = 2
int3 = 3
int4 = 4

# 3) Создал 3 переменных типа Float с разными значениями
float1 = 1.1
float2 = 2.2
float3 = 3.3

# 4) Реализовал 15 вариантов сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты вывел в консоль.
print('int1 > int2? -', int1 > int2)
print('int1 < int2? -', int1 < int2)
print('int1 >= int2? -', int1 >= int2)
print('int1 <= int2? -', int1 <= int2)
print('int1 != int2? -', int1 != int2)
print('---')
print('int1 > int3? -', int1 > int3)
print('int1 < int3? -', int1 < int3)
print('int1 >= int3? -', int1 >= int3)
print('int1 <= int3? -', int1 <= int3)
print('int1 != int3? -', int1 != int3)
print('---')
print('int1 > int4? -', int1 > int4)
print('int1 < int4? -', int1 < int4)
print('int1 >= int4? -', int1 >= int4)
print('int1 <= int4? -', int1 <= int4)
print('int1 != int4? -', int1 != int4)
print('---')

# 5) Реализовал 10 вариантов сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты вывел в консоль.
print('float1 > float2? -', float1 > float2)
print('float1 < float2? -', float1 < float2)
print('float1 >= float2? -', float1 >= float2)
print('float1 <= float2? -', float1 <= float2)
print('float1 != float2? -', float1 != float2)
print('---')
print('float1 > float3? -', float1 > float3)
print('float1 < float3? -', float1 < float3)
print('float1 >= float3? -', float1 >= float3)
print('float1 <= float3? -', float1 <= float3)
print('float1 != float3? -', float1 != float3)
print('---')

# 6) Реализовал 10 вариантов сравнения int переменных с операторами >, <, >=, <=, != и
# условными выражениями (and, or, not). Pезультаты вывести в консоль.
print('not int1 > int2 and int3 > int4? -', not int1 > int2 and int3 > int4)
print('int1 < int2 and int3 < int4? -', int1 < int2 and int3 < int4)
print('int1 >= int2 and int3 >= int4? -', int1 >= int2 and int3 >= int4)
print('int1 <= int2 and int3 <= int4? -', int1 <= int2 and int3 <= int4)
print('int1 != int2 and not int3 != int4? -', int1 != int2 and not int3 != int4)
print('---')
print('not int1 > int2 or int3 > int4? -', not int1 > int2 or int3 > int4)
print('int1 < int2 or int3 < int4? -', int1 < int2 or int3 < int4)
print('int1 >= int2 or int3 >= int4? -', int1 >= int2 or int3 >= int4)
print('int1 <= int2 or int3 <= int4? -', int1 <= int2 or int3 <= int4)
print('int1 != int2 or not int3 != int4? -', int1 != int2 or not int3 != int4)
print('---')

# 7) Сделал скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Выводить должна "Вы ввели число = (введённое число), которое (меньше/больше/равно) 30"

def compare():
  number = input('Введите число: ')

  if number < '30':
    print('Вы ввели число = {0}, которое меньше 30'.format(number))
  elif number > '30':
    print('Вы ввели число = {0}, которое больше 30'.format(number))
  elif number == '30':
    print('Вы ввели число = {0}, которое равно 30'.format(number))

# 8) Сделал скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы ввели число = (введённое число), которое (меньше/больше/равно) сгенерированному числу"

def random_compare():
  number = input('Введите число: ')
  x = str(random.randint(1, 100))

  if number < x:
    print('Вы ввели число = {0}, которое меньше {1}'.format(number, x))
  elif number > x:
    print('Вы ввели число = {0}, которое больше {1}'.format(number, x))
  elif number == x:
    print('Вы ввели число = {0}, которое равно {1}'.format(number, x))

# 9) Сделал скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы ввели число = (введённое число), которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"

def random_compare2():
  number = input('Введите число: ')
  x1 = str(random.randint(1, 100))
  x2 = str(random.randint(1, 100))

  if number < x1:
    if number < x2:
      print('Вы ввели число = {0}, которое меньше {1} и меньше {2}'.format(number, x1, x2))
    elif number > x2:
      print('Вы ввели число = {0}, которое меньше {1} и больше {2}'.format(number, x1, x2))
    elif number == x2:
      print('Вы ввели число = {0}, которое меньше {1} и равно {2}'.format(number, x1, x2))
  elif number > x1:
    if number < x2:
      print('Вы ввели число = {0}, которое больше {1} и меньше {2}'.format(number, x1, x2))
    elif number > x2:
      print('Вы ввели число = {0}, которое больше {1} и больше {2}'.format(number, x1, x2))
    elif number == x2:
      print('Вы ввели число = {0}, которое больше {1} и равно {2}'.format(number, x1, x2))
  elif number == x1:
    if number < x2:
      print('Вы ввели число = {0}, которое равно {1} и меньше {2}'.format(number, x1, x2))
    elif number > x2:
      print('Вы ввели число = {0}, которое равно {1} и больше {2}'.format(number, x1, x2))
    elif number == x2:
      print('Вы ввели число = {0}, которое равно {1} и равно {2}'.format(number, x1, x2))

compare()
random_compare()
random_compare2()