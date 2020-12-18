# Turning the txt file into a list
fp = open('bestsellers2.txt')
all_books = []
for line in fp:
    book_list = line.split('\t')
    all_books.append(book_list)
# For book in all_books:
#   print(book)

# Converting date string into its date form
from datetime import datetime
for book in all_books:
    book_date = book[3]
    book_date = datetime.strptime(book_date, '%m/%d/%Y').date()
    book[3] = book_date

# Search by title function
def search_by_title():
    title = input("Enter a title: ")
    title = title.replace(" ", "")
    any_output = False
    for book in all_books:
        if title.lower() in book[0].lower():
            book[3] = book[3]
            any_output = True
            a = str(book)
            b = a.replace("'", "").replace("[", "").replace("]", "")
            print(b)
    if any_output is False:
        print("nothing found")
        
# Search by author function
def search_by_author():
    author = input("Enter an author's name: ")
    author = author.replace(" ", "")
    any_output = False
    for book in all_books:
        if author.lower() in book[1].lower():
            book[3] = book[3]
            any_output = True
            a = str(book)
            b = a.replace("'", "").replace("[", "").replace("]", "")
            print(b)
    if any_output is False:
        print('nothing found')

# Search by year range function
def search_by_year_range():
    while True:
        try:
            y_1 = int(input("Enter beginning year: "))
            y_2 = int(input("Enter ending year: "))
        except ValueError:
            print("Oops!  That was not a valid input.  Try again...")
        else:
            break
    time_range = list(range(y_1, y_2 + 1))
    any_output = False
    print(f"All Titles between {y_1} and {y_2} are: ")
    for book in all_books:
        book_year = book[3].year
        if book_year in time_range:
            book[3] = book[3]
            any_output = True
            a = str(book)
            b = a.replace("'", "").replace("[", "").replace("]", "")
            print(b)
    if any_output is False:
        print('nothing found')

# Search engine for month/year
def search_by_month_year():
    while True:
        try:
            month = int(input("enter a month in number: "))
            year = int(input("enter a year: "))
        except ValueError:
            print("Oops!  That was not a valid input.  Try again...")
        else:
            break
    any_output= False
    print(f"All Titles in month {month} of {year} :")
    for book in all_books:
        book_year = book[3].year
        book_month = book[3].month
        if month == book_month and year == book_year:
            book[3] = book[3]
            any_output= True
            a = str(book)
            b = a.replace("'", "").replace("[", "").replace("]", "")
            print(b)
    if any_output is False:
            print("nothing found")

# Asking the user for input and display output
import sys
while True:
 question = str(input("What would you like to do?:\n1: Search for title\n2: Search for author\n"
                      "3: Look up year range\n4: Look up month/year\nQ:Quit\n>"))
 if question == '1':
    search_by_title()
 elif question == '2':
    search_by_author()
 elif question == '3':
    search_by_year_range()
 elif question == '4':
    search_by_month_year()
 elif question == "Q" or question == "q":
    print('Goodbye')
    sys.exit()
 else:
    print('Please select from the options in the menu')
