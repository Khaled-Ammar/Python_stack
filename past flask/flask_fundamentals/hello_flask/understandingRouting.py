from flask import Flask
app = Flask(__name__)
@app.errorhandler(404)
def page_not_found(error):
    return "You are lost", 404
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say_hi(name):
    return f'Hi {name}'

@app.route('/repeat/<times>/<value>')
def greet(times, value):
        return value*int(times)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 