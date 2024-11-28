from locust import HttpUser, task, between
from random import randint


class WebsiteUser(HttpUser):
    # The users are likely to wait a few seconds before doing the next task
    # This function waits before running the next task between 1 to 5 seconds
    wait_time = between(1, 5)

    # The number inside the task decorator is the weight
    # The weight specifies that how often the users are likely to do the task
    @task(2)
    def view_products(self):
        # It is more likely that the users are viewing the products in a specific collection
        # We only have products in collection 2 - 6
        collection_id = randint(2, 6)
        self.client.get(
            f'/store/products/?collection_id={collection_id}',
            name='/store/products'
        )

    @task(4)
    def view_product(self):
        product_id = randint(1, 1000)
        self.client.get(
            f'/store/products/{product_id}/',
            name='/store/products/:id'
        )

    @task(1)
    def add_to_cart(self):
        # Limiting the number of products to 10 so that we end up getting duplicate products in our shopping cart
        # This way we can see if updating the product quantity is gonna have performance issues
        product_id = randint(1, 10)
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name='/store/carts/items',
            # For sending data to the server:
            json={'product_id': product_id, 'quantity': 1}
        )
    
    # This is automatically called whenever a new user starts browsing our web server
    def on_start(self):
        response = self.client.post('/store/carts/')        
        result = response.json()
        self.cart_id = result['id']
