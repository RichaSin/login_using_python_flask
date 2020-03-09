from flask import Flask, render_template, request
import argparse

parser = argparse.ArgumentParser(description="Server to provide backend for login application.")
parser.add_argument("--ip", type=str, default="127.0.0.1", help="IP on which server will listen")
parser.add_argument("--port", type=str, default="5000", help="POST on which server will listen")
parser.add_argument("--protocol", type=str, default="HTTP", choices=["HTTP"],
                    help="Protocol on which server will listen")
#parser.add_argument("--logLevel", type=str, default="INFO", choices=["INFO", "DEBUG"], help="log level")

args = parser.parse_args()
print(args)
protocol = args.protocol
serverIp = args.ip
serverPort = args.port
baseAddress = protocol + "://" + serverIp + ":" + serverPort + "/"
signupAddress = baseAddress + "signup"
loginAddress = baseAddress + "login"

userCollection = dict()
userCollection['admin'] = 'admin'
app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("login.html", signupURL=signupAddress, loginURL=loginAddress)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login_name = request.form['userName']
        login_password = request.form['password']
        print("request : {}".format(request))
        print("userName : {}".format(login_name))
        print("userPassword : {}".format(login_password))
        if login_name in userCollection.keys():
            if login_password == userCollection.get(login_name):
                msg_str: str = "Welcome {}, You have successfully login using flask server".format(login_name)
                return render_template("response.html", message=msg_str, backToURL=loginAddress, buttonCaption="Login")
            else:
                msg_str: str = "Hey {}, Please provide correct password".format(login_name)
                return render_template("response.html", message=msg_str, backToURL=loginAddress, buttonCaption="Login")
        else:
            msg_str: str = "Hey {}, Kindly signup first".format(login_name)
            return render_template("response.html", message=msg_str, backToURL=signupAddress, buttonCaption="Sign up")

    elif request.method == "GET":
        return render_template("login.html", signupURL=signupAddress, loginURL=loginAddress)


@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        user_name = request.form['userName']
        user_password = request.form['password']

        if user_name in userCollection.keys():
            msg_str: str = "OhOo sorry, {}, is already taken, Please try something else".format(user_name)
            return render_template("response.html", message=msg_str, backToURL=signupAddress, buttonCaption="Sign up")
        else:
            userCollection[user_name] = user_password
            msg_str: str = "Thanks {}, for the registration, You can login now".format(user_name)
            return render_template("response.html", message=msg_str, backToURL=loginAddress, buttonCaption="Login")

    elif request.method == "GET":
        return render_template("register.html", signupURL=signupAddress, loginURL=loginAddress)


if __name__ == '__main_s_':
    # application will run on 8080 port
    app.run(host=serverIp, port=serverPort)
