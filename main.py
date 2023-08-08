import os
from datetime import datetime
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField
from flask import Flask, render_template, flash, request

app = Flask(__name__)
app.secret_key = "NJOROGE MUTURI MW@NGI 1st@254"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# SQLite DATABASE
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Mastude.db')


# MySQL Database
# NEW MySQL DB
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:daniel1st$mwangi@localhost/FadhiliDB"

db = SQLAlchemy(app)
migrate = Migrate(app,db)

# create a Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Name {self.student_name}>'

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
    name = StringField(' Name ', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone_number = StringField("Phone Number",validators=[DataRequired()])
    submit = SubmitField('Submit')

# UPDATE DATABASE RECORD
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = SchoolDataBaseValidationForm()  # Corrected the colon ':' here
    name_to_update = Student.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.name = request.form["name"]
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
                               name_to_update=name_to_update)


class SchoolValidationForm(FlaskForm):
    name = StringField('Full Name ', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = SchoolDataBaseValidationForm()
    if form.validate_on_submit():
        user = Student.query.filter_by(email=form.email.data).first()

        if user is None:
            user = Student(name=form.name.data,
                           email=form.email.data, phone_number = form.phone_number.data)
            db.session.add(user)
            db.session.commit()

        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        form.phone_number.data = ''
        flash("Student Added Successfully")
    our_users = Student.query.order_by(Student.date_added)
    return render_template("add_user.html", form=form, name=name, our_users=our_users)


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
        flash(" Submitted Successfully")
    return render_template("name.html", name=name, form=form)


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
