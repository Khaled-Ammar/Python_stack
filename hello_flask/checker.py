# from flask import Flask, render_template
# app = Flask(__name__) 

# @app.route('/<value1>/<value2>/<color1>/<color2>')
# def checker1(value1, value2, color1, color2):
#     return render_template("checker.html", value1=int(value1), value2=int(value2), color1=color1, color2=color2)

# if __name__=="__main__":  
#     app.run(debug=True) 





from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/<value1>/<value2>/<color1>/<color2>')
def checker1(value1, value2, color1, color2):
    return render_template("checker.html", value1=int(value1), value2=int(value2), color1=color1, color2=color2)

if __name__=="__main__":  
    app.run(debug=True)  