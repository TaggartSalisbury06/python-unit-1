### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

def create_new_book(book_list):
  title = input("Whats the title of the book you would like to add? - ")
  author = input("Who is the author of the book you would like to add? - ")
  try:
    year = int(input("What year was this book published? - "))
  except:
    year = int(input("Please type a number for the year. - "))
  try:
    rating = float(input("What rating out of 5 would you give this book? - "))
  except:
    rating = float(input("Give a number for the rating. - "))
  try:
    pages = int(input("How many pages are in this book? - "))
  except:
    pages = int(input("Put a number for the amount of pages. - "))
  
  with open(book_list, "a") as file:
    file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
# def books_display(book_list):
#   with open(book_list, "r") as f:
#     file = f.readlines()

#     for line in file:
#       title, author, year, rating, pages = line.split(", ")

#       book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": int(year),
#         "rating": float(rating),
#         "pages": int(pages)
#       }

#   print_list(book_list)



### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script



### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


def get_all_books_as_dictionary(book_file):

  book_list = []
  with open(book_file, "r") as f:
    file = f.readlines()
    for line in file:
      title, author, year, rating, pages = line.split(", ")
      book_list.append({
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
      })
  return book_list

def get_a_book(book):
  print(f"""
  Title: {book['title']}
  Author: {book['author']} 
  Year: {book['year']}
  Rating: {book['rating']}
  Page Count: {book['pages']}
  """)

def get_all_books(book_file):
  for books in get_all_books_as_dictionary(book_file):
    get_a_book(books)

def get_highest_rated(book_file):
  with open(book_file, "r") as f:
    lines = f.readlines()

  books = []

  for line in lines:
    title, author, year, rating, pages =  line.split(", ")
    book = {
      "title": title,
      "author": author,
      "year": year,
      "rating": rating,
      "pages": pages
    }

    books.append(book)

  sorted_books = sorted(books, key=lambda x: x["rating"], reverse=True)

  for book in sorted_books:
    print(f"""
    Title: {book['title']}
    Author: {book['author']}
    Year: {book['year']}
    Rating: {book['rating']}
    Pages: {book['pages']}
    """)

def total_pages(book_file):
  book_list = []
  with open(book_file, "r") as f:
    file = f.readlines()
    for line in file:
      title, author, year, rating, pages = line.split(", ")
      book_list.append({
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": int(pages)
      })

  total_pages = 0

  for books in book_list:
    total_pages += books["pages"]
  
  print(f"""
  Your library has a total of {total_pages} pages
  """)


def main_menu(book_file):
  active = True

  while active:
    choice = input("""
    If you want create a book type 1
    If you want all books type 2
    If you want to your total page count type 3
    If you want to see the books ranked heighest to lowest type 4
    Type 5 to exit the library
    What will it be, type here: """)

    if choice == "1":
      create_new_book(book_file)
    elif choice == "2":
      get_all_books(book_file)
    elif choice == "3":
      total_pages(book_file)
    elif choice == "4":
      get_highest_rated(book_file)
    elif choice == "5":
      print(""" 
      GoobBye
      """)
      active = False

if __name__ == '__main__':
  main_menu("library.txt")