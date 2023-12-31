# Lovely Loveseat that is the store’s namesake
lovley_loveseat_description = "Lovely loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or White."

#price for the loveseat
lovely_loveseat_price =  254.00

#nother characteristic piece of furniture! 
stylish_sette_description = " stylish settee. Faux leather on brich. 29.50 inches high x 54.75 inches wide x 28 inches deep. black"

#price for our Stylish Settee
stylish_sette_price = 180.50

#more item
luxurious_lamp_descriptipn = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. "

#price for the item
luxurious_lamp_price = 52.15

#sales tax 
sales_tax = .088

#First customer
customer_one_total = luxurious_lamp_price + lovely_loveseat_price + sales_tax

customer_one_tax = customer_one_total * sales_tax

#string functions 
The_lovley_string = "The lovley loveseat: "
The_luxurious_lamp = "The luxurious lamp: "

#description purchasing

customer_one_itemization = The_lovley_string.upper() + lovley_loveseat_description + The_luxurious_lamp.upper() + luxurious_lamp_descriptipn



# Printing the Customer receipt
print("Customer one item: " + customer_one_itemization) 
print("Customer one total: " + str(customer_one_total))



