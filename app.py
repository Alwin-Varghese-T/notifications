from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from test import RegisterForm
app = Flask(__name__)

# main page

@app.route('/')

@app.route('/pages-login.html')
def login():
    return render_template('pages-login.html')

@app.route('/index.html')
def home():

    items = {'name' : 'Scheme name1', 'link' : 'https://email.gov.in/' },{'name' : 'Scheme name2', 'link' : 'https://email.gov.in/' },{'name' : 'Scheme name3' ,'link' : 'https://email.gov.in/' },{'name' : 'Scheme name4', 'link' : 'https://email.gov.in/' },{'name' : 'Scheme name5' ,'link' : 'https://email.gov.in/' }


    return render_template('index.html', items=items)

@app.route('/users-profile.html')
def user():
    return render_template('users-profile.html')

@app.route('/pages-register.html')
def register():
    form = RegisterForm()
    return render_template('pages-register.html',form=form)

if __name__ == '__main__':
    app.run()

    