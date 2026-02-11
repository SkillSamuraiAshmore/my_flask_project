from flask import Flask,render_template
# from flask_SQLAlchemy import SQLAchemy
app = Flask(__name__)
print(app)
# app.config('SQLAchemy_DATABASE_URI') = 'sqlite:///yourdatabase.db'
# app.config('SECRET_KEY') = 'ba3f1b3757412c098d3215e2cb0d31716634c2dcfb1a1f57'
# db = SQLAlchemy(app)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/user/<name>')
def user(name):
  personal = f'<h1>Hello, {name}!</h1>'
  instruc = '<p>Change the name in the <em> browser adress bar</em> and reload the page.</p>'
  return personal + instruc

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

@app.route('/users')
def users():
  user_names = ['Alice', 'Bob', 'Charlie']
  return render_template('users.html', names=user_names)

