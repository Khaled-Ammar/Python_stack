from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello Ma Nigga"

@app.route("/about")
def welcum():
    return "Welcome u bish"

@app.route("/hello/<name>")
def greet(name):
    return f"Welcome {name}"


if __name__=="__main__":    
    app.run(debug=True)