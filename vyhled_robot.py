import xml.etree.ElementTree as ET
from maze import Bludiste


def load_maze_from_xml(file_path):
    """
    Načte bludiště z XML souboru.
    :param file_path: Cesta k XML souboru.
    :return: Instance třídy Maze.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    width = int(root.find("sirka").text)
    height = int(root.find("vyska").text)

    start_x = int(root.find("zacatek/x").text)
    start_y = int(root.find("zacatek/y").text)
    end_x = int(root.find("konec/x").text)
    end_y = int(root.find("konec/y").text)

    map_data = []
    for row in root.find("mapa"):
        row_values = [int(cell.text) if cell.text.isdigit() else cell.text for cell in row]
        map_data.append(row_values)

    return Bludiste(width, height, (start_x, start_y), (end_x, end_y), map_data)
