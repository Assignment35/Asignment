class CustomerBasket:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for _ in range(quantity):
            self.items.append(product)
        print(f"{quantity} x {product.title} added to your basket.")

    def view_basket(self):
        if not self.items:
            print("Basket is currently empty.")
            return
        print("\nBasket Contents:")
        total_cost = 0
        for product in self.items:
            print(f"{product.title} - ${product.cost:.2f}")
            total_cost += product.cost
        print(f"Total Cost: ${total_cost:.2f}\n")

    def empty_basket(self):
        self.items = []