import logging
import os
import pandas as pd

class Logger:
    def __init__(self, username, level=logging.CRITICAL):
        self.username = username
        self.level = level
        self.configure_logging()
        self.log_critical('*'*20 + 'Logged in' + '*'*20)
        self.configure_prompt_df()

    def configure_logging(self):
        self.user_dir = f'users/{self.username}'
        os.makedirs(self.user_dir, exist_ok=True)
        user_log_dir = f'{self.ser_dir}/logs'
        os.makedirs(user_log_dir, exist_ok=True)
        self.log_index = len(os.listdir(user_log_dir))
        self.log_file = os.path.join(user_log_dir, f'log_{self.log_index}.log')

        # Basic configuration for logging
        logging.basicConfig(filename=self.log_file, 
                            level=self.level, 
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def configure_prompt_df(self):
        self.prompt_df_dir = f'{self.user_dir}/prompt_history'
        os.makedirs(self.prompt_df_dir, exist_ok=True)
        prompt_df = pd.DataFrame(columns=['role', 'content'])
        self.prompt_df_path = f'{self.prompt_df_dir}/prompt_{self.log_index}.parquet'
        prompt_df.to_parquet(self.prompt_df_path)

    def log_error(self, message, exc_info=False):
        logging.error(message, exc_info=exc_info)

    def log_critical(self, message):
        logging.critical(message)
    
    def log_exit(self):
        logging.critical('*'*20 + 'Logged off' + '*'*20)
        logging.shutdown()