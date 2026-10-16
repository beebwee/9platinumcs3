#Code

class Publication:
    def __init__(self, title, author): #This initializes the attributes once a class is made.
        self.__title = title #This is attribute 1.
        self.__author = author #This is attribute 2.

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(title):
        if isinstance(title, str) and len(title.strip()) > 0:
            self.__title = title

    def set_author(author):
        if isinstance(author, str) and len(author.strip()) > 0:
            self.__author = author

    def display_info(self):
        print(f"Title: {self.get_title()}")
        print(f"Author: {self.get_author()}")


class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = number_pages

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        if number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.get_number_of_pages()}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.get_issue_number()}")


#These are the created objects.
pub1 = Publication("Philippines Journal of Science (PJS)", "Many Authors")
book1 = Book("Percy Jackson and the Olympians: The Lightning Thief", "Rick Riordan", 377)
mag1 = Magazine("Smithsonian", "Smithsonian Institution", 400)

print("Publication Information: ")
pub1.display_info()

print("\nBook Information: ")
book1.set_number_of_pages(-337)
book1.display_info()

print("\nMagazine Information: ")
mag1.set_issue_number(400)
mag1.display_info()
