name = input("Enter student name: ")
mark1 = int(input("Enter first subject mark: "))
mark2 = int(input("Enter second subject mark: "))

total = mark1 + mark2
average = total / 2

print("Student Name:", name)
print("Total Mark:", total)
print("Average Mark:", average)

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
