products = [
    {"Name": "Shoes", "Price": 300.0, "Quantity": 12, "Category": "Footwear"},
    {"Name": "Hood", "Price": 500.0, "Quantity": 10, "Category": "Clothing"},
    {"Name": "Hood", "Price": 500.0, "Quantity": 10, "Category": "Clothing"},
]


def add_item(products, name, price, quantity, category="General"):
    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        print("Invalid price or quantity.")
        return

    products.append(
        {"Name": name.strip(), "Price": price, "Quantity": quantity, "Category": category.strip()}
    )
    print(f"Product {name} added successfully.")


def remove_item(products, name):
    name = name.strip().lower()
    for index, product in enumerate(products):
        if product["Name"].lower() == name:
            removed = products.pop(index)
            print(f"Product {removed['Name']} removed successfully.")
            return

    print(f"No product named {name} found.")


def calculate_total(products):
    total_price = sum(product["Price"] * product["Quantity"] for product in products)
    total_quantity = sum(product["Quantity"] for product in products)

    print(f"Total Price: {total_price:.2f}")
    print(f"Total Quantity: {total_quantity}")


def display_cart(products):
    if not products:
        print("The cart is empty.")
        return

    print(f"{'Product':<15}{'Quantity':>10}{'Price':>10}{'Subtotal':>12}")
    print("-" * 47)

    for product in products:
        subtotal = product["Price"] * product["Quantity"]
        print(
            f"{product['Name']:<15}"
            f"{product['Quantity']:>10}"
            f"{product['Price']:>10.2f}"
            f"{subtotal:>12.2f}"
        )

    calculate_total(products)


def display_categories(products):
    categories = {product.get("Category", "General") for product in products}
    print("Categories:", ", ".join(sorted(categories)))


def main():
    print("------- Shopping Cart System ------------")

    while True:
        print("\n1. Add item")
        print("2. Remove item")
        print("3. Calculate total")
        print("4. Display cart")
        print("5. Show categories")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            product = input("Enter product name: ")
            quantity = input("Enter quantity: ")
            price = input("Enter price: ")
            category = input("Enter category: ")
            add_item(products, product, price, quantity, category)
        elif choice == "2":
            product = input("Enter product name to remove: ")
            remove_item(products, product)
        elif choice == "3":
            calculate_total(products)
        elif choice == "4":
            display_cart(products)
        elif choice == "5":
            display_categories(products)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()