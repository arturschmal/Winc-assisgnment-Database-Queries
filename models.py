# Models go here
from enum import unique
from peewee import *
import peewee

db = peewee.SqliteDatabase('webshop.db', pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    address = CharField()
    bank_account = CharField()


class Tag(BaseModel):
    name = CharField(unique=True)


class Product(BaseModel):
    name = CharField()
    description = CharField()
    price_per_unit = DecimalField(decimal_places=2, auto_round=True)
    quantity = IntegerField()
    seller = ForeignKeyField(User, backref='products')
    tags = ManyToManyField(Tag, backref='products')


class Transaction(BaseModel):
    product = ForeignKeyField(Product)
    quantity = IntegerField()
    buyer = ForeignKeyField(User)


ProductTag = Product.tags.get_through_model()