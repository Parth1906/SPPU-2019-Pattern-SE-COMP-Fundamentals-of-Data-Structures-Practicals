'''
GroupA-5
Write a python program to compute following operations on String:
a) To display word with the longest length.
b) To determine the frequency of occurance of particular character in the string
c) To check whether given string is palindrome or not
d) To display the index of first apperance of the substring
e) To count the occurance of each string
'''

#This will return longest length
def length(sett, length):
    longest=""
    for i in range(0,length):
        if len(longest) <= len(sett(i)):
            longest = sett(i)
        print(longest)
        
        
#Returns the frequency of particular char
def occurance(sett, length):
    return 0

# This will check Palindrome
def check(string, length):
    palin=[]
    for i in range(length, 0, -1):
        palin.append(string[i])
    string2= " ".join(palin)
    if string == string2:
        print("It is palindrome")
    else:
        print("It is not a palindrome")
        
# It will return the index of substring
def indexcheck(sett, length):
    substring= input("Enter a substring")
    for i in range(0,length):
        if sett[i] == substring:
            print(i)
            return 0


#Count occurance of each string
def count(sett, length):
    return 0


if __name__ == "__main__":
    string= input("Enter the string\n")
    length= len(string)
    sett= string.split()
    length(sett, length)
    occurance(sett, length)
    check(sett, length)
    indexcheck(sett, length)
    count(sett, length)
          
