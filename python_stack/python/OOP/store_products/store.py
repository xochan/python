# Start by creating a Store class that has 2 attributes: a name and a list of 
# products. The name must be provided upon creation, but the products list 
# should be empty.
# Next, create a Product class that has 3 attributes: a name, a price, and 
# a category. All of these should be provided upon creation.
# Let's give some methods to our Product class:
    # update_price(self, percent_change, is_increased) - updates the product's price. 
    # If is_increased is True, the price should increase by the percent_change 
    # provided. If False, the price should decrease by the percent_change provided.
    # print_info(self) - print the name of the product, its category, and its price.
# Let's also give some methods to our Store class:

    # add_product(self, new_product) - takes a product and adds it to the store
    # sell_product(self, id) - remove the product from the store's list of products 
    # given the id (assume id is the index of the product in the list) and print its info.
    # inflation(self, percent_increase) - increases the price of each product by the 
    # percent_increase given (use the method you wrote in the Product class!)
    # set_clearance(self, category, percent_discount) - updates all the products 
    # matching the given category by reducing the price by the percent_discount 
    # given (use the method you wrote in the Product class!)

class store:
    def __init__(self,name):
        self.name = name
        self.list = []

class product:
    def __init__(self,name, price, category):
        update_price(self, percent_change, is_increased)