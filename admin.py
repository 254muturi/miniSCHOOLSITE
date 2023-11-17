# {% extends "base.html" %}
#
# {% block content %}
#
# <html>
# <head>
#     <meta name="viewport" content="width=device-width, initial-scale=1">
#     <!-- Font Awesome -->
#     <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
#     <!-- Bootstrap core CSS -->
#     <link href="../css/bootstrap.min.css" rel="stylesheet">
#     <!-- Material Design Bootstrap -->
#     <link href="../css/mdb.min.css" rel="stylesheet">
#     <!-- Jarallax CSS (if not already included in your project) -->
#     <link href="path/to/jarallax.css" rel="stylesheet">
#     <!-- Your custom CSS styles -->
#     <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
#     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>
#
#     <style>
#         /* Global styles */
#         h5 {
#             color: #f0f0f0;
#         }
#
#         body {
#             margin: 0;
#             padding: 0;
#             font-family: 'Poppins', sans-serif;
#             background: #131313;
#         }
#
#         /* Global styles */
#         body {
#             margin: 0;
#             padding: 0;
#             font-family: 'Poppins', sans-serif;
#             background: #131313;
#         }
#
#         /* Hero section styles */
#         .hero {
#             background-image: url('/static/images/img_8.png');
#             background-size: cover;
#             background-position: center center;
#             text-align: center;
#             padding: 10% 0; /* Adjust as needed */
#             color: #fff;
#         }
#
#         .hero h1 {
#             font-size: 4vw; /* Responsive font size */
#         }
#
#         .hero p {
#             font-size: 1.5vw; /* Responsive font size */
#         }
#
#         .hero .btn {
#             display: inline-block;
#             padding: 10px 20px;
#             font-size: 1.2rem; /* Responsive font size */
#             background-color: #007BFF;
#             color: #fff;
#             text-decoration: none;
#             border-radius: 5px;
#         }
#
#         /* Media query for smaller screens */
#         @media (max-width: 768px) {
#             .hero {
#                 background-size: cover; /* Keep background-size to cover for small screens */
#                 padding: 20% 0; /* Increase padding for better readability */
#             }
#
#             .hero h1 {
#                 font-size: 6vw; /* Adjust font size for smaller screens */
#             }
#
#             .hero p {
#                 font-size: 3vw; /* Adjust font size for smaller screens */
#             }
#
#             .hero .btn {
#                 font-size: 1rem; /* Adjust font size for smaller screens */
#             }
#         }
#
#         /* Card section styles */
#         .card-container {
#             display: flex;
#             flex-wrap: wrap;
#             justify-content: space-around;
#             max-width: 1200px; /* Adjust as needed */
#             margin: 20px; /* Added margin for better spacing */
#         }
#
#         .card {
#             position: relative;
#             width: 320px;
#             max-width: 100%; /* Make the cards responsive */
#             height: 450px;
#             background: #131313;
#             border-radius: 20px;
#             overflow: hidden;
#             margin: 10px; /* Added margin for better spacing */
#             color: #fff;
#         }
#
#         .card:before {
#             content: '';
#             position: absolute;
#             top: 0;
#             left: 0;
#             width: 100%;
#             height: 100%;
#             background: #9bdc28;
#             clip-path: circle(150px at 80% 20%);
#             transition: 0.5s ease-in-out;
#         }
#
#         .card:hover:before {
#             clip-path: circle(300px at 80% -20%);
#         }
#
#         .card:after {
#             content: 'Fadhili School Shop';
#             position: absolute;
#             top: 60%;
#             left: -5%;
#             font-size: 3em;
#             font-weight: 800;
#             font-style: italic;
#             color: rgba(255, 255, 25, 0.05);
#         }
#
#         .card .imgBx {
#             position: absolute;
#             top: 50%;
#             transform: translateY(-50%);
#             z-index: 1; /* Lower z-index value */
#             width: 100%;
#             height: 220px;
#             transition: 0.5s;
#         }
#
#
#         .card:hover .imgBx {
#             top: 0%;
#             transform: translateY(0%);
#         }
#
#         .card .imgBx img {
#             position: absolute;
#             top: 50%;
#             left: 50%;
#             transform: translate(-50%, -50%) rotate(-25deg);
#             width: 270px;
#         }
#
#         .card .contentBx {
#             position: absolute;
#             bottom: -65px;
#             width: 100%;
#             height: 100px;
#             text-align: center;
#             transition: 1s;
#             z-index: 2; /* Higher z-index value */
#         }
#
#
#         .card:hover .contentBx {
#             height: 210px;
#         }
#
#         .card .contentBx h2 {
#             position: relative;
#             font-weight: 600;
#             letter-spacing: 1px;
#             margin: 0;
#         }
#
#         .card .contentBx .size,
#         .card .contentBx .color {
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             padding: 8px 20px;
#             transition: 0.5s;
#             opacity: 0;
#             visibility: hidden;
#             padding-top: 0;
#             padding-bottom: 0;
#         }
#
#         .card:hover .contentBx .size {
#             opacity: 1;
#             visibility: visible;
#             transition-delay: 0.5s;
#         }
#
#         .card:hover .contentBx .color {
#             opacity: 1;
#             visibility: visible;
#             transition-delay: 0.6s;
#         }
#
#         .card .contentBx .size h3,
#         .card .contentBx .color h3, h6 {
#             font-weight: 300;
#             font-size: 14px;
#             text-transform: uppercase;
#             letter-spacing: 2px;
#             margin-right: 10px;
#         }
#
#         .card .contentBx .size span {
#             width: 26px;
#             height: 26px;
#             text-align: center;
#             line-height: 26px;
#             font-size: 14px;
#             display: inline-block;
#             color: #007bff;
#             background: #fff;
#             margin: 0 5px;
#             transition: 0.5s;
#             color: #111;
#             border-radius: 4px;
#             cursor: pointer;
#         }
#
#         .card .contentBx .size span:hover {
#             background: #9bdc28;
#         }
#
#         .card .contentBx .color span {
#             width: 20px;
#             height: 20px;
#             background: #ff0;
#             border-radius: 50%;
#             margin: 0 5px;
#             cursor: pointer;
#         }
#
#         /*.card .contentBx .color span:nth-child(2) {*/
#         /*    background: #9bdc28;*/
#         /*}*/
#
#         /*.card .contentBx .color span:nth-child(3) {*/
#         /*    background: #03a9f4;*/
#         /*}*/
#
#         /*.card .contentBx .color span:nth-child(4) {*/
#         /*    background: #e91e63;*/
#         /*}*/
#
#         .card .contentBx a {
#             display: inline-block;
#             padding: 10px 20px;
#             background: #fff;
#             border-radius: 4px;
#             margin-top: 10px;
#             text-decoration: none;
#             font-weight: 600;
#             color: #000;
#             opacity: 0;
#             transform: translateY(50px);
#             transition: 0.5s;
#             margin-top: 0;
#         }
#
#         .card:hover .contentBx a {
#             opacity: 1;
#             transform: translateY(0px);
#             transition-delay: 0.75s;
#         }
#
#         #modal {
#             position: fixed;
#             top: 0;
#             left: 0;
#             width: 100%;
#             height: 100%;
#             background-color: rgba(0, 0, 0, 0.5);
#             z-index: 10;
#             display: none;
#         }
#
#
#     </style>
# </head>
# <body>
# <!-- Hero Section -->
# <div class="hero">
#     <div class="container">
#         <h1 class="display-3 mb-2 wow fadeInDown" data-wow-delay="0.3s">STATIONARY and UNIFORM
#             <a class="indigo-text font-weight-bold">COLLECTION</a>
#         </h1>
#         <h5 class="text-uppercase mb-5 mt-1 font-weight-bold wow fadeInDown" data-wow-delay="0.3s">
#             Free delivery & special prices
#         </h5>
#         <a href="#" class="btn wow fadeInDown" data-wow-delay="0.3s">Shop Now</a>
#     </div>
# </div>
# <style>
#     .cart-container {
#         display: flex;
#         justify-content: center; /* Center horizontally */
#         align-items: center; /* Center vertically */
#
#         align-items: center; /* Vertically center items */
#     }
#
#     #cart-icon {
#         margin-right: 10px; /* Add some space between the cart icon and search box */
#     }
#
#     .search-box {
#         display: flex;
#         align-items: center;
#         justify-content: center; /* Center horizontally */
#         align-items: center; /* Center vertically */
#
#     }
#
#     .search-input {
#         border: 1px solid #ccc;
#         padding: 5px;
#     }
#
#     .search-button {
#         background-color: #007bff;
#         color: #fff;
#         border: none;
#         padding: 5px 10px;
#         cursor: pointer;
#
#     }
# </style>
#
# <div class="mt-3 cart-container">
#     <a href="/cart" id="cart">
#         <svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" fill="currentColor"
#              class="bi bi-cart4 cart-icon" viewBox="0 0 21 21">
#             <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l.5 2H5V5H3.14zM6 5v2h2V5H6zm3 0v2h2V5H9zm3 0v2h1.36l.5-2H12zm1.11 3H12v2h.61l.5-2zM11 8H9v2h2V8zM8 8H6v2h2V8zM5 8H3.89l.5 2H5V8zm0 5a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"/>
#         </svg>
#     </a>
# </div>
#
#
# <div class=" mt-3 search-box">
#     <input type="text" class="search-input" placeholder="Search products...">
#     <button class="search-button">Search</button>
# </div>
# </div>
# <!-- Jarallax JavaScript (if not already included in your project) -->
# <script src="path/to/jarallax.min.js"></script>
#
# <div class="intro-info-content text-center">
#     <div class="text-center">
#
#         <h5 class="text-uppercase mt-5 mb-5 mt-1 font-weight-bold wow fadeInDown" data-wow-delay="0.3s">
#             SCHOOL UNIFORMS</h5>
#     </div>
# </div>
#
# <div class="custom-container">
#     <div class="card-container">
#         <!-- Define a list of cards with their properties -->
#
#         {% set set_cards = [
#
#         {
#         'title': 'Exercise Book 1',
#         'pages': ['200'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png')
#         },
#         {
#         'title': 'Exercise Book 2',
#         'pages': ['120'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/KARTASI01EXC1009-40402.jpg')
#         },
#         {
#         'title': 'Exercise Book 3',
#         'pages': ['96'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png')
#         },
#         {
#         'title': 'Exercise Book 4',
#         'pages': ['200'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png')
#         },
#         {
#         'title': 'Exercise Book 5',
#         'pages': ['120'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/KARTASI01EXC1009-40402.jpg')
#         },
#         {
#         'title': 'Exercise Book 6',
#         'pages': ['96'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png')
#         },
#         {
#         'title': 'Exercise Book 7',
#         'pages': ['64'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png') },
#         {
#         'title': 'Exercise Book 8',
#         'pages': ['48'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png') },
#         {
#         'title': 'Exercise Book 9',
#         'pages': [32],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png') },
#
#         {
#         'title': 'Boys Shorts ',
#         'pages': ['200'],
#         'price': 'Ksh 123.00',
#         'image_url': url_for('static', filename='images/img_4.png')
#         },
#         {
#         'title': 'Girls Scout Dress',
#         'pages': ['120'],
#         'price': 'Ksh 123.00',
#         'image_url': url_for('static', filename='images/img_3.png')
#         },
#         {
#         'title': 'Boys Trouser',
#         'pages': ['96'],
#         'price': 'Ksh 123.00',
#         'image_url': url_for('static', filename='images/img_2.png')
#         },
#         {
#         'title': 'Girls Dress',
#         'pages': ['64'],
#         'price': 'Ksh 123.00',
#         'image_url': url_for('static', filename='images/img_5.png')
#         },
#         {
#         'title': ' Sweeter',
#         'pages': ['48'],
#         'price': 'Ksh 123.00',
#         'image_url': url_for('static', filename='images/img_6.png')
#         },
#         {
#         'title': 'Exercise Book 6',
#         'pages': [32],
#         'price': 'Ksh 123.00',
#
#         'image_url': url_for('static', filename='images/img.png')
#         }
#         ] %}
#
#
#         <div class="row mb-4">
#             {% for card in set_cards %}
#             <div class="col-md-4">
#                 <div class="card">
#                     <div class="contentBx">
#                         <h2>{{ card.title }}</h2>
#
#                         <div class="price">
#                             <h6>Price: {{ card.price }}</h6></div>
#                         <a href="#">Buy Now</a>
#                         <button type="button" class="btn btn-success mt-1 add-to-basket"
#                                 data-product-name="{{ card.title }}" data-product-price="{{ card.price }}"
#                                 data-toggle="modal" data-target="#productModal"
#                                 onclick="addToCart('{{ card.title }}', '{{ card.price }}')">
#                             Add to Basket
#                         </button>
#
#                     </div>
#
#                     <div class="imgBx">
#                         <img src="{{ product.image }}" alt="{{ product.title }} Image">
#                     </div>
#                 </div>
#             </div>
#             {% if loop.index % 3 == 0 %}
#         </div>
#         <div class="row mb-4">
#             {% endif %}
#             {% endfor %}
#         </div>
#         <!-- End of loop -->
#     </div>
# </div>
#
#
# <div class="intro-info-content text-center">
#     <div class="text-center">
#         <h1 class="display-3 mb-2 wow fadeInDown" data-wow-delay="0.3s">Stationary
#             <a class="indigo-text font-weight-bold">COLLECTION</a>
#         </h1>
#         <h5 class="text-uppercase mb-5 mt-1 font-weight-bold wow fadeInDown" data-wow-delay="0.3s">
#             Free delivery & special prices</h5>
#     </div>
# </div>
#
#
# <div class="custom-container">
#     <div class="card-container">
#         <!-- Define a list of cards with their properties -->
#
#         {% set set_cards = [
#         {
#         'title': 'Oxford Set',
#         'pages': ['200'],
#         'price': 'Ksh 10000.00',
#         'image_url': url_for('static', filename='images/KARTASI01EXC1009-40402.jpg')
#         },
#         {
#         'title': 'Mathematical Set',
#         'pages': ['120'],
#         'price': 'Ksh 10000.00',
#         'image_url': url_for('static', filename='images/KARTASI01EXC1009-40402.jpg')
#         },
#         {
#         'title': 'HB Pencil',
#         'pages': ['96'],
#         'price': 'Ksh 10000.00',
#         'image_url': url_for('static', filename='images/Exercise Book1.Crayons.img_1.png')
#         },
#         {
#         'title': 'Exercise Book 4',
#         'pages': ['64'],
#         'price': 'Ksh 10000.00',
#         'image_url': 'URL_TO_IMAGE_4'
#         },
#         {
#         'title': 'Exercise Book 5',
#         'pages': ['48'],
#         'price': 'Ksh 10000.00',
#         'image_url': 'URL_TO_IMAGE_5'
#         },
#         {
#         'title': 'Exercise Book 6',
#         'pages': [32],
#         'price': 'Ksh 10000.00',
#
#         'image_url': 'URL_TO_IMAGE_6'
#         }
#         ] %}
#
#
#         <div class="row mb-4">
#             {% for card in set_cards %}
#             <div class="col-md-4">
#                 <div class="card">
#                     <div class="contentBx">
#                         <h2>{{ card.title }}</h2>
#                         <div class="size">
#                             <h3>Pages :</h3>
#                             {% for pages in card.pages %}
#                             <span>{{ pages }}</span>
#                             {% endfor %}
#                         </div>
#                         <div class="price">
#                             <h6>Price: {{ card.price }}</h6></div>
#                         <a href="#">Buy Now</a>
#                          <button type="button" class="btn btn-success mt-1 add-to-basket"
#                                 data-product-name="{{ card.title }}" data-product-price="{{ card.price }}"
#                                 data-toggle="modal" data-target="#productModal"
#                                 onclick="addToCart('{{ card.title }}', '{{ card.price }}')">
#                             Add to Basket
#                         </button>
#
#                     </div>
#                     <div class="imgBx">
#                         <img src="{{ product.image }}" alt="{{ product.title }} Image">
#                     </div>
#                 </div>
#             </div>
#             {% if loop.index % 3 == 0 %}
#         </div>
#         <div class="row mb-4">
#             {% endif %}
#             {% endfor %}
#         </div>
#         <!-- End of loop -->
#     </div>
# </div>
#
#
# <div class="intro-info-content text-center">
#     <div class="text-center">
#         <h1 class="display-3 mb-2 wow fadeInDown" data-wow-delay="0.3s">Exercise Books
#             <a class="indigo-text font-weight-bold">COLLECTION</a>
#         </h1>
#         <h5 class="text-uppercase mb-5 mt-1 font-weight-bold wow fadeInDown" data-wow-delay="0.3s">
#             Free delivery & special prices</h5>
#     </div>
# </div>
#
#
# <div class="custom-container">
#     <div class="card-container">
#         <!-- Define a list of cards with their properties -->
#
#         {% set set_cards = [
#         {
#         'title': 'Exercise Book',
#         'pages': ['200'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png')
#         },
#         {
#         'title': 'Exercise Book',
#         'pages': ['120'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/KARTASI01EXC1009-40402.jpg')
#         },
#         {
#         'title': 'Exercise Book',
#         'pages': ['96'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png')
#         },
#         {
#         'title': 'Exercise Book',
#         'pages': ['200'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png')
#         },
#         {
#         'title': 'Exercise Book',
#         'pages': ['120'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/KARTASI01EXC1009-40402.jpg')
#         },
#         {
#         'title': 'Exercise Book',
#         'pages': ['96'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png')
#         },
#         {
#         'title': 'Exercise Book',
#         'pages': ['64'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png') },
#         {
#         'title': 'Exercise Book',
#         'pages': ['48'],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png') },
#         {
#         'title': 'Exercise Book',
#         'pages': [32],
#         'price': 'Ksh 250.00',
#         'image_url': url_for('static', filename='images/Exercise Book4.img_1.png') }
#         ] %}
#
#
#         <div class="row mb-4">
#             {% for card in set_cards %}
#             <div class="col-md-4">
#                 <div class="card">
#                     <div class="contentBx">
#                         <h2>{{ card.title }}</h2>
#
#                         <div class="price">
#                             <h6>Price: {{ card.price }}</h6></div>
#                         <a href="#">Buy Now</a>
#                         <!-- Modify the "Add to Basket" button to call addToCart function -->
#                         <button type="button" class="btn btn-success mt-1 add-to-basket"
#                                 data-product-name="{{ card.title }}" data-product-price="{{ card.price }}"
#                                 data-toggle="modal" data-target="#productModal"
#                                 onclick="addToCart('{{ card.title }}', '{{ card.price }}')">
#                             Add to Basket
#                         </button>
#
#                     </div>
#                     <div class="imgBx">
#                         <img src="{{ product.image }}" alt="{{ product.title }} Image">
#
#                     </div>
#                 </div>
#             </div>
#             {% if loop.index % 3 == 0 %}
#         </div>
#         <div class="row mb-4">
#             {% endif %}
#             {% endfor %}
#         </div>
#         <!-- End of loop -->
#     </div>
# </div>
# <div class="modal fade" id="productModal" tabindex="-1" aria-labelledby="productModalLabel"
#      aria-hidden="true">
#     <div class="modal-dialog modal-dialog-centered modal-lg">
#         <div class="modal-content">
#             <div class="modal-header">
#                 <h5 class="modal-title" id="productModalLabel">Product Added to Cart</h5>
#                 <button type="button" class="close" data-dismiss="modal" aria-label="Close">
#                     <span aria-hidden="true">&times;</span>
#                 </button>
#             </div>
#             <div class="modal-body">
#                 <div class="text-center">
#                     <img id="productImageModal" src="" alt="Product Image">
#                 </div>
#                 <p class="mt-3">Item added to your cart:</p>
#                 <p id="productName"></p>
#                 <p id="productPrice"></p>
#             </div>
#             <div class="modal-footer">
#                 <button type="button" class="btn btn-secondary" data-dismiss="modal">Continue Shopping
#                 </button>
#                 <a href="/cart.html" class="btn btn-primary">Proceed to Cart</a>
#             </div>
#         </div>
#     </div>
# </div>
# <!-- JavaScript -->
# <script>
#     function addToCart(name, price) {
#         const existingItem = cart.items.find(item => item.name === name);
#
#         if (existingItem) {
#             // If the item already exists in the cart, increase its quantity
#             existingItem.quantity++;
#         } else {
#             // If it's a new item, add it to the cart with quantity 1
#             const newItem = {name, price, quantity: 1};
#             cart.items.push(newItem);
#         }
#
#         // Update the total price
#         cart.total += parseFloat(price);
#
#         // Update the cart display
#         displayCart();
#         showProductModal(name, price);
#     }
#
#     // Initialize cart data structure
#     const cart = {
#         items: [], // Array to store items
#         total: 0,  // Total price of items in the cart
#     };
#
#     // Get all "Add to Cart" buttons
#     const addToCartButtons = document.querySelectorAll(".add-to-basket");
#
#     // Get the cart element
#     const cartElement = document.getElementById("cart");
#
#     // Get the product modal element
#     const productModal = document.getElementById("productModal");
#
#     // Get the cart icon element
#     const cartIcon = document.getElementById("cart-icon");
#
#     // Function to add an item to the cart
#     function addToCart(name, price) {
#         const existingItem = cart.items.find(item => item.name === name);
#
#         if (existingItem) {
#             // If the item already exists in the cart, increase its quantity
#             existingItem.quantity++;
#         } else {
#             // If it's a new item, add it to the cart with quantity 1
#             const newItem = {name, price, quantity: 1};
#             cart.items.push(newItem);
#         }
#
#         // Update the total price
#         cart.total += parseFloat(price);
#
#         // Update the cart display
#         displayCart();
#         showProductModal(name, price);
#     }
#
#     // Function to display the cart
#     function displayCart() {
#         const cartElement = document.getElementById("cart");
#         cartElement.innerHTML = "";
#
#         cart.items.forEach(item => {
#             const listItem = document.createElement("li");
#             listItem.textContent = `${item.name} (Quantity: ${item.quantity}) - Subtotal: $${(item.price * item.quantity).toFixed(2)}`;
#             cartElement.appendChild(listItem);
#         });
#
#         // Display the total price
#         const totalElement = document.createElement("li");
#         totalElement.textContent = `Total: $${cart.total.toFixed(2)}`;
#         cartElement.appendChild(totalElement);
#     }
#
#     // Function to show the product modal
#     function showProductModal(name, price) {
#         const productName = document.getElementById("productName");
#         const productPrice = document.getElementById("productPrice");
#
#         // Set the modal content
#         productName.textContent = name;
#         productPrice.textContent = `${price}`;
#
#         // Show the modal
#         productModal.classList.add("show");
#         productModal.style.display = "block";
#     }
#
#     // Add event listeners to "Add to Basket" buttons
#     addToCartButtons.forEach(button => {
#         button.addEventListener("click", () => {
#             const name = button.getAttribute("data-product-name");
#             const price = button.getAttribute("data-product-price");
#             addToCart(name, price);
#         });
#     });
#
#     // Add event listener to cart icon to display cart items
#     cartIcon.addEventListener("click", () => {
#         displayCart();
#     });
# </script>
#
# </body>
# </html>
#
# </body>
#
# {% endblock %}
#
# {% extends "base.html" %}
#
# {% block content %}
# <head>
#     <title>Your Website</title>
#     <!-- Add Bootstrap CSS and MDB CSS links here -->
#     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.2/css/mdb.min.css">
#     <meta charset="utf-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#     <meta http-equiv="x-ua-compatible" content="ie=edge">
#     <title>Material Design Bootstrap Template</title>
#
#     <style>
#
#         html,
#         body,
#         header,
#         .jarallax {
#             height: 700px;
#         }
#
#         @media (max-width: 740px) {
#             html,
#             body,
#             header,
#             .jarallax {
#                 height: 100vh;
#             }
#         }
#
#         @media (min-width: 800px) and (max-width: 850px) {
#             html,
#             body,
#             header,
#             .jarallax {
#                 height: 100vh;
#             }
#         }
#
#         @media (min-width: 560px) and (max-width: 650px) {
#             header .jarallax h1 {
#                 margin-bottom: .5rem !important;
#             }
#
#             header .jarallax h5 {
#                 margin-bottom: .5rem !important;
#             }
#         }
#
#         @media (min-width: 660px) and (max-width: 700px) {
#             header .jarallax h1 {
#                 margin-bottom: 1.5rem !important;
#             }
#
#             header .jarallax h5 {
#                 margin-bottom: 1.5rem !important;
#             }
#         }
#
#
#
#         footer.page-footer {
#             background-color: #383838;
#         }
#
#         @media (max-width: 450px) {
#             .display-3 {
#                 font-size: 3rem;
#             }
#         }
#
#     </style>
#
#
#     <!-- Font Awesome -->
#     <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
#     <!-- Bootstrap core CSS -->
#     <link href="../css/bootstrap.min.css" rel="stylesheet">
#     <!-- Material Design Bootstrap -->
#     <link href="../css/mdb.min.css" rel="stylesheet">
#     <!-- Intro Section -->
#     <div class="view jarallax" data-jarallax='{"speed": 0.2}'
#          style="background-image: url(https://mdbootstrap.com/img/Photos/Others/model-3.jpg); background-repeat: no-repeat; background-size: cover; background-position: center center;">
#         <div class="mask rgba-white-light">
#             <div class="container h-100 d-flex justify-content-center align-items-center">
#                 <div class="row pt-5 mt-3">
#                     <div class="col-md-12 mb-3">
#                         <div class="intro-info-content text-center">
#                             <h1 class="display-3 mb-5 wow fadeInDown" data-wow-delay="0.3s">NEW
#                                 <a class="indigo-text font-weight-bold">COLLECTION</a>
#                             </h1>
#                             <h5 class="text-uppercase mb-5 mt-1 font-weight-bold wow fadeInDown" data-wow-delay="0.3s">
#                                 Free
#                                 delivery & special prices</h5>
#                             <a class="btn btn-outline-indigo btn-lg wow fadeInDown" data-wow-delay="0.3s">Shop</a>
#                             <a class="btn btn-indigo btn-lg wow fadeInDown" data-wow-delay="0.3s">Lookbook</a>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         </div>
#     </div>
#
# </head>
# <body>
# <main>
#     <div class="container">
#
#         <!-- Section 1: Row of Cards -->
#         <section class="section pb-3 wow fadeIn" data-wow-delay="0.3s">
#             <div class="container">
#                 <h2 class="font-weight-bold text-center h2 my-5">Section 1</h2>
#                 <!-- Grid row for Section 1 -->
#                 <div class="row">
#                     <!-- Card 1 -->
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <!--Card-->
#                         <div class="card card-ecommerce">
#                             <!--Card image-->
#                             <div class="view overlay z-depth-1">
#                                 <div class="image-container">
#                                     <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}"
#                                          class="d-block w-100" alt="Slide 1">
#                                 </div>
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <!-- Card 2 -->
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <div class="image-container">
#                                     <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}"
#                                          class="d-block w-100" alt="Slide 1">
#                                 </div>
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <div class="image-container">
#                                     <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}"
#                                          class="d-block w-100" alt="Slide 1">
#                                 </div>
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <div class="image-container">
#                                     <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}"
#                                          class="d-block w-100" alt="Slide 1">
#                                 </div>
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <div class="image-container">
#                                     <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}"
#                                          class="d-block w-100" alt="Slide 1">
#                                 </div>
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <div class="image-container">
#                                     <img src="{{ url_for('static', filename='images/skoolKids.jpeg') }}"
#                                          class="d-block w-100" alt="Slide 1">
#                                 </div>
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <!-- Repeat this structure for more cards in Section 1 -->
#                 </div>
#                 <!-- Grid row for Section 1 -->
#             </div>
#         </section>
#         <!-- Section 1: Row of Cards -->
#
#         <!-- Section 1: Row of Cards -->
#         <section class="section pb-3 wow fadeIn" data-wow-delay="0.3s">
#             <div class="container">
#                 <h2 class="font-weight-bold text-center h2 my-5">Section 2</h2>
#                 <!-- Grid row for Section 1 -->
#                 <div class="row">
#                     <!-- Card 1 -->
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay z-depth-1">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <!-- Card 2 -->
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <!-- Repeat this structure for more cards in Section 1 -->
#                 </div>
#                 <!-- Grid row for Section 1 -->
#             </div>
#         </section>
#         <!-- Section 1: Row of Cards -->
#         <!-- Section 1: Row of Cards -->
#         <section class="section pb-3 wow fadeIn" data-wow-delay="0.3s">
#             <div class="container">
#                 <h2 class="font-weight-bold text-center h2 my-5">Section 3</h2>
#                 <!-- Grid row for Section 1 -->
#                 <div class="row">
#                     <!-- Card 1 -->
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay z-depth-1">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <!-- Card 2 -->
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top img-fluid"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <div class="col-lg-4 col-md-6 mb-4">
#                         <div class="card card-ecommerce">
#                             <div class="view overlay">
#                                 <img src="https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/img%20(36).jpg"
#                                      class="card-img-top"
#                                      alt="">
#                                 <a>
#                                     <div class="mask rgba-white-slight"></div>
#                                 </a>
#                             </div>
#                             <div class="card-body text-center no-padding">
#                                 <a href="#" class="text-muted">
#                                     <h5>Blouse</h5>
#                                 </a>
#                                 <h4 class="card-title">
#                                     <strong>
#                                         <a href="#">White Blouse</a>
#                                     </strong>
#                                 </h4>
#                                 <p class="card-text">Neque porro quisquam est, qui dolorem ipsum quia dolor.</p>
#                                 <div class="card-footer">
#                                 <span class="float-left">$59
#                                     <span class="discount">$199</span>
#                                 </span>
#                                     <span class="float-right">
#                                     <a class="" data-toggle="tooltip" data-placement="top" title="Add to Wishlist">
#                                         <i class="fas fa-heart"></i>
#                                     </a>
#                                 </span>
#                                 </div>
#                             </div>
#                         </div>
#                     </div>
#                     <!-- Repeat this structure for more cards in Section 1 -->
#                 </div>
#                 <!-- Grid row for Section 1 -->
#             </div>
#         </section>
#         <!-- Section 1: Row of Cards -->
#
#         <!-- Add more sections with rows of cards as needed -->
#
#     </div>
# </main>
#
#
# <!--  SCRIPTS  -->
# <!-- JQuery -->
# <script type="text/javascript" src="../js/jquery-3.4.1.min.js"></script>
# <!-- Bootstrap tooltips -->
# <script type="text/javascript" src="../js/popper.min.js"></script>
# <!-- Bootstrap core JavaScript -->
# <script type="text/javascript" src="../js/bootstrap.min.js"></script>
# <!-- MDB core JavaScript -->
# <script type="text/javascript" src="../js/mdb.min.js"></script>
# <script>
#     new WOW().init();
#     <!-- Add Bootstrap JS and MDB JS scripts here -->
#     <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
# <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
# <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.19.2/js/mdb.min.js"></script>
#
# <!-- Initialize tooltips -->
# <script>
#     $(document).ready(function () {
#         $('[data-toggle="tooltip"]').tooltip()
#     });
# </script>
# </body>
# </html>
#
# {% endblock %}
# {% extends "base.html" %}
#
# {% block content %}
# <style>
#     .custom-container {
#         font-family: 'Poppins', sans-serif;
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         min-height: 100vh;
#         background: #131313;
#     }
#
#     .card-container {
#         display: flex;
#         flex-wrap: wrap;
#         justify-content: space-around;
#         max-width: 1200px; /* Adjust as needed */
#         margin: 20px; /* Added margin for better spacing */
#     }
#
#     .custom-container .card {
#         position: relative;
#         width: 320px;
#         max-width: 100%; /* Make the cards responsive */
#         height: 450px;
#         background: #131313;
#         border-radius: 20px;
#         overflow: hidden;
#         margin: 10px; /* Added margin for better spacing */
#     }
#
#
#     .custom-container .card:before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         background: #9bdc28;
#         clip-path: circle(150px at 80% 20%);
#         transition: 0.5s ease-in-out;
#     }
#
#     .custom-container .card:hover:before {
#         clip-path: circle(300px at 80% -20%);
#     }
#
#     .custom-container .card:after {
#         content: 'Fadhili';
#         position: absolute;
#         top: 30%;
#         left: -20%;
#         font-size: 12em;
#         font-weight: 800;
#         font-style: italic;
#         color: rgba(255, 255, 25, 0.05);
#     }
#
#     .custom-container .card .imgBx img {
#         width: 100%;
#         height: 100%;
#         object-fit: cover;
#     }
#
#     .custom-container .card .imgBx {
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#     }
#
#     .custom-container .card:hover .imgBx {
#         top: 0%;
#         transform: translateY(0%);
#     }
#
#     .custom-container .card .imgBx img {
#         position: absolute;
#         top: 50%;
#         left: 50%;
#         transform: translate(-50%, -50%) rotate(-25deg);
#         width: 270px;
#     }
#
#     .custom-container .card .contentBx {
#         position: relative;
#         z-index: 1; /* Content is in front of the image */
#         width: 100%;
#         height: 100%;
#         text-align: center;
#         transition: 1s;
#     }
#
#     .custom-container .card:hover .contentBx {
#         height: 210px;
#     }
#
#     .custom-container .card .contentBx h2 {
#         position: relative;
#         font-weight: 600;
#         letter-spacing: 1px;
#         color: #fff;
#         margin: 0;
#     }
#
#     .custom-container .card .contentBx .size,
#     .custom-container .card .contentBx .color {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         padding: 8px 20px;
#         transition: 0.5s;
#         opacity: 0;
#         visibility: hidden;
#         padding-top: 0;
#         padding-bottom: 0;
#     }
#
#     .custom-container .card:hover .contentBx .size {
#         opacity: 1;
#         visibility: visible;
#         transition-delay: 0.5s;
#     }
#
#     .custom-container .card:hover .contentBx .color {
#         opacity: 1;
#         visibility: visible;
#         transition-delay: 0.6s;
#     }
#
#     .custom-container .card .contentBx .size h3,
#     .custom-container .card .contentBx .color h3 {
#         color: #fff;
#         font-weight: 300;
#         font-size: 14px;
#         text-transform: uppercase;
#         letter-spacing: 2px;
#         margin-right: 10px;
#     }
#
#     .custom-container .card .contentBx .size span {
#         width: 26px;
#         height: 26px;
#         text-align: center;
#         line-height: 26px;
#         font-size: 14px;
#         display: inline-block;
#         color: #007bff;
#         background: #fff;
#         margin: 0 5px;
#         transition: 0.5s;
#         color: #111;
#         border-radius: 4px;
#         cursor: pointer;
#     }
#
#     .custom-container .card .contentBx .size span:hover {
#         background: #9bdc28;
#     }
#
#     .custom-container .card .contentBx .color span {
#         width: 20px;
#         height: 20px;
#         background: #ff0;
#         border-radius: 50%;
#         margin: 0 5px;
#         cursor: pointer;
#     }
#
#     .custom-container .card .contentBx .color span:nth-child(2) {
#         background: #9bdc28;
#     }
#
#     .custom-container .card .contentBx .color span:nth-child(3) {
#         background: #03a9f4;
#     }
#
#     .custom-container .card .contentBx .color span:nth-child(4) {
#         background: #e91e63;
#     }
#
#     .custom-container .card .contentBx a {
#         display: inline-block;
#         padding: 10px 20px;
#         background: #fff;
#         border-radius: 4px;
#         margin-top: 10px;
#         text-decoration: none;
#         font-weight: 600;
#         color: #000;
#         opacity: 0;
#         transform: translateY(50px);
#         transition: 0.5s;
#         margin-top: 0;
#     }
#
#     .custom-container .card:hover .contentBx a {
#         opacity: 1;
#         transform: translateY(0px);
#         transition-delay: 0.75s;
#     }
#
# </style>
# <!-- Font Awesome -->
# <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css">
# <!-- Bootstrap core CSS -->
# <link href="../css/bootstrap.min.css" rel="stylesheet">
# <!-- Material Design Bootstrap -->
# <link href="../css/mdb.min.css" rel="stylesheet">
# <!-- Intro Section -->
# <div class="view jarallax" data-jarallax='{"speed": 0.2}'
#      style="background-image: url(https://mdbootstrap.com/img/Photos/Others/model-3.jpg); background-repeat: no-repeat; background-size: cover; background-position: center center;">
#     <div class="mask rgba-white-light">
#         <div class="container h-100 d-flex justify-content-center align-items-center vh-100">
#             <div class="row pt-5 mt-3">
#                 <div class="col-md-12 mb-3">
#                     <div class="intro-info-content text-center">
#                         <h1 class="display-3 mb-2 wow fadeInDown" data-wow-delay="0.3s">STATIONARY
#                             <a class="indigo-text font-weight-bold">COLLECTION</a>
#                         </h1>
#                         <h5 class="text-uppercase mb-5 mt-1 font-weight-bold wow fadeInDown" data-wow-delay="0.3s">
#                             Free
#                             delivery & special prices</h5>
#                     </div>
#                 </div>
#             </div>
#         </div>
#     </div>
# </div>
#
# <div class="intro-info-content text-center">
#     <div class="text-center">
#         <h1 class="display-3 mb-2 wow fadeInDown" data-wow-delay="0.3s">NEW
#             <a class="indigo-text font-weight-bold">COLLECTION</a>
#         </h1>
#         <h5 class="text-uppercase mb-5 mt-1 font-weight-bold wow fadeInDown" data-wow-delay="0.3s">
#             Free delivery & special prices</h5>
#     </div>
# </div>
# <div class="custom-container">
#     <div class="card-container">
#         <!-- Define a list of cards with their properties -->
#         {% set set_cards = [
#         {
#         'title': 'Nike Shoes 1',
#         'size': ['7', '8', '9', '10'],
#         'colors': ['Red', 'Blue', 'Green'],
#         'image_url': 'URL_TO_IMAGE_1'
#         },
#         {
#         'title': 'Nike Shoes 2',
#         'size': ['6', '7', '8', '9'],
#         'colors': ['Black', 'White', 'Gray'],
#         'image_url': 'URL_TO_IMAGE_2'
#         },
#         {
#         'title': 'Nike Shoes 3',
#         'size': ['8', '9', '10', '11'],
#         'colors': ['Yellow', 'Orange', 'Purple'],
#         'image_url': 'URL_TO_IMAGE_3'
#         },
#         {
#         'title': 'Nike Shoes 4',
#         'size': ['7', '8', '9', '10'],
#         'colors': ['Red', 'Blue', 'Green'],
#         'image_url': 'URL_TO_IMAGE_4'
#         },
#         {
#         'title': 'Nike Shoes 5',
#         'size': ['6', '7', '8', '9'],
#         'colors': ['Black', 'White', 'Gray'],
#         'image_url': 'URL_TO_IMAGE_5'
#         },
#         {
#         'title': 'Nike Shoes 6',
#         'size': ['8', '9', '10', '11'],
#         'colors': ['Yellow', 'Orange', 'Purple'],
#         'image_url': 'URL_TO_IMAGE_6'
#         }
#         ] %}
#
#         <div class="row mb-4">
#             {% for card in set_cards %}
#             <div class="col-md-4">
#                 <div class="card">
#                     <div class="contentBx">
#                         <h2>{{ card.title }}</h2>
#                         <div class="size">
#                             <h3>Size :</h3>
#                             {% for size in card.size %}
#                             <span>{{ size }}</span>
#                             {% endfor %}
#                         </div>
#                         <div class="color">
#                             <h3>Color :</h3>
#                             {% for color in card.colors %}
#                             <span>{{ color }}</span>
#                             {% endfor %}
#                         </div>
#                         <a href="#">Buy Now</a>
#                     </div>
#                     <div class="imgBx">
#                         <img src="{{ card.image_url }}">
#                     </div>
#                 </div>
#             </div>
#             {% if loop.index % 3 == 0 %}
#         </div>
#         <div class="row mb-4">
#             {% endif %}
#             {% endfor %}
#         </div>
#         <!-- End of loop -->
#     </div>
# </div>
#
#
# <div class="intro-info-content text-center">
#     <div class="text-center">
#         <h1 class="display-3 mb-2 wow fadeInDown" data-wow-delay="0.3s">Exercise Book
#             <a class="indigo-text font-weight-bold">COLLECTION</a>
#         </h1>
#         <h5 class="text-uppercase mb-5 mt-1 font-weight-bold wow fadeInDown" data-wow-delay="0.3s">
#             Free delivery & special prices</h5>
#     </div>
# </div>
# <div class="custom-container">
#     <div class="card-container">
#         <!-- Define a list of cards with their properties -->
#
#         {% set set_cards = [
#         {
#         'title': 'Exercise Book',
#         'Pages': ['200'],
#         'image_url': url_for('static', filename='images/skoolKids.jpeg')
#         },
#         {
#         'title': 'Exercise Book',
#         'Pages': ['120'],
#         'image_url': url_for('static', filename='images/KARTASI01EXC1009-40402.jpg')
#         },
#         {
#         'title': 'Exercise Book',
#         'Pages': ['96'],
#         'image_url':url_for('static', filename='images/img.png') },
#         {
#         'title': 'Exercise Book',
#         'Pages': ['64'],
#
#         'image_url': 'URL_TO_IMAGE_4'
#         },
#         {
#         'title': 'Exercise Book',
#         'Pages': ['48'],
#         'image_url': 'URL_TO_IMAGE_5'
#         },
#         {
#         'title': 'Exercise Book',
#         'Pages': [32],
#         'image_url': 'URL_TO_IMAGE_6'
#         }
#         ] %}
#
#         <div class="row mb-4">
#             {% for card in set_cards %}
#             <div class="col-md-4">
#                 <div class="card">
#                     <div class="contentBx">
#                         <h2>{{ card.title }}</h2>
#                         <div class="size">
#                             <h3>Pages :</h3>
#                             {% for pages in card.pages %}
#                             <span>{{ pages }}</span>
#                             {% endfor %}
#                         </div>
#
#                         <a href="#">Buy Now</a>
#                     </div>
#                     <div class="imgBx">
#                         <img src="{{ card.image_url }}">
#                     </div>
#                 </div>
#             </div>
#             {% if loop.index % 3 == 0 %}
#         </div>
#         <div class="row mb-4">
#             {% endif %}
#             {% endfor %}
#         </div>
#         <!-- End of loop -->
#     </div>
# </div>
#
# {% endblock %}
#
