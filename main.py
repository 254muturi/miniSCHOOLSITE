from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from flask import request
from shop_products import *
from sqlalchemy.orm import session
from datetime import datetime
from flask_admin import Admin
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from flask_mysqldb import MySQL

from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_admin.contrib.sqla import ModelView
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, EqualTo, Length
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, jsonify, json
from wtforms import StringField, FileField, SelectField, SubmitField, DecimalField, IntegerField, PasswordField, \
    BooleanField, \
    ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage


app = Flask(__name__)

# MySQL Database  First MySQL Database
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:daniel1st$mwangi@localhost/comments"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:daniel1st$mwangi@localhost/FadhiliDB"
app.config['UPLOADED_PHOTOS_DEST'] = 'students'
app.secret_key = "NJOROGE MUTURI MW@NGI 1st@254"

# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin()
admin.init_app(app)

# Initialize MySQL
mysql = MySQL(app)

# FLASK LOGIN MANENOZ
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    try:
        return Student.query.get(int(user_id))
    except Exception as e:
        # Handle exceptions gracefully (e.g., log the error)
        return None


class ProductsForm(FlaskForm):
    title = StringField('Product Name', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    pages = StringField('Pages', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    image_url = FileField('Product Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Only images are allowed.')])
    submit = SubmitField("Submit")


class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    pages = db.Column(db.String(25), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)  # Specify a length for VARCHAR, e.g., 255
    description = db.Column(db.String(500))
    cart_items = db.relationship('CartItem', backref='product', lazy='dynamic')


# create a CartItems Model
class CartItem(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)
    user_id = Column(Integer, ForeignKey('shopuser.id'))  # Foreign key linking cart to ShopUser
    # Define a relationship with the Product model
    product_item = db.relationship('Product', backref='cart_item')
    user = relationship('ShopUser', back_populates='cart')

    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity


