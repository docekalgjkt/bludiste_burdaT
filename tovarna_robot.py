from Robot import Maze
from vyhled_robot import load_maze_from_xml
from vykresleni import MazeRenderer

class RobotFactoryBase:
    """Základní továrna pro tvorbu robotů a jejich vizualizace."""
    def vytvor_robota(self, maze):
        raise NotImplementedError("Tato metoda musí být implementována v podtřídě.")

    def vytvor_vizualizaci_robota(self, canvas, robot):
        raise NotImplementedError("Tato metoda musí být implementována v podtřídě.")


class ZakladniTovarnaRobotu(RobotFactoryBase):
    """Továrna pro vytvoření základního typu robota."""
    def vytvor_robota(self, maze):
        return Maze(maze)

    def vytvor_vizualizaci_robota(self, canvas, robot):
        return load_maze_from_xml(canvas, robot)
