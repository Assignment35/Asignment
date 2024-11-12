class Purchase:
    def __init__(self, purchase_id, items, delivery_option):
        self.purchase_id = purchase_id
        self.items = items
        self.delivery_option = delivery_option
        self.status = "Awaiting Confirmation"

    def show_purchase(self):
        print(f"\nOrder ID: {self.purchase_id}")
        total_cost = 0
        for product in self.items:
            print(f"{product.title} - ${product.cost:.2f}")
            total_cost += product.cost
        print(f"Delivery Option: {self.delivery_option}")
        print(f"Total: ${total_cost:.2f}")
        print(f"Status: {self.status}\n")