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
        players_at_tie = self.points_player_one == self.points_player_two

        if players_at_tie:
            if self.points_player_one == 0:
                result = "Love-All"
            elif self.points_player_one == 1:
                result = "Fifteen-All"
            elif self.points_player_one == 2:
                result = "Thirty-All"
            else:
                result = "Deuce"

        else:
            result_player_one = ""
            result_player_two = ""

            result, result_player_one, result_player_two = self.get_result_one_player_has_zero_points(result_player_one,
                                                                                                      result_player_two)

            if self.points_player_one > self.points_player_two and self.points_player_one < 4:
                if self.points_player_one == 2:
                    result_player_one = "Thirty"
                if self.points_player_one == 3:
                    result_player_one = "Forty"
                if self.points_player_two == 1:
                    result_player_two = "Fifteen"
                if self.points_player_two == 2:
                    result_player_two = "Thirty"
                result = result_player_one + "-" + result_player_two
            if self.points_player_two > self.points_player_one and self.points_player_two < 4:
                if self.points_player_two == 2:
                    result_player_two = "Thirty"
                if self.points_player_two == 3:
                    result_player_two = "Forty"
                if self.points_player_one == 1:
                    result_player_one = "Fifteen"
                if self.points_player_one == 2:
                    result_player_one = "Thirty"
                result = result_player_one + "-" + result_player_two

            if self.points_player_one > self.points_player_two and self.points_player_two >= 3:
                result = f"Advantage {self.name_player_one}"

            if self.points_player_two > self.points_player_one and self.points_player_one >= 3:
                result = f"Advantage {self.name_player_two}"

            if self.points_player_one >= 4 and (self.points_player_one - self.points_player_two) >= 2:
                result = f"Win for {self.name_player_one}"
            if self.points_player_two >= 4 and (self.points_player_two - self.points_player_one) >= 2:
                result = f"Win for {self.name_player_two}"
        return result

    def get_result_one_player_has_zero_points(self, result_player_one: str, result_player_two: str) -> tuple:
        player_one_won = self.points_player_one > self.points_player_two
        result_winning_player, result_losing_player = (result_player_one, result_player_two) if player_one_won else (result_player_two, result_player_one)
        winning_player_points, losing_player_points = (self.points_player_one, self.points_player_two) if player_one_won else (self.points_player_two, self.points_player_one)

        if winning_player_points > 0 and losing_player_points == 0:
            if winning_player_points == 1:
                result_winning_player = "Fifteen"
            if winning_player_points == 2:
                result_winning_player = "Thirty"
            if winning_player_points == 3:
                result_winning_player = "Forty"

            result_losing_player = "Love"
            result_player_one, result_player_two = (result_winning_player, result_losing_player) if player_one_won else (result_losing_player, result_winning_player)
            result = result_player_one + "-" + result_player_two
        else:
            result = ""
        return result, result_player_one, result_player_two

    def increase_p1_score(self) -> None:
        self.points_player_one += 1

    def increase_p2_score(self) -> None:
        self.points_player_two += 1
