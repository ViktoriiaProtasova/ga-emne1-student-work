book = {"title": "Harry Potter", "author": "J.K. Rowling", "pages": 350, "available": True}

print(f"Title: {book['title']}\nAuthor: {book['author']}")

book['available'] = False
book['year'] = 1997

print(book)