import os


class Config(object):
    """
    Variables that use os.getenv() function should be changed
    in .env file.
    """

    OPENAI_KEY = os.getenv("OPENAI_KEY")
