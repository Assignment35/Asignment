class ManagerDashboard:
    def __init__(self, catalog, orders):
        self.catalog = catalog
        self.orders = orders

    def show_all_orders(self):
        if not self.orders:
            print("No orders yet.")
            return
        print("\nAll Orders:")
        for order in self.orders:
            order.show_purchase()

    def modify_order_status(self, purchase_id, status):
        for order in self.orders:
            if order.purchase_id == purchase_id:
                order.status = status
                print(f"Order {purchase_id} status updated to '{status}'.")
                return
        print("Order not located.")

    def display_admin_options(self):
        print("\nManager Dashboard:")
        print("1. Review Orders")
        print("2. Adjust Order Status")
        print("3. Show Product Catalog")
        print("4. Logout")