import os
from datetime import datetime
from flask_admin import Admin
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired, EqualTo, Length
from flask_admin.contrib.sqla import ModelView
from flask import Flask, render_template, flash, request
from wtforms import StringField, SubmitField, FileField, PasswordField
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

app = Flask(__name__)

# MySQL Database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:daniel1st$mwangi@localhost/FadhiliDB"
app.secret_key = "NJOROGE MUTURI MW@NGI 1st@254"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin()

admin.init_app(app)


# create a Model
class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Class_Teacher = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(100), nullable=False)
    parent_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name


admin.add_view(ModelView(Student, db.session))


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = SchoolDataBaseValidationForm()
    if form.validate_on_submit():
        user_data = Student.query.filter_by(email=form.email.data).first()

        if user_data is None:
            # PASSWORD HASHING
            user_data = Student(Class_Teacher=form.Class_Teacher.data,
                                name=form.name.data, grade=form.grade.data,
                                parent_name=form.parent_name.data,
                                email=form.email.data, phone_number=form.phone_number.data)
            db.session.add(user_data)
            db.session.commit()

        name = form.name.data
        form.Class_Teacher.data = ''
        form.name.data = ''
        form.grade.data = ''
        form.parent_name.data = ''
        form.email.data = ''
        form.phone_number.data = ''

        flash("Student Added Successfully")
    our_users = Student.query.order_by(Student.date_added)
    return render_template("add_user.html", form=form, name=name, our_users=our_users)



@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = Student.query.get_or_404(id)
    name = None
    form = SchoolDataBaseValidationForm()
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("Student Deleted Successfully")
        our_users = Student.query.order_by(Student.date_added)
        return render_template("add_user.html", form=form, name=name, our_users=our_users)


    except:
        flash("Student Not Deleted Successfully")
        our_users = Student.query.order_by(Student.date_added)
        return render_template("add_user.html", form=form, name=name, our_users=our_users)


class SchoolDataBaseValidationForm(FlaskForm):
    Class_Teacher = StringField(' Class Teacher ', validators=[DataRequired()])
    password_hash = PasswordField('Password',
                                  validators=[DataRequired(), EqualTo('Password_hash2', message='Password Must Match')])
    password_hash2 = PasswordField('Confirm  Password', validators=[DataRequired()])
    name = StringField(' Name ', validators=[DataRequired()])
    grade = StringField(' Class ', validators=[DataRequired()])
    parent_name = StringField(' Parent Name ', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    submit = SubmitField('Submit')

    # UPDATE DATABASE RECORD


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = SchoolDataBaseValidationForm()  # Corrected the colon ':' here
    name_to_update = Student.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.name = request.form["name"]
        name_to_update.grade = request.form["grade"]
        name_to_update.parent_name = request.form["parent_name"]
        name_to_update.email = request.form["email"]
        name_to_update.phone_number = request.form["phone_number"]

        try:
            db.session.commit()
            flash("Student Updated Successfully")
            return render_template("update.html",
                                   form=form,
                                   name_to_update=name_to_update)
        except:
            flash("Error Updating Student Try Again")
            return render_template("update.html",
                                   form=form,
                                   name_to_update=name_to_update)
    else:
        return render_template("update.html",
                               form=form,
                               name_to_update=name_to_update, id=id)


class SchoolValidationForm(FlaskForm):
    password_hash = PasswordField('Password ', validators=[DataRequired(),
                                                           EqualTo('Password_hash2', message='Passwords  Must Match')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    name = StringField('Student Name ', validators=[DataRequired()])
    parent_name = StringField('Parent Name ', validators=[DataRequired()])
    phone_number = StringField('Phone Number  ', validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = SchoolValidationForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash(" Admission Request Submitted Successfully Patiently Wait For Our Response")
    return render_template("name.html", name=name, form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/students')
def students():
    return render_template('students.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


@app.route('/parents_and_guardians')
def parents_and_guardians():
    return render_template('parents_and_guardians.html')


@app.route('/admissions')
def admissions():
    return render_template('admissions.html')


@app.route('/how_to_help')
def how_to_help():
    return render_template('how_to_help.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")


def create_db():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_db()
    app.run(debug=True, port=5002)
