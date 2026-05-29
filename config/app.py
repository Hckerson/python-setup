import os

class AppConfig:
    FILE_PATH = os.path.abspath(__file__)
    ROOT_DIR = os.path.dirname(os.path.dirname(FILE_PATH))

    OUTPUT_DIR = os.path.join(ROOT_DIR, "data", "output")
    INPUT_DIR = os.path.join(ROOT_DIR, "data", "INPUT")
    print(ROOT_DIR)
    pass


def get_app_config() -> AppConfig:
    return AppConfig()