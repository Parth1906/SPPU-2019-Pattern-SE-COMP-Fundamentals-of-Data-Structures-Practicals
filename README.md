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
