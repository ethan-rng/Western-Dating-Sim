from User import User
import json
from exceptions import IncorrectPassword, IncorrectPrivilege
from hashlib import sha256

"""
TODO
: Complete the Developer class implementation
jumptoScreens(self, screenName: str) -> bool:
modifyUserStats(self, username: str, stats: dict) -> bool
debugGame(self) -> bool
"""

class Developer(User):
    Players:List[Player]

    def __init__(self) -> None:
        with open(f'../data/AdminPasswords.json') as file:
            file_data = json.load(file)

        # Attributes to Simulate Player
        self._charisma = 0
        self._intelligence = 0
        self._attraction = 0
        self._attractionScore = {
            "Serena": 0,
            "Grace": 0,
            "Afnan": 0,
            "Jack":  0,
        }

        super().__init__("developer", file_data["developer"])
    
    # PRIVATE FACING METHODS
    """ Helper function which checks if the developer is logged in before allowing access (throws IncorrectPrivilege exception) """
    def _checkPrivilege(self) -> None:
        if super().LoggedInUser != "developer":
            raise IncorrectPrivilege()
    

    # PUBLIC FACING METHODS
    """ Overrides the login in the user class (throws IncorrectPassword exception)"""
    def login(self, password:str) -> None:
        if super().password == sha256(password.encode()).hexdigest():
            super().LoggedInUser = self
        raise IncorrectPassword("developer", password)
    
    """ Public Method which allows the developer to jump to a specific screen (throws IncorrectPrivilege exception) """
    def jumptoScreen(self, screen:str) -> None:
        self._checkPrivilege()

    """ Public Method which allows the change any user's stats (throws IncorrectPrivilege, KeyError and UserNotFound exception) """
    def modifyUserStats(self, username:str, stat:str, character:str):
        self._checkPrivilege()

        

    """ Public Method which returns a dictionary of various debugging data (throws IncorrectPrivilege exception) """
    def debugGame(self) -> dict:
        self._checkPrivilege()


    # SETTERS AND GETTERS (All throw IncorrectPrivilege exception)
    @property
    def charisma(self):
        self._checkPrivilege()
        return self._charisma

    @charisma.setter
    def charisma(self, value):
        self._checkPrivilege()
        self._charisma = value

    @property
    def intelligence(self):
        self._checkPrivilege()
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value):
        self._checkPrivilege()
        self._intelligence = value

    @property
    def attraction(self):
        self._checkPrivilege()
        return self._attraction

    @attraction.setter
    def attraction(self, value):
        self._checkPrivilege()
        self._attraction = value

    @property
    def attractionScore(self):
        self._checkPrivilege()
        return self._attractionScore

    @attractionScore.setter
    def attractionScore(self, value):
        self._checkPrivilege()
        self._attractionScore = value




        

  