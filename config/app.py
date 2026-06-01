import os


class AppConfig:
    FILE_PATH = os.path.abspath(__file__)
    ROOT_DIR = os.path.dirname(os.path.dirname(FILE_PATH))

    OUTPUT_DIR = os.path.join(ROOT_DIR, "data", "output")
    INPUT_DIR = os.path.join(ROOT_DIR, "data", "input")

    def ensure_directories(self):
        [
            os.makedirs(dir_path, exist_ok=True)
            for dir_path in [self.OUTPUT_DIR, self.INPUT_DIR]
        ]


def get_app_config() -> AppConfig:
    config = AppConfig()
    config.ensure_directories()
    return config
