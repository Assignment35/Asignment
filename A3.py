# Food Ordering System
def show_menu():
    menu = {
        1: ("Burger", 5.00),
        2: ("Pizza", 8.00),
        3: ("Fries", 2.50),
        4: ("Soda", 1.50),
        5: ("Salad", 4.00)
    }
    print("\nMenu:")
    for item_id, (item_name, price) in menu.items():
        print(f"{item_id}. {item_name} - ${price:.2f}")
    return menu

def take_order(menu):
    order = {}
    while True:
        choice = input("\nEnter the item number to order (or 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break
        if choice.isdigit() and int(choice) in menu:
            item_id = int(choice)
            quantity = input("Enter quantity for {menu[item_id][0]}: ").strip()
            if quantity.isdigit():
                quantity = int(quantity)
                if item_id in order:
                    order[item_id]  += quantity
                else:
                    order[item_id] = quantity
                print(f"{menu[item_id][0]} x {quantity} added to your order.")
            else:
                print("Please enter a valid quantity.")
        else:
            print("Please select a valid menu item number.")
    return order

def calculate_total(order, menu):
    total = 0
    print("\nYour Order Summary:")
    for item_id, quantity in order.items():
        item_name, price = menu[item_id]
        item_total = price * quantity
        total += item_total
        print(f"{item_name} x {quantity} = ${item_total:.2f}")
    print(f"\nTotal Amount: ${total:.2f}")
    return total

def main():
    print("Welcome to the Food Ordering System!")
    menu = show_menu()
    order = take_order(menu)
    if order:
        calculate_total(order, menu)
        print("\nThank you for your order!")
    else:
        print("No items were ordered.")

if __name__ == "__main__":

    
    main()