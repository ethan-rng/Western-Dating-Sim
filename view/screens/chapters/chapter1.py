from view.screens.chapters.Chapter import Chapter

dialogue = [
    "A bustling Talbot College hallway...",
    "You bump into a hurried girl (LI), causing her to drop her music score...",
    "Oh, sorry! Gotta run!!",
    "Y/N : Wait!",
    "She runs off, and you notice a music sheet with contact info for an exam..",
    "Narrator: She's gone but left a dropped sheet with her contact. Do you return it?"
]

class Chapter1(Chapter):
    def __init__(self):
        super().__init__(dialogue)
