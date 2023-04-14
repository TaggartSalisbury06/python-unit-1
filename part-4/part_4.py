### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# title = input("Whats the title of the book you would like to add? - ")
# author = input("Who is the author of the book you would like to add? - ")
# year = input("What year was this book published? - ")
# rating = input("What rating out of 5 would you give this book? - ")
# pages = input("How many pages are in this book? - ")

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def create_new_book():
#   title = input("Whats the title of the book you would like to add? - ")
#   author = input("Who is the author of the book you would like to add? - ")
#   year = int(input("What year was this book published? - "))
#   rating = float(input("What rating out of 5 would you give this book? - "))
#   pages = int(input("How many pages are in this book? - "))

#   book = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#   return book

# print(create_new_book())
### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

# def create_new_book():
#   title = input("Whats the title of the book you would like to add? - ")
#   author = input("Who is the author of the book you would like to add? - ")
#   try:
#     year = int(input("What year was this book published? - "))
#   except:
#     year = int(input("Please type a number for the year. - "))
#   try:
#     rating = float(input("What rating out of 5 would you give this book? - "))
#   except:
#     rating = float(input("Give a number for the rating. - "))
#   try:
#     pages = int(input("How many pages are in this book? - "))
#   except:
#     pages = int(input("Put a number for the amount of pages. - "))

#   book = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#   return book

# print(create_new_book())


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# def main_menu(books):
#   choice = input(" - If you would like to add a book type 'add book'\n  - If you would like to search a book type the name of the book\n - If you would like to see all book type 'all books'\n - If you would like to exit type 'exit'. - ")

#   if choice == "add book":
#     books.append(create_new_book())
#   elif choice == f"{books['title']}":
#     print(choice)
#   elif choice == "all books":
#     print_list(books)
#   elif choice == "exit":
#     print("\nGoodbye")
#     active = False

# main_menu(books)
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

fav_books = [
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997,
        "rating": 4.5,
        "pages": 309
    },
    {
        "title": "Twilight",
        "author": "Stephenie Meyer",
        "year": 2005,
        "rating": 3.6,
        "pages": 498
    },
    {
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "year": 2012,
        "rating": 4.2,
        "pages": 313
    },
    {
        "title": "Divergent",
        "author": "Veronica Roth",
        "year": 2011,
        "rating": 4.2,
        "pages": 487
    }
]

def create_new_book():
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

  book = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

  return book

def print_list(books):
  for book in books:

    print(f" Title: {book['title']}\n Author: {book['author']}\n Year: {book['year']}\n Rating: {book['rating']}\n Page Count: {book['pages']}\n -----------------")

def main_menu(books):

  active = True

  while active:

    choice = input(" - If you would like to add a book type 'add book'\n - If you would like to search a book type the name of the book\n - If you would like to see all book type 'all books'\n - If you would like to exit type 'exit'. - ")

    if choice == "add book":
      books.append(create_new_book())
    elif choice == "all books":
      print_list(books)
    elif choice == "exit":
      print("\nGoodbye")
      active = False

main_menu(fav_books)