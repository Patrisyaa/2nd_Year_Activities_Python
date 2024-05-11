##printing

print("\t\t\t\tSERVICES\n\n")
print("\tCode\t\tDescription\t\tPrice")
print("\t[A]\t\t\tHair Cut\t\tP 100.00")
print("\t[B]\t\t\tMassage\t\t\tP500.00")
print("\t[C]\t\t\tNail Treatment\tP200.00")

total=0
order=eval(input("How many services do you want to purchase?"))

for i in range(order):
    
    code=input("Type the Code of your Choice:")
    quantity=eval(input("Type the quantity of your service:"))
    
    if code=="A" or code=="a":
        ser_total=100*quantity
        print(quantity,end="")
        print(" Hair Cut P", ser_total,".00")
        total=total+ser_total
    
    elif code=="B" or code=="b":
        ser_total=500*quantity
        print(quantity,end="")
        print(" Massage P", ser_total,".00")
        total=total+ser_total
        
    
    elif code=="C" or code=="c":
        ser_total=200*quantity
        print(quantity,end="")
        print(" Nail Treatment P", ser_total,".00")
        total=total+ser_total
        
    
    else:
        print("Invalid code!")

print("Total Purchase: ",total)

payment=eval(input("Payment Amount: "))

print("Your change is ",payment-total)

if payment-total < 0:
    print("Insufficient amount.")
    payment=eval(input("Please retype your Payment Amount: "))
    print("Your change is ",payment-total)


 