# -------------------------------------------------
# Simple Shopping System
# -------------------------------------------------
# This program simulates a basic online shopping
# experience similar to Amazon. Users can browse
# products, add items to a cart, view the cart,
# and checkout.
# -------------------------------------------------

# Store products as a dictionary
products = {
    1: {"name": "Laptop", "price": 899.99},
    2: {"name": "Headphones", "price": 199.99},
    3: {"name": "Keyboard", "price": 89.99},
    4: {"name": "Mouse", "price": 49.99},
    5: {"name": "Monitor", "price": 299.99}
}

cart = {}  # Stores product_id : quantity


def display_products():
    print("\nAvailable Products")
    print("-" * 40)
    for pid, item in products.items():
        print(f"{pid}. {item['name']} - ${item['price']:.2f}")


def add_to_cart():
    try:
        product_id = int(input("Enter product ID to add: "))
        if product_id not in products:
            print("Invalid product ID.")
            return

        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        cart[product_id] = cart.get(product_id, 0) + quantity
        print("Item added to cart.")

    except ValueError:
        print("Invalid input.")


def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\nYour Shopping Cart")
    print("-" * 40)

    total = 0
    for pid, qty in cart.items():
        item = products[pid]
        cost = item["price"] * qty
        total += cost
        print(f"{item['name']} x {qty} = ${cost:.2f}")

    print("-" * 40)
    print(f"Total: ${total:.2f}")


def checkout():
    if not cart:
        print("Your cart is empty.")
        return

    view_cart()
    confirm = input("\nProceed to checkout? (y/n): ").lower()

    if confirm == "y":
        print("Order placed successfully!")
        cart.clear()
    else:
        print("Checkout canceled.")


# Main program loop
while True:
    print("\nAmazon-Style Shopping Menu")
    print("1 - View Products")
    print("2 - Add to Cart")
    print("3 - View Cart")
    print("4 - Checkout")
    print("5 - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_products()
    elif choice == "2":
        display_products()
        add_to_cart()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
    elif choice == "5":
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please try again.")
