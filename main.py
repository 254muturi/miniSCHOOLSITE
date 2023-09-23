from flask import request
from shop_products import *
from sqlalchemy.orm import session
import os
from datetime import datetime
from flask_admin import Admin
from flask_wtf import FlaskForm
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_admin.contrib.sqla import ModelView
# from flask_uploads import UploadSet, configure_uploads, IMAGES
# from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, EqualTo, Length
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
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


# create a Model
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
        return f"Student('{self.name}', '{self.email}')"


# Define class names for different grades
class Grade1Student(Student):
    pass


class Grade2Student(Student):
    pass


class Grade3Student(Student):
    pass


class Grade4Student(Student):
    pass


class Grade5Student(Student):
    pass


class Grade6Student(Student):
    pass


class Grade7Student(Student):
    pass


class Grade8Student(Student):
    pass


class GradePP1Student(Student):
    pass


class GradePP2Student(Student):
    pass


# dictionary to map grade names to class names
GRADE_CLASSES = {
    "Grade 1": Grade1Student,
    "Grade 2": Grade2Student,
    "Grade 3": Grade3Student,
    "Grade 4": Grade4Student,
    "Grade 5": Grade5Student,
    "Grade 6": Grade6Student,
    "Grade 7": Grade7Student,
    "Grade 8": Grade8Student,
    "Grade PP1": GradePP1Student,
    "Grade PP2": GradePP2Student,
    # Add more grades here
}

# Create instances dynamically based on grade names
for grade_name, grade_class in GRADE_CLASSES.items():
    globals()[grade_class.__name__] = type(
        grade_class.__name__,
        (Student,),
        {"__tablename__": grade_name.lower() + "_students"}
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


class ImageUploadForm(FlaskForm):
    # image = FileField('Upload Image', validators=[FileAllowed(photos, 'Only Images Are Allowed'), FileRequired()])
    # submit = SubmitField('Upload')

    # UPDATE DATABASE RECORD
    GRADE_CLASSES = {
        'Grade 1': Grade1Student,
        'Grade 2': Grade2Student,
        'Grade 3 ': Grade3Student,
        'Grade 4': Grade4Student,
        'Grade 5': Grade5Student,
        'Grade 6': Grade6Student,
        'Grade 7': Grade7Student,
        'Grade 8': Grade8Student,
        'PP1': GradePP1Student,
        'PP2': GradePP2Student,
        # Add other grades here
    }


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


@app.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
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
                               name_to_update=name_to_update, id=id)


