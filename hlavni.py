from tovarna_robot import ZakladniTovarnaRobotu
from vyhled_robot import load_maze_from_xml
from xml_nacitani import nacti_bludiste_z_xml
import time


def move_robot(robot, robot_view, steps, visualization, delay=0.5):
    """Posouvá robota po naplánované cestě."""
    for step in steps:
        dx = step[0] - robot.position[0]
        dy = step[1] - robot.position[1]

        if robot.move((dx, dy)):
            robot_view.update()
            visualization.window.update()  # Aktualizuje GUI
            time.sleep(delay)  # Zpoždění mezi pohyby


if __name__ == "__main__":
    # Načtení bludiště z XML souboru
    maze = load_maze_from_xml("Bludiste_xml.xml")

    # Vytvoření továrny pro robota a jeho zobrazení
    robot_factory = ZakladniTovarnaRobotu()
    robot = robot_factory.vytvor_robota(maze)
    visualization = nacti_bludiste_z_xml(maze)
    robot_view = robot_factory.create_robot_view(visualization, robot)

    # Vykreslení počátečního stavu
    visualization.draw_maze()
    robot_view.draw()

    # Vyhledání cesty a pohyb robota
    steps = robot.find_path()
    move_robot(robot, robot_view, steps, visualization)

    visualization.window.mainloop()
