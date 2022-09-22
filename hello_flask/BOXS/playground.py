
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def boxes():
     return render_template("boxes1.html")


@app.route('/play/<x>/<color>')
def boxez(x, color):
     return render_template("boxes1.html", times=int(x), color=color)



@app.route('/play/<x>')
def boxez_color(x):
     return render_template("boxes1.html", times=int(x))

if __name__=="__main__":
     app.run(debug=True) 