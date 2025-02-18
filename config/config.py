import os

def get_env(variable_name):
    """
    Fetch the value of an environment variable.
    
    :param variable_name: The name of the environment variable to fetch.
    :return: The value of the environment variable or None if not found.
    """
    return os.getenv(variable_name)
