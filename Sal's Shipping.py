# Sal's Shipping

# build a program that will take the weight of a package and determine the cheapest way to ship that package using sal's shippers

# Ground shipping small flat charge plus a rate based on the weight of your package.

#Ground shipping premuim  much higher flat charge, but you aren’t charged for weight.

#Drone shipping which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

#change the weight = get another price in every ship method
weight = 15

if weight <= 2:
    Ground_ship_cost = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
    Ground_ship_cost = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
    Ground_ship_cost = weight * 4.00 + 20
elif weight > 10:
    Ground_ship_cost = weight * 4.75 + 20

print("The Weight shipping costs" +" "+"$"+str(Ground_ship_cost))


#premuim
premuim_ground_shipping = "$125.00"
print("The premuim ground shipping costs" +" "+ premuim_ground_shipping)



#drone shipping 
if weight < 2:
    Drone_Shippin = weight * 4.50 + 0.00
elif weight > 2 and weight <= 6:
    Drone_Shippin = weight * 9.00 + 0.00
elif weight > 6 and weight < 10:
    Drone_Shippin = weight * 12.00 + 0.00
elif weight > 10:
    Drone_Shippin = weight * 14.25 + 0.00

print("That will costs you" + " " +"$"+str(Drone_Shippin))
