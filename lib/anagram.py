

class Anagram:
    
    def __init__(self, word):        
        self.word = word
    
    def match(self, list):       
       

                
            
            
        return [item for item in list if sorted([letter for letter in self.word]) == sorted([letter for letter in item])]
        
        
    
   