class SchoolValidationForm(FlaskForm):
    password_hash = PasswordField('Password ', validators=[DataRequired(),
                                                           EqualTo('Password_hash2', message='Passwords  Must Match')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    name = StringField('Student Name ', validators=[DataRequired()])
    parent_name = StringField('Parent Name ', validators=[DataRequired()])
    phone_number = StringField('Phone Number  ', validators=[DataRequired()])

    submit = SubmitField('Submit')


class PasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')


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
    return render_template("name.html", name=name, form=form)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route('/add_comment', methods=['POST'])
def add_comment():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        content = request.form['content']

        comment = Comment(name=name, email=email, content=content)
        db.session.add(comment)
        db.session.commit()

    return redirect(url_for('contact_us'))


@app.route('/contact_us')
def contact_us():
    comments = Comment.query.all()
    return render_template('contact_us.html', comments=comments)


@app.route
def test_pw():
    email = None
    password = None
    pw_to_check = None
    form = PasswordForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password_hash.data

        # Clear
        form.email.data = ""
        form.password_hash.data = ""

        # Lookup Teacher By Email
        pw_to_check = Student.query.filter_by(form.email.data)

        passed = check_password_hash(pw_to_check)
    return render_template("test_pw", email=email, passed=passed,
                           password=password, pw_to_check=pw_to_check, form=form)


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



# Define a route to add items to the cart
@app.route('/cart', methods=['POST'])
def add_to_basket():
    product_name = request.form['product_name']
    product_price = request.form['product_price']

    # Add the item to the cart as a dictionary
    cart_item = {'name': product_name, 'price': product_price}
    cart.append(cart_item)

    return redirect(url_for('product_list'))


# Define a route to display the cart content
@app.route('/cart')
def cart():
    total_price = sum(float(item['price']) for item in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)


@app.route('/shop')
def shop():
    return render_template('shop.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


#

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

# <!DOCTYPE html>
# <html>
# <head>
#     <title>{{ product.name }} Details</title>
#     <!-- Include Bootstrap CSS -->
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
# </head>
# <body>
# <h1>{{ product.name }} Details</h1>
# <p>{{ product.description }}</p>
#
# <div id="selected-variant">
# </div>
#
# <!-- Cart Container -->
# <div id="cart-container">
#     <h2>Shopping Cart</h2>
#     <ul id="cart-items">
#         <!-- Cart items will be displayed here -->
#     </ul>
#     <p>Total Price: $<span id="total-price">0.00</span></p>
#     <button id="checkout-button" class="btn btn-primary">Checkout</button>
# </div>
# <br>
#
# <form action="/add_to_cart" method="post">
#     <div class="row" id="variant-cards">
#         {% for variant in product.variants %}
#         <div class="col-md-4">
#             <div class="card mb-4" id="variant-card-{{ variant.id }}">
#                 <img src="{{ variant.images[0] }}" class="card-img-top"
#                      alt="{{ variant.id }} - {{ variant.images[0] }}">
#                 <div class="card-body">
#                     <h5 class="card-title">Variant: {{ variant.id }}</h5>
#                     <p class="card-text">Size: {{ variant.size }}</p>
#                     <p class="card-text">Color: {{ variant.color }}</p>
#                     <p class="card-text">Price: ${{ variant.price }}</p>
#                     <div class="form-group">
#                         <label for="quantity-{{ variant.id }}">Quantity:</label>
#                         <input type="number" class="form-control" id="quantity-{{ variant.id }}" name="quantity"
#                                value="1" min="1">
#                     </div>
#                 </div>
#                 <div class="card-footer">
#                     <a href="#" class="btn btn-primary btn-block">Buy Now</a>
#                     <button type="button" class="btn btn-primary btn-block add-to-cart"
#                             data-variant-id="{{ variant.id }}">Add to Cart
#                     </button>
#                 </div>
#             </div>
#         </div>
#         {% endfor %}
#     </div>
# </form>
#
# <script>
#
#     // JavaScript to update selected variant information and images
#     const variantInputs = document.querySelectorAll('.add-to-cart');
#     const selectedVariantDiv = document.getElementById('selected-variant');
#     const variantCardsDiv = document.getElementById('variant-cards');
#     const product = JSON.parse('{{ product | tojson | safe }}');
#
#     variantInputs.forEach(input => {
#         input.addEventListener('click', (event) => {
#             const variantId = event.currentTarget.getAttribute('data-variant-id');
#             const quantityInput = document.getElementById(`quantity-${variantId}`);
#             const quantity = parseInt(quantityInput.value);
#
#             const selectedVariant = product.variants.find(variant => variant.id === variantId);
#
#             if (selectedVariant) {
#                 const price = selectedVariant.price;
#
#                 // Check if the variant is already in the cart
#                 const existingItem = cart.find(item => item.variantId === variantId);
#
#                 if (existingItem) {
#                     // If it exists, update the quantity and price
#                     existingItem.quantity += quantity;
#                 } else {
#                     // If it doesn't exist, add a new item to the cart
#                     cart.push({ variantId, quantity, price });
#                 }
#
#                 // Clear the quantity input
#                 quantityInput.value = '1';
#
#                 // Update the cart display
#                 updateCart();
#             }
#         });
#     });
#
#     // Cart data (an array to store selected items)
#     const cart = [];
#
#     // Function to update the cart display
#     function updateCart() {
#         // Clear the cart display
#         cartItemsList.innerHTML = '';
#
#         let totalPrice = 0;
#
#         // Loop through the cart items and add them to the display
#         cart.forEach(item => {
#             const cartItem = document.createElement('li');
#             cartItem.textContent = `Variant: ${item.variantId}, Quantity: ${item.quantity}, Price: $${(item.price * item.quantity).toFixed(2)}`;
#             cartItemsList.appendChild(cartItem);
#
#             // Calculate and update the total price
#             totalPrice += item.price * item.quantity;
#         });
#
#         // Update the total price display
#         totalPriceElement.textContent = totalPrice.toFixed(2);
#     }
#
#     // Add a click event listener to the "Checkout" button
#     const checkoutButton = document.getElementById('checkout-button');
#     checkoutButton.addEventListener('click', () => {
#         // You can implement the checkout logic here
#         alert('Checkout functionality is not implemented in this example.');
#     });
#
#     // Cart items list and total price element
#     const cartItemsList = document.getElementById('cart-items');
#     const totalPriceElement = document.getElementById('total-price');
# </script>
#
# <!-- Include Bootstrap JS (optional) -->
# <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
# </body>
# </html>
