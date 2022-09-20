from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/table')
def table():
    myTable = [
        {'First Name': "Khaled", 'Last Name': "Ammar"},
        {'First Name': "Zaki", 'Last Name': "Nahhas"},
        {'First Name': "Yousef", 'Last Name': "Assi"}
    ]
    return render_template("table.html", tableinfo=myTable, table=myTable[0])

if __name__=="__main__":  
    app.run(debug=True)