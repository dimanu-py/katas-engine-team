from enum import Enum

ROTATION_STEP = 1
FORWARD_STEP = 1

GRID_SIZE = 10
ORIENTATION = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


class Orientation(int, Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Rover:

    def __init__(self) -> None:
        self.orientation = Orientation.NORTH
        self.vertical_position = 0
        self.horizontal_position = 0

    def execute(self, command: str) -> str:
        for c in command:
            if c == "R":
                self.orientation += ROTATION_STEP
            elif c == "L":
                self.orientation -= ROTATION_STEP
            elif c == "M":
                if self.orientation == Orientation.NORTH:
                    self.vertical_position += FORWARD_STEP
                elif self.orientation == Orientation.SOUTH:
                    self.vertical_position -= FORWARD_STEP
                elif self.orientation == Orientation.EAST:
                    self.horizontal_position += FORWARD_STEP
                elif self.orientation == Orientation.WEST:
                    self.horizontal_position -= FORWARD_STEP

        self.vertical_position %= GRID_SIZE
        self.horizontal_position %= GRID_SIZE

        return f"{self.vertical_position}:{self.horizontal_position}:{ORIENTATION[self.orientation % 4]}"
