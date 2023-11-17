# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="daniel1st$mwangi",
#     database="FadhiliProductsDB"  # Add the database name here
# )
#
# my_cursor = mydb.cursor()
#
# my_cursor.execute("CREATE DATABASE FadhiliProductsDB")
#
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)
# import mysql.connector
# #
# # Replace with your database credentials
# db_config = {
#     "host": "localhost",
#     "user": "root",
#     "password": "daniel1st$mwangi",
#     "database": "FadhiliDB",
# }
# #
# # Connect to the database
# connection = mysql.connector.connect(**db_config)
# #
# # Create a cursor
# cursor = connection.cursor()
# # #
# # # Execute an SQL query
# # query = "SELECT * FROM FadhiliDB"
# # cursor.execute(query)
# # #
# # # Fetch all rows
# # rows = cursor.fetchall()
# # #
# # # Display the data
# # for row in rows:
# #     print(row)
#
# # Close the cursor and connection
# # cursor.close()
# # connection.close()
# from sqlalchemy.orm import session
# import os
# from datetime import datetime
# from flask_admin import Admin
# from flask_wtf import FlaskForm
# from flask_migrate import Migrate
# from flask_wtf.csrf import CSRFProtect
# # from werkzeug.utils import secure_filename
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.exc import IntegrityError
# # from flask_uploads import UploadSet, IMAGES, configure_uploads
# # from flask_admin.contrib.sqla import ModelView
# from flask_wtf.file import FileField, FileAllowed, FileRequired
# from wtforms.validators import DataRequired, EqualTo, Length
# from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
# from wtforms import StringField, SelectField, SubmitField, IntegerField, PasswordField, BooleanField, \
#     ValidationError
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
#
# # from werkzeug.utils import secure_filename
# # from werkzeug.datastructures import FileStorage
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel1"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel1"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #
# # #     <div id="carousel2" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel2"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel2"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #     <div id="carousel3" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel3"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel3"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #
# # #
# # #     <div id="carousel4" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #             <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item" >
# # #             <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel4"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel4"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #     <div id="carousel5" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel5"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel5"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #
# # #     <div id="carousel6" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel6"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel6"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #     <div id="carousel7" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel7"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel7"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #
# # #
# # #     <div id="carousel8" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #             <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item" >
# # #             <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel8"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel8"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #     <div id="carousel9" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel9"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel9"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #
# # #     <div id="carousel10" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel10"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel10"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #     <div id="carousel11" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #                 <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100"
# # #                      alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel11"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel11"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #
# # #
# # #     <div id="carousel12" class="carousel slide" data-bs-ride="carousel">
# # #         <div class="carousel-inner">
# # #             <div class="carousel-item active">
# # #                 <img src="{{ url_for('static', filename='images/MOCKUP.jpg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h3>Overall Best Student</h3>
# # #                     <p>An esteemed Student ,excellent and comprehensive in his education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item">
# # #             <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #             <div class="carousel-item" >
# # #             <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}" class="d-block w-100" alt="Slide 1">
# # #                 <div class="carousel-caption d-none d-md-block">
# # #                     <h5>Fadhili Foundation</h5>
# # #                     <p>An esteemed organization providing excellent and comprehensive education.</p>
# # #                 </div>
# # #             </div>
# # #         </div>
# # #         <button class="carousel-control-prev" type="button" data-bs-target="#carousel12"
# # #                 data-bs-slide="prev">
# # #             <span class="carousel-control-prev-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Previous</span>
# # #         </button>
# # #         <button class="carousel-control-next" type="button" data-bs-target="#carousel12"
# # #                 data-bs-slide="next">
# # #             <span class="carousel-control-next-icon" aria-hidden="true"></span>
# # #             <span class="visually-hidden">Next</span>
# # #         </button>
# # #     </div>
# # #
# # #     </form>
# # # {% endblock %}
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# #
# #
# # # <!--{  % extends "base.html" %}-->
# # #
# # # <!--{% block content %}-->
# # # <!--<center><h1>Overall Best Students</h1></center>-->
# # # <!--<div class="container">-->
# # # <!--    <div class="row">-->
# # # <!--        <div class="col-6 mx-auto mt-5 text-center">-->
# # # <!--            <h2 class="mb-4">FLASK IMAGE</h2>-->
# # #
# # # <!--            <form method="post" enctype="multipart/form-data">-->
# # # <!--                {{ form.hidden_tag }}-->
# # # <!--                {% for error in form.photo.errors %}-->
# # # <!--                <span style="color: darkred;">{{ error }}</span>-->
# # # <!--                {% endfor %}-->
# # # <!--                <div class="justify-content-center">-->
# # # <!--                    <div class="col-auto">-->
# # # <!--                        {{ form.photo(class="form-control")}}-->
# # #
# # # <!--                    </div>-->
# # # <!--                    <div class="col-auto">-->
# # # <!--                        {{ form.submit(class="btn btn-success")}}-->
# # #
# # # <!--                    </div>-->
# # # <!--            </form>-->
# # # <!--            {% if file_url %}-->
# # # <!--             <div class="mt-5">-->
# # # <!--                 <img src="{{ file_url }}">-->
# # # <!--                 </div>-->
# # #
# # # <!--            {% endif %}-->
# # # <!--        </div>-->
# # # <!--        <div></div>-->
# # # <!--        {% endblock %}-->
# #
# # import random
# #
# #
# # def GET_PLAYER():
# #     player_choice = input("choice_either rock paper or scissors: ")
# #     return player_choice
# #
# #
# # def COMPUTER_CHOICE():
# #     comp_choice = ['rock','paper', 'scissors']
# #     return random.choice(comp_choice)
# #
# #
# # def GET_WINNER(player, computer):
# #     if player == computer:
# #         print("Its a Tie")
# #     elif player == 'rock' and computer == 'scissors' or player == "paper" and computer == "rock" or player == "scissors" == computer == "paper":
# #         print("YOU WIN BITCH")
# #     else:
# #         print("The Comp Fucked You Bitch")
# #
# #
# # def PLAY_GAME():
# #     while True:
# #         player = GET_PLAYER()
# #         computer = COMPUTER_CHOICE()
# #         print(f"You chose {player} ")
# #         print(f"Computer chose {computer} ")
# #         result =GET_WINNER(player, computer)
# #         print(result)
# # PLAY_GAME()
