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


# Function to catch exceptions in other calls and return the error message.
def catch(fun, *args, **kwargs):
    # Try.
    try:
        # Run the function and return.
        return fun(*args, **kwargs)
    # Catch errors.
    except Exception as e:
        # Return the error message.
        return str(e)
