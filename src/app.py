def name2bin(name:str):
    result = "".join(format(ord(element), "08b") for element in name)
    return result

if __name__ == "__main__":
    name = str(input("enter your name: "))
    binThisName = name2bin(name)
    print("your name in binary:", binThisName)
 
