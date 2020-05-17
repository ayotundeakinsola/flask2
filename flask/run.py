# provides a way of using operating system dependent functionality
import os

import json

#import Flask class
from flask import Flask, render_template

#Name of the application module
app = Flask(__name__)

#this is a decorator and it is used to wrap functions
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route('/careers')
def careers():
    return render_template("careers.html", page_title="Careers")


#This is an internal environment variable that cloud9 has set and we're using the os module from the standard library to get that environment variable for us. 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)