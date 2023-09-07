gst = .05
pst = .07

finalPrice = 0

basePrice = float(input("Enter the price of the item: "))

finalPrice = round(basePrice * (1+gst+pst), 2)

print("GST: " + str(gst))
print ("PST: " + str(pst))
print("Total: " + str(finalPrice))