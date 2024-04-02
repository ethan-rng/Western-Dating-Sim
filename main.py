from controller.controller import RunGame

# You can start by describing what the script does in a docstring right below the module definition.
"""
This script is the entry point for a game. When run, it initializes the game by
calling the `RunGame` function from the `controller` package. This should be
executed within a properly set up Python virtual environment where all the necessary
dependencies have been installed.

TODO: Instructions for setting up a virtual environment and installing dependencies
might be added here or to an accompanying README file.

To run the game, simply execute this script in the command line with a Python interpreter.
"""

if __name__ == '__main__':
    # Setup and run the game.
    # The main check is used to ensure that this script is being run directly
    # and not being imported as a module in another script. If it is run directly,
    # the game initialization and start-up sequence is triggered.
    RunGame()
