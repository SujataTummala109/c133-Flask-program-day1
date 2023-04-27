#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

@app.route("/flask_2")

def second_flask():
    return "Python is fun!"
#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

# define a function with a different end point "/flask_2"





#run the application on local server
app.run(debug = True)

# pip install flask 
