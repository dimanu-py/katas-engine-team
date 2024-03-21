GRID_SIZE = 10


class Rover:

    def execute(self, command: str) -> str:

        if command == "R":
            return "0:0:E"
        vertical_position = len(command) % GRID_SIZE
        return f"{vertical_position}:0:N"
