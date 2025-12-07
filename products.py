def product_details(prod_id, name, quantity, price):
    result = (
        f"Product ID: {prod_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result

if __name__ == "__main__":
    print(product_details(101, "iPhone", 1, 155000))
