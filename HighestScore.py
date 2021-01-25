student_scores = input("Input a list of student scores ").split(",")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# print(student_scores)
highest_score=0
for n in student_scores:
    if n>highest_score:
        highest_score=n
print(f"highest_score: {highest_score}.")

# minimum score
minimum_score=100
for n in student_scores:
    if n<minimum_score:
        minimum_score=n
print(f"minimum_score: {minimum_score}")