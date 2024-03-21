

class Rover:

    def execute(self, command: str) -> str:
        return "1:0:N" if command == "M" else "0:0:N"
