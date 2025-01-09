# Library Management Software  

## Showcase  
Here’s a demonstration of how the calculator looks in action:

![Showcase](Assets/showcase.gif)

## Overview  
This project is part of the **BTEC Level 3 Diploma in Computing - Unit 16: Object-Oriented Programming**. The goal is to design and develop an object-oriented solution for managing a small library system. The application demonstrates key programming principles, including **inheritance**, **polymorphism**, and **method overloading**, while also featuring a **graphical user interface (GUI)** for usability.

---

## Features  
1. **Graphical User Interface (GUI):**  
   - Built using **Tkinter** for an interactive and user-friendly experience.  
   - Includes buttons for listing books, adding books, deleting books, and viewing book details.

2. **Core Functionalities:**  
   - Add a new book to the library.  
   - View details of a specific book by its title.  
   - Delete a book from the library.  
   - List all books currently stored in the library.  

3. **Object-Oriented Design:**  
   - **Base Class:** `Library` handles file operations and core functionalities.  
   - **Derived Class:** `GUISystem` extends the functionality with a Tkinter-based GUI interface.  
   - Demonstrates **inheritance**, **polymorphism**, and **method overloading**.  

4. **File-Based Storage:**  
   - The program reads and writes book data from/to a text file (`books.txt`).  
   - Data is stored in the format:  
     ```
     Title, Author, Year, Page Count
     ```
     Example:  
     ```
     The Great Gatsby, F. Scott Fitzgerald, 1925, 218
     To Kill a Mockingbird, Harper Lee, 1960, 324
     ```

5. **Error Handling:**  
   - Handles cases like missing files or invalid user inputs gracefully.

---

## Technology Stack  
- **Programming Language:** Python  
- **GUI Library:** Tkinter  

---

## File Structure  
- `library.py`: Main program file containing the source code.  
- `books.txt`: File used for storing library data.  
- `README.md`: Documentation for the project.

---

## How to Run the Application  

### Prerequisites  
1. Install **Python 3.x**.  
2. Tkinter (usually pre-installed with Python).  

### Steps to Run  
1. Clone the repository or download the project files.  
2. Ensure there is a `books.txt` file in the same directory. If the file is missing, the program will start with an empty library.  
3. Run the program using the following command:  
   ```bash
   python library.py
   ```  

4. Use the graphical interface to interact with the library:  
   - Click on **List Books** to see all books in the library.  
   - Click on **Add Book** to add a new book. Fill in the details in the popup window and click "Add".  
   - Click on **Delete Book** to remove a book by its title.  
   - Click on **View Book** to see details of a specific book.

---

## Example Output  

### **GUI Overview:**  
When you run the program, the following interface will appear:  

![Library Management GUI](Assets/library_gui.png)  

### **Book Data Example (`books.txt`):**  
```
The Great Gatsby, F. Scott Fitzgerald, 1925, 218
To Kill a Mockingbird, Harper Lee, 1960, 324
1984, George Orwell, 1949, 328
```

### **List Books:**  
A popup will display the following:  
```
Books in Library:
- The Great Gatsby
- To Kill a Mockingbird
- 1984
```

### **View Book Details (Example):**  
If you search for "1984", a popup will display:  
```
Title: 1984  
Author: George Orwell  
Year: 1949  
Pages: 328  
```

---

## Future Enhancements  
- Add search functionality for partial matches.  
- Add sorting options (by title, author, or year).  
- Implement user authentication for library management.  

---

## License  
This project is free to use and distribute for educational purposes.