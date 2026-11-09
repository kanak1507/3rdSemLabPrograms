time = [1,2,5,10]
total = 0
total += time[1]
total += time[0]
total += time[3]
total += time[1]
total += time[1]
print("Minimum time: ",total,"minutes")
'''1. What is the Bridge and Torch problem?
It is a puzzle where four people must cross a bridge at night using one torch. Only two people can cross at a time, and the torch must always be carried.

2. What is the purpose of this program?
To calculate the minimum time required for all people to cross the bridge.

3. What does time = [1,2,5,10] represent?
It represents the crossing times of four people in minutes.

5. What is the use of total = 0?
It initializes the total crossing time to zero.

6. What does total += time[1] mean?
It adds the value at index 1 to total.

7. What is the value of time[1]?
It is 2.

8. What is the value of time[0]?
It is 1.

9. What is the value of time[3]?
It is 10.

10. Why does indexing start from 0?
Python uses zero-based indexing, so the first element is at index 0.

11. What is the difference between + and +=?
+ performs addition.
+= adds a value to an existing variable and updates it.

12. What is the use of print()?
It displays the output on the screen.

14. How is the total calculated?
time[1] = 2
time[0] = 1
time[3] = 10
time[1] = 2
time[1] = 2
Total = 2 + 1 + 10 + 2 + 2 = 17 minutes.

23. Is 17 minutes the minimum time for the given crossing times?

No. The optimal strategy takes 17 minutes? Let's calculate carefully: for times 1, 2, 5, 10, the minimum is 17 minutes using the strategy:
1 and 2 cross: 2
1 returns: 1
5 and 10 cross: 10
2 returns: 2
1 and 2 cross: 2
Total = 17 minutes. So yes, 17 minutes is the minimum.


'''