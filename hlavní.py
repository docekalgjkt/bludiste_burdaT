from maze import Maze
from visualization import MazeCanvas
from robot import MazeRobot
from robot_display import RobotDisplay
import time


def move_robot(robot, display, path, canvas, delay=0.5):
    """Posouvá robota po naplánované cestě."""
    for step in path:
        dx = step[0] - robot.position[0]
        dy = step[1] - robot.position[1]

        if robot.move((dx, dy)):
            display.update_view()
            canvas.window.update()  # Aktualizuje GUI
            time.sleep(delay)  # Zpoždění mezi pohyby


if __name__ == "__main__":
    maze = Maze(4, 4, (0, 0), (3, 3), [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 0, 'E']
    ])

    canvas = MazeCanvas(maze)
    robot = MazeRobot(maze)
    display = RobotDisplay(canvas, robot)

    # Vykreslení počátečního stavu
    canvas.draw_maze()
    display.draw_robot()

    # Vyhledání cesty a pohyb robota
    path = robot.find_path()
    move_robot(robot, display, path, canvas)

    canvas.window.mainloop()
