name = input("Enter student name: ")
mark1 = int(input("Enter first subject mark: "))
mark2 = int(input("Enter second subject mark: "))

average = (mark1 + mark2) / 2

print("Student Name:", name)
print("Average Mark:", average)

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
