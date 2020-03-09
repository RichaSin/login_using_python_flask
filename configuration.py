from typing import Dict, Any, Optional

# Defining a dictionay which can store key and value of any data-type
config: Dict[Any, Any] = dict()


def init_config(args) -> bool:
    global config
    for key, value in args.__dict__.items():
        config[key] = value
    else:
        return True


def set_config(key: str, value: str, overrite: bool) -> bool:
    global config
    if key in config.keys():
        if overrite is False:
            print(f"Overrite is set to False, and value of {key} is already configured")
            return False
        print(f"Previous value for {key} was {config[key]}, Now replacing with new value {value}")
    else:
        print(f"No value found for {key}, Inserting new value {value}")
    config[key] = value
    return True


# This function can return string or None
def get_config(key: str) -> Optional[str]:
    global config
    if key in config.keys():
        rtn_value: str = config[key]
        print(f"get_config is called, value for {key} is {rtn_value}")
        return rtn_value
    else:
        return None
