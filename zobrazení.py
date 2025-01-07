import tkinter as tk


class MazeVisualizer:
    def __init__(self, maze, cell_size=50):
        """
        Inicializace vizualizační třídy pro zobrazení bludiště pomocí tkinter.

        :param maze: Instance třídy Maze.
        :param cell_size: Velikost jedné buňky v pixelech.
        """
        self.maze = maze
        self.cell_size = cell_size
        self.window = tk.Tk()
        self.canvas = tk.Canvas(
            self.window,
            width=self.maze.width * cell_size,
            height=self.maze.height * cell_size,
        )
        self.canvas.pack()

    def render(self):
        """
        Vykreslí bludiště na canvas.
        """
        self.canvas.delete("all")
        for y, row in enumerate(self.maze.map):
            for x, cell in enumerate(row):
                x1, y1 = x * self.cell_size, y * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size

                color = "white"
                if cell == 1:
                    color = "black"
                elif cell == "E":
                    color = "green"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        # Vykreslení pozice robota
        robot_x, robot_y = self.maze.position
        x1, y1 = robot_x * self.cell_size, robot_y * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")

    def update(self, new_position):
        """
        Aktualizuje pozici robota a překreslí bludiště.

        :param new_position: Nová pozice robota (x, y).
        """
        if self.maze.move_to(new_position):
            self.render()
        else:
            print("Movement failed - hit a wall or moved out of bounds.")

    def start(self):
        """
        Spustí aplikaci.
        """
        self.render()
        self.window.mainloop()
