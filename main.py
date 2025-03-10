
regular_menu = {
    'veg-Pizza':40,
    'pasta':25,
    'noodles':30,
    'manchurian':35,
    'fried Rice':20,
    'tea':10,
    'coffee':15,

}

print("WELCOME TO DESI CHINESE RESTAURANT")
print(" veg-pizza:Rs.40\n pasta :Rs.25 \n noodles:Rs.30 \n manchurian:Rs.35 \n fried rice:Rs.20 \n tea:Rs.10 \n coffee:Rs.15")

Total_order = 0

item_1 = input("Enter the name of your item you want to order:")
if item_1 in regular_menu:
    Total_order += regular_menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"This item {item_1}is not available in the menu !")

another_order = input("Do you want somenthing else ?(Yes/No):")
if another_order == 'Yes':
    item_2 = input("Enter your another item that you want to order:")
    if item_2 in regular_menu:
        Total_order += regular_menu[item_2]
        print(f"item{item_2} has been added to your order")

    else:
        print(f"this ordered item {item_2}is not available in the menu!")

print(f"the total amount of order items is:clear{Total_order}")



    
