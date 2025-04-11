# 🛒 ShopSphere

**ShopSphere** is a minimal e-commerce web application developed using **Django**. This resume project simulates a clothing shopping platform where users can browse products, view product details, add items to a cart, and place orders via a fake payment flow. The site is styled with a clean black-and-white theme and emphasizes both functionality and user experience.

---

## 🚀 Features

### 🔐 Authentication
- User registration and login
- Secure session management

### 🏷️ Product Management (Admin)
- Add, update, and delete product categories
- Manage product listings with image, price, and description

### 🛍️ User Functionality
- View all available products
- Detailed product view with "Add to Cart" option
- Quantity-based cart system with live updates
- View cart summary with price breakdown and discount
- Fake payment page to simulate order confirmation

### 🧾 Checkout & Order Flow
- Payment page with order summary
- Order confirmation success page with personalized message

---

## 📷 Screenshots

| Main Page | Product Detail | Cart Page | Payment Page | Order Success |
|-----------|----------------|-----------|---------------|----------------|
| ![Main](./screenshots/main.png) | ![Detail](./screenshots/product.png) | ![Cart](./screenshots/cart.png) | ![Payment](./screenshots/payment.png) | ![Success](./screenshots/success.png) |

> *Screenshots are for illustration. Upload yours in a `/screenshots` folder.*

---

## ⚙️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (black & white theme), Bootstrap
- **Database**: SQLite (default Django DB)
- **Deployment**: [PythonAnywhere](https://www.pythonanywhere.com)

---

## 📁 Project Structure

shopsphere/
├── manage.py
├── db.sqlite3
├── shopsphere/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shopapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── migrations/
│       └── __init__.py
├── templates/
│   ├── main.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── payment.html
│   └── success.html
├── static/
│   └── css/
│       └── styles.css
└── README.md

