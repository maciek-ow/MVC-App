#View
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired
from python_files.Controler import db, login_manager
from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, request, flash, session
from python_files.Model import *
from python_files.functions import *
from datetime import date

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')

class TMform(FlaskForm):
    task_name = StringField('Task name', validators=[DataRequired()])
    task_due_date = DateField('Due Date', format='%Y-%m-%d', default=date.today)
    submit = SubmitField('Submit task')
    status = SelectField('Status', choices=[
        (TaskStatus.TODO.value, 'To Do'),
        (TaskStatus.IN_PROGRESS.value, 'In Progress'),
        (TaskStatus.DONE.value, 'Done')
    ], default=TaskStatus.TODO.value)
    submit = SubmitField('Submit Task')
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
        form = TMform()
        if form.validate_on_submit():
            task = Tasks(
            task_name=form.task_name.data,
            task_assignee=current_user.user_name,
            task_due_date=form.task_due_date.data,
            user_id=current_user.id,
            status=form.status.data
            )
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('tasks'))
        tasks = get_tasks()
        return render_template('TaskMaster.html',form=form, tasks=tasks, title='taskmaster')
     
    @App.route('/update_status/<int:task_id>', methods=['POST'])
    @login_required
    def update_status(task_id):
        task = Tasks.query.get_or_404(task_id)
        # Toggle status between 'Pending' and 'Completed'
        task.status = 'Completed' if task.status == 'Pending' else 'Pending'
        db.session.commit()
        return redirect(url_for('tasks'))
     
    @App.route('/delete_task/<int:task_id>', methods=['POST'])
    @login_required
    def delete_task(task_id):
        task = Tasks.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('tasks'))

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