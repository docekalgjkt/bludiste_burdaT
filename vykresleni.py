import tkinter as tk

# Vstupní vnořený seznam reprezentující bludiště (0 = cesta, 1 = zeď)
maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

# Nastavení velikosti každé buňky
cell_size = 40

# Funkce pro vykreslení bludiště
def draw_maze(canvas, maze_data):
    for row_index, row in enumerate(maze_data):
        for col_index, cell in enumerate(row):
            x1 = col_index * cell_size
            y1 = row_index * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = "black" if cell == 1 else "white"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Bludiště")

# Vytvoření canvasu (plátna)
canvas_width = len(maze[0]) * cell_size
canvas_height = len(maze) * cell_size
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Vykreslení bludiště
draw_maze(canvas, maze)

# Spuštění aplikace
root.mainloop()
