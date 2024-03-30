from User import User

# CONSTANTS
MAX_SCORE = 10 

# Player Class
class Player(User):
    def __init__(self, username: str, password: str, charisma: int, intel: int, attraction: int) -> bool:    
        # Stats for Individual Players
        if charisma + intel + attraction > MAX_SCORE or (charisma < 0 or intel < 0 or attraction < 0):
            print("Player Stats Exceeded Maximum of 10")
            return False
        self.level = 0

        self.charisma = charisma
        self.intelligence = intel
        self.attraction = attraction

        # Individual Attraction Score
        self._attractionScore = {
            "Serena": 0,
            "Grace": 0,
            "Afnan": 0,
            "Jack":  0,
        }
        
        # Need to Account for loading in a player
        return super().__init__(username, password)

    def loadUser(self, username:str)
    def updateStats(self, character, newAttractionScore) -> int:
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
                bias += self.charisma
            elif characterBias == "intel":
                bias += self.intelligence
            elif characterBias == "attraction":
                bias += self.attraction
            
        self._attractionScore[character] += newAttractionScore * (bias * 0.1 * 0.5 + 1)
        return self._attractionScore[character]
    
    
    # Not sure how to implement this 
    def chooseDialogue(self):
        pass

    def getFinalScore(self) -> int:
        finalScore = 0
        for score in self._attractionScore.values():
            score += finalScore
        
        return finalScore
        
    
    """ Public method to logout the player """
    def logout(self) -> None:
        super().logout()
        
        # Save Progress to Disk

