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

class GUISystem(Library):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.root = tk.Tk()
        self.root.title("library system")
        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="library system", font=("arial", 18)).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="list books", command=self.show_books).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(frame, text="add book", command=self.add_book_window).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(frame, text="delete book", command=self.delete_book_window).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(frame, text="view book", command=self.view_book_window).grid(row=1, column=1, padx=10, pady=5)

    def show_books(self):
        books = self.list_books()
        messagebox.showinfo("books in library", "\n".join(books) if books else "no books available.")

    def add_book_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("add book")

        tk.Label(add_window, text="title").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(add_window, text="author").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(add_window, text="year").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(add_window, text="pages").grid(row=3, column=0, padx=5, pady=5)

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
            messagebox.showinfo("success", "book added successfully!")
            add_window.destroy()

        tk.Button(add_window, text="add", command=add).grid(row=4, column=0, columnspan=2, pady=10)

    def delete_book_window(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("delete book")

        tk.Label(delete_window, text="title").grid(row=0, column=0, padx=5, pady=5)
        title_entry = tk.Entry(delete_window)
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        def delete():
            if self.delete_book(title_entry.get()):
                messagebox.showinfo("success", "book deleted successfully!")
            else:
                messagebox.showwarning("error", "book not found!")
            delete_window.destroy()

        tk.Button(delete_window, text="delete", command=delete).grid(row=1, column=0, columnspan=2, pady=10)

    def view_book_window(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("view book")

        tk.Label(view_window, text="title").grid(row=0, column=0, padx=5, pady=5)
        title_entry = tk.Entry(view_window)
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        def view():
            book = self.view_book(title_entry.get())
            if book:
                details = f"title: {book['title']}\nauthor: {book['author']}\nyear: {book['year']}\npages: {book['pages']}"
                messagebox.showinfo("book details", details)
            else:
                messagebox.showwarning("error", "book not found!")
            view_window.destroy()

        tk.Button(view_window, text="view", command=view).grid(row=1, column=0, columnspan=2, pady=10)

    def run(self):
        self.root.mainloop()

# run the application
if __name__ == "__main__":
    gui = GUISystem("books.txt")
    gui.run()
