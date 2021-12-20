# Define function
def shop():
    # Create empty dictionary
    cart = {}
    # Start while loop so that the program will run until user quits
    running = True
    while(running == True):
        # Ask user what they want to do
        what_next = input("Would you like to add items, delete items, or quit? a/d/q ")
        # If q, end the while loop
        if what_next.lower() == 'q':
            running = False
        # If a, add to shopping list
        elif what_next.lower() == 'a':
            # Get input
            item = input("What are you shopping for today? ")
            price = input("Price: ")
            # Store input data to dictionary
            cart[item] = price
            # Print out current cart
            print("Your shopping List:")
            for item, price in cart.items():
                print(f"{item.title()} - ${price}")
        # If d, delete items from shopping list
        elif what_next.lower() == 'd':
            to_delete = input("What item would you like to delete? ")
            if to_delete in cart:
                del cart[to_delete]
                #Print out current shopping list
                print("")
                print("Your Shopping List:")
                for item, price in cart.items():
                    print(f"{item.title()} - ${price}")
            else:
                print("That is not on the list.")
                continue
        else:
            print("Please enter a, d, or q")
            continue
            
    # When finished, print out the final list
    total_items = 0
    total_price = 0
    print("")
    print("Here is your final list:")
    for item, price in cart.items():
        print(f"{item.title()} - ${price}")
        total_items +=1
        total_price = total_price + int(price)
    print(f"{total_items} total items for a total of ${total_price}.") 
    
# Call function
shop()
