

class HighScoreTable:
    def __init__(self) -> None:
        self.scores = self.reloadScores()

    def reloadScores(self) -> dict:
        with 