import tkinter as tk


class MazeRenderer:
    def __init__(self, maze, cell_size=50):
        """
        Inicializuje canvas pro zobrazení bludiště.
        :param maze: Instance třídy Maze.
        :param cell_size: Velikost jedné buňky na canvasu (v pixelech).
        """
        self.maze = maze
        self.cell_size = cell_size
        self.window = tk.Tk()
        self.window.title("Maze")
        self.canvas = self._initialize_canvas()

    def _initialize_canvas(self):
        """Vytvoří a vrátí Canvas pro kreslení."""
        width = self.maze.width * self.cell_size
        height = self.maze.height * self.cell_size
        canvas = tk.Canvas(self.window, width=width, height=height)
        canvas.pack()
        return canvas

    def draw_maze(self):
        """Vykreslí celou mapu bludiště na canvas."""
        self.canvas.delete("all")  # Vyčištění předchozího obsahu
        for y, row in enumerate(self.maze.map):
            for x, cell in enumerate(row):
                self._draw_cell(x, y, cell)
        self._draw_robot()

    def _draw_cell(self, x, y, cell_type):
        """Nakreslí jednotlivou buňku podle jejího typu."""
        x1, y1, x2, y2 = self._get_cell_coordinates(x, y)
        color = {
            0: "white",  # Průchodná cesta
            1: "black",  # Zeď
            'E': "green"  # Východ
        }.get(cell_type, "gray")
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def _draw_robot(self):
        """Vykreslí robota jako kruh na aktuální pozici."""
        x, y = self.maze.position
        x1, y1, x2, y2 = self._get_cell_coordinates(x, y)
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")

    def _get_cell_coordinates(self, x, y):
        """Vrátí souřadnice (x1, y1, x2, y2) dané buňky v canvasu."""
        x1 = x * self.cell_size
        y1 = y * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        return x1, y1, x2, y2

    def update_position(self, new_position):
        """
        Aktualizuje pozici robota a překreslí bludiště.
        :param new_position: Nová pozice robota (x, y).
        """
        if self.maze.move_to(new_position):
            self.draw_maze()
        else:
            print("Movement failed - hit a wall or went out of bounds.")

    def start(self):
        """Spustí hlavní smyčku grafického rozhraní."""
        self.draw_maze()
        self.window.mainloop()
