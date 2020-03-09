from collections import namedtuple

import configuration
import inmemorydb as db

returnData = namedtuple('returnData', 'message, backToUrl, caption')


def signup(request) -> returnData:
    """
    :rtype: returnData
    """
    user_name = request.form['userName']
    user_password = request.form['password']

    if db.is_user_exist(user_name):
        msg_str: str = "OhOo sorry, {}, is already taken, Please try something else".format(user_name)
        return returnData(message=msg_str, backToUrl=configuration.get_config("signupAddress"), caption="Sign up")
    else:
        db.set_user(user_name, user_password)
        msg_str: str = "Thanks {}, for the registration, You can login now".format(user_name)
        return returnData(message=msg_str, backToUrl=configuration.get_config("loginAddress"), caption="Login")
