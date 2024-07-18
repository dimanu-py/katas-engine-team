class TennisGame4:
    scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1Name, player2Name):
        self.server = player1Name
        self.receiver = player2Name
        self.serverScore = 0
        self.receiverScore = 0

    def won_point(self, playerName):
        if self.server == playerName:
            self.serverScore += 1
        else:
            self.receiverScore += 1

    def score(self):
        if self.isDeuce():
            result = TennisResult("Deuce", "")
        elif self.serverHasWon():
            result = TennisResult("Win for " + self.server, "")
        elif self.receiverHasWon():
            result = TennisResult("Win for " + self.receiver, "")
        elif self.serverHasAdvantage():
            result = TennisResult("Advantage " + self.server, "")
        elif self.receiverHasAdvantage():
            result = TennisResult("Advantage " + self.receiver, "")
        else:
            result = TennisResult(self.scores[self.serverScore], self.scores[self.receiverScore])
        return result.format()

    def receiverHasAdvantage(self):
        return self.receiverScore >= 4 and (self.receiverScore - self.serverScore) == 1

    def serverHasAdvantage(self):
        return self.serverScore >= 4 and (self.serverScore - self.receiverScore) == 1

    def receiverHasWon(self):
        return self.receiverScore >= 4 and (self.receiverScore - self.serverScore) >= 2

    def serverHasWon(self):
        return self.serverScore >= 4 and (self.serverScore - self.receiverScore) >= 2

    def isDeuce(self):
        return self.serverScore >= 3 and self.receiverScore >= 3 and (self.serverScore == self.receiverScore)


class TennisResult:
    def __init__(self, serverScore, receiverScore):
        self.serverScore = serverScore
        self.receiverScore = receiverScore

    def format(self):
        if "" == self.receiverScore:
            return self.serverScore
        if self.serverScore == self.receiverScore:
            return self.serverScore + "-All"
        return self.serverScore + "-" + self.receiverScore