# create a Shop-User Model
class ShopUser(db.Model):
    __tablename__ = 'shopuser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(50))
    full_name = db.column(db.String(100))
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)

    cart = db.relationship('CartItem', backref='cart', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("Password is not a readable Attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class ShopUsersForm(FlaskForm):
    full_name = StringField('Full Names', validators=[DataRequired()])
    username = StringField('User Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_hash = StringField('Password', validators=[DataRequired()])
    submit = SubmitField("Submit")



class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    Class_Teacher = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(100), nullable=False)
    parent_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(200))
    amount_paid = db.Column(db.Integer)
    comment = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError("Password is not a readable Attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


# Define class names for different grades using a dictionary
GRADE_CLASSES = {
    "Grade 1": "Grade1Student",
    "Grade 2": "Grade2Student",
    "Grade 3": "Grade3Student",
    "Grade 4": "Grade4Student",
    "Grade 5": "Grade5Student",
    "Grade 6": "Grade6Student",
    "Grade 7": "Grade7Student",
    "Grade 8": "Grade8Student",
    "Grade PP1": "GradePP1Student",
    "Grade PP2": "GradePP2Student",
    # Add more grades here
}

# Create classes dynamically based on grade names
for grade_name, class_name in GRADE_CLASSES.items():
    globals()[class_name] = type(
        class_name,
        (Student,),
        {"__tablename__": class_name.lower() + "_students"}
    )


class SchoolDataBaseValidationForm(FlaskForm):
    Class_Teacher = StringField(' Class Teachers Name ', validators=[DataRequired()])
    username = StringField('User Name ', validators=[DataRequired()])
    name = StringField('Student Name ', validators=[DataRequired()])
    grade = SelectField(' Grade ', choices=[('Grade 1', 'Grade 1'), ('Grade 2', 'Grade 2'),
                                            ('Grade 3', 'Grade 3'), ('Grade 4', 'Grade 4'),
                                            ('Grade 5', 'Grade 5'), ('Grade 6', 'Grade 6'),
                                            ('Grade 7', 'Grade 7'), ('Grade 8', 'Grade 8'),
                                            ('Grade PP1', 'Grade PP1'), ('Grade PP2', 'Grade PP2')]
                        , validators=[DataRequired()])
    parent_name = StringField(' Parent Name ', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone_number = StringField("Parent Phone Number", validators=[DataRequired()])
    password_hash = PasswordField("Password",
                                  validators=[DataRequired(), EqualTo("password_hash2", message='Password must Match')])
    password_hash2 = PasswordField("Confirm Password", validators=[DataRequired(), ])
    amount_paid = IntegerField("Amount Paid", validators=[DataRequired(), ])
    comment = StringField(' comment ', validators=[DataRequired()])
    title = StringField('Product Name', validators=[DataRequired()])
    pages = StringField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    image = FileField('Product Image', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField("Submit")

    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/student/add', methods=['GET', 'POST'])
@login_required
def add_student():
    username = current_user.username.strip().lower()
    if username == "marto":
        name = ""
        form = SchoolDataBaseValidationForm()

        # Retrieve all students from the database
        our_users = Student.query.all()

        # Create a set to store unique Class_Teacher names
        unique_teacher_names = set()

        # Iterate through the students and add their Class_Teacher names to the set
        for user in our_users:
            unique_teacher_names.add(user.Class_Teacher)

        # Calculate the total amount paid by summing up the amount_paid attribute of each student
        total_amount_paid = sum(user.amount_paid for user in our_users)

        num_students = len(our_users)  # Calculate the total number of students
        num_teachers = len(unique_teacher_names)  # Calculate the total number of unique teachers

        # Rest of your view code...

        if form.validate_on_submit():
            try:
                # Check if a student with the same name already exists
                existing_student = Student.query.filter_by(name=form.name.data).first()
                if existing_student:
                    flash("A student with the same name already exists.")
                else:
                    hashed_pw = generate_password_hash(form.password_hash.data, method='scrypt')
                    grade = form.grade.data
                    if grade in GRADE_CLASSES:
                        StudentClass = GRADE_CLASSES[grade]
                        user_data = StudentClass(
                            Class_Teacher=form.Class_Teacher.data,
                            username=form.username.data,
                            name=form.name.data,
                            grade=form.grade.data,
                            parent_name=form.parent_name.data,
                            email=form.email.data,
                            phone_number=form.phone_number.data,
                            password_hash=hashed_pw,
                            amount_paid=0,
                            comment=form.comment.data,

                        )

                        # Save the data to the appropriate table
                        db.session.add(user_data)
                        db.session.commit()
                        form.Class_Teacher.data = ''
                        form.username.data = ''
                        form.name.data = ''
                        form.grade.data = ''
                        form.parent_name.data = ''
                        form.email.data = ''
                        form.phone_number.data = ''
                        form.password_hash.data = ''
                        form.amount_paid.data = ''

                        flash("Student Added Successfully")

            except IntegrityError as e:
                db.session.rollback()  # Rollback the transaction in case of error
                flash("An error occurred while adding the student. Please try again.")

        return render_template("add_student.html", form=form, name=name, our_users=our_users,
                               GRADE_CLASSES=GRADE_CLASSES,
                               num_students=num_students, total_amount_paid=total_amount_paid,
                               num_teachers=num_teachers)
    else:
        flash(" But Access Denied")
        return redirect(url_for('login'))


@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = Student.query.get_or_404(id)
    name = ""
    form = SchoolDataBaseValidationForm()
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("Student Deleted Successfully")
        our_users = Student.query.order_by(Student.date_added)
        return render_template("add_student.html", form=form, name=name, our_users=our_users)


    except:
        flash("Student Not Deleted Successfully")
        our_users = Student.query.order_by(Student.date_added)
        return render_template("add_student.html", form=form, name=name, our_users=our_users,
                               GRADE_CLASSES=GRADE_CLASSES)


#
@login_required
def update_student(id):
    form = SchoolDataBaseValidationForm()
    name_to_update = Student.query.get_or_404(id)

    if request.method == 'POST':
        # Make sure the keys match the names of your form fields in HTML
        name_to_update.Class_Teacher = request.form["Class_Teacher"]
        name_to_update.username = request.form["username"]  # Changed "UserName" to "username"
        name_to_update.name = request.form["name"]
        name_to_update.grade = request.form["grade"]
        name_to_update.parent_name = request.form["parent_name"]
        name_to_update.email = request.form["email"]
        name_to_update.phone_number = request.form["phone_number"]
        name_to_update.amount_paid = request.form["amount_paid"]

        try:
            db.session.commit()
            flash("Student Updated Successfully")
            return render_template("update.html",
                                   form=form,
                                   name_to_update=name_to_update)
        except:
            flash("Error Updating Student. Try Again.")
            return render_template("update.html",
                                   form=form,
                                   name_to_update=name_to_update)
    else:
        return render_template("update.html",
                               form=form,
                               name_to_update=name_to_update)


class SchoolValidationForm(FlaskForm):
    password_hash = PasswordField('Password ', validators=[DataRequired(),
                                                           EqualTo('Password_hash2', message='Passwords  Must Match')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    name = StringField('Student Name ', validators=[DataRequired()])
    parent_name = StringField('Parent Name ', validators=[DataRequired()])
    phone_number = StringField('Phone Number  ', validators=[DataRequired()])

    submit = SubmitField('Submit')


#
# class PasswordForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired()])
#     submit = SubmitField('Submit')
#

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = ''
    form = SchoolDataBaseValidationForm()
    if form.validate_on_submit():
        name = form.name.data
        parent_name = form.parent_name.data
        # parent_name = form.parent_name.data

        form.name.data = ''
        form.parent_name.data = ''
        form.phone_number = ''

        flash(" Admission Request Submitted Successfully Patiently Wait For Our Response")
    return render_template("name.html", name=name, form=form, parent_name=parent_name)


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')


# create  login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        student = Student.query.filter_by(username=form.username.data).first()
        if student:
            if check_password_hash(student.password_hash, form.password.data):
                login_user(student)
                flash('Login Successful')
                return redirect(url_for('add_student'))
            else:
                flash("Wrong Password Try Again")
        else:
            flash("User Doesn't Exist Try Again")

    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/students')
def students():
    return render_template('students.html')


@app.route('/parents_and_guardians')
def parents_and_guardians():
    return render_template('parents_and_guardians.html')


@app.route('/admissions')
def admissions():
    return render_template('admissions.html')


@app.route('/how_to_help')
def how_to_help():
    return render_template('how_to_help.html')


# Create an Admin Page
@app.route('/admin')
def admin():
    form = SchoolDataBaseValidationForm()

    return render_template('admin.html', form=form)




# @app.route('/add_user', methods=['GET', 'POST'])
# def add_user():
#     form = ShopUsersForm()
#
#     if form.validate_on_submit():
#         hashed_pw = generate_password_hash(form.password_hash.data, method='scrypt')
#
#         shopuser = ShopUser(
#             username=form.username.data,
#             email=form.email.data,
#             phone_number=form.phone_number.data,
#             password_hash=hashed_pw,
#             full_name=form.full_name.data
#         )
#
#         form.username.data = ''
#         form.email.data = ''
#         form.phone_number.data = ''
#         form.full_name.data = ''
#         # ADD PRODUCT TO DATABASE
#         db.session.add(shopuser)
#         db.session.commit()
#         flash("Welcome")
#
#         return redirect(url_for('shop_user'))  # Correct the redirect URL
#
#     our_products = ShopUser.query.order_by(ShopUser.id.asc()).all()
#     return render_template("add_user.html", form=form, our_products=our_products)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if current_user.is_authenticated:
        return redirect(url_for('shop'))
    form = ShopUsersForm()

    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password_hash.data, method='scrypt')

        shopuser = ShopUser(
            username=form.username.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            password_hash=hashed_pw,
            full_name=form.full_name.data
        )

        form.username.data = ''
        form.email.data = ''
        form.phone_number.data = ''
        form.full_name.data = ''
        # ADD PRODUCT TO DATABASE
        db.session.add(shopuser)
        db.session.commit()
        flash("Welcome!")

        return redirect(url_for('shop'))

    our_products = ShopUser.query.order_by(ShopUser.id.asc()).all()
    return render_template("add_user.html", form=form, our_products=our_products)

@app.route('/cart')
@login_required
def cart():
    user_id = current_user.id
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    products = []
    final_total = 0

    for item in cart_items:
        product = Product.query.get(item.product_id)
        product.quantity = item.quantity
        final_total += float(product.price) * item.quantity
        products.append(product)

    return render_template('cart.html', cart=products, final_total=final_total)


@app.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    try:
        product_id = request.get_json().get('id')
        user_id = current_user.id
        product = Product.query.get(product_id)

        if product:
            cart_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()

            if cart_item:
                # If the product is already in the cart, increase the quantity
                cart_item.quantity += 1
            else:
                # If the product is not in the cart, create a new cart item
                cart_item = CartItem(user_id=user_id, product_id=product_id, quantity=1)

            db.session.add(cart_item)
            db.session.commit()

            return jsonify({'success': True, 'message': 'Product added to the cart!'})
        else:
            return jsonify({'success': False, 'message': 'Product not found'})
    except Exception as e:
        return jsonify({"success": False, 'error': str(e)})

# app.route('/cart', methods=['GET'])
# def cart():
#     if current_user.is_authenticated:
#         user_id = current_user.id
#         cart_items = Product.query.filter_by(user_id=user_id).all()
#         products = []
#         final_total = 0
#
#         for item in cart_items:
#             product = Product.query.get(item.product_id)
#             product.quantity = item.quantity
#             final_total += product.price * product.quantity
#             products.append(product)
#             return render_template('cart.html', cart=products, final_total=final_total)
#
#         else:
#             # Handle for unauthenticated users and redirects them to a login page
#             flash("Please login in to access the Cart ", 'warning')
#             return redirect(url_for('add_ser.html'))

# @app.route('/add_to_cart', methods=['POST'])
# def add_to_cart():
#     try:
#         product_id = request.get_json().get('id')
#         user_id = current_user.id  # Assuming you're using Flask-Login
#
#         product = Product.query.get(product_id)
#
#         if product:
#             cart_item = Product.query.filter_by(user_id=user_id, product_id=product_id).first()
#
#             if cart_item:
#                 # If the product is already in the cart, increase the quantity
#                 cart_item.quantity += 1
#             else:
#                 # If the product is not in the cart, create a new cart item
#                 cart_item = CartItem(product=product, user_id=user_id)
#
#             db.session.add(cart_item)
#             db.session.commit()
#
#             return jsonify({'success': True, 'message': 'Product added to the cart!'})
#         else:
#             return jsonify({'success': False, 'message': 'Product not found'})
#     except Exception as e:
#         return jsonify({"success": False, 'error': str(e)})


@app.route('/checkout')
def checkout():
    # Add checkout logic here
    return render_template('checkout.html')


@app.route('/shop', defaults={'product_id': None})
def shop(product_id):
    if product_id is not None:
        # Display the product detail for the given 'product_id'
        product = Product.query.get(product_id)
        if product:
            return render_template('product_detail.html', product=product)
        else:
            # Handle the case where the product with the specified ID is not found.
            return render_template('500.html')
    else:
        # Display a list of products
        products = Product.query.all()
        return render_template('shop.html', products=products)


@app.route('/add_products', methods=['GET', 'POST'])
def add_products():
    form = ProductsForm()
    if form.validate_on_submit():
        product = Product(
            title=form.title.data,
            pages=form.pages.data,
            price=form.price.data,
            description=form.description.data,
            image_url=form.image_url.data  # Use the form field name

        )

        # CLEAR FORM
        form.title.data = ''
        form.pages.data = ''
        form.price.data = ''
        form.description.data = ''
        form.image_url.data = ''

        # ADD PRODUCT TO DATABASE
        db.session.add(product)
        db.session.commit()
        flash("Product added Successfully")

    our_products = Product.query.order_by(Product.title.asc()).all()
    return render_template("add_products.html", form=form, our_products=our_products)
    return redirect(url_for('add_products.html'))


# Your Flask route for product deletion
@app.route('/delete/<int:id>', methods=['POST'])
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully', 'success')
    else:
        flash('Product not found', 'error')
    return redirect(url_for('add_products'))  # Redirect to the products page


# Flask route for updat    ing a product
@app.route('/update_product/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    form = ProductsForm()  # Instantiate the form
    product = Product.query.get(id)

    if request.method == 'POST':
        # Handle the form submission to update the product
        new_title = request.form['new_title']
        new_price = request.form['new_price']
        new_pages = request.form['new_pages']
        new_description = request.form['new_description']
        image_url = request.form['image_url']  # Use request.form to access image_url
        # Update the product fields
        product.title = new_title
        product.price = new_price
        product.pages = new_pages
        product.description = new_description
        product.image = image_url

        db.session.commit()
        flash('Product updated successfully', 'success')
        return redirect(url_for('add_products'))

    return render_template('update_product.html', product=product, form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# Define a Product model with an image field

@app.route('/product/<int:product_id>')
def product_details(product_id):
    # Find the product by ID
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        # Handle product not found
        return "Product not found", 404

    return render_template('product_details.html', product=product)


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")


def create_db():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_db()
    app.run(debug=True, port=5002)
