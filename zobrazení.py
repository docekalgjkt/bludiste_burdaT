import tkinter as tk


class MazeRenderer:
    def __init__(self, maze, cell_size=50):
        """
        Initializes the renderer for displaying the maze using tkinter Canvas.

        :param maze: Instance of the Maze class
        :param cell_size: Size of one cell in pixels
        """
        self.maze = maze
        self.cell_size = cell_size
        self.window = tk.Tk()
        self.canvas = tk.Canvas(
            self.window,
            width=self.maze.width * cell_size,
            height=self.maze.height * cell_size
        )
        self.canvas.pack()

    def draw(self):
        """Renders the maze onto the canvas."""
        self.canvas.delete("all")

        for row_index, row in enumerate(self.maze.map):
            for col_index, cell in enumerate(row):
                x1, y1 = col_index * self.cell_size, row_index * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size

                color = "white" if cell == 0 else "black" if cell == 1 else "green"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        # Draw the robot
        robot_x, robot_y = self.maze.position
        x1, y1 = robot_x * self.cell_size, robot_y * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size
        self.canvas.create_oval(x1, y1, x2, y2, fill="red")

    def update(self, new_position):
        """
        Updates the robot's position and redraws the maze.

        :param new_position: New position of the robot (x, y)
        """
        if self.maze.move(new_position):
            self.draw()
        else:
            print("Invalid move: hit a wall or out of bounds.")

    def run(self):
        """Starts the application."""
        self.draw()
        self.window.mainloop()
