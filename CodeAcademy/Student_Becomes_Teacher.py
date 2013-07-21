Lloyd = {
    "name":"Lloyd",
    "homework": [90,97,75,92],
    "quizzes": [ 88,40,94],
    "tests": [ 75,90]
    }
Alice = {
    "name":"Alice",
    "homework": [100,92,98,100],
    "quizzes": [82,83,91],
    "tests": [89,97]
    }
Tyler = {
    "name":"Tyler",
    "homework": [0,87,75,22],
    "quizzes": [0,75,78],
    "tests": [100,100]
    }

def average(list):
	avg = sum(list)/len(list)
	return avg

def getAverage(student):
    weight_avg  = (average(student["homework"]) * .10) + (average(student["quizzes"])*.3) + (average(student["tests"])*.6)
    return weight_avg
	
def getLetterGrade(score):
    score = round(score)
    if score >= 90:
        return "A"
    elif score >=80 and score < 90:
        return "B"
    elif score >=70 and score < 80:
        return "C"
    elif score >=60 and score < 70:
        return "D"
    else:
        return "F"

def getAverage(kid):
    bar = average
    return bar(kid["homework"])*.1 + bar(kid["quizzes"])*.3 + bar(kid["tests"])*.6

students = [Lloyd,Alice,Tyler]

def getClassAverage(student_list):
    c= 0
    for i in student_list:
        c = + getAverage(student_list[i])
    c = c/len(student_list)
    return c