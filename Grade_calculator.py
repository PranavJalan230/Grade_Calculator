# grade_calculator.py
def calculate_grades(marks):
    avg = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("Average Score:", avg)
    print("Highest Score:", highest)
    print("Lowest Score:", lowest)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Final Grade:", grade)

if __name__ == "__main__":
    marks = [50,40,60,80,95]
    calculate_grades(marks)