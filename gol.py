
import random
import time
import os


def crate_table(f, c):
    table = [[] for _ in range(f)]
    for x in range(f):
        table[x] = [random.randint(0, 1) for _ in range(c)]

    return table


def print_table(table_, c):
    for x in range(len(table_)):
        tmp = [str(e) for e in table_[x]]
        print("|".join(tmp).replace("1", "#").replace("0", "."))


def game(f, c):
    t = crate_table(f, c)
    print_table(t, c)
    print("-------------")
    while True:
        for i, e in enumerate(t):
            for ii, ee in enumerate(e):
                v = 0
                for x in range(-1, 2):
                    if (i + x) != -1 and (i + x) < f:
                        for xx in range(-1, 2):
                            if (ii + xx) != -1 and (ii + x) < c:
                                try:
                                    if t[i + x][ii + xx]:
                                        v += 1
                                except IndexError as e:
                                    pass
                if ee:
                    v -= 1
                if v < 2 or v >= 4:
                    t[i][ii] = 0
                elif v == 3:
                    t[i][ii] = 1

        os.system("clear")
        print_table(t, c)
        print("-------------")
        time.sleep(1)


game(10, 10)
