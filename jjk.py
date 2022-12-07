
def length(sett, length):
    longest=""
    for i in range(0,length):
        if len(longest) <= len(sett(i)):
            longest = sett(i)
        print(longest)
        
        
def occurance():
    pass
def check():
    pass
def indexcheck():
    pass
def count():
    pass


if __name__ == "__main__":
    string= input("Enter the string\n")
    length= len(string)
    sett= string.split()
    length(sett, length)
    occurance()
    check()
    indexcheck()
    count()
          
