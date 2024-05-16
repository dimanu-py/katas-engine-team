from abc import ABC, abstractmethod
from enum import Enum
from typing import Union

ROTATION_STEP = 1
FORWARD_STEP = 1

GRID_SIZE = 10
NUMBER_ORIENTATIONS = 4
ORIENTATION = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


class Orientation(int, Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class OrientationAdvanced(ABC):

    @abstractmethod
    def rotate_left(self) -> "OrientationAdvanced":
        pass


class North(OrientationAdvanced):
    def rotate_left(self) -> OrientationAdvanced:
        return West()


class South(OrientationAdvanced):

    def rotate_left(self) -> "OrientationAdvanced":
        return self


class West(OrientationAdvanced):
    def rotate_left(self) -> OrientationAdvanced:
        return South()


class Rover:

    def __init__(self) -> None:
        self.orientation = Orientation.NORTH
        self.orientation_advanced: Union[North, West] = North()
        self.vertical_position = 0
        self.horizontal_position = 0

    def execute(self, command: str) -> str:
        command_instructions = {
            "R": self.rotate_right,
            "L": self.rotate_left,
            "M": self.move
        }
        for step in command:
            command_instructions[step]()

        return str(self)

    def __str__(self):
        return f"{self.vertical_position}:{self.horizontal_position}:{ORIENTATION[self.orientation % 4]}"

    def move(self) -> None:
        if self.orientation == Orientation.NORTH:
            self.vertical_position += FORWARD_STEP
        elif self.orientation == Orientation.SOUTH:
            self.vertical_position -= FORWARD_STEP
        elif self.orientation == Orientation.EAST:
            self.horizontal_position += FORWARD_STEP
        elif self.orientation == Orientation.WEST:
            self.horizontal_position -= FORWARD_STEP
        else:
            raise NotImplementedError

        self.vertical_position %= GRID_SIZE
        self.horizontal_position %= GRID_SIZE

    def rotate_left(self) -> None:
        self.orientation = (self.orientation - ROTATION_STEP) % NUMBER_ORIENTATIONS
        if isinstance(self.orientation_advanced, North):
            self.orientation_advanced = self.orientation_advanced.rotate_left()

    def rotate_right(self) -> None:
        self.orientation = (self.orientation + ROTATION_STEP) % NUMBER_ORIENTATIONS
