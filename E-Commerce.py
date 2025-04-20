import uuid
from datetime import datetime

class Product:
    def __init__(self, name, price, stock, category):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.reviews = []

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def add_review(self, review, rating):
        self.reviews.append({"review": review, "rating": rating})
        return "Review added successfully."


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_all(self):
        return [f"{p.name} (${p.price}) - Stock: {p.stock} - Category: {p.category}" for p in self.products]


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.update_stock(quantity):
            self.items[product] = self.items.get(product, 0) + quantity
            return True
        return False

    def remove_product(self, product):
        if product in self.items:
            product.stock += self.items[product]
            del self.items[product]
            return True
        return False

    def apply_discount(self, percentage):
        return sum(product.price * qty * (1 - percentage / 100) for product, qty in self.items.items())

    def view_cart(self):
        if not self.items:
            return "Cart is empty."
        return "\n".join(f"{product.name}: {qty} x ${product.price}" for product, qty in self.items.items())

    def apply_coupon(self, code):
        coupons = {"SAVE10": 10, "NEWYEAR": 20}
        discount = coupons.get(code.upper(), 0)
        return self.apply_discount(discount)


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        return self.cart.add_product(product, quantity)

    def remove_from_cart(self, product):
        return self.cart.remove_product(product)


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.date = datetime.now()
        self.total_price = customer.cart.apply_discount(0)

    def process_order(self):
        total = self.customer.cart.apply_discount(0)
        self.customer.cart.items.clear()
        return f"Order processed for {self.customer.name} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}. Total: ${total:.2f}"

    def make_payment(self, method="Credit Card"):
        return f"Payment successfully received using {method}."


# Example usage
product1 = Product("Laptop", 1000, 5, "Electronics")
product2 = Product("Phone", 500, 10, "Electronics")

product1.add_review("Great laptop!", 5)
product2.add_review("Good value for money.", 4)

customer = Customer("Muqtasid Khan")
customer.add_to_cart(product1, 1)
customer.add_to_cart(product2, 2)

print(customer.cart.view_cart())

order = Order(customer)
print(order.process_order())
print(order.make_payment("PayPal"))
