# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Если мы не учитываем целые числа
inp = list(map(float, input('Insert numbers: ').split()))
ans = list()
for i in inp:
    x = i - int(i)
    if x != 0:
        ans.append(round(x, 5))
print(max(ans) - min(ans))

# Если учитываем, т.е. дробная часть = 0
# inp = list(map(float, input('Insert numbers: ').split()))
# ans = list()
# for i in inp:
#     ans.append(round(i - int(i), 5))
# print(max(ans) - min(ans))
