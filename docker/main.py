from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    user = os.environ['ATC_USERNAME']
    passwd = os.environ['ATC_PASSWORD']
    return "Username is "+ user+" . Password is "+passwd+""

if __name__ == "__main__":
    app.run(host='0.0.0.0')
