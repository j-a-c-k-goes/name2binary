class Name():
    def __init__(self, name):
        self.name = name
    def get(self):
        return self.name
    def set(self):
        setName = self.name
        return setName
    def update(self, newName:str):
        self.name = newName
        return self.name
    def _8bit(self, name:str):
        result = "".join(format(ord(element), "08b") for element in name)
        return result
    def _16bit(self, name:str):
        result = "".join(format(ord(element), "16b") for element in name)
        return result

# if __name__ == "__main__":
