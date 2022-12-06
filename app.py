from flask import Flask, jsonify, request, render_template

import functions

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False

@app.route('/books')
def read_books():
	return jsonify(functions.get_books())

@app.route('/books/<int:book_id>')
def read_book(book_id):
	return jsonify(functions.get_book_by_id(book_id))

@app.route('/books', methods=['POST'])
def create_book():
	book = {}
	post_data = request.json
	book["title"] = post_data.get("title")
	book["author"] = post_data.get("author")
	book["year"] = post_data.get("year")
	book_created = functions.add_book(book)
	return jsonify(book_created)

@app.route('/books/‹int:book_id›', methods=['PUT'])
def update_book(book_id):
	book = functions.get_book_by_id(book_id)
	post_data = request.json
	book["title"] = post_data.get("title")
	book["author"] = post_data.get("author")
	book["year"] = post_data.get("year")
	functions.update_book(book_id, book)
	return jsonify(book)


@app.route('/books/‹int:book_id›', methods=['DELETE'])
def delete_book(book_id):
	functions.delete_book(book_id)
	return ""

if __name__ == '__main__':
	app.run(debug=True)