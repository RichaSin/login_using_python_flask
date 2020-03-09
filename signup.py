from collections import namedtuple

from flask import render_template

import inmemorydb as db
import configuration

returnData = namedtuple('returnData', 'message, backToUrl, caption')


def signup(request: object) -> object:
    """

    :rtype: object
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
        # return render_template("response.html", message=msg_str, backToURL=configuration.get_config("loginAddress"),
        #                        buttonCaption="Login")
