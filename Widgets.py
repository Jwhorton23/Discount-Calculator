# Widgets
# This program calculates the discount applied based on how many units are purchased


# Named constants
price_per_widget = 95


# Menu
print('10% off on 10-19 widgets purchased')
print('20% off on 20-49 widgets purchased')
print('30% off on 50-99 widgets purchased')
print('40% off on 100+ widgets purchased')
print('------------------------------------------------------------')
# User input
number_widgets_purchased = float(input('Enter the number of widgets you would like to purchase: '))


# Calculate the discount amount
if number_widgets_purchased  >= 10 and number_widgets_purchased <= 19:
# Calculate the discount for 10% off
    discount = price_per_widget * number_widgets_purchased * .10

# 20% discount on items 20-49
elif number_widgets_purchased  >= 20 and number_widgets_purchased <= 49:
# Calculate the discount for 20% off
    discount = price_per_widget * number_widgets_purchased * .20


# 30% discount on items 50-99
elif number_widgets_purchased  >= 50 and number_widgets_purchased <= 99:
# Calculate the discount for 30% off
    discount = price_per_widget * number_widgets_purchased * .30


# 40% discount on items 100+
elif number_widgets_purchased > 99:
# Calculate the discount for 40% off
    discount = price_per_widget * number_widgets_purchased * .40


# Calculate total discount
total_discount = discount
print('Your total discount is: ' , total_discount)


# calculate total cost
total_cost = price_per_widget * number_widgets_purchased - total_discount
print('Your total cost: ' , total_cost)
