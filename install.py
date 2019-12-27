import os


def install():
    """
    Run when artpress starts for the first time.

    :return:
    """

    os.system("pip install -r requirements.txt")


if __name__ == '__main__':
    install()
