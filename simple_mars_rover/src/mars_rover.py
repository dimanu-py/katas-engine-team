GRID_SIZE = 10
ORIENTATION = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


class Rover:

    def execute(self, command: str) -> str:

        number_rigth_rotations = command.count('R') % 4
        number_left_rotations = command.count('L') % 4
        vertical_position = command.count('M') % GRID_SIZE
        return f"{vertical_position}:0:{ORIENTATION[(number_rigth_rotations - number_left_rotations) % 4]}"
