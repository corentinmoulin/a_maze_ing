import MazeGenerator as Maze
from MazeGenerator import Color


if __name__ == "__main__":
    Maze = Maze.MazeGenerator()
    cells = Maze.main()
    color = Color.WHITE
    Maze.maze_show(cells, color)
    show_path: bool = False
    while True:
        inp = input("1: regen\n2: change color\n3: show/hide path\n"
                    + "4: perfect/imperfect\n0: quit\nYour choice:")
        if inp == "1":
            if show_path is True:
                cells = Maze.maze_gen()
                if Maze.PERFECT is False:
                    Maze.imperfect_gen(cells)
                Maze.output(cells, Maze.solve_maze(cells))
                Maze.maze_show(cells, color, Maze.solve_maze(cells))
            else:
                cells = Maze.maze_gen()
                if Maze.PERFECT is False:
                    Maze.imperfect_gen(cells)
                Maze.output(cells, Maze.solve_maze(cells))
                Maze.maze_show(cells, color)
        elif inp == "2":
            if color == Color.WHITE:
                color = Color.RED
            elif color == Color.RED:
                color = Color.CYAN
            elif color == Color.CYAN:
                color = Color.MAGENTA
            else:
                color = Color.WHITE

            if show_path is True:
                Maze.maze_show(cells, color, Maze.solve_maze(cells))
            else:
                Maze.maze_show(cells, color)
        elif inp == "3":
            if show_path is True:
                show_path = False
            else:
                show_path = True
            if show_path is True:
                Maze.maze_show(cells, color, Maze.solve_maze(cells))
            else:
                Maze.maze_show(cells, color)
        elif inp == "4":
            if Maze.PERFECT is True:
                Maze.PERFECT = False
            else:
                Maze.PERFECT = True
            if show_path is True:
                cells = Maze.maze_gen()
                if Maze.PERFECT is False:
                    Maze.imperfect_gen(cells)
                Maze.output(cells, Maze.solve_maze(cells))
                Maze.maze_show(cells, color, Maze.solve_maze(cells))
            else:
                cells = Maze.maze_gen()
                if Maze.PERFECT is False:
                    Maze.imperfect_gen(cells)
                Maze.output(cells, Maze.solve_maze(cells))
                Maze.maze_show(cells, color)
        elif inp == "0":
            break
        else:
            print("\nERROR: Wrong input\n")
