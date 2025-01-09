
class Alphabet:
    def __init__(self):
        self.letters = [chr(i) for i in range(65, 91)]  
        self.index = 0  
    
    def __iter__(self):
        self.index = 0 
        return self  
    
    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration  

alphabet = Alphabet()

for letter in alphabet:
    print(letter)
