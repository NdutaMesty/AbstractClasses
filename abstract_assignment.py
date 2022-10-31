from abc import ABC, abstractmethod
'''
Implement an abstract class called ProductAbstract to have the following method:
create_product
edit_product
get_product_by_id
get_all_products
upload_product_image
delete_product

NB: Note to define parameters as needed

'''
class Product():
    product_name = ''
    product_id =''
    product_image =''

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, name:Product):
        pass

    @abstractmethod
    def edit_product(self):
        pass

    @abstractmethod
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def upload_product_image(self, product_image):
        pass

    @abstractmethod
    def delete_product(self):
        pass


'''

Implement a class called ProductManager to implement ProductAbstract. 
Do note to add implementation for all the abstract methods of the ProductAbstract class

'''

class ProductManager(ProductAbstract):
    def create_product(self, name: Product):
        print(f"Name of Product: {name}")

    def edit_product(self):
        print("This is a new product")

    def get_product_by_id(self, product_id):
        print(f"The product ID is labelled as {product_id}")

    def get_all_products(self):
        print("That's everything in the inventory")

    def upload_product_image(self, product_image):
        print(f"Take clear images and upload. Here is the image: {product_image}")

    def delete_product(self):
        print("Product deleted")                




new_product = ProductManager()
new_product.create_product("Condoms")
new_product.edit_product()
new_product.get_product_by_id("404")
new_product.get_all_products()
new_product.upload_product_image(
    ".../contra.jpeg")
new_product.delete_product()    
