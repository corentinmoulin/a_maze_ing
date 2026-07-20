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
    all_fd = [
        FD_BLACK, FD_BLUE, FD_CYAN, FD_GREEN, FD_MAGENTA, FD_RED, FD_BROWN]


class MazeGenerator:
    def __init__(self) -> None:
        self.WIDTH: int = 11
        self.HEIGHT: int = 11
        self.START: tuple[int, int] = (0, 0)
        self.END: tuple[int, int] = (0, 0)
        self.OUTPUT_FILE: str = "maze.txt"
        self.PERFECT: bool = True
        self.SEED = 4

    @staticmethod
    def to_hex(value: int) -> str:
        digits = "0123456789ABCDEF"
        if value == 0:
            return "0"
        result = ""
        while value > 0:
            result = digits[value % 16] + result
            value //= 16
        return result

    def output(
            self,
            cells: dict[tuple[int, int], list[int]],
            path: list[tuple[int, int]]
            ) -> None:
        with open(self.OUTPUT_FILE, 'w') as f:
            for y in range(self.HEIGHT):
                for x in range(self.WIDTH):
                    f.write(self.to_hex(cells[(x, y)][1]))
                f.write("\n")
            f.write("\n")
            f.write("\n")
            f.write(str(self.START).strip("(").strip(")") + "\n")
            f.write(str(self.END).strip("(").strip(")") + "\n")
            directions = [
                (0, -1),   # NORTH
                (1, 0),    # EAST
                (0, 1),    # SOUTH
                (-1, 0),   # WEST
            ]
            for i in range(len(path) - 1):
                if path[i + 1][0] == path[i][0] + directions[0][0] \
                        and path[i + 1][1] == path[i][1] + directions[0][1]:
                    f.write("N")
                if path[i + 1][0] == path[i][0] + directions[1][0] \
                        and path[i + 1][1] == path[i][1] + directions[1][1]:
                    f.write("E")
                if path[i + 1][0] == path[i][0] + directions[2][0] \
                        and path[i + 1][1] == path[i][1] + directions[2][1]:
                    f.write("S")
                if path[i + 1][0] == path[i][0] + directions[3][0] \
                        and path[i + 1][1] == path[i][1] + directions[3][1]:
                    f.write("W")

    def solve_maze(
            self,
            cells: dict[tuple[int, int], list[int]]
            ) -> list[tuple[int, int]]:
        directions = [
            (1, 0, -1),   # NORTH
            (2, 1, 0),    # EAST
            (4, 0, 1),    # SOUTH
            (8, -1, 0),   # WEST
        ]
        ft_logo = self.create_ft()
        to_visit: list[tuple[int, int]] = [self.START]
        index_to_visit = 0
        parents_children: dict[tuple[int, int], tuple[int, int] | None] = {}
        parents_children[self.START] = None
        voisin: tuple[int, int]
        visited: set[tuple[int, int]] = {self.START}

        while index_to_visit < len(to_visit):
            x, y = to_visit[index_to_visit]
            index_to_visit += 1

            if (x, y) == self.END:
                break

            current_walls = cells[x, y][1]
            for wall, x_dir, y_dir in directions:
                nw_x = x + x_dir
                nw_y = y + y_dir

                voisin = (nw_x, nw_y)

                if voisin in visited:
                    continue

                if current_walls & wall:
                    continue

                if not (0 <= nw_x < self.WIDTH and 0 <= nw_y < self.HEIGHT):
                    continue

                if (nw_x, nw_y) in ft_logo:
                    continue

                visited.add(voisin)
                parents_children[voisin] = (x, y)
                to_visit.append(voisin)

        path: list[tuple[int, int]] = []
        current_position: tuple[int, int] | None = self.END
        while current_position is not None:
            path.append(current_position)
            current_position = parents_children[current_position]
        path.reverse()
        return path

    def imperfect_gen(
        self,
        cells: dict[tuple[int, int], list[int]]
       ) -> None:
        ft = self.create_ft()
        deadend_check = [7, 11, 13, 14]
        for x in range(0, self.WIDTH):
            for y in range(0, self.HEIGHT):
                if cells[(x, y)][1] in deadend_check and (x, y) not in ft:
                    possibility = [1, 2, 3, 4]
                    while cells[(x, y)][1] in deadend_check and len(
                            possibility) != 0:
                        z = choice(possibility)
                        if z == 1 and x > 0 and cells[(x, y)][1] != 7 and (
                                x - 1, y) not in ft:  # west
                            cells[(x, y)][1] = cells[(x, y)][1] - 8
                            cells[(x - 1, y)][1] = cells[(x - 1, y)][1] - 2
                        if z == 2 and y < self.HEIGHT - 1 and cells[(
                                x, y)][1] != 11 and (x, y + 1) not in ft:
                            cells[(x, y)][1] = cells[(x, y)][1] - 4
                            cells[(x, y + 1)][1] = cells[(x, y + 1)][1] - 1
                        if z == 3 and x < self.WIDTH - 1 and cells[(
                                x, y)][1] != 13 and (x + 1, y) not in ft:
                            cells[(x, y)][1] = cells[(x, y)][1] - 2
                            cells[(x + 1, y)][1] = cells[(x + 1, y)][1] - 8
                        if z == 4 and y > 0 and cells[(x, y)][1] != 14 and (
                                x, y - 1) not in ft:  # north
                            cells[(x, y)][1] = cells[(x, y)][1] - 1
                            cells[(x, y - 1)][1] = cells[(x, y - 1)][1] - 4
                        possibility.remove(z)

    def maze_gen(self) -> dict[tuple[int, int], list[int]]:
        ft = self.create_ft()
        cells: dict[tuple[int, int], list[int]] = {}
        i = 1
        for x in range(0, self.WIDTH):
            for y in range(0, self.HEIGHT):
                cells[(x, y)] = [i, 15]
                i += 1
        while all(v[0] == 1 for v in cells.values()) is not True:
            x = randint(0, self.WIDTH - 1)
            y = randint(0, self.HEIGHT - 1)
            if (x, y) not in ft:
                check = 0
                possibility = [1, 2, 3, 4]
                while check != 1 and len(possibility) != 0:
                    z = choice(possibility)
                    if z == 1 and x > 0:  # west
                        if cells[(x, y)][0] != cells[(x - 1, y)][0] and (
                                x - 1, y) not in ft:
                            cells[(x, y)][1] = cells[(x, y)][1] - 8
                            cells[(x - 1, y)][1] = cells[(x - 1, y)][1] - 2
                            check = 1
                            reg = min(cells[(x, y)][0], cells[(x - 1, y)][0])
                            to_change = max(
                                cells[(x, y)][0], cells[(x - 1, y)][0]
                                )
                            cells[(x, y)][0] = reg
                            cells[(x - 1, y)][0] = reg
                            for k in cells:
                                if cells[k][0] == to_change:
                                    cells[k][0] = reg
                    if z == 2 and y < self.HEIGHT - 1:  # south
                        if cells[(x, y)][0] != cells[(x, y + 1)][0] and (
                                x, y + 1) not in ft:
                            cells[(x, y)][1] = cells[(x, y)][1] - 4
                            cells[(x, y + 1)][1] = cells[(x, y + 1)][1] - 1
                            check = 1
                            reg = min(cells[(x, y)][0], cells[(x, y + 1)][0])
                            to_change = max(
                                cells[(x, y)][0], cells[(x, y + 1)][0]
                                )
                            cells[(x, y)][0] = reg
                            cells[(x, y + 1)][0] = reg
                            for k in cells:
                                if cells[k][0] == to_change:
                                    cells[k][0] = reg
                    if z == 3 and x < self.WIDTH - 1:  # east
                        if cells[(x, y)][0] != cells[(x + 1, y)][0] and (
                                x + 1, y) not in ft:
                            cells[(x, y)][1] = cells[(x, y)][1] - 2
                            cells[(x + 1, y)][1] = cells[(x + 1, y)][1] - 8
                            check = 1
                            reg = min(cells[(x, y)][0], cells[(x + 1, y)][0])
                            to_change = max(
                                cells[(x, y)][0], cells[(x + 1, y)][0]
                                )
                            cells[(x, y)][0] = reg
                            cells[(x + 1, y)][0] = reg
                            for k in cells:
                                if cells[k][0] == to_change:
                                    cells[k][0] = reg
                    if z == 4 and y > 0:  # north
                        if cells[(x, y)][0] != cells[(x, y - 1)][0] and (
                                x, y - 1) not in ft:
                            cells[(x, y)][1] = cells[(x, y)][1] - 1
                            cells[(x, y - 1)][1] = cells[(x, y - 1)][1] - 4
                            check = 1
                            reg = min(cells[(x, y)][0], cells[(x, y - 1)][0])
                            to_change = max(
                                cells[(x, y)][0], cells[(x, y - 1)][0]
                                )
                            cells[(x, y)][0] = reg
                            cells[(x, y - 1)][0] = reg
                            for k in cells:
                                if cells[k][0] == to_change:
                                    cells[k][0] = reg
                    possibility.remove(z)
            else:
                cells[(x, y)][0] = 1
        return cells

    def create_ft(self) -> list[tuple[int, int]]:
        ft: list[tuple[int, int]] = []
        if self.WIDTH < 9 or self.HEIGHT < 7:
            return ft
        x = floor(self.WIDTH / 2 - 3)
        y = ceil(self.HEIGHT / 2 - 3)
        moves = [
            (0, 0), (0, 1), (0, 1), (1, 0), (1, 0),
            (0, 1), (0, 1), (4, 0), (-1, 0), (-1, 0),
            (0, -1), (0, -1), (1, 0), (1, 0), (0, -1), (0, -1),
            (-1, 0), (-1, 0),
        ]
        for dx, dy in moves:
            x += dx
            y += dy
            ft.append((x, y))
        return ft

    def verif_config(self) -> None:
        if self.WIDTH < 1 or self.HEIGHT < 1:
            raise ValueError(
                "La largeur et la hauteur doivent etre superieur a 0."
                            )
        if self.START == self.END:
            raise ValueError("L'entrée et la sortie doivent etre differentes.")

        ft = self.create_ft()
        if self.START in ft:
            raise ValueError("L'entrée ne peut pas être dans le logo 42.")
        if self.END in ft:
            raise ValueError("La sortie ne peut pas être dans le logo 42.")

    def new_config(self) -> None:
        prefix: str = ""
        name_file = ""
        seen: set[str] = set()
        mandatory = {
            "WIDTH",
            "HEIGHT",
            "ENTRY",
            "EXIT",
            "OUTPUT_FILE",
            "PERFECT",
        }
        if len(sys.argv) != 2:
            raise ValueError("Trop ou trop peu d'arguments")
        else:
            for i in range(len(sys.argv)):
                extention_name = sys.argv[i].split('.')
                if len(extention_name) != 2:
                    continue
                else:
                    if extention_name[1] != "txt":
                        continue
                    else:
                        name_file = sys.argv[i]
            if name_file == "":
                raise ValueError("pas le bon format de fichier")

        with open(name_file, "r") as f:
            values = f.read().split("\n")
        for i in range(len(values)):
            if values[i].startswith("#"):
                continue
            index_start = values[i].find("=") + 1
            if index_start == -1:
                continue
            prefix = values[i][:index_start - 1]
            values[i] = values[i][index_start:]
            if prefix in seen:
                raise ValueError()
            if prefix == "WIDTH":
                self.WIDTH = int(values[i])
                seen.add(prefix)
            if prefix == "HEIGHT":
                self.HEIGHT = int(values[i])
                seen.add(prefix)
            if prefix == "ENTRY":
                x, y = values[i].split(",")
                self.START = (int(x), int(y))
                if self.START[0] >= self.WIDTH \
                    or self.START[1] >= self.HEIGHT \
                    or self.START[0] < 0 \
                   or self.START[1] < 0:
                    raise ValueError(
                        "Les coordonnee d'entree doivent etre dans "
                        "le labyrinthe"
                        )
                seen.add(prefix)
            if prefix == "EXIT":
                x, y = values[i].split(",")
                self.END = (int(x), int(y))
                if self.END[0] >= self.WIDTH \
                    or self.END[1] >= self.HEIGHT \
                    or self.END[0] < 0 \
                   or self.END[1] < 0:
                    raise ValueError(
                        "Les coordonnee de sortie doivent etre dans le "
                        "labyrinthe"
                        )
                seen.add(prefix)
            if prefix == "OUTPUT_FILE":
                self.OUTPUT_FILE = str(values[i])
                seen.add(prefix)
            if prefix == "PERFECT":
                self.PERFECT = values[i].strip().lower() == "true"
                seen.add(prefix)
            if prefix == "SEED":
                self.SEED = int(values[i])
                seen.add(prefix)
        missing = mandatory - seen
        if missing:
            raise ValueError("All mandatory part are not in the config file")

    def maze_show(
            self,
            cells: dict[tuple[int, int], list[int]],
            color: str,
            path: list[tuple[int, int]] | None = None
            ) -> None:
        if path is None:
            path = []
        if self.WIDTH < 9 or self.HEIGHT < 7:
            print("Too small to print 42 !!")
        ft = self.create_ft()
        for _ in range(self.WIDTH):
            print(f"{color}████", end="")
        print("██")
        for y in range(self.HEIGHT):
            print(f"{color}█", end="")
            for x in range(self.WIDTH):

                west = ((cells[(x, y)][1] >> 3) & 1) == 0
                east = ((cells[(x, y)][1] >> 1) & 1) == 0

                if west and (x - 1, y) in path:
                    left = f"{Color.FD_GREEN} "
                elif west:
                    left = f"{Color.FD_BLACK} "
                else:
                    left = f"{color}█"

                if east and (x + 1, y) in path:
                    right = f"{Color.FD_GREEN} "
                elif east:
                    right = f"{Color.FD_BLACK} "
                else:
                    right = f"{color}█"

                if (x, y) == self.START:
                    print(f"{left}{
                        Color.FD_BLUE}  ​{right}{Color.RESET}{color}",
                            end="")
                    continue
                elif (x, y) == self.END:
                    print(f"{left}{
                        Color.FD_BROWN}  ​{right}{Color.RESET}{color}",
                            end="")
                    continue

                if (x, y) in ft:
                    print(f"█{Color.FD_BLUE}  {Color.FD_BLACK}█", end="")
                elif (x, y) in path:
                    west = ((cells[(x, y)][1] >> 3) & 1) == 0
                    east = ((cells[(x, y)][1] >> 1) & 1) == 0

                    if west and (x - 1, y) in path:
                        left = f"{Color.FD_GREEN} "
                    elif west:
                        left = f"{Color.FD_BLACK} "
                    else:
                        left = f"{color}█"

                    if east and (x + 1, y) in path:
                        right = f"{Color.FD_GREEN} "
                    elif east:
                        right = f"{Color.FD_BLACK} "
                    else:
                        right = f"{color}█"

                    print(f"{left}{
                        Color.FD_GREEN}  ​{right}{Color.RESET}{color}",
                            end="")
                else:
                    west = ((cells[(x, y)][1] >> 3) & 1) == 0
                    east = ((cells[(x, y)][1] >> 1) & 1) == 0
                    left = " " if west else "█"
                    right = " " if east else "█"
                    print(f"{left}  ​{right}", end="")
            print("█")
            print("█", end="")
            for x in range(self.WIDTH):
                if ((cells[(x, y)][1] >> 2) & 1) == 0:
                    if (x, y) in path and (x, y + 1) in path:
                        print(f"█{Color.FD_GREEN}  ​█{Color.FD_BLACK}", end="")
                    else:
                        print("█  ​█", end="")
                else:
                    print("████", end="")
            print(f"█{Color.RESET}")

    def main(self) -> dict[tuple[int, int], list[int]]:
        try:
            self.new_config()
            self.verif_config()
        except Exception as e:
            print(e)
            exit()
        cells: dict[tuple[int, int], list[int]] = self.maze_gen()
        if self.PERFECT is False:
            self.imperfect_gen(cells)
        self.output(cells, self.solve_maze(cells))
        return cells
