name = input("Enter your name: ")
marks = int(input("Enter your Marks: "))
print(f"Hey! {name}, your marks are: {marks}")
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks > 45:
    print("Grade: D")
else:
    print("Grade: Fail")