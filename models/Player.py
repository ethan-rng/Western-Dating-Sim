from models.User import User
from models.exceptions import IllegalStats, UserNotFound
from typing import List
import os, json

# CONSTANTS
MAX_SCORE = 10
CHARACTER_BIAS = {
    "Serena": ["charisma", "intel"]
}


# Player Class
class Player(User):
    Players: List[dict] = []

    def __init__(self) -> None:
        super().__init__()
        if not Player.Players:
            with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
                jsonData = json.load(file)
                for data in jsonData:
                    Player.Players.append({
                        "username": data["username"],
                        "level": data["level"],
                        "charisma": data["charisma"],
                        'intel': data["intel"],
                        "attraction": data["attraction"],
                        "attractionScore": data["attractionScore"],
                        "finalScore": data["finalScore"],
                    })

        # Base Stats
        self._level = 1
        self._charisma = 0
        self._intelligence = 0
        self._attraction = 0

        # Individual Attraction Score
        self._attractionScore = {
            "Serena": 0,
        }

    # PUBLIC FACING METHODS
    """ Public Method which creates a new player account (throws AdminLevelAccount DuplicateUser, IllegalStats) """
    def createPlayer(self, username: str, password: str, charisma: int, intel: int, attraction: int) -> None:

        # Stats for Individual Players
        if charisma + intel + attraction > MAX_SCORE or (charisma < 0 or intel < 0 or attraction < 0):
            raise IllegalStats(charisma, intel, attraction)

        super().createUser(username, password)

        # Base Stats
        self._level = 1
        self._charisma = charisma
        self._intelligence = intel
        self._attraction = attraction

        # Individual Attraction Score
        self._attractionScore = {
            "Serena": 0,
        }

    """ Public Method which allows the player to load from a previous game state (throws UserNotFound exception) """

    def loadPlayer(self, username: str) -> None:
        super().loadUser(username)
        with open(os.path.join("models", "data", "UserGameStates.json"), "r") as file:
            jsonData = json.load(file)
            for data in jsonData:
                if data["username"] == username:
                    self._level = data["level"]
                    self._charisma = data["charisma"]
                    self._intelligence = data["intel"]
                    self._attraction = data["attraction"]
                    self._attractionScore = data["attractionScore"]
                    return
                
            raise UserNotFound(username)

    """ Public Method which saves all progress of the player to the disk """
    def saveProgress(self) -> None:
        with open(os.path.join("models", "data", "UserGameStates.json"), "w") as file:
            playerData = {
                "username": self.username,
                "level": self._level,
                "charisma": self._charisma,
                "intel": self._intelligence,
                "attraction": self._attraction,
                "attractionScore": self._attractionScore,
                "finalScore": self.getFinalScore(),
            }
            Player.Players.append(playerData)
            json.dump(Player.Players, file, ensure_ascii=False, indent=4)

    """ Public Method which allows the player to update their stats after an interaction (throws IncorrectPrivilege, KeyError)"""
    def updateStats(self, character: str, newAttractionScore: int) -> int:
        # Checking If AttractionScore is Maxed Out or Mined Out
        if self._attractionScore[character] >= 100 and newAttractionScore > 0:
            print(f"Attraction Score Maxed Out With {character}")
            return 100
        if self._attractionScore[character] <= 0 and newAttractionScore < 0:
            print(f"Attraction Score Minimized With {character}")
            return 0

        # Calculating New Attraction Score After Factoring Player Bias
        bias = 0
        for characterBias in CHARACTER_BIAS[character]:
            if characterBias == "charisma":
                bias += self._charisma
            elif characterBias == "intel":
                bias += self._intelligence
            elif characterBias == "attraction":
                bias += self._attraction

        self._attractionScore[character] += newAttractionScore * (bias * 0.1 * 0.5 + 1)
        return self._attractionScore[character]

    """ Public Method which calculates the final score of the player (Sum of all the individuals scores) """
    def getFinalScore(self) -> int:
        finalScore = 0
        for score in self._attractionScore.values():
            finalScore += score

        return finalScore

    # SETTERS AND GETTERS
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def charisma(self):
        return self._charisma

    @charisma.setter
    def charisma(self, value):
        self._charisma = value

    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        self._intelligence = value

    @property
    def attraction(self):
        return self._attraction

    @attraction.setter
    def attraction(self, value):
        self._attraction = value

    @property
    def attractionScore(self):
        return self._attractionScore

    @attractionScore.setter
    def attractionScore(self, value):
        self._attractionScore = value
