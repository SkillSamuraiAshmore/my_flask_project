from flask import Flask,render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length
  
app = Flask(__name__)
# print(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SECRET_KEY'] = 'ba3f1b3757412c098d3215e2cb0d31716634c2dcfb1a1f57'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Task(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(100), nullable = False)
  description = db.Column(db.String(200), nullable = True)
  is_complete = db.Column(db.Boolean, default = False)
  
class TaskForm(FlaskForm):
  title = StringField('Title', validators=[InputRequired(), Length(min=1, max=200)])
  description = TextAreaField('Description', validators=[Length(min=0, max=200)])
  is_complete = BooleanField('Completed')
  submit = SubmitField('Submit')


@app.route('/task', methods=['GET','POST'])
def task():
  form = TaskForm()
  if form.validate_on_submit():
      new_task = Task(
        title = form.title.data,
        description = form.description.data,
        is_complete = form.is_complete.data
      )
      db.session.add(new_task)
      db.session.commit
  return redirect(url_for('hello_world'))
  return render_template('task.html', form = form)

@app.route('/task/list/')
def display_tasks():
  tasks = Task.query.all()
  return render_template('task_list.html',tasks=tasks)

@app.route('/task/update-status/<int:task_id>', methods = ["POST"])
def update_task_status(task_id):
  task=Task.query.get_or_404(task_id)
  task.is_complete = 'is_complete' in request.form
  db.session.commit()
  return redirect(url_for('display_task'))

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

