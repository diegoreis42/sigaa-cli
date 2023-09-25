from dotenv import load_dotenv
from pathlib import Path
import os


def getEnvVirable(virable):
    
    dotenv_path = Path('../.env')
    load_dotenv(dotenv_path=dotenv_path)

    return os.getenv(virable)
