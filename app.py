from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/users-profile.html')
def user():
    return render_template('users-profile.html')
@app.route('/pages-login.html')
def login():
    return render_template('pages-login.html')
@app.route('/pages-register.html')
def register():
    return render_template('pages-register.html')

if __name__ == '__main__':
    app.run()