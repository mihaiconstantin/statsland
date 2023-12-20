# Load packages.
import os


# Get value of environmental variable.
def get_env_value(key):
    # Attempt to get the value.
    value = os.environ.get(key)

    # Throw if missing.
    if value is None:
        raise Exception(f"Missing environmental variable: '{key}'.")

    # Return the value.
    return value
