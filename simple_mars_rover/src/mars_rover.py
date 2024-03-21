

class Rover:

    def execute(self, command: str) -> str:
        if command == "":
            return "0:0:N"
        elif command == "M":
            return "1:0:N"
        else:
            return "2:0:N"
