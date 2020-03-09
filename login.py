from flask import render_template
import inmemorydb as db
import configuration
from collections import namedtuple
returnData = namedtuple('returnData', 'message, backToUrl, caption')

def login(request: object) -> render_template:
    login_name = request.form['userName']
    login_password = request.form['password']
    print("request : {}".format(request))
    print("userName : {}".format(login_name))
    print("userPassword : {}".format(login_password))
    if db.is_user_exist(login_name):
        if login_password == db.get_user(login_name):
            msg_str: str = "Welcome {}, You have successfully login using flask server".format(login_name)
            return returnData(message=msg_str, backToUrl=configuration.get_config("loginAddress"), caption="Login")
        else:
            msg_str: str = "Hey {}, Please provide correct password".format(login_name)
            return returnData(message=msg_str, backToUrl=configuration.get_config("loginAddress"), caption="Login")
    else:
        msg_str: str = "Hey {}, Kindly signup first".format(login_name)
        return returnData(message=msg_str, backToUrl=configuration.get_config("signupAddress"), caption="Sign up")
