import sys, os
import copy
from pkg_resources import resource_string
import yaml


# Merge two dictionaries
def merge_dicts(default, user):
    default = copy.deepcopy(default)
    user = copy.deepcopy(user)
    if isinstance(user, dict) and isinstance(default, dict):
        for k, v in default.items():
            if k not in user:
                user[k] = v
            else:
                user[k] = merge_dicts(user[k], v)
    return user


# Load config data
def load_config():
    """
    Loads config values from the default config.yml file installed with the package,
    and overrides those values with values found in a config.yml file in ~/.config/python-skeleton
    """
    # ----------------------------------------------------------------------------------------------
    # Load default config
    #
    try:
        default_config = yaml.load(resource_string('python_skeleton', 'config.yml'))
    except Exception:
        print('Couldn\'t load default configuration data. Something went wrong with the '
              'installation.')
        sys.exit(1)
    # ----------------------------------------------------------------------------------------------
    # Load an optional config file with user-defined values that will override default values
    #
    # Try to read the config.yml file in ~/.config/python-skeleton
    config_dir = os.path.expanduser('~/.config/python-skeleton')
    try:
        with open('{}/config.yml'.format(config_dir)) as f:
            user_config = yaml.load(f)
    except FileNotFoundError:
        user_config = default_config
    except Exception:
        print('There was a problem reading ~/.config/python-skeleton/config.yml')
        sys.exit(1)
    # If the user config file is empty, set the config data equal to the default data
    if not user_config:
        user_config = default_config
    # Override default values with the user-defined values
    try:
        config = merge_dicts(default_config, user_config)
    except UnboundLocalError:
        config = default_config
    # Return the config dict
    return config


def main(argv=None):

    print("This is the main function.")


if __name__ == "__main__":
    main(sys.argv[1:])
