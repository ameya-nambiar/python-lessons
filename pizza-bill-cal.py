# This program calculates the total amount of the bill for the pizza order 

customer_name = input("What's your name? ")

number_of_pizzas = input("How many Pizzas would you like to order " + customer_name + " ? ")


# Price per Pizza is $5
pizza_price = 5.0

# Subtotal is number of pizzas multiplied by price of pizza
subtotal = float(number_of_pizzas) * pizza_price

# Tax is 8% of subtotal in Atlanta
tax = subtotal * (8.0/100.0)

final_total = float(subtotal + tax)

print ( "So " + customer_name + " the total price today for " + number_of_pizzas + " is $" +  str(final_total))

