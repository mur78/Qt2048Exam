from random import randint
import time

class Game2048Tmp(object):

    def __init__(self, xn, yn):
        self.width = xn
        self.height = yn
        self.grid = []

        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append(0)
        self.add_one()

    def add_one(self):
        not_filled = []
        random_values = [2, 4]
        for e in range(self.height):
            for j in range(self.width):
                if self.grid[e][j] == 0:
                    not_filled.append((e, j))
        random_cell = not_filled[randint(0, len(not_filled) - 1)]
        self.grid[random_cell[0]][random_cell[1]] = random_values[randint(0, len(random_values) - 1)]
        if len(not_filled) == 1:
            return self.check_gameover()
        return 0

    def check_gameover(self):
        for i in range(self.height):
            for j in range(self.width-1):
                if self.grid[i][j] == self.grid[i][j+1]:
                    return 0
        for i in range(self.height-1):
            for j in range(self.width):
                if self.grid[i][j] == self.grid[i+1][j]:
                    return 0
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    return 0
        return -1

    def swap_left(self):
        edit = False
        point = 0
        for i in range(self.height):
            start, end = 0, 1
            while end < self.width:
                start_value = self.grid[i][start]
                end_value = self.grid[i][end]
                if start_value == end_value and start_value > 0:
                    self.grid[i][start] *= 2
                    self.grid[i][end] = 0
                    point += self.grid[i][start]
                    edit = True
                    start += 1
                    end += 1
                elif start_value == 0 and end_value > 0:
                    self.grid[i][start] = end_value
                    self.grid[i][end] = 0
                    edit = True
                    end += 1
                elif start_value == end_value == 0:
                    end += 1
                elif start_value > 0 and end_value == 0:
                    end += 1
                elif 0 < start_value != end_value > 0:
                    start += 1
                else:
                    print('Произошел баг')
                    print(f'start_value = {start_value}')
                    print(f'end_value = {end_value}')
                    print(f'start = {start}')
                    print(f'end = {end}')
                    return -1
                while start >= end:
                    end += 1
        return self.add_one() + point if edit else self.check_gameover()

    def swap_right(self):
        edit = False
        point = 0
        for i in range(self.height):
            start, end = self.width-1, self.width-2
            while end > -1:
                start_value = self.grid[i][start]
                end_value = self.grid[i][end]
                if start_value == end_value and start_value > 0:
                    self.grid[i][start] *= 2
                    self.grid[i][end] = 0
                    point += self.grid[i][start]
                    edit = True
                    start -= 1
                    end -= 1
                elif start_value == 0 and end_value > 0:
                    self.grid[i][start] = end_value
                    self.grid[i][end] = 0
                    edit = True
                    end -= 1
                elif start_value == end_value == 0:
                    end -= 1
                elif start_value > 0 and end_value == 0:
                    end -= 1
                elif 0 < start_value != end_value > 0:
                    start -= 1
                else:
                    print('Произошел баг')
                    print(f'start_value = {start_value}')
                    print(f'end_value = {end_value}')
                    print(f'start = {start}')
                    print(f'end = {end}')
                    return -1
                while start <= end:
                    end -= 1
        return self.add_one() + point if edit else self.check_gameover()

    def swap_down(self):
        edit = False
        point = 0
        for i in range(self.width):
            start, end = self.height-1, self.height-2
            while end > -1:
                start_value = self.grid[start][i]
                end_value = self.grid[end][i]
                if start_value == end_value and start_value > 0:
                    self.grid[start][i] *= 2
                    self.grid[end][i] = 0
                    point += self.grid[start][i]
                    edit = True
                    start -= 1
                    end -= 1
                elif start_value == 0 and end_value > 0:
                    self.grid[start][i] = end_value
                    self.grid[end][i] = 0
                    edit = True
                    end -= 1
                elif start_value == end_value == 0:
                    end -= 1
                elif start_value > 0 and end_value == 0:
                    end -= 1
                elif 0 < start_value != end_value > 0:
                    start -= 1
                else:
                    print('Произошел баг')
                    print(f'start_value = {start_value}')
                    print(f'end_value = {end_value}')
                    print(f'start = {start}')
                    print(f'end = {end}')
                    return -1
                while start <= end:
                    end -= 1
        return self.add_one() + point if edit else self.check_gameover()

    def swap_up(self):
        edit = False
        point = 0
        for i in range(self.width):
            start, end = 0, 1
            while end < self.height:
                start_value = self.grid[start][i]
                end_value = self.grid[end][i]
                if start_value == end_value and start_value > 0:
                    self.grid[start][i] *= 2
                    self.grid[end][i] = 0
                    point += self.grid[start][i]
                    edit = True
                    start += 1
                    end += 1
                elif start_value == 0 and end_value > 0:
                    self.grid[start][i] = end_value
                    self.grid[end][i] = 0
                    edit = True
                    end += 1
                elif start_value == end_value == 0:
                    end += 1
                elif start_value > 0 and end_value == 0:
                    end += 1
                elif 0 < start_value != end_value > 0:
                    start += 1
                else:
                    print('Произошел баг')
                    print(f'start_value = {start_value}')
                    print(f'end_value = {end_value}')
                    print(f'start = {start}')
                    print(f'end = {end}')
                    return -1
                while start >= end:
                    end += 1
        return self.add_one() + point if edit else self.check_gameover()

    def __str__(self):
        string_ = ''
        for i in range(self.height):
            for j in range(self.width):
                string_ += f'{self.grid[i][j]}  '
            string_ += '\n'
        return string_


if __name__ == '__main__':
    game = Game2048Tmp(4, 4)
    random_functions = [game.swap_right, game.swap_left, game.swap_up, game.swap_down]
    for i in range(10):
        game.swap_down()
    print(game)
    game.swap_left()
    print(game)
    game.swap_left()
    print(game)
    print('Конец игры')