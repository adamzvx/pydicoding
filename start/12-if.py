amount = int(input("Enter amount: "))
if amount<1000:
   discount = amount*0.05
   print ("Discount",discount)
elif amount<5000:
   discount = amount*0.10
   print ("Discount",discount)
else:
   discount = amount*0.15
   print ("Discount",discount)
print ("Net payable:",amount-discount)



#Ternary
# condition_if_true if condition else condition_if_false
# is_nice = True
# state = "nice" if is_nice else "not nice"
condition = True
print(2 if condition else 1/0)

#print((1/0, 2)[condition])



#Shorthand Ternary
output = None
msg = output or "No data returned"
print(msg)