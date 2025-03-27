class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            if product.product_id in self.cart:
                self.cart[product.product_id]['quantity'] += quantity
            else:
                self.cart[product.product_id] = {'product': product, 'quantity': quantity}
            product.stock -= quantity
            print(f"Added {quantity} x {product.name} to cart.")
        else:
            print(f"Not enough stock for {product.name}.")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            print("\nShopping Cart:")
            for item in self.cart.values():
                print(f"{item['product'].name} - ${item['product'].price} x {item['quantity']}")

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Add items before checkout.")
            return
        total = sum(item['product'].price * item['quantity'] for item in self.cart.values())
        print(f"\nTotal amount: ${total}")
        print("Checkout successful. Thank you for shopping!")
        self.cart.clear()


class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def view_products(self):
        print("\nAvailable Products:")
        for product in self.products.values():
            print(product)


# Sample Usage
store = Store()
store.add_product(Product(1, "Laptop", 800, 5))
store.add_product(Product(2, "Phone", 500, 10))
store.add_product(Product(3, "Headphones", 50, 15))

cart = ShoppingCart()

while True:
    print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        store.view_products()
    elif choice == "2":
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        if product_id in store.products:
            cart.add_to_cart(store.products[product_id], quantity)
        else:
            print("Invalid product ID.")
    elif choice == "3":
        cart.view_cart()
    elif choice == "4":
        cart.checkout()
    elif choice == "5":
        print("Thank you for visiting!")
        break
    else:
        print("Invalid option. Please try again.")
