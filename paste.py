from arrow import Arrow

class Paste:
    Author: str
    Title: str
    Content: str
    Date: str

    def __init__(self, author:str, title: str, content:str, datetime:str):
        self.Author = author
        self.Title = title
        self.Content = content
        self.Date = datetime
        