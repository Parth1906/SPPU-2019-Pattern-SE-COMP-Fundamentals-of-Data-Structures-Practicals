'''
GroupA-5
Write a python program to compute following operations on String:
a) To display word with the longest length.
b) To determine the frequency of occurance of particular character in the string
c) To check whether given string is palindrome or not
d) To display the index of first apperance of the substring
e) To count the occurance of each string
'''
def length(sett, length):
    longest=""
    for i in range(0,length):
        if len(longest) <= len(sett(i)):
            longest = sett(i)
        print(longest)
        
        
def occurance(sett, length):
    pass
def check(sett, length):
    pass
def indexcheck(sett, length):
    pass
def count(sett, length):
    pass


if __name__ == "__main__":
    string= input("Enter the string\n")
    length= len(string)
    sett= string.split()
    length(sett, length)
    occurance(sett, length)
    check(sett, length)
    indexcheck(sett, length)
    count(sett, length)
          
