from ..models.models import Books, Category, Book_category
from playhouse.shortcuts import model_to_dict
from peewee import *

class Controller:
    def create_book(book_obj):
        book = Books(title=book_obj['title'], description=book_obj['description'], price=book_obj['price'], stock=book_obj['stock'])
        book.save()
        return model_to_dict(book)

    def create_category(category_obj):
        category = Category(title=category_obj['title'])
        category.save()
        return model_to_dict(category)
    
    def create_book_category(book_category_obj):
        book_category = Book_category(book_id=book_category_obj['book_id'], category_id=book_category_obj['category_id'])
        book_category.save()
        return model_to_dict(book_category)

    def get_all_books():
        category_fetch = Category.select()
        categories = []
        print(category_fetch)
        for category in category_fetch:
            categories.append(model_to_dict(category))

        book_category_fetch = Book_category.select()
        book_categories = []
        for book_category in book_category_fetch:
            book_categories.append(model_to_dict(book_category))

        book_fetch = Books.select()
        books = []
        for book in book_fetch:
            books.append(model_to_dict(book))

        for book in books:
            book['book_categories'] = []
            for book_category in book_categories:
                if book['id'] == book_category['book_id']['id']:
                    book['book_categories'].append(book_category)
        return books

    def get_all_categories():
        category_fetch = Category.select().join(Book_category).join(Books)
        categories = []
        print(category_fetch)
        for category in category_fetch:
            categories.append(model_to_dict(category))
        return categories

    def get_all_book_categories():
        book_category_fetch = Book_category.select()
        book_categories = []
        for book_category in book_category_fetch:
            book_categories.append(model_to_dict(book_category))
        return book_categories
