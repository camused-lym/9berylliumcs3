class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def GetTitle(self):
        return self.title
    def GetAuthor(self):
        return self.author
    def SetTitle(self, newtitle):
        self.title = newtitle
    def SetAuthor(self, newauthor):
        self.author = newauthor
    def DisplayInfo(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Book(Publication):
    def __init__(self, title, author, numberpages):
        super().__init__(title, author)
        self.numberpages = numberpages
    def GetNumberOfPages(self):
        return self.numberpages
    def SetNumberOfPages(self, newpages):
        if newpages > 0:
            self.numberpages = newpages
        else:
            print("Number of pages must be positiv")
    def DisplayInfo(self):
        super().DisplayInfo()
        print(f"Number of pages: {self.numberpages}")


class Magazine(Publication):
    def __init__(self, title, author, issuenumber):
        super().__init__(title, author)
        self.issuenumber = issuenumber
    def GetIssueNumber(self):
        return self.issuenumber
    def SetIssueNumber(self, newissue):
        if newissue > 0:
            self.issuenumber = newissue
        else:
            print("Issue number must be positive")
    def DisplayInfo(self):
        super().DisplayInfo()
        print(f"Issue number: {self.issuenumber}")


public = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
public.DisplayInfo()

print("\nBook Information:")
book.DisplayInfo()

print("\nMagazine Information:")
mag.DisplayInfo()
