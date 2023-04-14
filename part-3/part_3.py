my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_book_list = [
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 4.5,
        "pages": 223
    },
    {
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J.K. Rowling",
        "year": 1998,
        "rating": 4.4,
        "pages": 251
    },
    {
        "title": "Harry Potter and the Prisoner of Azkaban",
        "author": "J.K. Rowling",
        "year": 1999,
        "rating": 4.7,
        "pages": 317
    },
    {
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "year": 2000,
        "rating": 4.5,
        "pages": 636
    },
    {
        "title": "Harry Potter and the Order of the Phoenix",
        "author": "J.K. Rowling",
        "year": 2003,
        "rating": 5,
        "pages": 766
    },
    {
        "title": "Harry Potter and the Half-Blood Prince",
        "author": "J.K. Rowling",
        "year": 2005,
        "rating": 4.9,
        "pages": 672
    },
    {
        "title": "Harry Potter and the Deathly Hallows",
        "author": "J.K. Rowling",
        "year": 2007,
        "rating": 5,
        "pages": 784
    }
]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def parse_book(book_dictionary):
    book_string = f"{book_dictionary['title']} is {book_dictionary['pages']} pages long and was written by {book_dictionary['author']} and published in {book_dictionary['year']} it was given a rating of {book_dictionary['rating']}"
    return book_string

print(parse_book(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def title_parse(book_dictionary):
    return f"{book_dictionary['title']}"

def author_parse(book_dictionary):
    return f"{book_dictionary['author']}"

def year_parse(book_dictionary):
    return f"{book_dictionary['year']}"

def rating_parse(book_dictionary):
    return f"{book_dictionary['rating']}"

def pages_parse(book_dictionary):
    return f"{book_dictionary['pages']}"

print(title_parse(my_book))
print(author_parse(my_book))
print(year_parse(my_book))
print(rating_parse(my_book))
print(pages_parse(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def list_books(book_dictionary_list):
    for book_dictionary in book_dictionary_list:
        print(parse_book(book_dictionary))

list_books(my_book_list)

def get_authors(book_dictionary_list):
    authors = set()

    for book_dictionary in book_dictionary_list:
        authors.add(book_dictionary["author"])

    return authors

print(get_authors(my_book_list))

def total_pages(book_dictionary_list):
    total_pages = 0

    for book_dictionary in book_dictionary_list:
        total_pages += book_dictionary["pages"]

    return total_pages

print(total_pages(my_book_list))