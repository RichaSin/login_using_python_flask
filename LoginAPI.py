from flask import Flask, render_template, request

protocol = "http"
serverIp = "127.0.0.1"
serverPort = "8123"
baseAddress = protocol + "://" + serverIp + ":" + serverPort + "/"
signupAddress = baseAddress + "signup"
loginAddress = baseAddress + "login"

userCollection = dict()
userCollection["admin"] = "admin"


app = Flask(__name__,static_url_path='/static')
@app.route('/', methods=["POST", "GET"])
def index():
  return render_template("login.html", signupURL=signupAddress,  loginURL=loginAddress)

@app.route('/login', methods=["POST", "GET"])
def login():
  if request.method == "POST":
    loginName = request.form['userName']
    loginPassword = request.form['password']
    print("request : {}".format(request))
    print("userName : {}".format(loginName))
    print("userPassword : {}".format(loginPassword))
    if (loginName in userCollection.keys()):
      if (loginPassword == userCollection.get(loginName)):
        msgStr = "Welcome {}, You have successfully login using flask server".format(loginName)
        return render_template("response.html", message=msgStr, backToURL = loginAddress,  buttonCaption = "Login")
      else:
        msgStr = "Hey {}, Please provide correct password".format(loginName)
        return render_template("response.html", message = msgStr, backToURL = loginAddress, buttonCaption = "Login")
    else:
      msgStr =  "Hey {}, Kindly signup first".format(loginName)
      return render_template("response.html", message=msgStr, backToURL = signupAddress,  buttonCaption = "Sign up")

  elif request.method == "GET":
    return render_template("login.html", signupURL=signupAddress, loginURL=loginAddress)


@app.route('/signup', methods=["POST", "GET"])
def signup():
  if request.method == "POST":
    userName = request.form['userName']
    userPassword = request.form['userPassword']

    if userName in  userCollection.keys():
      msgStr = "OhOo sorry, {}, is already taken, Please try something else".format(userName)
      return render_template("response.html", message=msgStr, backToURL=signupAddress,  buttonCaption = "Sign up")
    else:
      userCollection[userName] = userPassword
      return render_template("login.html", signupURL=signupAddress, loginURL=loginAddress)

  elif request.method == "GET":
    return render_template("register.html", signupURL=signupAddress, loginURL=loginAddress)


if __name__ == '__main__':
  #application will run on 8080 port
  app.run(host=serverIp, port=serverPort)