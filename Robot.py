class MazeRobot:
    def __init__(self, maze):
        """
        Konstruktor pro robotu.
        :param maze: Instance třídy Maze.
        """
        self.maze = maze
        self.position = maze.start
        self.path = []

    def move(self, direction):
        """
        Posune robota na základě zadaného směru.
        :param direction: Směr pohybu (např. (0, 1) znamená pohyb dolů).
        :return: True pokud se pohyb uskutečnil, jinak False.
        """
        new_position = (self.position[0] + direction[0], self.position[1] + direction[1])
        if self.maze.move_to(*new_position):
            self.position = new_position
            self.path.append(new_position)
            return True
        return False

    def find_path(self):
        """
        Hledání cesty bludištěm pomocí algoritmu prohledávání do hloubky (DFS).
        :return: Seznam pozic, které tvoří cestu.
        """
        visited = set()
        stack = [(self.position, [])]

        while stack:
            current_position, current_path = stack.pop()
            if current_position in visited:
                continue
            visited.add(current_position)

            if current_position == self.maze.end:
                return current_path

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_position = (current_position[0] + dx, current_position[1] + dy)
                if self.maze.can_move_to(*next_position):
                    stack.append((next_position, current_path + [next_position]))
        return []
