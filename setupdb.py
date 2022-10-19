import peewee
import models
from models import *
import os


def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "webshop.db")
    if os.path.exists(database_path):
        os.remove(database_path)


def populate_test_database(models):

    # open de database connectie
    models.db.connect()

    # maak de tabellen aan
    db.create_tables([
                        User, 
                        Product, 
                        Tag, 
                        Transaction,
                        ProductTag
                    ])
    
    
    # maak users aan
    artur = User.create(
        name = 'Artur',
        address = 'Dorpsstraat 1, 0101AB, Amsterdam',
        bank_account = 'NL00ABCD0123456789')

    fatma = User.create(
        name = 'Fatma',
        address = 'Middenweg 10, 1100CD, Haarlem',
        bank_account = 'NL00ABCD9876543210')

    mete = User.create(
        name = 'Mete',
        address = 'Schoolsteeg 15, 0011AC, Leiden',
        bank_account = 'NL00ABCD0123987456')

    sena = User.create(
        name = 'Sena',
        address = 'Stadsplein 20, 1111DD, Den Haag',
        bank_account = 'NL00ABCD0258741963')

    
    # maak tags aan
    hout = Tag.create(name='hout')
    monster = Tag.create(name='monster')
    pokemon = Tag.create(name='pokemon')
    trui = Tag.create(name='trui')
    poster = Tag.create(name='poster')
    design = Tag.create(name='design')
    letters = Tag.create(name='letters')
    sieraden = Tag.create(name='sieraden')
    goud = Tag.create(name='goud')
    comic = Tag.create(name='comic')
    telefoonhoes = Tag.create(name='telefoonhoes')
    vilt = Tag.create(name='vilt')
    manga = Tag.create(name='manga')
    

    # maak producten aan
    godzilla = Product.create(
        name = 'Godzilla',
        description = 'Godzilla gemaakt van hout. Hoogte 30 cm.',
        price_per_unit = 21.50,
        quantity = 5,
        seller = mete
        )

    pokemon_trui = Product.create(
        name = 'Pokemon sweater',
        description = 'Pokemon sweater van hoge kwaliteit katoen. Verkrijgbaar in S/M/L.',
        price_per_unit = 49.95,
        quantity = 4,
        seller = mete
        )

    zeefdruk = Product.create(
        name = 'Typografische poster',
        description = 'Zeefdruk met typografisch design. Formaat A1',
        price_per_unit = 80.00,
        quantity = 2,
        seller = artur
        )

    alfabet = Product.create(
        name = 'New Serif',
        description = 'Alfabet gemaakt van houtblokken',
        price_per_unit = 39.95,
        quantity = 2,
        seller = artur
        )

    ketting = Product.create(
        name = 'Ketting',
        description = 'Gouden ketting',
        price_per_unit = 89.95,
        quantity = 6,
        seller = fatma)

    armband = Product.create(
        name = 'Armband',
        description = 'Gouden armband',
        price_per_unit = 59.95,
        quantity = 4,
        seller = fatma
        )

    stripverhaal = Product.create(
        name = 'Manga comic',
        description = 'Manga comic getekend met inkt en verf',
        price_per_unit = 12.95,
        quantity = 2,
        seller = sena
        )

    iPhone_hoes = Product.create(
        name = 'iPhone hoes',
        description = 'Beschermhoes voor iPhone 12. Gemaakt van vilt',
        price_per_unit = 18.75,
        quantity = 4,
        seller = sena
        )
    

    # maak many to many relatie aan tussen producten en tags
    godzilla.tags.add([hout, monster])
    pokemon_trui.tags.add([pokemon, trui])
    zeefdruk.tags.add([poster, design])
    alfabet.tags.add([letters, design])
    ketting.tags.add([sieraden, goud])
    armband.tags.add([sieraden, goud])
    stripverhaal.tags.add([comic, design, manga])
    iPhone_hoes.tags.add([telefoonhoes, vilt])

    # sluit de database connectie
    models.db.close()
    


if __name__ == "__main__":
    delete_database()
    populate_test_database(models)