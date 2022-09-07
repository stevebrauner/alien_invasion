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
