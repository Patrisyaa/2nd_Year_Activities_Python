product = ""
productUnit = ""
quantity = 0
productPrice = 0
amount = 0
totalStock = 0
remarks = ""


print("\n\t\t\t\t\t\t Stock Count Tracking")


print("\t\t\t\t\t\t\t\tSERVICES\n\n")   
print("\t\t\t\t\tCode\tDescription")
print("\t\t\t\t\t[A]\t\tCheck Inventory")
print("\t\t\t\t\t[B]\t\tAdd Items")
print("\t\t\t\t\t[C]\t\tDelete Items")


for i in range (srvcCode):
    product = input("Please enter the name of product: ")
    quantity=eval(input("Type the quantity of your item:"))
    price = float(input("Please enter the product price: "))
    
srvcCode=input("Type the code of your choice: ")

if srvcCode == "A" or srvcCode == "a":
    with open (joinPath, "r") as jsonLoad:
        jsonRead = jsonLoad.readlines()
    jsonRead_dict = json.loads(jsonRead[0])
    
    if is_newFile == True:
        print("No data available.")

    else:
        table = pd.DataFrame (jsonRead_dict)
        print(table)
    
    reSrvc = input("Would you like to use another service? [y/n] ")
   
    while reSrvc == "Y" or reSrvc == "y":
        print("\t\t\t\t\t\t\t\tSERVICES\n\n")   
        print("\t\t\t\t\tCode\tDescription")
        print("\t\t\t\t\t[A]\t\tCheck Inventory")
        print("\t\t\t\t\t[B]\t\tAdd Items")
        print("\t\t\t\t\t[C]\t\tDelete Items")
        
        srvcCode=input("Type the code of your choice: ")
        
        if srvcCode == "A" or srvcCode == "a":
            func.srvcCode_A()
        elif srvcCode == "B" or srvcCode == "b":
            func.servcCode_B()
        elif srvcCode == "C" or srvcCode == "a":
            pass
        reSrvc = input("Would you like to use another service? [y/n] ")
        continue
    else: 
        break
    
    
    

amount = quantity * productPrice
totalStock += quantity


print("Product: ", product)
print("Product Unit: ", productUnit)
print("Quantity: ", quantity)
print("Product Price: ", productPrice)
print("Amount: ", amount)
print("Total Stock: ", totalStock)