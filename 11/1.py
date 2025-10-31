class Publication:
    def __init__(self, name):
        self.name = name
        
    def print_information(self):
        print(self.name)
    
class Book(Publication):
    def __init__(self, name, author, pages):
        self.author = author
        self.pages = pages
        super().__init__(name)
        
    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.pages}")
      
class Clip(Publication):
    def __init__(self, name, editorchief):
        self.editorchief = editorchief
        super().__init__(name)
        
    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.editorchief}")
    
publications = []
publications.append(Clip("Donald Duck", "Aki Hyyppä"))
publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))

publications[0].print_information()
print()
publications[1].print_information()