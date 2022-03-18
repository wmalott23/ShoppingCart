from shoppingcart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.my_cart = ShoppingCart(name)

    def cart_add(self, product):
        self.my_cart.add_item(product)

    def look_in_cart(self):
        for each in self.my_cart.inventory:
            print(f'You see {each.name} in the shopping cart')
        if self.my_cart.inventory == []:
            print("The cart is empty")

    