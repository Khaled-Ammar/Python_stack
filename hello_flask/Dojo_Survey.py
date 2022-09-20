from flask import Flask, render_template,request,redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Dojo_Survey.html")


@app.route("/users",methods= ['POST', 'GET'])
def returnIndex():
    if request.method == 'POST':
        name = request.form['name']
        loc = request.form['Location']
        fav = request.form['fav_lang']
        com = request.form['comment']
        
        return render_template("index1.html",name1=name,loc1=loc,fav1=fav,com1=com)
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)


