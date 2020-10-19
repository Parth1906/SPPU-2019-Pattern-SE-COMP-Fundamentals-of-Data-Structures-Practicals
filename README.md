# SPPU-2019-Pattern-SE-COMP-Fundamentals-of-Data-Structures-Practicals

GroupA_Practical1(python) : 
Experiment No. 1 : In a second year computer engineering class, group A students play cricket, group B students play
                   badminton and group C students play football.
                   Write a python program using functions to compute following:
                   a) List of students who play both cricket and badminton.
                   b) List of students who play either cricket or badminton but not both.
                   c) Number of students who play neither cricket nor badminton.
                   d) Number of students who play cricket and football but not badminton.
(NOTE : While realising the group, duplicate entries should be avoided. Do not use SET built-in functions)



GroupA_Practical2(python) :
Experiment Number 2 : Write a python program to store marks stored in subject "Fundamentals of Data Structure" by
                         N students in the class. Write functions to compute following:
                         1. The average score of the class.
                         2. Highest score and lowest score of the class.
                         3. Count of students who were absent for the test.
                         4. Display mark with highest frequency.
                         
                         
                         
GroupA_Practical7(python) :
Experiment No. 7 : Write a python program for MAGIC SQUARE.
                   A magic square is an n*n matrix of the integers 1 to (n^2) such that the sum of each row,
                   column and diagonalis the same.
                   The figure given below is an example of the magic square for case n=5. In this example
                   the common sum is 65.

                   9  |   3  |  22  |  16  |  15  |
                   2  |  21  |  20  |  14  |   8  |
                  25  |  19  |  13  |   7  |   1  |
                  18  |  12  |   6  |   5  |  24  |
                  11  |  10  |   4  |  23  |  17  |

Conditions for placing the values in the matrix in appropriate manner (CIRCULAR ARRAY) :

   1. The position of next number is calculated by decrementing row number of previous number by 1, and incrementing
      the column number of previous number by 1. At any time, if the calculated row position becomes -1, it will wrap
      around to n-1. Similarly, if the calculated column position becomes n, it will wrap around to 0.

   2. If the magic square already contains a number at the calculated position, calculated column position will be
      decremented by 2, and calculated row position will be incremented by 1.

   3. If the calculated row position is -1 & calculated column position is n, the new position would be: (0, n-2).
   
   
   
GroupB_Practical13(python) :
Experiment No. 13 : Write a python program to maintain club members, sort on roll numbers in ascending order.
                    Write function “Ternary_Search” to search whether particular student is member of club or not.
                    Ternary search is modified binary search that divides array into 3 halves instead of two.
                    
                    
                    
GroupB_Practical14(python) :
Experiment Number 14: Write a python program to store first year percentage of students in an array.
                      Write function for sorting array of floating point numbers in ascending order using:
                      a) Selection Sort
                      b) Bubble Sort and display top five scores



GroupB_Practical16(python) :
Experiment No. 16 : Write a python program to store first year percentage of students in array.
                    Write function for sorting array of floating point numbers in ascending order using
                    quick sort and display top five scores.
                    

GroupC_Practical19(C++) :
Experiment No. 19 : Department of Computer Engineering has student's club named
                   'Pinnacle Club'. Students of Second, third and final year of
                    department can be granted membership on request. Similarly one
                    may cancel the membership of club. First node is reserved for
                    president of club and last node is reserved for secretary of
                    club. Write C++ program to maintain club member‘s information
                    using singly linked list. Store student PRN and Name. Write
                    functions to
                    a) Add and delete the members as well as president or even
                       secretary.
                    b) Compute total number of members of club
                    c) Display members
                    d) Display list in reverse order using recursion
                    e) Two linked lists exists for two divisions. Concatenate two
                       lists


GroupC_Practical20(C++) :
Experiment No. 20 : The ticket booking system of Cinemax theater has to
                    be implemented using C++ program.
                    There are 10 rows and 7 seats in each row. Doubly
                    circular linked list has to be maintained
                    to keep track of free seats at rows. Assume some
                    random booking to start with. Use array to store
                    pointers (Head pointer) to each row. On demand
                    a) The list of available seats is to be displayed
                    b) The seats are to be booked
                    c) The booking can be cancelled
                    
                    
GroupD_Practical25(C++) :
Experiment No. 25 : A palindrome is a string of character that‘s the same forward and backward.
                    Typically, punctuation, capitalization, and spaces are ignored. For example, “Poor Dan is in a droop” is a palindrome, 
                    as can be seen by examining the characters “poor danisina droop” and observing that they are the same forward and backward.
                    One way to check for a palindrome is to reverse the characters in the string and then compare with them the original-in a 
                    palindrome, the sequence will be identical. Write C++ program with functions- 
                    a) To print original string followed by reversed string using stack 
                    b) To check whether given string is palindrome or not


GroupD_Practical26(C++) :
Experiment No. 26 : In any language program mostly syntax error occurs due to unbalancing delimiter such as (),{},[]. 
                    Write C++ program using stack to check whether given expression is well parenthesized or not.
                    
                    
GroupE_Practical29(C++) :
Experiment No. 29 : Queues are frequently used in computer programming, and a typical example is the creation of a job queue by an operating system. 
                    If the operating system does not use priorities, then the jobs are processed in the order they enter the system.
                    Write C++ program for simulating job queue. Write functions to add job and delete job from queue.
                    
                    
GroupE_Practical31(C++) :
Experiment No. 31 : A double-ended queue (deque) is a linear list in which additions and deletions may be made at either end. Obtain a data
                    representation mapping a deque into a one-dimensional array. Write C++ program to simulate deque with functions to add 
                    and delete elements from either end of the deque. 
                    
                    
GroupE_Practical32(C++) :
Experiment No. 32 : Pizza parlor accepting maximum M orders. 
                    Orders are served in first come first served basis. Order once placed can not be cancelled. 
                    Write C++ program to simulate the system using circular queue using array.
                    
