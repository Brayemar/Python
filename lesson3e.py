# Below is a grading system based on what a student will have gotten
marks = int(input("Enter student marks: "))
# print("The entered marks is ", marks)
if marks > 0 and marks < 30:
    print("below average")
elif marks >= 30 and marks < 40:
    print("Average") 
elif marks >= 40 and marks < 70:
    print("Above average")
elif marks >= 70 and marks <= 100:
    print("excellent")
else:
    print("invalid input")