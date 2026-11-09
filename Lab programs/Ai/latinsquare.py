# Latin Square Problem
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        print((i + j) % n + 1, end=" ")
    print()
'''
1. What is a Latin Square?
A Latin Square is an n × n matrix in which each number appears exactly once in every row and every column.

2. What is the purpose of a Latin Square?
To arrange numbers so that no number is repeated in any row or column.

3. What is the order of a Latin Square?
The order is the number of rows or columns. For example, a 3 × 3 square has order 3.

5. Can we create a 4 × 4 Latin Square?
Yes. We can create Latin Squares of any positive integer order.

Python program questions
6. Why do we use n = int(input())?
To get the size of the Latin Square from the user.

7. Why do we use range(n)?
To repeat the loop n times.

8. Why do we use two for loops?
The outer loop represents rows, and the inner loop represents columns.

9. What does (i + j) % n + 1 mean?
It generates numbers from 1 to n without repeating in any row or column.

10. What is the use of the % operator?
It is the modulus operator. It returns the remainder after division.

11. What is the use of print(..., end=" ")?
It prints values on the same line with a space between them.

12. Why do we use print() after the inner loop?
To move to the next line after printing each row.

'''