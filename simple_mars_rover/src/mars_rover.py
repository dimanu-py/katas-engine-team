

class Rover:

    def execute(self, command: str) -> str:
        vertical_position = len(command)
        return f"{vertical_position}:0:N"
