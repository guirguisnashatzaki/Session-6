class UserExtractor:
    
    path = ""
    content = {}
    
    def __init__(self, file_path):
        self.path = file_path

    def read_txt_file(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                content = file.readlines()
                for record in content:
                    self.content[record.split(":")[0]] = record.split(":")[1]
                print(self.content)    
            
        except FileNotFoundError:
            print(f"Error: The file '{self.path}' was not found.")
        except IOError:
            print("Error: An error occurred while reading the file.")
            
            
            
extractor = UserExtractor("test.txt")

extractor.read_txt_file()            
            
