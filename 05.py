# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21][Негафибоначчи]

def Fibo(number):
    if number == 1 or number == 2:
        return 1
    else:
        return Fibo(number - 1) + Fibo(number - 2)


N = int(input('Insert number: '))
ans = list()
for i in range(1, N + 1):
    ans.append(Fibo(i)*((-1)**(i+1)))
ans.reverse()
ans.append(0)
for i in range(1, N + 1):
    ans.append(Fibo(i))
print(*ans)
