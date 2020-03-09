from collections import namedtuple
from flask import Flask, render_template, request
import argparse
import login as mylogin
import signup as mysignup
import configuration
import inmemorydb

parser = argparse.ArgumentParser(description="Server to provide backend for login application.")
parser.add_argument("--ip", type=str, default="127.0.0.1", help="IP on which server will listen")
parser.add_argument("--port", type=str, default="5000", help="POST on which server will listen")
parser.add_argument("--protocol", type=str, default="http", choices=["http"],
                    help="Protocol on which server will listen")
parser.add_argument("--logLevel", type=str, default="INFO", choices=["INFO", "DEBUG"], help="log level")

args = parser.parse_args()
if args.logLevel == "INFO":
    print(args)

configuration.init_config(args)
inmemorydb.initilize_db()
protocol = args.protocol
serverIp = args.ip
serverPort = args.port
baseAddress = protocol + "://" + serverIp + ":" + serverPort + "/"
signupAddress = baseAddress + "signup"
loginAddress = baseAddress + "login"
configuration.set_config("signupAddress", signupAddress, overrite=True)
configuration.set_config("loginAddress", loginAddress, overrite=True)
returnData = namedtuple('returnData', 'message, backToUrl, caption')
app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("login.html", signupURL=signupAddress, loginURL=loginAddress)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        rtn_data: returnData = mylogin.login(request)
        return render_template("response.html", message=rtn_data.message, backToURL=rtn_data.backToUrl,
                               buttonCaption=rtn_data.caption)
    elif request.method == "GET":
        return render_template("login.html", signupURL=signupAddress, loginURL=loginAddress)


@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        rtn_data: returnData = mysignup.signup(request)
        return render_template("response.html", message=rtn_data.message, backToURL=rtn_data.backToUrl,
                               buttonCaption=rtn_data.caption)
    elif request.method == "GET":
        return render_template("register.html", signupURL=signupAddress, loginURL=loginAddress)


# @app.errorhandler(404)
# def not_found():
#     """Page not found."""
#     return make_response(render_template("signup.html"), 404)
#
#
# @app.errorhandler(400)
# def bad_request():
#     """Bad request."""
#     return make_response(render_template("signup.html"), 400)
#
#
# @app.errorhandler(500)
# def server_error():
#     """Internal server error."""
#     return make_response(render_template("signup.html"), 500)

if __name__ == '__main__':
    app.run(host=serverIp, port=serverPort)
