from flask import *
app= Flask(__name__)
app.secret_key='mysecretkey'

@app.route('/')
def homepage():
    return(render_template("homepage.html"))

@app.route('/signup')
def signup():
    return(render_template("signup.html"))

@app.route('/signin')
def signin():
    return(render_template("signin.html"))

@app.errorhandler(404)
def pgntfnd(y):
    return(render_template("error404.html"))

if (__name__ == '__main__'):
    app.run(debug=True)