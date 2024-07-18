class TennisGame4:
    scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player_one_name, player_two_name):
        self.server = player_one_name
        self.receiver = player_two_name
        self.server_score = 0
        self.receiver_score = 0

    def won_point(self, player_name):
        if self.server == player_name:
            self.server_score += 1
        else:
            self.receiver_score += 1

    def score(self):
        if self.is_deuce():
            result = TennisResult("Deuce", "")
        elif self.server_has_won():
            result = TennisResult("Win for " + self.server, "")
        elif self.receiver_has_won():
            result = TennisResult("Win for " + self.receiver, "")
        elif self.server_has_advantage():
            result = TennisResult("Advantage " + self.server, "")
        elif self.receiver_has_advantage():
            result = TennisResult("Advantage " + self.receiver, "")
        else:
            result = TennisResult(self.scores[self.server_score], self.scores[self.receiver_score])
        return result.format()

    def receiver_has_advantage(self):
        return self.receiver_score >= 4 and (self.receiver_score - self.server_score) == 1

    def server_has_advantage(self):
        return self.server_score >= 4 and (self.server_score - self.receiver_score) == 1

    def receiver_has_won(self):
        return self.receiver_score >= 4 and (self.receiver_score - self.server_score) >= 2

    def server_has_won(self):
        return self.server_score >= 4 and (self.server_score - self.receiver_score) >= 2

    def is_deuce(self):
        return self.server_score >= 3 and self.receiver_score >= 3 and (self.server_score == self.receiver_score)


class TennisResult:
    def __init__(self, server_score, receiver_score):
        self.server_score = server_score
        self.receiver_score = receiver_score

    def format(self):
        if "" == self.receiver_score:
            return self.server_score
        if self.server_score == self.receiver_score:
            return self.server_score + "-All"
        return self.server_score + "-" + self.receiver_score
