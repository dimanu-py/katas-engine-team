class TennisGame2:
    def __init__(self, planer_one_name: str, player_two_name: str) -> None:
        self.name_player_one = planer_one_name
        self.name_player_two = player_two_name
        self.points_player_one = 0
        self.points_player_two = 0

    def won_point(self, player_name: str) -> None:
        if player_name == self.name_player_one:
            self.increase_p1_score()
        else:
            self.increase_p2_score()

    def score(self) -> str:
        result = ""
        if (self.points_player_one == self.points_player_two and self.points_player_one < 3):
            if (self.points_player_one == 0):
                result = "Love"
            if (self.points_player_one == 1):
                result = "Fifteen"
            if (self.points_player_one == 2):
                result = "Thirty"
            result += "-All"
        if (self.points_player_one == self.points_player_two and self.points_player_one > 2):
            result = "Deuce"

        result_player_one = ""
        result_player_two = ""
        if (self.points_player_one > 0 and self.points_player_two == 0):
            if (self.points_player_one == 1):
                result_player_one = "Fifteen"
            if (self.points_player_one == 2):
                result_player_one = "Thirty"
            if (self.points_player_one == 3):
                result_player_one = "Forty"

            result_player_two = "Love"
            result = result_player_one + "-" + result_player_two
        if (self.points_player_two > 0 and self.points_player_one == 0):
            if (self.points_player_two == 1):
                result_player_two = "Fifteen"
            if (self.points_player_two == 2):
                result_player_two = "Thirty"
            if (self.points_player_two == 3):
                result_player_two = "Forty"

            result_player_one = "Love"
            result = result_player_one + "-" + result_player_two

        if (self.points_player_one > self.points_player_two and self.points_player_one < 4):
            if (self.points_player_one == 2):
                result_player_one = "Thirty"
            if (self.points_player_one == 3):
                result_player_one = "Forty"
            if (self.points_player_two == 1):
                result_player_two = "Fifteen"
            if (self.points_player_two == 2):
                result_player_two = "Thirty"
            result = result_player_one + "-" + result_player_two
        if (self.points_player_two > self.points_player_one and self.points_player_two < 4):
            if (self.points_player_two == 2):
                result_player_two = "Thirty"
            if (self.points_player_two == 3):
                result_player_two = "Forty"
            if (self.points_player_one == 1):
                result_player_one = "Fifteen"
            if (self.points_player_one == 2):
                result_player_one = "Thirty"
            result = result_player_one + "-" + result_player_two

        if (self.points_player_one > self.points_player_two and self.points_player_two >= 3):
            result = f"Advantage {self.name_player_one}"

        if (self.points_player_two > self.points_player_one and self.points_player_one >= 3):
            result = f"Advantage {self.name_player_two}"

        if (self.points_player_one >= 4 and self.points_player_two >= 0 and (self.points_player_one - self.points_player_two) >= 2):
            result = f"Win for {self.name_player_one}"
        if (self.points_player_two >= 4 and self.points_player_one >= 0 and (self.points_player_two - self.points_player_one) >= 2):
            result = f"Win for {self.name_player_two}"
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.increase_p1_score()

    def SetP2Score(self, number):
        for i in range(number):
            self.increase_p2_score()

    def increase_p1_score(self) -> None:
        self.points_player_one += 1

    def increase_p2_score(self) -> None:
        self.points_player_two += 1
