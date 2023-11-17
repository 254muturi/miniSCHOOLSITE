from main import *  # Import the ECommerceProduct model


@app.route('/ecommerce/add', methods=['GET', 'POST'])
@login_required
def add_product():
    # Check if the user has permission to add products
    username = current_user.username.strip().lower()
    if username == "marto":
        form = SchoolDataBaseValidationForm()

        if form.validate_on_submit():
            try:
                # Create a new ECommerceProduct instance and populate it with form data
                product = Product(
                    name=form.name.data,
                    description=form.description.data,
                    price=form.price.data,
                    image_url=form.image_url.data
                )

                # Save the product to the database
                db.session.add(product)
                db.session.commit()

                flash("Product Added Successfully")

            except IntegrityError as e:
                db.session.rollback()  # Rollback the transaction in case of error
                flash("An error occurred while adding the product. Please try again.")

        # Rest of your code for displaying products, validation, and rendering the template...
    else:
        flash("Access Denied")

    return render_template("add_product.html", form=form, name=name)
