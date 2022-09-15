from flask import Flask, render_template 
app = Flask(__name__)
# 1
@app.route("/")
def index():
    return "Hello World!"
# 2
@app.route("/dojo")
def dojo():
    return "Dojo!"
# 3
@app.route("/say/<name>")
def greet(name):
        return f" Hi  {name}!"
# 4
@app.route("/repeat/<ints>/<called>")
def page(ints,called):
    return f"{called}"*int(ints)
    
if (__name__) == ("__main__"):
    app.run(debug = True)