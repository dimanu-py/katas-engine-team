class TennisGame2:
    score_without_tie: dict[int, str] = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

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
        if self.points_player_one == self.points_player_two:
            result = self.get_tied_result()
        elif max(self.points_player_one, self.points_player_two) < 4:
            result = self.get_result_without_tie_during_game(self.points_player_one, self.points_player_two)
        else:
            result = self.get_result_when_advantage()
        return result

    def get_result_when_advantage(self) -> str:
        point_difference = self.points_player_one - self.points_player_two
        winning_player = self.name_player_one if point_difference > 0 else self.name_player_two

        if abs(point_difference) == 1:
            return f"Advantage {winning_player}"

        return f"Win for {winning_player}"

    def get_tied_result(self) -> str:
        if self.points_player_one < 3:
            result = f"{self.score_to_str(self.points_player_one)}-All"
        else:
            result = "Deuce"
        return result

    def get_result_without_tie_during_game(self, result_player_one: int, result_player_two: int) -> str:
        score_player_one = self.score_to_str(result_player_one)
        score_player_two = self.score_to_str(result_player_two)
        return score_player_one + "-" + score_player_two

    def score_to_str(self, score_player: int) -> str:
        try:
            return self.score_without_tie[score_player]
        except KeyError as e:
            raise e.add_note("La cagué")

    def increase_p1_score(self) -> None:
        self.points_player_one += 1

    def increase_p2_score(self) -> None:
        self.points_player_two += 1
