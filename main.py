import os, json

# Defining all important file locations.
MAIN_DIRECTORY_PATH = os.getcwd()
GAME_DATA_FILE_PATH = os.path.join(MAIN_DIRECTORY_PATH, "gamedata.json")

class Game:
    
    def __init__(self):
        """
        Initialisation of the class Game.
        """

        # current_tick is used as a clock. Increments by one when function tick is run.
        self.current_tick = 0  
        self.load_game_data()

    def load_game_data(self):
        """
        Loads the gamedata.json file into self.data

        Run duing initialisation of class Game.
            
        In case file doesn't exist, it throws an exception.
        """

        if os.path.isfile(GAME_DATA_FILE_PATH):
            with open(GAME_DATA_FILE_PATH, "r") as file_handle:
                self.data = json.load(file_handle)

        else:
            return Exception("File gamedata.json doesn't exist.")

    def save_game_data(self):
        """
        Saves self.data into the file gamedata.json.
        """

        with open(GAME_DATA_FILE_PATH, "w") as file_handle:
            json.dump(self.data, file_handle)

    def tick(self):
        """
        Run this function to progress the game by one step.
        """

        global isRunning
        isRunning = False

        self.current_tick += 1

    def close(self):
        """
        Run this function before exiting the program.
        """

        self.save_game_data()


isRunning = True
if __name__ == "__main__":
    game = Game()

    while isRunning:
        game.tick()

game.close()
