

class Rover:

    def execute(self, command: str) -> str:
        vertical_position = len(command)
        if vertical_position >= 10:
            vertical_position = 0
        return f"{vertical_position}:0:N"
