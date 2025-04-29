#View
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from Controler import db, login_manager
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, request, flash, session
from Model import User, Tasks
from functions import *

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')

class TSform(FlaskForm):
    task_name = StringField('Task name', validators=[DataRequired()])
    task_assignee = PasswordField('Task assignee', validators=[DataRequired()])
    submit = SubmitField('Submit task')

### LOGIN LOGOUT STUFF ###

def init_routes(App):

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #returns user id to use in any place in the code


    @App.route('/login', methods=['GET', 'POST'], endpoint='login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()

        #get form data
        form_username = form.username.data
        form_password= form.password.data

        if form.validate_on_submit():
            user = User.query.filter_by(user_name = form_username).first()
            password = user.password
            if user is None or user.password != form_password:
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user)
            session.permanent = True
            return redirect(url_for('index'))
        return render_template('login.html', title='Sign In', form=form)
    
    @App.route('/TaskMaster', methods=['GET','POST'])
    @login_required
    def tasks():
        form = TSform()
        if request.method == 'POST':
            task_name = request.form.get('task_name')
            task_assignee = request.form.get('task_assignee')
            tasks = Tasks(task_name=task_name, task_assignee=task_assignee)
            db.session.add(tasks)
            db.session.commit()
            return redirect(url_for('tasks'))
        tasks = get_tasks()
        return render_template('TaskMaster.html', form=form, tasks=tasks, title='taskmaster')
    
    @App.route("/logout", endpoint='logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    @App.route("/")
    def index():
        return render_template('index.html')

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('login'))