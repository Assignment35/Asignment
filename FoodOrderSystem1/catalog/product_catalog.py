class Product:
    def __init__(self, code, title, cost, category):
        self.code = code
        self.title = title
        self.cost = cost
        self.category = category

class ProductCatalog:
    def __init__(self):
        self.products = [
            Product(1, "Veggie Pizza", 12.99, "Pizza"),
            Product(2, "Cheese Burger", 8.99, "Burger"),
            Product(3, "Spaghetti", 10.49, "Pasta"),
            Product(4, "Caesar Salad", 6.99, "Salad"),
            Product(5, "Pepperoni Pizza", 14.99, "Pizza"),
            Product(6, "Grilled Chicken Salad", 9.99, "Salad"),
        ]

    def show_catalog(self):
        print("\nAvailable Products:")
        for product in self.products:
            print(f"{product.code}. {product.title} - ${product.cost:.2f} (Category: {product.category})")

    def find_product(self, code):
        for product in self.products:
            if product.code == code:
                return product
        return None

    def search_product(self, search_term):
        results = [product for product in self.products if search_term.lower() in product.title.lower()]
        if not results:
            print("No products found.")
            return
        print("\nSearch Results:")
        for product in results:
            print(f"{product.code}. {product.title} - ${product.cost:.2f} (Category: {product.category})")