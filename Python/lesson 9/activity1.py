class library:
    def __init__(self, book_list, name):
        self.book_list = book_list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"\nBooks available in {self.name}:")
        for book in self.book_list:
            print(f" - {book}")

    def lendBook(self, user, )