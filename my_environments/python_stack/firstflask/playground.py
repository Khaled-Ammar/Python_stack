from turtle import color
from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/play")
def index(num=3,col='blue'):
    return render_template('playground.html' , number=int(num) , color=col)

@app.route("/play/<num>")
def index1(num,col):
    return render_template('playground.html' , number=int(num) , color=col)

@app.route("/play/<num>/<col>")
def index2(num,col):
    return render_template('playground.html' , number=int(num) , color=col)

if (__name__) == ("__main__"):
    app.run(debug = True)