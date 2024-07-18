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

        elif max(self.points_player_one, self.points_player_two) < 4:
            result = self.get_result_without_tie_during_game(self.points_player_one, self.points_player_two)

        else:
            if self.points_player_one > self.points_player_two >= 3:
                result = f"Advantage {self.name_player_one}"
            if self.points_player_two > self.points_player_one >= 3:
                result = f"Advantage {self.name_player_two}"
            if self.points_player_one >= 4 and (self.points_player_one - self.points_player_two) >= 2:
                result = f"Win for {self.name_player_one}"
            if self.points_player_two >= 4 and (self.points_player_two - self.points_player_one) >= 2:
                result = f"Win for {self.name_player_two}"
        return result

    def get_result_without_tie_during_game(self, result_player_one: int, result_player_two: int) -> str:
        score_player_one = self.score_to_str(result_player_one)
        score_player_two = self.score_to_str(result_player_two)
        return score_player_one + "-" + score_player_two

    def score_to_str(self, score_player: int) -> str:
        if score_player == 0:
            result = "Love"
        elif score_player == 1:
            result = "Fifteen"
        elif score_player == 2:
            result = "Thirty"
        elif score_player == 3:
            result = "Forty"
        else:
            raise Exception("La cagué")
        return result

    def increase_p1_score(self) -> None:
        self.points_player_one += 1

    def increase_p2_score(self) -> None:
        self.points_player_two += 1
