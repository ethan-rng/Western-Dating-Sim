import pygame
import sys
import os
import threading

from controller.constants import *
from view.screens.chapters import *
from models.Player import Player
from models.Instructor import Instructor
from typing import Optional


# Importing Screens
from view.screens.Menu import Menu
from view.screens.NewGame import NewGameScreen
from view.screens.settings.SettingsMain import SettingsMain
from view.screens.settings.SettingsControls import SettingsControls
from view.screens.settings.SettingsSound import SettingsSound
from view.screens.help.Help1 import Help1
from view.screens.help.Help2 import Help2
from view.screens.NewGame import NewGameScreen
from view.screens.Login import Login
from view.screens.InstructorLogin import InstructorLogin
from view.screens.InstructorPanel import InstructorPanel
from view.screens.chapters.Chapter1 import Chapter1
from view.screens.chapters.Chapter2 import Chapter2
from view.screens.chapters.Chapter3 import Chapter3
from view.screens.chapters.Chapter4 import Chapter4
from view.screens.chapters.Chapter5 import Chapter5
from view.screens.chapters.Chapter6 import Chapter6
from view.screens.Album import Album
from view.screens.Language import Language
from view.screens.VideoSettings import VideoSettings

class RunGame:
    def __init__(self) -> None:
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Dating Simulator Ver. Western")

        # Initialize Sounds
        pygame.mixer.init()
        self.music_thread: Optional[threading.Thread] = None
        # self.start_music("backsound.mp3")

        # Initializing Variables for PyGame
        self.currPlayer: Player = Player()
        self.screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        self.menu = Menu()
        self.main_settings = SettingsMain()
        self.control_settings = SettingsControls()
        self.sound_settings = SettingsSound()
        self.help1_page = Help1()
        self.help2_page = Help2()
        self.album_screen = Album()
        self.language_screen = Language()
        self.videosettings_screen = VideoSettings()
        self.new_game_screen = NewGameScreen(self.currPlayer)
        self.login_screen = Login()

        # Controller Variables For The Game
        self.game_state = "main"
        # self.currPlayer.level = 2 # comment out to do normal game
        self.controls = {}  # issue

        # For Creating User
        username: str = ""
        password: str = ""

        # Main Loop (Determines Which Screen To Display)
        while True:
            if self.game_state == "main":
                self.game_state = Menu().event_handler(self.screen)
            if self.game_state == "login":
                loginOutcome: tuple[str, str, str] = self.login_screen.event_handler(self.screen, self.currPlayer, False)

                self.game_state = loginOutcome[0]
                if self.game_state == "start":
                    # Used to Persist to Next Stage
                    username = loginOutcome[1]
                    password = loginOutcome[2]
                    
            elif self.game_state == "load":
                self.game_state = self.login_screen.event_handler(self.screen, self.currPlayer, True)[0]
                    
            elif self.game_state == "start":
                self.game_state = NewGameScreen(self.currPlayer).event_handler(self.screen, username, password)

                # Clearing This Out For The Next Time Someone Makes a New Game
                username = ""
                password = ""

            elif self.game_state == "help1":
                self.game_state = Help1().event_handler(self.screen)
            elif self.game_state == "help2":
                self.game_state = Help2().event_handler(self.screen)
            elif self.game_state == "album":
                self.game_state = Album().event_handler(self.screen)
            elif self.game_state == "language":
                self.game_state = Language().event_handler(self.screen)
            elif self.game_state == "videosettings":
                self.game_state = VideoSettings().event_handler(self.screen)
            elif self.game_state == "settings":
                self.game_state = SettingsMain().event_handler(self.screen)
            elif self.game_state == "controls":
                self.game_state = SettingsControls().event_handler(self.screen)
            elif self.game_state == "sound":
                self.game_state = SettingsSound().event_handler(self.screen)
            elif self.game_state == "load":
                self.game_state = Login()
            elif self.game_state == "instructor_login":
                self.game_state = InstructorLogin().event_handler(self.screen)
            elif self.game_state == "instructor_panel":
                self.game_state = InstructorPanel().event_handler(self.screen)
            elif self.game_state == "chp" and self.currPlayer.level == 1:
                self.game_state = Chapter1(self.screen,
                                           self.currPlayer,
                                           "Chapter 1",
                                           [
                                               "A bustling Talbot College hallway...",
                                               f"You bump into a hurried girl, causing her to drop her music score...",
                                               "Oh, sorry! Gotta run!!",
                                               f"{self.currPlayer.username} : Wait!",
                                               "She runs off, and you notice a music sheet with contact info for an exam..",
                                               "Narrator: She's gone but dropped her sheet music on the ground. You see her name (Serena) and her number on the sheet. Do you return it?"
                                           ],
                                           [
                                               os.path.join('view', 'assets', 'chp1', 'talbot-1.jpg'),
                                               os.path.join('view', 'assets', 'chp1', 'talbot-2.jpg'),
                                               os.path.join('view', 'assets', 'chp1', 'talbot-3.jpg'),
                                               os.path.join('view', 'assets', 'chp1', 'talbot-4.jpg'),
                                               os.path.join('view', 'assets', 'chp1', 'talbot-5.jpg'),
                                               os.path.join('view', 'assets', 'chp1', 'talbot-6.jpg')
                                           ],
                                           self.controls
                                           ).event_handler()

            elif self.game_state == "chp" and self.currPlayer.level == 2:
                self.game_state = Chapter2(self.screen,
                                           self.currPlayer,
                                           "Chapter 2",
                                           [
                                               "You agree to meet up at UCC to return the sheet music.",
                                               "She thanks you, and you guys decide to grab something to eat at the Spoke..",
                                               "What do you talk about in line?",
                                               "Oh! I have an idea. As thanks for helping me get my sheet music back, I can draw a picture of you!",
                                               "How do you respond?",
                                               "Let’s meet at my place tomorrow at 1pm!"
                                           ],
                                           [
                                               os.path.join('view', 'assets', 'chp2', 'spoke-1.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-2.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-3.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-3.1.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-3.2.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-4.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-5.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-5.1.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-5.2.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-6.jpg'),
                                           ],
                                           self.controls
                                           ).event_handler()

            elif self.game_state == "chp" and self.currPlayer.level == 3:
                self.game_state = Chapter3(self.screen,
                                           self.currPlayer,
                                           "Chapter 3",
                                           [
                                               "S: Sorry, it is really messy in here. ",
                                               "How do you respond?",
                                               "S: Haha. Yeah. Come follow me.",
                                               "She laughs, appreciating the joke, and leads you into her drawing room. You take a seat on a stool, feeling shy under her intense focus. After an hour, she’s finished.",
                                               "S: Here, I finished take a look.",
                                               "How do you respond?",
                                               "S: Thanks you so much again for bringing back my music score and modeling for me.",
                                               "You look around the room, and notice family pictures.",
                                               "Wow you and your family must be close!",
                                               "S: Yeah, I love spending time with them. I have an older brother who is annoying.. Haha",
                                               "How do you respond?",
                                               "As it gets late, the visit comes to an end",
                                               "S: Alright, it’s probably time for you to go. Get home safe!",
                                               "After some time to think, you decide to call Serena to ask if she wants to get Boba sometime... ",
                                               "Y/N: Hi Serena, I really enjoyed today. Do you want to get Boba sometime?"
                                           ],
                                           [
                                               os.path.join('view', 'assets', 'chp3', 'herplace-1.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-2.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-3.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-4.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-5.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-6.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-7.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-8.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-9.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-10.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-11.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-12.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-13.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-14.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-15.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-15.1.jpg'),
                                               os.path.join('view', 'assets', 'chp3', 'herplace-15.2.jpg'),
                                           ],
                                           self.controls
                                           ).event_handler()
                # Chapter3(self.screen, self.GameSession.player)
            elif self.game_state == "chp" and self.currPlayer.level == 4:
                    self.game_state = Chapter4(self.screen,
                                           self.currPlayer,
                                           "Chapter 4",
                                           [
                                               "What should I wear?",
                                               "What should I wear?",
                                               "Hm... now what should I bring?",
                                               "Hm... now what should I bring?",
                                               "You and Serena get boba together, chatting about your hobbies, dreams, and what you're looking for in a relationship. As the date winds down, the bill arrives.",
                                               "Do you pay the bill?",
                                               "S: I had a lot of fun today!",
                                               "Feeling positive about the day, you decide to text Serena.",
                                               "Feeling positive about the day, you decide to text Serena."
                                           ],
                                           [
                                               os.path.join('view', 'assets', 'chp4', 'date-1.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-2.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-3.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-4.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-5.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-6.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-6.1.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-6.2.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-6.3.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-7.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-8.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-8.1.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-8.2.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-8.3.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-9.jpg'),
                                               os.path.join('view', 'assets', 'chp4', 'date-10.jpg')
                                           ],
                                           self.controls
                                           ).event_handler()
                # Chapter4(self.screen, self.GameSession.player)
            elif self.game_state == "chp" and self.currPlayer.level == 5:
                    self.game_state = Chapter5(self.screen,
                                           self.currPlayer,
                                           "Chapter 5",
                                           [
                                               "You've decided it's time to see if Serena wants to take things to the next level. You meet at UC Hill.",
                                               "So, what's up?"
            
                                    
                                           ],
                                           [
                                               os.path.join('view', 'assets', 'chp5', 'uchill-1.jpg'),
                                               os.path.join('view', 'assets', 'chp5', 'uchill-2.jpg'),
                                               os.path.join('view', 'assets', 'chp5', 'uchill-2.1.jpg'),
                                               os.path.join('view', 'assets', 'chp5', 'uchill-2.2.jpg'),
                                           ],
                                           self.controls
                                           ).event_handler()
                # Chapter5(self.screen, self.GameSession.player)
            elif self.game_state == "chp" and self.currPlayer.level == 6:
                    self.game_state = Chapter6(self.screen,
                                           self.currPlayer,
                                           "Chapter 6",
                                           [
                                               "You agree to meet up at UCC to return the sheet music.",
                                               "She thanks you, and you guys decide to grab something to eat at the Spoke..",
                                               "What do you talk about in line?",
                                               "Oh! I have an idea. As thanks for helping me get my sheet music back, I can draw a picture of you!",
                                               "How do you respond?",
                                               "Let’s meet at my place tomorrow at 1pm!"
                                           ],
                                           [
                                               os.path.join('view', 'assets', 'chp2', 'spoke-1.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-2.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-3.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-3.1.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-3.2.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-4.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-5.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-5.1.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-5.2.jpg'),
                                               os.path.join('view', 'assets', 'chp2', 'spoke-6.jpg'),
                                           ],
                                           self.controls
                                           ).event_handler()
                # Chapter6(self.screen, self.GameSession.player)
            else:
                print(self.game_state)
                print(self.currPlayer.level)
                pygame.quit()
                sys.exit()

    # METHODS TO CONTROL THE MUSIC
    def _play_music(self, file_path: str) -> None:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(os.path.join('view', 'assets', 'music', file_path))
        pygame.mixer.music.play(-1)  

    """ Public Method to Start Music """
    def start_music(self, file_path: str) -> None:
        # Stop any existing music thread before starting a new one
        if self.music_thread is not None and self.music_thread.is_alive():
            pygame.mixer.music.stop()  # Stop the music if the thread is alive
            self.music_thread.join()  # Wait for the thread to finish before starting a new one

        # Create a new thread to play music in the background
        self.music_thread = threading.Thread(target=self._play_music, args=(file_path,))
        self.music_thread.start()

    """ Public Method to Stop Music """
    def stop_music(self) -> None:
        # Stop the music playback
        pygame.mixer.music.stop()

        # Stop the music thread if it's running
        if self.music_thread is not None and self.music_thread.is_alive():
            self.music_thread.join()  # Wait for the thread to finish

