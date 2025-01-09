import os

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
        if not self.books:
            print("no books in the library.")
        else:
            print("library books:")
            for book in self.books:
                print(f"- {book['title']} by {book['author']}")

    def view_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None

# test functionality
if __name__ == "__main__":
    library = Library("books.txt")
    library.list_books()
    print("details:", library.view_book("title of first book"))
