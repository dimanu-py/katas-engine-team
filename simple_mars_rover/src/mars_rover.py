GRID_SIZE = 10
ORIENTATION = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


class Rover:

    def __init__(self) -> None:
        self.orientation = 0
        self.vertical_position = 0

    def execute(self, command: str) -> str:
        for c in command:
            if c == "R":
                self.orientation += 1
            elif c == "L":
                self.orientation -= 1
            elif c == "M":
                if self.orientation == 0:
                    self.vertical_position += 1
                elif self.orientation == 2:
                    self.vertical_position -= 1

        self.vertical_position %= GRID_SIZE
        return f"{self.vertical_position}:0:{ORIENTATION[self.orientation % 4]}"
