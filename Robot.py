class Maze:
    def __init__(self, width, height, start, end, layout):
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        self.layout = layout
        self.current_position = start

    def can_move(self, new_x, new_y):
        if 0 <= new_x < self.width and 0 <= new_y < self.height:
            return self.layout[new_y][new_x] in (0, 'E')  # Free path or exit
        return False

    def move(self, new_x, new_y):
        if self.can_move(new_x, new_y):
            self.current_position = (new_x, new_y)
            return True
        return False

    def is_finished(self):
        return self.current_position == self.end

    def draw_maze(self):
        for row_index, row in enumerate(self.layout):
            for col_index, cell in enumerate(row):
                if (col_index, row_index) == self.current_position:
                    print("P", end=" ")  # Player position
                elif cell == 1:
                    print("#", end=" ")  # Wall
                elif cell == 'E':
                    print("X", end=" ")  # Exit
                else:
                    print(".", end=" ")  # Path
            print()  # New line after each row
        print()
