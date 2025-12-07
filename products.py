#Develop a Python program with a function that accepts product details including product ID, name, quantity, and price. The function should return the product information in a well-formatted string. Also, create a separate test file using pytest to ensure the function gives the correct output for given inputs.

def product_details(prod_id, name, quantity, price):
  result = (
    f"Product ID : {prod_id}\n"
    f"Product Name: {name}\n"
    f"Quantity: {quantity}\n"
    f"Price: {price}\n"
  )
  return result
if __name__ == "__main__":
  #sample input (you can change)
  prod_id = 101
  name = "iPhone"
  quantity = 1
  price = 155000
  print(product_details(prod_id, name, quantity, price))
