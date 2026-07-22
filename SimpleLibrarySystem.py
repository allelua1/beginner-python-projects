# Books stored as a list of dictionaries {title, author, available}
# Functions to: borrow, return, search by author
# Track borrowed books in a separate list

books = [{"title": "Computer Programming", "author": "Sifuna", "available": True}]
borrowed_books = []


# function for adding books into library system
def adding_books(books, title, author, available):
    books.append({"title": title, "author": author, "available": available})
    print(f"{title} book added into system")


# function for borrowing books
def borrow_book(books, book_title):
    for book in books:
        if book["title"] == book_title:
            if book["available"]:
                book["available"] = False
                borrowed_books.append(book_title)
                books.remove(book)
                print(f'Book "{book_title}" has been borrowed')
                return
            else:
                print(f'Book "{book_title}" is not available')
                return

    print(f'Book "{book_title}" was not found in the library')


# function for returning books
def return_book(books, book_title, author, available):
    if book_title in borrowed_books:
        books.append({"title": book_title, "author": author, "available": available})
        borrowed_books.remove(book_title)
        print(f"{book_title} has been returned")
    else:
        print(f"this book for {book_title} has not been borrowed")


# function for searching books by author
def search_by_author(books, author):
    matches = [book for book in books if book["author"].lower() == author.lower()]
    if matches:
        print(f"Books by {author}:")
        for book in matches:
            print(f"- {book['title']}")
    else:
        print(f"No books found for author {author}")


print("\nAdding books into system")
adding_books(books, "Python", "Karake", True)
adding_books(books, "Cybersecurity", "Linux", False)

print("\nBorrowed books")
borrow_book(books, "Computer Programming")
borrow_book(books, "Operating System")

print("\nReturned books")
return_book(books, "Computer Programming", "Sifuna", True)
return_book(books, "Cloud Computing", "Bernard", True)

print("\nSearch book by author:")
search_by_author(books, "Sifuna")

