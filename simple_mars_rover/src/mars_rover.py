GRID_SIZE = 10
ORIENTATION = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


class Rover:

    def __init__(self) -> None:
        self.orientation = 0

    def execute(self, command: str) -> str:
        for c in command:
            if c == "R":
                self.orientation += 1
            if c == "L":
                self.orientation -= 1

        vertical_position = command.count('M') % GRID_SIZE
        return f"{vertical_position}:0:{ORIENTATION[self.orientation % 4]}"
