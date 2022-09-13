"""
app.py is the main entry file for running the Alien Invasion game.

The main function instantiates and runs the game (the Model, View,
and Controller classes) and is ran when file is executed.
"""

from controller import Controller
from model import Model
from view import View


def main():
    model = Model()
    view = View()
    controller = Controller(view, model)

    controller.run()


if __name__ == "__main__":
    main()
