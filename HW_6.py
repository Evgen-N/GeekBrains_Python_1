# Задача 30
#
# def arithmetic_progression(a1, n, d):
#     return d + arithmetic_progression(a1, n - 1, d) if n > 1 else a1
#
# A1 = int(input("input first element: "))
# N = int(input("input number of elements: "))
# D = int(input("input difference: "))
#
# print(arithmetic_progression(A1, N, D))

# Задача 32
#
# import random
#
# N = int(input("input the size of the list: "))
# LIST_MIN = int(input("input min: "))
# LIST_MAX = int(input("input max: "))
#
# spisok = [random.randint(0, 99) for i in range(N)]
# print(spisok)
# print('indexes of elements in range: ', [spisok.index(x) for x in spisok if x > LIST_MIN and x < LIST_MAX])
#
# Задача XO необязательная
# !Нолики никогда не проигрывают!
# import random
# from itertools import combinations
# import time
#
#
# def output(field):
#     # рисует игровое поле
#     print(' | '.join(field[:3]))
#     print(' | '.join(field[3:6]))
#     print(' | '.join(field[6:]), '\n', '\n')
#
#
# def f_your_step(rows, steps, your_steps):
#     # отображает ход игрока
#     print('Your turn')
#     test = True
#     while test:
#         col = int(input("input column: "))
#         row = int(input("input row: "))
#         your_step = row * rows + col
#         test = your_step in steps
#         if test is True:
#             print('Incorrect! Another cell, please.')
#
#     field[your_step] = 'X'
#     output(field)
#     steps.append(your_step)
#     your_steps.append(your_step)
#
#
# def f_comp_step(steps, comp_steps):
#     # рассчитывает и отображает ход компьютера
#     print('Computers turn')
#     if len(comp_steps) == 0:
#         if 4 not in steps:
#             comp_step = 4
#         else:
#             comp_step = 0
#     else:
#         comp_step = step_forecast(comp_steps, steps)
#         if comp_step == 10:
#             comp_step = step_forecast(your_steps, steps)
#         if comp_step == 10 and len(comp_steps) == 1:
#             comp_step = random.choice([i for i in {0, 2, 6, 8} if i not in steps])
#         elif comp_step == 10:
#             comp_step = random.choice([i for i in range(9) if i not in steps])
#     field[comp_step] = 'O'
#     time.sleep(1)
#     output(field)
#     steps.append(comp_step)
#     comp_steps.append(comp_step)
#
#
# def step_forecast(lst_1, lst_2):
#     # предсказывает наличие победного хода
#     for i in range(9):
#         your_step_forecast = lst_1.copy()
#         if i not in lst_2:
#             your_step_forecast.append(i)
#         if victory_check(your_step_forecast):
#             return i
#     return 10
#
#
# def victory_check(lst):
#     # проверяет соответствие условию победы
#     list_comb = [set(x) for x in combinations(lst, 3)]
#     return len([x for x in list_comb if x in win_list]) > 0
#
#
# rows = 3
# cols = 3
# steps = []
# your_steps = []
# comp_steps = []
# win_list = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
#
# field = [' ' for i in range(rows * cols)]
# output(field)
#
# for i in range((rows * cols)//2 + 1):
#
#     f_your_step(rows, steps, your_steps)
#     if victory_check(your_steps):
#         print('YOU WON!')
#         break
#
#     if i < (rows * cols)//2:
#         f_comp_step(steps, comp_steps)
#     else:
#         print('DRAW!')
#     if victory_check(comp_steps):
#         print('COMPUTER WON!')
#         break
