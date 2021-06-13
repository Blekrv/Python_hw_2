import random
from typing import Union
# list

# l = [1, 2, 3]
# print(l)
# l = list((4, 5, 6))
# print(l)
# l = list('text')
# print(l)

# l = [1, 2, 3]
# l2 = l
# l3 = l[:]
# l3 = list(l)
# l3 = l.copy()
# l[2] = 55
# print(l2)
# print(l3)

# print(len('TEXT'))
# print(str(l)*2)
# print(max("TEXT"))
# print(min(l))

# l = random.sample(range(1, 21), 20)  # randomizer
# print(l)
# print(random.choice(l))
# print(random.sample(l, 5))
# print(random.choices(l, k=3))

# l.append(1000)
# l.extend((0, 77, 88))              # v kinec
# l.insert(1, 8888)                  # add
# l.pop(0)                           # del i vertae
# del l[0]                           # ne vertae
# l.remove(5)
# print(l)
# print(l.index(88, 15, 25))
# print(l.count(88))

# print(sorted(l, reverse=True))
# l.sort(reverse=True)
# print(l)

# a = []
# for i in range(1, 11):
#     a.append(i)
# print(a)

# b = [i for i in range(1, 11) if i % 2 == 0]
# print(b)

# c = []
# for i in range(1, 4):
#     for j in range(1, 4):
#         c.append([i, j])
# print(c)
# print(c[1][1])

# GENERATOR LIST
# d = [[i, j] for i in range(1, 4) for j in range(1, 4)]
# print(d)

# f = []
# for i in d:
#     for j in i:
#         f.append(j)
# print(f)

# h = [j for i in d for j in i]               # list comprehension
# print(h)

# e = [0]*10
# print(e)

# m = n = 3
# r = [[0 for i in range(m)] for j in range(n)]
# print(r)
# ---------------------------------tupl------------------------------ UNMUTABLE
# a = 5
# b = 6
# b, a = a, b
# print(a, b)

# c = a, b
# print(c)


# x, *y, z = 1, 2, 3, 4, 5
# print(x, y, z)
# print(tuple('text'))
# print(tuple([1]))


# d = (1, 2, 55, 2)
# print(d)
# print(len(d), max(d), min(d))
# print(d.index(2))
# print(d[2])
# print(d.count(2))
# d += tuple([77])
# print(d)

# ----------------------------------dict----------------------------
# d = {}
# print(d)
# d = dict(a1=1000, a2=2222, a3=3000)
# print(d)
# print(d['a1'])

# d = ({'k1': 111, "k2": 222})
# print(d['k1'])

# d = ({'k1': 111, "k2": 222})
# print(d['k2'])


# a = {2: 'a', "x": 'b', (1, 2): 'c'}
# print(a[(1, 2)])

# print(2 in a)
# print(len(a))
# print(list(a.keys()))
# # del a['x']
# # print(a.pop('x'))
# print(a)

# for key in a.keys():
#     print(f"\t{key}: {a[key]}")
# a.update({"Some key": 2222})
# print(a)

# print(a.values())

# l1 = ['x', 'y']
# l2 = [11111, 22222]
# l3 = list(zip(l1, l2))
# print(l3)
# l3 = dict(zip(l1, l2))
# print(l3)


# # GENERATOR DICT
# l3 = {m: n for (m, n) in zip(l1, l2)}
# print(l3)
# ----------------------------------set----------------------------- MUTABLE
# my_list = [1, 2, 2, 5, 7, 8, 8, 9]
# # print(' '.join(my_list))
# s = set(my_list)

# a = set((1, 2, 5, 100))

# print(s, a)

# a = set.union(a, s)
# a.add(77)
# print(a)
# print(len(a))


# a.update([10, 20, 30, 3])
# print(a)
# a.discard(100)
# print(a)
# # a.remove(1000)
# print(a)
# # c = set(dict({k: 1, k1: 2}))
# # print(c)
# c = frozenset(a)

# print(c)
# --string---
# s = "    Some text    ".strip(' ')
# # .title().capitalize().lower().upper().swapcase().center(20)
# s = s.replace('e', 'd')
# print(s.find("d"))
# print(s.rfind("d"))
# print(s.index('d'))
# print(s)


# a = list(s)
# print(''.join(a))
