# As a developer, I want to use Python’s proper snake_case for variable names.

# As a developer, I want to create a Customer, ShoppingCart, and Product class.

# As a developer, I want the Product class to have class properties to keep track of the Product’s name, price, and category.

# As a developer, I want the Product class’s initializer to take in the initial values for the name, price, and category via parameters

# As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products (list).

# As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.

# As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list)

# As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart.

# As a developer, I want the Customer class to have class instance variables to keep track of the Customer’s name and shopping cart object. (Set the shopping cart instance variable equal to a new ShoppingCart object in the initializer HINT: You will have to import the ShoppingCart class into the customer.py file)

# As a developer, I want the Customer class’s initializer to take in the initial value for the customer’s name via a parameter.

# As a developer, I want the Customer class to have a method to add a new product to the customer’s shopping cart (within this method you will call the shopping cart’s add product method)

# As a developer, I want the Customer class to have a method to view all products in the customer’s shopping cart. (Loop over the shopping cart’s products list and print each product to the terminal)

# As a developer, I want to import the Customer and Product classes into main.py so I can instantiate a customer object as well as three Product ob# jects and interact with the object’s methods


from product import Product
from customer import Customer

customer = Customer("Jonathan")
product_one = Product("salt", 1, "seasoning")
product_two = Product("chimken nuggies", 42, "food")
product_three = Product("water", 1, "liquid")

print(customer.name)

customer.cart_add(product_one)
customer.cart_add(product_two)
customer.cart_add(product_three)

customer.look_in_cart()

total = customer.my_cart.total_count()
print(total)

customer.my_cart.flip_cart()

customer.look_in_cart()
