E-Commerce System in Python

A simple object-oriented e-commerce system built with Python. It simulates core functionality found in online shopping platforms such as product listing, cart management, stock tracking, order processing, and review handling.



Features

Product Management

Unique product ID generation

Product categorization

Stock updates on purchase

Customer reviews with ratings


Customer Cart

Add/remove products

View cart contents

Apply discount or coupon codes


Order Handling

Order processing with timestamp

Payment simulation with method selection


Inventory Management

Maintain a product catalog

Display available products with stock status




---

Technologies Used

Python 3

Standard libraries: uuid, datetime




How to Use

1. Clone the Repository

git clone https://github.com/yourusername/ecommerce-system-python.git
cd ecommerce-system-python


2. Run the Script

python ecommerce.py


3. Sample Output

Laptop: 1 x $1000
Phone: 2 x $500
Order processed for Muqtasid Khan on 2025-04-20 15:30:45. Total: $2000.00
Payment successfully received using PayPal.



Code Structure

ecommerce.py
│
├── Product            # Product details, stock handling, and reviews
├── Inventory          # Collection of available products
├── ShoppingCart       # Cart logic, discounts, and coupons
├── Customer           # Customer profile and cart actions
├── Order              # Order creation, processing, and payment
