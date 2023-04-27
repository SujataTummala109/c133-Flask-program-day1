from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")

def first_webpage():
    name = 'Pen'
    return render_template('index.html', var1 = name)

app.run(debug = True)