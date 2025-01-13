import os
import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                for line in file:
                    title, author, year, pages = line.strip().split(", ")
                    self.books.append({
                        "title": title,
                        "author": author,
                        "year": year,
                        "pages": pages
                    })
        else:
            print("file not found. starting with an empty library.")

    def save_books(self):
        with open(self.file_name, "w") as file:
            for book in self.books:
                file.write(f'{book["title"]}, {book["author"]}, {book["year"]}, {book["pages"]}\n')

    def list_books(self):
        return [book["title"] for book in self.books]

    def view_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None

    def add_book(self, title, author, year, pages):
        self.books.append({
            "title": title,
            "author": author,
            "year": year,
            "pages": pages
        })
        self.save_books()

    def delete_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                return True
        return False

class DigitalLibrary(Library):
    def add_book(self, title, author, year, pages, file_format):
        self.books.append({
            "title": title,
            "author": author,
            "year": year,
            "pages": pages,
            "file_format": file_format
        })
        self.save_books()

    def view_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None

class GUISystem(Library):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.root = tk.Tk()
        self.root.title("Library System")
        self.create_ui()

    def create_ui(self):
        self.root.geometry("400x200")  # set the initial window size
        tk.Label(self.root, text="Library System", font=("Arial", 18)).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="List Books", command=self.show_books).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame, text="Add Book", command=self.add_book_window).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(frame, text="Delete Book", command=self.delete_book_window).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(frame, text="View Book", command=self.view_book_window).grid(row=1, column=1, padx=10, pady=5)

    def show_books(self):
        books = self.list_books()
        if not books:
            messagebox.showinfo("Books in Library", "No books available.")
            return

        # create a new window to display the books
        books_window = tk.Toplevel(self.root)
        books_window.title("Books in Library")
        books_window.geometry("300x400")

        tk.Label(books_window, text="Books", font=("Arial", 16)).pack(pady=10)

        # create a frame for the book list
        list_frame = tk.Frame(books_window)
        list_frame.pack(fill=tk.BOTH, expand=True)

        # add a scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # create a listbox with the scrollbar
        listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=20, width=40)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # configure the scrollbar to work with the listbox
        scrollbar.config(command=listbox.yview)

        # populate the listbox with book titles
        for book in books:
            listbox.insert(tk.END, book)

        def open_book_details(event):
            # get the selected book title
            selected_book = listbox.get(tk.ANCHOR)
            if selected_book:
                book = self.view_book(selected_book)
                if book:
                    # open a new window showing the book details
                    details_window = tk.Toplevel(self.root)
                    details_window.title(f"Details of {book['title']}")
                    details_window.geometry("300x200")

                    # display book details
                    details_text = (
                        f"Title: {book['title']}\n"
                        f"Author: {book['author']}\n"
                        f"Year: {book['year']}\n"
                        f"Pages: {book['pages']}"
                    )
                    tk.Label(details_window, text=details_text, justify=tk.LEFT, font=("Arial", 12)).pack(pady=20)
                else:
                    messagebox.showwarning("Error", "Book not found!")

        # bind a double-click event to open the details of the selected book
        listbox.bind("<Double-1>", open_book_details)

    def add_book_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Book")

        tk.Label(add_window, text="Title").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Author").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Year").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(add_window, text="Pages").grid(row=3, column=0, padx=5, pady=5)

        title_entry = tk.Entry(add_window)
        author_entry = tk.Entry(add_window)
        year_entry = tk.Entry(add_window)
        pages_entry = tk.Entry(add_window)

        title_entry.grid(row=0, column=1, padx=5, pady=5)
        author_entry.grid(row=1, column=1, padx=5, pady=5)
        year_entry.grid(row=2, column=1, padx=5, pady=5)
        pages_entry.grid(row=3, column=1, padx=5, pady=5)

        def add():
            self.add_book(title_entry.get(), author_entry.get(), year_entry.get(), pages_entry.get())
            messagebox.showinfo("Success", "Book added successfully!")
            add_window.destroy()

        tk.Button(add_window, text="Add", command=add).grid(row=4, column=0, columnspan=2, pady=10)

    def delete_book_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Book")

        tk.Label(delete_window, text="Title").grid(row=0, column=0, padx=5, pady=5)
        title_entry = tk.Entry(delete_window)
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        def delete():
            if self.delete_book(title_entry.get()):
                messagebox.showinfo("Success", "Book deleted successfully!")
            else:
                messagebox.showwarning("Error", "Book not found!")
            delete_window.destroy()

        tk.Button(delete_window, text="Delete", command=delete).grid(row=1, column=0, columnspan=2, pady=10)

    def view_book_window(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Book")

        tk.Label(view_window, text="Title").grid(row=0, column=0, padx=5, pady=5)
        title_entry = tk.Entry(view_window)
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        def view():
            book = self.view_book(title_entry.get())
            if book:
                details = f"Title: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nPages: {book['pages']}"
                messagebox.showinfo("Book Details", details)
            else:
                messagebox.showwarning("Error", "Book not found!")
            view_window.destroy()

        tk.Button(view_window, text="View", command=view).grid(row=1, column=0, columnspan=2, pady=10)

    def run(self):
        self.root.mainloop()

# run the application
if __name__ == "__main__":
    gui = GUISystem("books.txt")
    gui.run()
