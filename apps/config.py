import os
from dotenv import load_dotenv

class Config(object):
    """
    Variables that use os.getenv() function should be changed
    in .env file.
    """
    load_dotenv()
    OPENAI_KEY = os.getenv("OPENAI_KEY")
