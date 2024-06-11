class Author:
    def __init__(self,author_name,book_name,pages):
        self.author_name=author_name
        self.book_name=book_name
        self.pages=pages
    

    #__len__ => back method for length function
    def __len__(self):
        return self.pages
    
    #__str__ => represents string version of object when object is printed
    def __str__(self):
        return f"{self.book_name} by {self.author_name}"
    
    #__call__ => to call an object as a method
    def __call__(self):
        print('call object')
    
author=Author('Jenny','Python basics to advance',300)
print(author)
print('-' * 50)
# print('-' * 50)
print(len(author))
print('-' * 50)
author()