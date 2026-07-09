from random import randint, choice


HEIGHT = 10
WIDTH = 10
cells: dict[tuple[int, int]: list[int, int]] = {}
i = 1
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        cell: list[int, int] = []
        cells[tuple([x, y])] = [i, 15]
        i += 1
while all(v[0] == 1 for v in cells.values()) is not True:
    x = randint(0, WIDTH - 1)
    y = randint(0, HEIGHT - 1)
    check = 0
    possibility = [1, 2, 3, 4]
    while check != 1 and len(possibility) != 0:
        z = choice(possibility)
        if z == 1 and x > 0:  # west
            if cells[(x, y)][0] != cells[(x - 1, y)][0]:
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
            if cells[(x, y)][0] != cells[(x, y + 1)][0]:
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
            if cells[(x, y)][0] != cells[(x + 1, y)][0]:
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
            if cells[(x, y)][0] != cells[(x, y - 1)][0]:
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
for i in range(WIDTH):
    print("████", end="")
print("██")
for y in range(HEIGHT):
    print("█", end="")
    for x in range(WIDTH):
        west = ((cells[(x, y)][1] >> 3) & 1) == 0
        east = ((cells[(x, y)][1] >> 1) & 1) == 0
        left = " " if west else "█"
        right = " " if east else "█"
        print(f"{left}  {right}", end="")
    print("█")
    print("█", end="")
    for x in range(WIDTH):
        if ((cells[(x, y)][1] >> 2) & 1) == 0:
            print("█  █", end="")
        else:
            print("████", end="")
    print("█")
