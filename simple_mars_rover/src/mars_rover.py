GRID_SIZE = 10
ORIENTATION = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


class Rover:

    def execute(self, command: str) -> str:
        orientation = 0
        for c in command:
            if c == "R":
                orientation += 1
            if c == "L":
                orientation -= 1

        vertical_position = command.count('M') % GRID_SIZE
        return f"{vertical_position}:0:{ORIENTATION[orientation % 4]}"
