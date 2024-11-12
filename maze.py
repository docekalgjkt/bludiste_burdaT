import tkinter as tk

class Maze:
    def __init__(self, layout):
        self.layout = layout
        self.start_position = None
        self.end_position = None
        self.locate_start_and_end()

    def locate_start_and_end(self):
        for row_index, row in enumerate(self.layout):
            for col_index, cell in enumerate(row):
                if cell == 3:
                    self.start_position = (row_index, col_index)  # Store starting position
                elif cell == 4:
                    self.end_position = (row_index, col_index)  # Store ending position

class MazeView:
    def __init__(self, parent, maze):
        self.parent = parent
        self.maze = maze
        self.cell_size = 50
        self.canvas = tk.Canvas(parent, width=len(maze.layout[0]) * self.cell_size,
                                height=len(maze.layout) * self.cell_size)
        self.canvas.pack()
        self.render_maze()

    def render_maze(self):
        for row_index, row in enumerate(self.maze.layout):
            for col_index, cell in enumerate(row):
                x0 = col_index * self.cell_size
                y0 = row_index * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                if cell == 1:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill='black')  # Wall
                elif cell == 0:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill='white')  # Free path
                elif cell == 3:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill='green')  # Start
                elif cell == 4:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill='red')  # End

class MazeApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Maze")
        self.maze_layout = [
            [1, 1, 3, 1, 1, 1],
            [1, 0, 0, 1, 0, 4],
            [1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
        ]
        self.maze = Maze(self.maze_layout)
        self.view = MazeView(parent, self.maze)

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()
