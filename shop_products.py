from main import *
from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory

from wtforms import StringField, FileField, SelectField, SubmitField, DecimalField, IntegerField, PasswordField
# class Product(db.Model):
#     __tablename__ = 'product'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     pages = db.Column(db.String, nullable=False)
#     price = db.Column(db.String(20), nullable=False)
#     description = db.Column(db.String(500))
#
#
# class ProductsForm(FlaskForm):
#     title = StringField('Product Name', validators=[DataRequired()])
#     pages = StringField('Quantity', validators=[DataRequired()])
#     description = StringField('Description', validators=[DataRequired()])
#     price = DecimalField('Price', validators=[DataRequired()])
#     submit = SubmitField("Submit")


# Initialize an empty cart when your Flask app starts
cart = []
#
#
# @app.route('/add_products', methods=['GET', 'POST'])
# def add_products():
#     form = ProductsForm()
#     if form.validate_on_submit():
#         product = Product(
#             title=form.title.data,
#             pages=form.pages.data,
#             price=form.price.data,
#             description=form.description.data,
#         )
#
#         # CLEAR FORM
#         form.title.data = ''
#         form.pages.data = ''
#         form.price.data = ''
#         form.description.data = ''
#
#         # ADD PRODUCT TO DATABASE
#         db.session.add(product)
#         db.session.commit()
#         flash("Product added Successfully")
#
#     our_products = Product.query.order_by(Product.title.asc()).all()
#     return render_template("add_products.html", form=form, our_products=our_products)
#     return redirect(url_for('add_products.html'))


## Sample product data with variants
# products = [
#     {
#         'id': 1,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Blue',
#                 'price': 200,
#                 'images': [
#                     '/static/images/img_4.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Blue',
#                 'price': 250,
#                 'images': [
#                     '/static/images/img_4.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 300,
#                 'images': [
#                     '/static/images/img_4.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 2,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': '',
#                 'price': 450,
#                 'images': [
#                     '/static/images/img_3.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': '',
#                 'price': 500,
#                 'images': [
#                     '/static/images/img_3.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': '',
#                 'price': 550,
#                 'images': [
#                     '/static/images/img_3.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 3,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Red',
#                 'price': 380,
#                 'images': [
#                     '/static/images/img_2.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Red',
#                 'price': 460,
#                 'images': [
#                     '/static/images/img_2.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 570,
#                 'images': [
#                     '/static/images/img_2.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 4,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Blue',
#                 'price': 350,
#                 'images': [
#                     '/static/images/img_5.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Blue',
#                 'price': 380,
#                 'images': [
#                     '/static/images/img_5.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 450,
#                 'images': [
#                     '/static/images/img_5.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 5,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Red',
#                 'price': 430,
#                 'images': [
#                     '/static/images/img_6.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Red',
#                 'price': 499,
#                 'images': [
#                     '/static/images/img_6.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 550,
#                 'images': [
#                     '/static/images/img_6.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 6,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Blue',
#                 'price': 200,
#                 'images': [
#                     '/static/images/img.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Blue',
#                 'price': 250,
#                 'images': [
#                     '/static/images/img.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Purple For Girls',
#                 'price': 300,
#                 'images': [
#                     '/static/images/img_22.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 7,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': '',
#                 'price': 450,
#                 'images': [
#                     '/static/images/img_23.png',
#
#
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': '',
#                 'price': 500,
#                 'images': [
#                     '/static/images/img_3.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': '',
#                 'price': 550,
#                 'images': [
#                     '/static/images/img_3.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 3,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Red',
#                 'price': 380,
#                 'images': [
#                     '/static/images/img_2.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Red',
#                 'price': 460,
#                 'images': [
#                     '/static/images/img_2.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 570,
#                 'images': [
#                     '/static/images/img_2.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 4,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Blue',
#                 'price': 350,
#                 'images': [
#                     '/static/images/img_5.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Blue',
#                 'price': 380,
#                 'images': [
#                     '/static/images/img_5.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 450,
#                 'images': [
#                     '/static/images/img_5.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 5,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Red',
#                 'price': 430,
#                 'images': [
#                     '/static/images/img_6.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Red',
#                 'price': 499,
#                 'images': [
#                     '/static/images/img_6.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 550,
#                 'images': [
#                     '/static/images/img_6.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 6,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Blue',
#                 'price': 200,
#                 'images': [
#                     '/static/images/img_4.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Blue',
#                 'price': 250,
#                 'images': [
#                     '/static/images/img_22.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 300,
#                 'images': [
#                     '/static/images/img_4.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 2,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': '',
#                 'price': 450,
#                 'images': [
#                     '/static/images/img_3.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': '',
#                 'price': 500,
#                 'images': [
#                     '/static/images/img_3.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': '',
#                 'price': 550,
#                 'images': [
#                     '/static/images/img_3.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 3,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Red',
#                 'price': 380,
#                 'images': [
#                     '/static/images/img_2.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Red',
#                 'price': 460,
#                 'images': [
#                     '/static/images/img_2.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 570,
#                 'images': [
#                     '/static/images/img_2.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 4,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Blue',
#                 'price': 350,
#                 'images': [
#                     '/static/images/img_5.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Blue',
#                 'price': 380,
#                 'images': [
#                     '/static/images/img_5.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 450,
#                 'images': [
#                     '/static/images/img_5.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     {
#         'id': 5,
#         'name': 'Product Name',
#         'description': 'Product Description',
#         'variants': [
#             {
#                 'id': 'variant-1',
#                 'size': 'Small',
#                 'color': 'Red',
#                 'price': 430,
#                 'images': [
#                     '/static/images/img_6.png',
#
#                 ]
#             },
#             {
#                 'id': 'variant-2',
#                 'size': 'Medium',
#                 'color': 'Red',
#                 'price': 499,
#                 'images': [
#                     '/static/images/img_6.png',
#
#                 ]
#             },
#
#             {
#                 'id': 'variant-3',
#                 'size': 'Large',
#                 'color': 'Blue',
#                 'price': 550,
#                 'images': [
#                     '/static/images/img_6.png',
#                 ]
#             },
#             # Add more variants with images as needed
#         ]
#     },
#     # Add more products as needed
# ]
#
