import logging
import os
from time import time

class Logger:
    def __init__(self, username, level=logging.CRITICAL):
        self.username = username
        self.level = level
        self.time = int(time())
        self.configure_logging()
        self.log_critical('*'*20 + 'Logged in' + '*'*20)

    def configure_logging(self):
        user_dir = f'users/{self.username}'
        os.makedirs(user_dir, exist_ok=True)
        user_log_dir = f'{user_dir}/logs'
        os.makedirs(user_log_dir, exist_ok=True)
        self.log_file = os.path.join(user_log_dir, f'log_{self.time}.log')

        # Basic configuration for logging
        logging.basicConfig(filename=self.log_file, 
                            level=self.level, 
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def log_error(self, message, exc_info=False):
        logging.error(message, exc_info=exc_info)

    def log_critical(self, message):
        logging.critical(message)
    
    def log_exit(self):
        logging.critical('*'*20 + 'Logged off' + '*'*20)
        logging.shutdown()