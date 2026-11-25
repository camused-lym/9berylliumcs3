class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.number_of_pages = number_pages
    def get_number_of_pages(self):
        return self.number_of_pages
    def set_number_of_pages(self, number_pages):
        if number_pages > 0:
            self.number_of_pages = number_pages
        else:
            print("Number of pages must be positiv")
    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.number_of_pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
    def get_issue_number(self):
        return self.issue_number
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.issue_number = issue_number
        else:
            print("Issue number must be positive")
    def display_info(self):
        super().display_info()
        print(f"Issue number: {self.issue_number}")
