from typing import Dict, Any, Optional

userCollection: Dict[Any, Any] = dict()


def initilize_db():
    global userCollection
    userCollection['admin'] = 'admin'


def get_user(user_name: str) -> Optional[str]:
    global userCollection
    if user_name in userCollection.keys():
        return userCollection[user_name]
    else:
        return None


def is_user_exist(user_name: str) -> bool:
    global userCollection
    if user_name in userCollection.keys():
        print(f"User name matched")
        return True
    else:
        print(f"User does not exist")
        return False


def set_user(user_name: str, password: str) -> bool:
    global userCollection
    if user_name in userCollection.keys():
        print(f"User with name {user_name} already exist")
        return False
    else:
        print(f"Adding new user with username: {user_name} and password: {password}")
        userCollection[user_name] = password
        return True
