from peewee import *

db = MySQLDatabase('asia_quest_test', user='root', password='', host='127.0.0.1', port=3306)

class BaseModel(Model):
    class Meta:
        database = db

class Books(BaseModel):
    id: int = AutoField(primary_key=True)
    title: str = CharField()
    description: str = CharField()
    price: int = IntegerField()
    stock: int = IntegerField()

class Category(BaseModel):
    id: int = AutoField(primary_key=True)
    title: str = CharField()

class Book_category(BaseModel):
    id: int = AutoField(primary_key=True)
    book_id: int = ForeignKeyField(Books, backref='book_category')
    category_id: int = ForeignKeyField(Category, backref='book_category')
    