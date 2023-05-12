print('Bookstore Clerk Management system')

import sqlite3

# Connect to the Database
db = sqlite3.connect("ebookstore.db")

# Create a Cursor object to Execute SQL Commands
cursor = db.cursor()

# Create The book Table

cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, "
               "qty INT)")
# AUTOINCREMENT will ensure that the id values are assigned in ascending order without any gaps

# Insert Data into the Table

cursor.execute("INSERT OR IGNORE INTO books (id, title, author, qty) VALUES (3001, 'A Tale of Two Cities', "
               "'Charles Dickens', 30)")

cursor.execute("INSERT OR IGNORE  INTO books (id, title, author, qty) VALUES (3002, 'Harry Potter and Philosopher''s', "
               "'J.K Rowling', 40)")  # escape the apostrophe within the string using another apostrophe
cursor.execute("INSERT OR IGNORE  INTO books (id, title, author, qty)VALUES (3003, 'The Lion, the witch and the "
               "wardrobe', "
               "'C.S Lewis', 25)")
cursor.execute("INSERT OR IGNORE INTO books (id, title, author, qty)VALUES (3004, 'The Lord of the Rings',"
               "'J.R.R Tolkien', 37)")
cursor.execute("INSERT OR IGNORE  INTO books (id, title, author, qty)VALUES (3005, 'Alice in Wonderland ',"
               "'Lewis Carroll', 12)")


# Define The Main Function that presents the Menu and Handle user input
def main():
    while True:
        # Print The Menu
        print("1. Enter book")
        print("2. Update Book")
        print("3. Delete book")
        print("4. Search Book/s")
        print("0. Exit Menu")

        selection = int(input("Please Enter a number to select from the menu:"))
        if selection == 1:
            enter_book()
        elif selection == 2:
            update_book()
        elif selection == 3:
            delete_book()
        elif selection == 4:
            search_books()
        elif selection == 0:
            # Exit the program
            break


# Define a function to enter a new book
def enter_book():
    # Request Book details from user
    id = int(input("Enter The book's ID: "))
    title = input("Enter The book's tittle: ")
    author = input("Enter the name of the Author: ")
    qty = int(input("Enter the Book's Quantity: "))

    try:
        # Add the book in the database (add a new row)
        cursor.execute(
            "INSERT INTO books (id, title, author, qty) VALUES (?,?,?,?)", (id, title, author, qty))
        print(f'Book name: {title}\n '
              f'with ID: {id} \n'
              f'Written by: {author} \n'
              f'with quantity {qty} \n'
              f'has been added successfully.\n')
    except sqlite3.IntegrityError:
        print(f'The book with ID {id} already exists.')
        choice = input('Do you want to enter a new book? (y/n): ')
        if choice.lower() == 'y':
            enter_book()


# Define a function to update book
def update_book():
    try:
        # Request user to enter book ID, so we find the book and Read through it
        id = int(input("Enter the ID of the Book you wish to update:"))

        # Find the book in the database using the User's Inputted ID
        cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
        book = cursor.fetchone()

        # If the book was not found, display error message
        if book is None:
            print("Book not Found")
            return

        # Print the book's Current details
        print("Current Details ")
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Quantity: {book[3]}")

        # Request user to enter the changes and read the updated details from the user
        title = input("Enter the updated title or enter to leave unchanged:")
        author = input("Enter the updated author or leave unchanged:")
        qty = input("Enter the updated quantity or leave unchanged:")

        # update the book's details in the table
        if title:
            cursor.execute("UPDATE books SET title=? where id=?", (title, id))
        if author:
            cursor.execute("UPDATE books SET author=? where id=?", (author, id))
        if qty:
            qty = int(qty)
            cursor.execute("UPDATE books SET qty=? where id=?", (qty, id))

        db.commit()
        print("Book updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid quantity.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Define the function to delete a book
def delete_book():
    # Request the Book's id from user
    id = int(input("Enter the book's ID:"))

    # Find the book in the table
    cursor.execute("SELECT * FROM books WHERE id =?", (id,))
    book = cursor.fetchone()

    # If book is not found, display the error message and exit the function
    if book is None:
        print("Book not found.")
        return

    # If the book is found Print the details of the book
    print("Current details:")
    print(f"ID: {book[0]}")
    print(f"Title: {book[1]}")
    print(f"Author: {book[2]}")
    print(f"Quantity: {book[3]}")

    # Confirm that the user wants to delete the book
    confirm = input("Are you sure you want to delete this book? (y/n) ")
    if confirm == "y":
        cursor.execute("DELETE FROM books WHERE id=?", (id,))
        db.commit()
        print("Book deleted successfully!")


# Define the function to search for books by ID
def search_books():
    # Read the search criteria from the user
    id = input("Enter the book ID:")

    # Construct the SELECT statement
    query = "SELECT * FROM books WHERE id = ?"

    # Execute the SELECT statement
    try:
        cursor.execute(query, (id,))
        results = cursor.fetchall()
    except sqlite3.Error as e:
        print("Error executing query:", e)
        return

    # Print the search results
    if len(results) == 0:
        print("No matching books found")
    else:
        print(f"Found {len(results)} matching book(s):")
        for book in results:
            print(f"ID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(f"Quantity: {book[3]}")


# Call the main function to start the program
main()
# Close the cursor and connection
cursor.close()
db.close()
