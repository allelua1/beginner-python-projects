#Dictionary stores {product: quantity}
#Functions to: restock, sell an item, check low stock
#Alert when any item drops below a threshold

stores = [
    {"name":"Books","quantity":30, "Supplier":"Benigne", "price":200},
    {"name":"Pen", "quantity":10, "Supplier":"Dianekk", "price":100},
    {"name":"Socket","quantity":50, "Supplier":"Benjamin","price":2000},
    {"name":"Laptop", "quantity":25, "Supplier":"Sengajj", "price":120000}
]

def display_inventory(stores):
    print("n\Inventory: ")
    print("Name\tQuantity\tSupplier\tPrice")
    for item in stores:
        print(f"{item["name"]}\t{item["quantity"]}\t{item["Supplier"]}\t\t{item['price']}")

def restock(stores, name, quantity, supplier, price):
    for item in stores:
        if item["name"].lower() == name.lower():
            item["quantity"] += quantity
            item["Supplier"] = supplier
            item["price"] = price
            print(f"{quantity} {name} added successfully")
            return
    stores.append({
        "name": name,
        "quantity": quantity,
        "Supplier": supplier,
        "price": price
    })
    print(f"{quantity} {name} added as a new item. ")

def sell_item(stores, name, quantity):
    for item in stores:
        if item["name"].lower() == name.lower():
            if item["quantity"] >= quantity:
                item["quantity"] -= quantity
                total_price = quantity * item["price"]
                print(f"{quantity} {name} sold successfully")
            else:
                print(f"Not enough stock for {name}.")
            return
    print(f"{name} not found in inventory")

def check_low_stock(stores, threshold = 10):
    print("\nLow Stock Items: ")
    found = False
    for item in stores:
        if item["quantity"] < threshold:
            print(f"{item["name"]} has only {item["quantity"]} left")
            found = True
    if not found:
        print("No low stock items. ")

display_inventory(stores)
restock(stores, "Books", 10, "Benigne", 200)
display_inventory(stores)
sell_item(stores, "Books", 20)
check_low_stock(stores)
display_inventory(stores)
