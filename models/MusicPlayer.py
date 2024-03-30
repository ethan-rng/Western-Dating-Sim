import vlc

"""
TODO
Finished, need to do testing to check if code is able to play music without blocking execution
"""

class MusicPlayer:
    def __init__(self) -> None:
        self._current_song = None
        self._player = None

    def changeCurrMusic(self, song:str):
        self._current_song = song
        self.playMusic()

    def playMusic(self):
        if self._player == None:
            self._player = vlc.MediaPlayer(f"../data/songs/{self._current_song}")     
        self._player.play()

    def stopMusic(self):
        self._player.stop()
        