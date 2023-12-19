import math
from typing import List

from config import BOARD_RADIUS, CENTER_X, CENTER_Y


def calculate_pos_contour(num_points: int) -> List[int]:
    """
    Helper function to calculate the box positions
    on the board's contour.
    """
    positions = []
    angle = 0
    rotation = 2 * math.pi / num_points

    for _ in range(num_points):
        x = CENTER_X + int(BOARD_RADIUS * math.cos(angle))
        y = CENTER_Y + int(BOARD_RADIUS * math.sin(angle))
        positions.append((x, y))
        angle += rotation

    return positions


def calculate_all_pos() -> List[int]:
    """
    Utility function to calculate all boxes positions on the whole board. 
    """
    # First, evaluate positions on contour (42 boxes)
    box_positions = calculate_pos_contour(42)

    # Adding box positions on "bridges",
    # diameters excluding extremities (11 points)
    for n_bridge in range(3):
        # Defining extremities
        begin_pos = box_positions[n_bridge * 7]
        end_pos = box_positions[n_bridge * 7 + 21]
        # Managing the 11 boxes on the current bridge
        for n_box in range(1, 12):
            fraction = n_box / 12
            box_x = begin_pos[0] + fraction * (end_pos[0] - begin_pos[0])
            box_y = begin_pos[1] + fraction * (end_pos[1] - begin_pos[1])
            # Appending position if not on the center
            if n_box != 6:
                box_positions.append((box_x, box_y))
            else:
                center_position = (box_x, box_y)  # Storing the center's position for later

    # Finally, appending the center's position
    box_positions.append(center_position)

    return box_positions
