from flask import Flask , render_template
app = Flask(__name__) # to create new web application __name__ represented this file
@app.route('/')  # flask designed alot of routes while route is part of the url type in order to determine in which page you request
def index(): # when the user go to the that url this is what i want to apper
    return 'hello world'
#add new route  127.0.0.1:5000/about
@app.route('/about')
def about():
    return 'About us'

# when we need to go to non specific url
@app.route('/<string:name>')
def hello(name):
    name = name.capitalize()
    return f'<h1>hello {name}</h1>'

# to render templates 1st we have to import render_template
@app.route('/temp')
def temp():
    return render_template('hello.html')




