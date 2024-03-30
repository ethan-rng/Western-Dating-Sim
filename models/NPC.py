# Need To Figure Out
from typing import List


class NPC:
    def __init__(self, name:str, bias:List[str]) -> None:
        self._name = name
        self._attractionScore = 0
        self._bias = bias

    # IDFK what this does
    def respondToPlayer(self, dialogue) -> None:
        print(f"NPC: {self._name} says: {dialogue}")

    def setAttractionLevel(self, level):
        self.attractionLevel = level

    def __str__(self) -> str:
        return f"NPC: {self._name} likes {self._bias}"