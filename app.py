from flask import Flask, request, jsonify
from playhouse.shortcuts import model_to_dict
from .controller.controllers import Controller

app = Flask(__name__)

@app.post("/create/book")
def create_book():
    book = Controller.create_book(request.json)
    return {"data": book}

@app.post("/create/category")
def create_category():
    categories = Controller.create_category(request.json)
    return {"data": categories}

@app.post("/create/book/category")
def create_book_category():
    book_category = Controller.create_book_category(request.json)
    return {"data": book_category}

@app.get("/books")
def get_books():
    books = Controller.get_all_books()
    return {"data": books}

@app.get("/categories")
def get_categories():
    categories = Controller.get_all_categories()
    return {"data": categories}

@app.get("/book/category")
def get_book_category():
    book_category = Controller.get_all_book_categories()
    return {"data": book_category}