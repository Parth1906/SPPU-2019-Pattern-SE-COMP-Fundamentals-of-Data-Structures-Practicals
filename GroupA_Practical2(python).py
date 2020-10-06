'''

Experiment Number 2 : Write a python program to store marks stored in subject "Fundamentals of Data Structure" by
                         N students in the class. Write functions to compute following:
                         1. The average score of the class.
                         2. Highest score and lowest score of the class.
                         3. Count of students who were absent for the test.
                         4. Display mark with highest frequency.
'''


# Function for average score of the class

def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            sum+=listofmarks[i]
            count+=1
    avg=sum/count
    print("Total Marks : ", sum)
    print("Average Marks : {:.2f}".format(avg))

#<----------------------------------------------------------------------------------------------------->

# Function for Highest score in the test for the class

def Maximum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Max=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]>Max:
            Max=listofmarks[i]
    return(Max)

#<------------------------------------------------------------------------------------------------------>

# Function for Lowest score in the test for the class

def Minimum(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks[i]!=-999:
            Min=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]<Min:
            Min=listofmarks[i]
    return(Min)

#<------------------------------------------------------------------------------------------------------->

# Function for counting the number of students absent for the test

def absentcount(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if listofmarks[i]==-999:
            count+=1
    return(count)

#<------------------------------------------------------------------------------------------------------->

# Function for displaying marks with highest frequency
def maxFrequency(listofmarks):
    i=0
    Max=0
    print("Marks  |  Frequency")
    for j in listofmarks:
        if (listofmarks.index(j)==i):
            print(j,"    |  ",listofmarks.count(j))
            if listofmarks.count(j)>Max:
                Max=listofmarks.count(j)
                mark=j
        i=i+1
    return(mark,Max)


#<------------------------------------------------------------------------------------------------------->

# Main function

marksinFDS=[]
numberofstudents=int(input("Enter total number of students : "))
for i in range(numberofstudents):
    marks=int(input("Enter marks of student "+str(i+1)+" : "))
    marksinFDS.append(marks)

flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. Total and Average Marks of the Class")
    print("2. Highest and Lowest Marks in the Class")
    print("3. Number of Students absent for the test")
    print("4. Marks with Highest Frequency")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        average(marksinFDS)
        a = input("Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==2:
        print("Highest Score in Class : ", Maximum(marksinFDS))
        print("Lowest Score in Class : ", Minimum(marksinFDS))
        a = input("Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==3:
        print("Number of Students absent in the test : ", absentcount(marksinFDS))
        a = input("Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==4:
        mark,fr = maxFrequency(marksinFDS)
        print("Highest frequency is of marks {0} that is {1} ".format(mark,fr))
        a = input("Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==5:
        flag=0
        print("Thanks for using this program!")

    else:
        print("!!Wrong Choice!! ")
        a=input("Do you want to continue (yes/no) :")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program!")

#<---------------------------------------------END OF PROGRAM--------------------------------------->



