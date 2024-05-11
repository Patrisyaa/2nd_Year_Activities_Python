productUnit = ""
quantity = 0
productPrice = 0
amount = 0
totalStock = 0
remarks = ""


product = input("Please enter the name of product: ")
productUnit = input("Please enter the product unit (pack, bag, case, kg, lbs): ")
quantity = int(input("Please enter the quantity: "))
productPrice = float(input("Please enter the product price: "))

amount = quantity * productPrice
totalStock += quantity

print("Product: ", product)
print("Product Unit: ", productUnit)
print("Quantity: ", quantity)
print("Product Price: ", productPrice)
print("Amount: ", amount)
print("Total Stock: ", totalStock)