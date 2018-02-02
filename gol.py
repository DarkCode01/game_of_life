#! /usr/bin/env python3


import random
import time
import os
from termcolor import colored


class GameOfLife(object):

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.table = self.crate_table()

    def crate_table(self):
        tmp = [[] for _ in range(self.rows)]

        for i in range(len(tmp)):
            tmp[i] = [random.randint(0, 1) for _ in range(self.columns)]

        return tmp

    def print_table(self):
        for i in range(len(self.table)):
            tmp = map(
                lambda _: colored("#", "green") if _ else colored(".", "red"),
                self.table[i])

            print("|".join(tmp))

    def check_neighbors(self, _neighbors=0, **pos):
        for rv in range(-1, 2):
            if pos["row"] + rv >= 0:
                for cv in range(-1, 2):
                    if pos["col"] + cv >= 0:
                        try:
                            if self.table[pos["row"] + rv][pos["col"] + cv]:
                                _neighbors += 1
                        except IndexError:
                            pass

        if self.table[pos["row"]][pos["col"]]:
            _neighbors -= 1

        if _neighbors < 2 or _neighbors >= 4:
            self.table[pos["row"]][pos["col"]] = 0
        elif _neighbors == 3:
            self.table[pos["row"]][pos["col"]] = 1

    def game(self):
        while True:
            for index_row, _row in enumerate(self.table):
                for index_col, _col in enumerate(_row):
                    self.check_neighbors(row=index_row, col=index_col)

            os.system("clear")
            self.print_table()
            time.sleep(3)


gol = GameOfLife(5, 5)
gol.game()
