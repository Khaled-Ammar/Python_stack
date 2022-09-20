from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'

@app.route("/")
def count():
    if 'count' in session:
        session['count']=session.get('count')+1
    else:
        session['count']=1
    return render_template( "counter.html")

@app.route('/remove')
def remove():
    session.pop('count',None)
    return render_template("counter.html")
    
@app.route('/increase')
def increase():
    session['count']=session.get('count')+1
    return redirect('/')

@app.route('/reset')
def reset():
        session['count']=0
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)