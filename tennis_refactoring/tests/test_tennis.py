import pytest

from tennis_refactoring.src.tennis_1 import TennisGame1
from tennis_refactoring.src.tennis_2 import TennisGame2
from tennis_refactoring.src.tennis_3 import TennisGame3
from tennis_refactoring.src.tennis_4 import TennisGame4
from tennis_refactoring.src.tennis_5 import TennisGame5
from tennis_refactoring.src.tennis_6 import TennisGame6

test_cases = [
    (0, 0, "Love-All", 'player1', 'player2'),
    (1, 1, "Fifteen-All", 'player1', 'player2'),
    (1, 1, "Fifteen-All", 'Nadal', 'Federer'),
    (2, 2, "Thirty-All", 'player1', 'player2'),
    (3, 3, "Deuce", 'player1', 'player2'),
    (4, 4, "Deuce", 'player1', 'player2'),

    (1, 0, "Fifteen-Love", 'player1', 'player2'),
    (0, 1, "Love-Fifteen", 'player1', 'player2'),
    (2, 0, "Thirty-Love", 'player1', 'player2'),
    (0, 2, "Love-Thirty", 'player1', 'player2'),
    (3, 0, "Forty-Love", 'player1', 'player2'),
    (0, 3, "Love-Forty", 'player1', 'player2'),
    (4, 0, "Win for player1", 'player1', 'player2'),
    (0, 4, "Win for player2", 'player1', 'player2'),

    (2, 1, "Thirty-Fifteen", 'player1', 'player2'),
    (1, 2, "Fifteen-Thirty", 'player1', 'player2'),
    (3, 1, "Forty-Fifteen", 'player1', 'player2'),
    (1, 3, "Fifteen-Forty", 'player1', 'player2'),
    (4, 1, "Win for player1", 'player1', 'player2'),
    (1, 4, "Win for player2", 'player1', 'player2'),

    (3, 2, "Forty-Thirty", 'player1', 'player2'),
    (2, 3, "Thirty-Forty", 'player1', 'player2'),
    (4, 2, "Win for player1", 'player1', 'player2'),
    (2, 4, "Win for player2", 'player1', 'player2'),

    (4, 3, "Advantage player1", 'player1', 'player2'),
    (3, 4, "Advantage player2", 'player1', 'player2'),
    (5, 4, "Advantage player1", 'player1', 'player2'),
    (4, 5, "Advantage player2", 'player1', 'player2'),
    (15, 14, "Advantage player1", 'player1', 'player2'),
    (14, 15, "Advantage player2", 'player1', 'player2'),

    (6, 4, 'Win for player1', 'player1', 'player2'),
    (4, 6, 'Win for player2', 'player1', 'player2'),
    (16, 14, 'Win for player1', 'player1', 'player2'),
    (14, 16, 'Win for player2', 'player1', 'player2'),

]


def play_game(TennisGame, p1Points, p2Points, p1Name, p2Name):
    game = TennisGame(p1Name, p2Name)
    for i in range(max(p1Points, p2Points)):
        if i < p1Points:
            game.won_point(p1Name)
        if i < p2Points:
            game.won_point(p2Name)
    return game


class TestTennisGame1:

    @pytest.mark.skip
    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()


class TestTennisGame2:

    @pytest.mark.skip
    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame2, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()


class TestTennisGame3:

    @pytest.mark.skip
    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame3, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()


class TestTennisGame4:

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame4, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()


class TestTennisGame5:

    @pytest.mark.skip
    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score_game5(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame5, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()


class TestTennisGame6:

    @pytest.mark.skip
    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(TennisGame6, p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()
