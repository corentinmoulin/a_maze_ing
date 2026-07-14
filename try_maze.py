from random import randint, choice
from math import ceil, floor
import sys


class Color:
    RESET = "\033[0m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BROWN = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    FD_BLACK = "\033[40m"
    FD_RED = "\033[41m"
    FD_GREEN = "\033[42m"
    FD_BROWN = "\033[43m"
    FD_BLUE = "\033[44m"
    FD_MAGENTA = "\033[45m"
    FD_CYAN = "\033[46m"
    FD_WHITE = "\033[47m"
    all = [RED, GREEN, BROWN, BLUE, MAGENTA, CYAN, WHITE]
    all_fd = [FD_BLACK, FD_BLUE, FD_CYAN, FD_GREEN, FD_MAGENTA, FD_RED, FD_BROWN]


def create_ft(WIDTH: int, HEIGHT: int) -> list[tuple[int, int]]:
    ft: list[tuple[int, int]] = []
    x = floor(WIDTH / 2 - 3)
    y = ceil(HEIGHT / 2 - 3)
    ft += [(x, y)]
    y += 1
    ft += [(x, y)]
    y += 1
    ft += [(x, y)]
    x += 1
    ft += [(x, y)]
    x += 1
    ft += [(x, y)]
    y += 1
    ft += [(x, y)]
    y += 1
    ft += [(x, y)]
    x += 4
    ft += [(x, y)]
    x -= 1
    ft += [(x, y)]
    x -= 1
    ft += [(x, y)]
    y -= 1
    ft += [(x, y)]
    y -= 1
    ft += [(x, y)]
    x += 1
    ft += [(x, y)]
    x += 1
    ft += [(x, y)]
    y -= 1
    ft += [(x, y)]
    y -= 1
    ft += [(x, y)]
    x -= 1
    ft += [(x, y)]
    x -= 1
    ft += [(x, y)]
    return ft


def maze_gen(PERFECT: bool) -> dict[tuple[int, int], list[int]]:
    HEIGHT = 21
    WIDTH = 21
    ft = create_ft(HEIGHT, WIDTH)
    cells: dict[tuple[int, int], list[int]] = {}
    i = 1
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # cell: list[int] = []
            cells[(x, y)] = [i, 15]
            i += 1
    while all(v[0] == 1 for v in cells.values()) is not True:
        x = randint(0, WIDTH - 1)
        y = randint(0, HEIGHT - 1)
        if (x, y) not in ft:
            check = 0
            possibility = [1, 2, 3, 4]
            while check != 1 and len(possibility) != 0:
                z = choice(possibility)
                if z == 1 and x > 0:  # west
                    if cells[(x, y)][0] != cells[(x - 1, y)][0] and (x - 1, y) not in ft:
                        cells[(x, y)][1] = cells[(x, y)][1] - 8
                        cells[(x - 1, y)][1] = cells[(x - 1, y)][1] - 2
                        check = 1
                        reg = min(cells[(x, y)][0], cells[(x - 1, y)][0])
                        to_change = max(cells[(x, y)][0], cells[(x - 1, y)][0])
                        cells[(x, y)][0] = reg
                        cells[(x - 1, y)][0] = reg
                        for k in cells:
                            if cells[k][0] == to_change:
                                cells[k][0] = reg
                if z == 2 and y < HEIGHT - 1:  # south
                    if cells[(x, y)][0] != cells[(x, y + 1)][0] and (x, y + 1) not in ft:
                        cells[(x, y)][1] = cells[(x, y)][1] - 4
                        cells[(x, y + 1)][1] = cells[(x, y + 1)][1] - 1
                        check = 1
                        reg = min(cells[(x, y)][0], cells[(x, y + 1)][0])
                        to_change = max(cells[(x, y)][0], cells[(x, y + 1)][0])
                        cells[(x, y)][0] = reg
                        cells[(x, y + 1)][0] = reg
                        for k in cells:
                            if cells[k][0] == to_change:
                                cells[k][0] = reg
                if z == 3 and x < WIDTH - 1:  # east
                    if cells[(x, y)][0] != cells[(x + 1, y)][0] and (x + 1, y) not in ft:
                        cells[(x, y)][1] = cells[(x, y)][1] - 2
                        cells[(x + 1, y)][1] = cells[(x + 1, y)][1] - 8
                        check = 1
                        reg = min(cells[(x, y)][0], cells[(x + 1, y)][0])
                        to_change = max(cells[(x, y)][0], cells[(x + 1, y)][0])
                        cells[(x, y)][0] = reg
                        cells[(x + 1, y)][0] = reg
                        for k in cells:
                            if cells[k][0] == to_change:
                                cells[k][0] = reg
                if z == 4 and y > 0:  # north
                    if cells[(x, y)][0] != cells[(x, y - 1)][0] and (x, y - 1) not in ft:
                        cells[(x, y)][1] = cells[(x, y)][1] - 1
                        cells[(x, y - 1)][1] = cells[(x, y - 1)][1] - 4
                        check = 1
                        reg = min(cells[(x, y)][0], cells[(x, y - 1)][0])
                        to_change = max(cells[(x, y)][0], cells[(x, y - 1)][0])
                        cells[(x, y)][0] = reg
                        cells[(x, y - 1)][0] = reg
                        for k in cells:
                            if cells[k][0] == to_change:
                                cells[k][0] = reg
                possibility.remove(z)
        else:
            cells[(x, y)][0] = 1
    if PERFECT is False:
        deadend_check = [7, 11, 13, 14]
        for x in range(0, WIDTH):
            for y in range(0, HEIGHT):
                if cells[(x, y)][1] in deadend_check and (x, y) not in ft:
                    possibility = [1, 2, 3, 4]
                    while cells[(x, y)][1] in deadend_check and len(possibility) != 0:
                        z = choice(possibility)
                        if z == 1 and x > 0 and cells[(x, y)][1] != 7 and (x - 1, y) not in ft:  # west
                            cells[(x, y)][1] = cells[(x, y)][1] - 8
                            cells[(x - 1, y)][1] = cells[(x - 1, y)][1] - 2
                        if z == 2 and y < HEIGHT - 1 and cells[(x, y)][1] != 11 and (x, y + 1) not in ft:  # south
                            cells[(x, y)][1] = cells[(x, y)][1] - 4
                            cells[(x, y + 1)][1] = cells[(x, y + 1)][1] - 1
                        if z == 3 and x < WIDTH - 1 and cells[(x, y)][1] != 13 and (x + 1, y) not in ft:  # east
                            cells[(x, y)][1] = cells[(x, y)][1] - 2
                            cells[(x + 1, y)][1] = cells[(x + 1, y)][1] - 8
                        if z == 4 and y > 0 and cells[(x, y)][1] != 14 and (x, y - 1) not in ft:  # north
                            cells[(x, y)][1] = cells[(x, y)][1] - 1
                            cells[(x, y - 1)][1] = cells[(x, y - 1)][1] - 4
                        possibility.remove(z)
    return cells


def maze_show(
        cells: dict[tuple[int, int], list[int]],
        color: str,
        ) -> None:
    HEIGHT = 21
    WIDTH = 21
    ft = create_ft(WIDTH, HEIGHT)
    fd_color = choice(Color.all_fd)
    if fd_color == Color.FD_BLACK:
        fd_color = Color.FD_GREEN
    elif fd_color == Color.FD_GREEN:
        fd_color = Color.FD_CYAN
    elif fd_color == Color.FD_CYAN:
        fd_color = Color.FD_RED
    elif fd_color == Color.FD_RED:
        fd_color = Color.FD_BROWN
    elif fd_color == Color.FD_BROWN:
        fd_color = Color.FD_BLUE
    elif fd_color == Color.FD_BLUE:
        fd_color = Color.FD_BLACK
    for _ in range(WIDTH):
        print(f"{color}████", end="")
    print("██")
    for y in range(HEIGHT):
        print(f"{color}█", end="")
        for x in range(WIDTH):
            if (x, y) in ft:
                print(f"█{fd_color}  {Color.FD_BLACK}█", end="")
            else:
                west = ((cells[(x, y)][1] >> 3) & 1) == 0
                east = ((cells[(x, y)][1] >> 1) & 1) == 0
                left = " " if west else "█"
                right = " " if east else "█"
                print(f"{left}  ​{right}", end="")
        print("█")
        print("█", end="")
        for x in range(WIDTH):
            if ((cells[(x, y)][1] >> 2) & 1) == 0:
                print("█  ​█", end="")
            else:
                print("████", end="")
        print(f"█{Color.RESET}")


def to_hex(value: int) -> str:
    digits = "0123456789ABCDEF"
    if value == 0:
        return "0"
    result = ""
    while value > 0:
        result = digits[value % 16] + result
        value //= 16
    return result


def output(cells: dict[tuple[int, int], list[int]], WIDTH: int, HEIGHT: int) -> None:
    with open('output.txt', 'w') as f:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                f.write(to_hex(cells[(x, y)][1]))
            f.write("\n")


START = (1,1)
END = (9,9)


def solve_maze(cells: dict[tuple[int, int], list[int]]) -> list[tuple[int, int]]:
    HEIGHT = 21
    WIDTH = 21
    directions = [
        (1, 0, -1),   # NORTH
        (2, 1, 0),    # EAST
        (4, 0, 1),    # SOUTH
        (8, -1, 0),   # WEST
    ]



PERFECT = True
cells = maze_gen(PERFECT)
output(cells, 21, 21)
color = Color.WHITE
maze_show(cells, color)
while True:
    inp = input("1: regen\n2: change color\n3: show/hide path\n0: quit\nYour choice:")
    if inp == "1":
        cells = maze_gen(PERFECT)
        output(cells, 21, 21)
        maze_show(cells, color)
    elif inp == "2":
        if color == Color.WHITE:
            color = Color.RED
        elif color == Color.RED:
            color = Color.BLUE
        elif color == Color.BLUE:
            color = Color.CYAN
        elif color == Color.CYAN:
            color = Color.GREEN
        elif color == Color.GREEN:
            color = Color.MAGENTA
        elif color == Color.MAGENTA:
            color = Color.BROWN
        else:
            color = Color.WHITE
        maze_show(cells, color)
    elif inp == "3":
        pass
    elif inp == "4":
        if PERFECT is True:
            PERFECT = False
        else:
            PERFECT = True
        cells = maze_gen(PERFECT)
        output(cells, 21, 21)
        maze_show(cells, color)
    elif inp == "0":
        break
    else:
        print("\nERROR: Wrong input\n")
# colors
# cells = maze_gen()
# random = choice(Color.all)
# Color.all.remove(random)
# random2 = choice(Color.all)
# WIDTH = 10
# HEIGHT = 10
# for i in range(WIDTH):
#     print(f"{random}████", end="")
# print("██")
# for y in range(HEIGHT):
#     print("█", end="")
#     for x in range(WIDTH):
#         west = ((cells[(x, y)][1] >> 3) & 1) == 0
#         east = ((cells[(x, y)][1] >> 1) & 1) == 0
#         left = f"{random2}█" if west else f"{random}█"
#         right = f"{random2}█" if east else f"{random}█"
#         print(f"{left}{random2}██{right}", end="")
#     print("█")
#     print("█", end="")
#     for x in range(WIDTH):
#         if ((cells[(x, y)][1] >> 2) & 1) == 0:
#             print(f"█{random2}██{random}█", end="")
#         else:
#             print("████", end="")
#     print("█")
