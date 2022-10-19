__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"


from models import User, Product, Tag, Transaction


def search(term):
    # formuleer de queries
    products = (Product.select()
                .where((Product.name.contains(term.lower())
                | Product.description.contains(term.lower()))))

    tags = (Tag.select()
            .where(Tag.name.contains(term.lower())))

    users = (User.select()
            .where(User.name.contains(term.lower())))

    # check of de queries resultaten opleveren en itereer daar vervolgens over
    if len(products) > 0:
        for product in products:
            print(product.name)
    elif len(tags) > 0:
        for tag in tags:
            for product in tag.products:
                print(product.name)
    elif len(users) > 0:
        for user in users:
            for product in user.products:
                print(product.name)
    else:
        print('Geen producten gevonden')


def list_user_products(user_id):
    user_products = User.select().where(User.id == user_id)
    for user in user_products:
        for product in user.products:
            print(product.name)


def list_products_per_tag(tag_id):
    tag_products = Tag.select().where(Tag.id == tag_id)
    for tag in tag_products:
        for product in tag.products:
            print(product.name)


def add_product_to_catalog(user_id, product):
    Product.create(
        name = product['name'],
        description = product['description'],
        price_per_unit = product['price_per_unit'],
        quantity = product['quantity'],
        seller = user_id
        )
    verkoper = User.select().where(User.id == 1).get()
    print(f'{product["name"]} toegevoegd aan producten van {verkoper.name}')



def update_stock(product_id, new_quantity):
    update_product = Product.select().where(Product.id == product_id).get()
    update_product.quantity = new_quantity
    update_product.save()

    print(update_product.name, update_product.quantity)


def purchase_product(product_id, buyer_id, quantity):
    product = Product.get_by_id(product_id)
    current_quantity = product.quantity
    buyer = User.get_by_id(buyer_id)

    if current_quantity >= quantity:
        Transaction.create(
            product = product.id,
            quantity = quantity,
            buyer = buyer.id
        )
    else:
        print(f'{product.name} is niet op voorraad')

    new_quantity = current_quantity - quantity

    update_stock(product.id, new_quantity)


def remove_product(product_id):
    product = Product.get(Product.id == product_id)
    product.delete_instance(recursive=True)
    print(f'{product.name} is verwijderd uit de webshop')



if __name__ == "__main__":
    search('Sena')
    print('\n')
    
    list_user_products(1)
    print('\n')
    
    list_products_per_tag(6)
    print('\n')
    
    product = {'name': 'Poster', 'description': 'Supervette poster', 'price_per_unit': 24.95, 'quantity': 5}
    add_product_to_catalog(2, product)
    print('\n')

    update_stock(8, 2)
    print('\n')

    purchase_product(2, 4, 3)
    print('\n')

    remove_product(1)
