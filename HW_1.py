# 1-9) Создал переменные различных типов
string = 'string'
integer = 1
float_ = 2.1
bytes_ = b'bytes'
list_ = []
tuple_ = ()
set_ = {'h', 'e', 'l', 'l', 'o'}
frozenset_ = frozenset('hello')
dict_ = {}

# 10) Вывел в консоль все выше перечисленные переменные с добавлением типа данных.
print(string, type(string))
print(integer, type(integer))
print(float_, type(float_))
print(bytes_, type(bytes_))
print(list_, type(list_))
print(tuple_, type(tuple_))
print(set_, type(set_))
print(frozenset_, type(frozenset_))
print(dict_, type(dict_))

# 11) Создал 2 переменные String, создал переменную в которой суммирую эти переменные. Вывел в консоль.

str1 = 'qwe'
str2 = 'rty'
str3 = str1 + str2
print(str3)

# 12) Создал 2 переменные Integer, создал переменную в которой суммирую эти переменные. Вывел в консоль.

int1 = 11
int2 = 2
int3 = int1 + int2
print(int3)

# 13) Создал переменную в которой Разделил эти переменные Int. Вывел в консоль.

int4 = int1 / int2
print(int4)

# 14) Создал переменную в которой Умножил эти переменные Int. Вывел в консоль.

int5 = int1 * int2
print(int5)

# 15) Создал переменную в которой Разделил без остатка эти переменные Int. Вывел в консоль.

int6 = int1 // int2
print(int6)

# 16) Создал переменную в которую присвоил остаток от деления этих переменные Int. Вывел в консоль.

int7 = int1 % int2
print(int7)