class text_reader():
    path = ""
    content = ""
    
    def __init__(self,path):
        self.path = path
        
    def read(self):
        f = open(self.path, "r")
        self.content = f.read() 
        print(f"the content of the file is : \n{self.content}")  
        
    def count_lines(self):
        f = open(self.path, "r")
        print(f"Number of lines is {len(f.readlines())}")
        
    def count_chars(self):
        print(f"Number of characters is {len(self.content)}")
        
    def count_words(self):
        print(f"Number of words is {len(self.content.split(" "))}")        
     
    def display(self):
        print(f"the content of the file is : \n{self.content}")  
        
reader = text_reader("test.txt")   
reader.read()    
reader.count_lines()  
reader.count_chars()
reader.count_words() 
reader.display()