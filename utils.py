import yaml 
import logging

def load_config(file_path:str = r"D:/loan approval/config/config.yaml"):
    with open(file_path, "r") as file :
        config = yaml.safe_load(file)

    return config


def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s'
                        )
    return logging.getLogger(__name__)