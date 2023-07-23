
# Задача 10
#
# import random
#
# N = int(input("input N: "))
# list_monet = [random.randint(0, 1) for i in range(N)]
# print(min(list_monet.count(0), list_monet.count(1)))
#
# Задача 12
#
# S = int(input("input summ: "))
# P = int(input("input multi: "))
#
# N = 1000
#
# for i in range(N):
#     for j in range(N):
#         if i * j == P and i + j == S:
#             print(i, j)
#             exit()
#
# Задача 14
#
# N = int(input("input N: "))
#
# list_power_2 = [2 ** i for i in range(N) if 2 ** i < N]
# print(list_power_2)


# Задача 1 необязательная
#
# def sum_digits(n):
#     return n % 10 + sum_digits(n // 10) if n > 9 else n
#
#
# numb = float(input("input int or float number: "))
# while numb - int(numb) > 0:
#     numb *= 10
#
# print(int(sum_digits(numb)))

# Задача 2 необязательная
#
# import time
#
# t = time.perf_counter_ns()
# N = 100
# size = random.randint(3, 15)
#
# for i in range(N):
#     list_of_pred = [random.choice([True, False]) for i in range(size)]
#     A = True
#     B = False
#
#     for j in range(size):
#         A = A and list_of_pred[j]
#         B = B or (not list_of_pred[j])
#     if (not A) == B:
#         print("TRUE")
#     else:
#         print("FALSE")
#
# print(f"predicate quantity = {size}")
# print(f"time = {time.perf_counter_ns() - t} nanoseconds")
#
# Задача 3 необязательная
#
# def all_divisors(n):
#     if n <= 0:
#         return []
#     divisors = [1, n]
#     for div in range(1, int(n ** 0.5 + 1)):
#         if n % div == 0:
#             divisors.extend([n // div, div])
#     return sorted(list(set(divisors)))
#
#
# N = int(input("input N: "))
# print(f'All divisors of N: {all_divisors(N)}')
