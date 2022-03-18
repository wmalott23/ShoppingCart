from product import Product

class ShoppingCart:
    def __init__(self, cart_user):
        self.cart_user = cart_user
        self.inventory = []

    def total_count(self):
        count = 0
        for each in self.inventory:
            count += each.price
        return count

    def add_item(self, product):
        self.inventory.append(product)

    def flip_cart(self):
        self.inventory = []
        print("You empty your cart")