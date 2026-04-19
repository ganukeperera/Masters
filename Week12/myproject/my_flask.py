from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return ""
    return render_template("index.html")

@app.route("/bye")
def bye():
    return "<p>Bye, Flask!</p>"

@app.route("/username/<name>")
def learn(name):
    return f"<p style='font-size:30px;'>Welcome {name} !!!</p>" + 2345

@app.route("/<name>/<int:time>")
def welcome(name,time):
    return f"<p style='font-size:30px;'>{name} has been learning Flask since {time} a.m.</p>"

if __name__ == '__main__':
    app.run(debug=True)