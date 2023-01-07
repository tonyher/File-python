


class Write:
    def __init__(self):
        self.text = " "
        
    def writeInFile(self):
        
        while True:
            self.text = input("Enter anything you want:")
            self.writeInline()
            
    
    def writeInline(self):
        f = open('file.txt', "a")
        f.writelines(self.text)
        f.writelines("\n")
        f.close()

Ok = Write()
Ok.writeInFile()