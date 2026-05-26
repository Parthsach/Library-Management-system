from abc import ABC, abstractmethod


# ---------------- PERSON (Parent Class) ----------------
class Person:
    def __init__(self, person_id, name):
        self._id = person_id
        self._name = name

    def display_details(self):
        pass


# ---------------- BOOK CLASS ----------------
class Book:
    def __init__(self, book_id, book_name, author):
        self.__book_id = book_id
        self.__book_name = book_name
        self.__author = author
        self.__available = True

    # Getters
    def get_id(self):
        return self.__book_id

    def get_name(self):
        return self.__book_name

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    # Setter
    def set_availability(self, status):
        self.__available = status

    def display_details(self):
        status = "Available" if self.__available else "Issued"
        print(
            f"ID: {self.__book_id}, Name: {self.__book_name}, "
            f"Author: {self.__author}, Status: {status}"
        )


# ---------------- STUDENT CLASS ----------------
class Student(Person):
    def __init__(self, student_id, name, department):
        super().__init__(student_id, name)
        self.__department = department
        self.__borrowed_books = []

    def borrow_book(self, book):
        if len(self.__borrowed_books) >= 3:
            raise Exception("Student cannot borrow more than 3 books")

        self.__borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.__borrowed_books:
            raise Exception("Student did not borrow this book")

        self.__borrowed_books.remove(book)

    def display_details(self):  # Polymorphism
        print(
            f"Student ID: {self._id}, Name: {self._name}, "
            f"Dept: {self.__department}"
        )

        print("Borrowed Books:")
        for book in self.__borrowed_books:
            print("-", book.get_name())


# ---------------- LIBRARIAN CLASS ----------------
class Librarian(Person):
    def display_details(self):  # Polymorphism
        print(f"Librarian ID: {self._id}, Name: {self._name}")


# ---------------- ABSTRACTION ----------------
class LibraryOperations(ABC):
    @abstractmethod
    def issue_book(self, student_id, book_id):
        pass

    @abstractmethod
    def return_book(self, student_id, book_id):
        pass


# ---------------- LIBRARY CLASS ----------------
class Library(LibraryOperations):
    def __init__(self):
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)

    def add_student(self, student):
        self.students.append(student)

    def view_books(self):
        for book in self.books:
            book.display_details()

    def find_book(self, book_id):
        for book in self.books:
            if book.get_id() == book_id:
                return book
        raise Exception("Book not found")

    def find_student(self, student_id):
        for student in self.students:
            if student._id == student_id:
                return student
        raise Exception("Student not found")

    def issue_book(self, student_id, book_id):
        student = self.find_student(student_id)
        book = self.find_book(book_id)

        if not book.is_available():
            raise Exception("Book already issued")

        student.borrow_book(book)
        book.set_availability(False)

        print("Book issued successfully")

    def return_book(self, student_id, book_id):
        student = self.find_student(student_id)
        book = self.find_book(book_id)

        student.return_book(book)
        book.set_availability(True)

        print("Book returned successfully")


# ---------------- MAIN MENU ----------------
library = Library()

while True:
    print("\n1.Add Book")
    print("2.View Books")
    print("3.Add Student")
    print("4.Issue Book")
    print("5.Return Book")
    print("6.View Student Details")
    print("7.Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            bid = int(input("Book ID: "))
            name = input("Book Name: ")
            author = input("Author: ")

            library.add_book(Book(bid, name, author))
            print("Book added")

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            sid = int(input("Student ID: "))
            name = input("Student Name: ")
            dept = input("Department: ")

            library.add_student(Student(sid, name, dept))
            print("Student added")

        elif choice == "4":
            sid = int(input("Student ID: "))
            bid = int(input("Book ID: "))

            library.issue_book(sid, bid)

        elif choice == "5":
            sid = int(input("Student ID: "))
            bid = int(input("Book ID: "))

            library.return_book(sid, bid)

        elif choice == "6":
            sid = int(input("Student ID: "))
            student = library.find_student(sid)
            student.display_details()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)
