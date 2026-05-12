# Student array for recording grades
# Pass or fail, and goes deeper into it later on
# Something like a classification system, at the end of the day

def GradeSystem(NumStudents):
    # initialise Gradebook as a dictionary for all of the students
    # a dictionary is a 2D array in pseudocode, but it is called a 'dictionary' in Python
    GradeBook = {}
    Failed = 0
    Passed = 0
    TotalScore = 0
    StudentsEntered = 0

    for StudentsEntered in range(NumStudents):

        StudentName = input("Input your name: ")
        StudentScore = -1

        while StudentScore < 0 or StudentScore > 100:
            StudentScore = int(input("Input your test score: "))
            if StudentScore < 0 or StudentScore > 100:
                print("Invalid. The test score must be between 0 and 100. Input again.")

        GradeBook[StudentName] = StudentScore
        StudentsEntered += 1
        TotalScore += StudentScore

        if StudentScore < 50:
            Failed += 1
        else:
            Passed += 1

    AverageScore = TotalScore/NumStudents
    AverageScore = round(AverageScore, 2)

    if Failed >= Passed:
        LowAchieving(AverageScore, GradeBook)
    else:
        HighAchieving(AverageScore, GradeBook)

    print("The average score of all students is" + str(AverageScore) + "marks.")
    print("Pass the device to the next student, please.")
    return AverageScore, GradeBook, Passed, Failed

# Operator Modules


def Addition():
    import random
    addnum1 = random.randint(-700000, 700000)
    addnum2 = -700001
    while addnum1 == addnum2:
        addnum2 = random.randint(-700000, 700000)
    addans = addnum1 + addnum2
    userans = input(f"What is {addnum1} + {addnum2}?")
    if addans == float(userans):
        print("Correct!")
        return True
    else:
        print("Incorrect.")
        return False


def Subtraction():
    import random
    subnum1 = random.randint(-700000, 700000)
    subnum2 = -700001
    while subnum1 == subnum2:
        subnum2 = random.randint(-700000, 700000)
    subans = subnum1 - subnum2
    userans = input(f"What is {subnum1} - {subnum2}?")
    if subans == float(userans):
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is" + str(subans) + ".")
        return False


def Multiplication():
    import random
    multnum1 = random.randint(-50000, 50000)
    multnum2 = random.randint(-50000, 50000)
    multans = multnum1 * multnum2
    userans = input(f"What is {multnum1} * {multnum2} ? ")
    if float(userans) == multans:
        print("Correct.")
        return True
    else:
        return False


def Division():
    import random
    divnum1 = random.randint(-50000, 50000)
    divnum2 = -433333
    while divnum2 >= divnum1:
        divnum2 = random.randint(-50000, 50000)
    divans = divnum1 // divnum2
    userans = input(
        f"What is {divnum1} / {divnum2}? Give your answer to the nearest whole number, there is no need for mention of a remainder.")
    if float(userans) == divans:
        print("Correct.")
        return True
    else:
        return False

# End of Operator Modules


def HighAchieving(AverageScore, GradeBook):
    Gifted = []
    LogicalThinkers = []
    for StudentName, StudentScore in GradeBook.items():
        if StudentScore > AverageScore + 18:
            Gifted.append(StudentName)
        else:
            LogicalThinkers.append(StudentName)


def LowAchieving(AverageScore, GradeBook):
    import random
    Struggling = []
    Weak = []
    for StudentName, StudentScore in GradeBook.items():
        if StudentScore < AverageScore - 15:
            Struggling.append(StudentName)
        else:
            Weak.append(StudentName)

    QuestionList = [Addition, Subtraction, Multiplication, Division]

    for StudentName in Struggling:
        streak = 0
        print("Welcome to this session" + StudentName +
              ". This is specificially designed for you such that you may be able to improve your operation skills.")
        while streak != 5:
            calledmodule = random.choice(QuestionList)
            if calledmodule():
                if streak == 4:
                    print("Well done! You got 5 correct answers!")
                streak += 1
                print(
                    "Nice, you got it correct! Keep it going until you get 5 correct answers!")
                print(f"Current streak: {streak}")
            else:
                print(
                    StudentName + ", your streak has been reset as you got an answer wrong.")
                streak = 0
                continue
        print("Well done! Hope this helped you improve your skills using basic mathematical operations! You have reached mastery!")

    for StudentName in Weak:
        print("You aren't that far off reaching the heights of your potential. The main area setting you back is your complacency and the idea of procrastination.")
        print("Keep working hard and you will be soaring in no time, keep practicing!")
        print("You may revise through websites such as rocketrevise.com and using YouTube channels such as MathAntics.")


if __name__ == "__main__":
    num_students = int(input("How many students are there in your class?"))
    GradeSystem(num_students)
