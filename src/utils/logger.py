import logging
import os


class Logger:
    _instance = None

    def __new__(cls, log_dir="src//logs"):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, log_dir="src//logs") -> None:
        if self._initialized:
            return
        self._initialized = True
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)
        self._configure_logging()

    def _configure_logging(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        formatter_detailed = logging.Formatter(
            "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter_detailed)
        self.logger.addHandler(console_handler)

        info_file_handler = logging.FileHandler(
            os.path.join(self.log_dir, "info.log"), encoding="utf-8"
        )
        info_file_handler.setLevel(logging.INFO)
        info_file_handler.setFormatter(formatter_detailed)
        self.logger.addHandler(info_file_handler)

        error_file_handler = logging.FileHandler(
            os.path.join(self.log_dir, "error.log"), encoding="utf-8"
        )
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(formatter_detailed)
        self.logger.addHandler(error_file_handler)

        aiogram_logger = logging.getLogger("aiogram")
        aiogram_logger.setLevel(logging.INFO)
        aiogram_logger.addHandler(console_handler)

    def get_logger(self, name: str):
        return logging.getLogger(name)


logger = Logger()
logger_main = logger.get_logger("src.main")
logger_handler_user = logger.get_logger("src.handler.handler_user")
handler_user_fsm_feedback = logger.get_logger("src.handler.handler_user_fsm_feedback")
