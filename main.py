__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


from models import User, Product, Tag, Transaction


def search(term):
    products = Product.select().where((Product.name.contains(term.lower()) | Product.description.contains(term.lower())))
    # if len(products) > 0:
    for product in products:
        print(product.name)

def list_user_products(user_id):
    ...


def list_products_per_tag(tag_id):
    ...


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...


if __name__ == "__main__":
    # search('pokemon')

    # vraag tags van een product op
    godzilla = Product.get(Product.name == 'Godzilla')
    for tag in godzilla.tags:
        print(tag.name)

    # producten bij een tag op
    design = Tag.get(Tag.name == 'design')
    for product in design.products:
        print(product.name)
    
    # query = Product.select()
    for product in Product.select():
        print(product.name, product.tags)
    
