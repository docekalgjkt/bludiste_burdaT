class Maze:
    def __init__(self, width, height, start, end, map_layout):
        """
        Konstruktor pro třídu Maze.
        :param width: Šířka bludiště.
        :param height: Výška bludiště.
        :param start: Počáteční pozice (x, y).
        :param end: Konečná pozice (x, y).
        :param map_layout: Matice reprezentující bludiště.
        """
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        self.map_layout = map_layout
        self.position = start

    def can_move_to(self, x, y):
        """
        Zkontroluje, zda lze na danou pozici vstoupit.
        :param x: X souřadnice.
        :param y: Y souřadnice.
        :return: True, pokud je pohyb možný, jinak False.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map_layout[y][x] in (0, 'E')  # Volná cesta nebo východ
        return False

    def move_to(self, x, y):
        """
        Pokusí se přesunout na novou pozici.
        :param x: X souřadnice cíle.
        :param y: Y souřadnice cíle.
        :return: True, pokud se pohyb podařil, jinak False.
        """
        if self.can_move_to(x, y):
            self.position = (x, y)
            return True
        return False

    def at_end(self):
        """
        Zkontroluje, zda robot dosáhl cílové pozice.
        :return: True, pokud je robot na konci, jinak False.
        """
        return self.position == self.end

    def draw(self):
        """
        Vykreslí bludiště do konzole.
        """
        for y, row in enumerate(self.map_layout):
            for x, cell in enumerate(row):
                if (x, y) == self.position:
                    print("R", end=" ")
                elif cell == 1:
                    print("1", end=" ")
                elif cell == 'E':
                    print("E", end=" ")
                else:
                    print("0", end=" ")
            print()  # Nový řádek pro každý řádek mapy
        print()
