# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def deciToBinary(number):
    ans = list()
    rest = number % 2
    rez = number // 2
    ans.append(rest)
    while rez != 0:
        rest = rez % 2
        rez = rez // 2
        ans.append(rest)
    ans.reverse
    return ans


N = int(input('Insert number: '))
answer = deciToBinary(N)
print(N, ' in binary = ', *answer, sep='')

# А здесь можно переводить в любую систему с основанием меньше 10
# def deciToAny(number, base):
#     ans = list()
#     rest = number % base
#     rez = number // base
#     ans.append(rest)
#     while rez != 0:
#         rest = rez % base
#         rez = rez // base
#         ans.append(rest)
#     ans.reverse
#     return ans

# N = int(input('Insert number: '))
# b = int('Insert base < 10: ')
# answer = deciToAny(N, b)
# print(*answer, sep='')
