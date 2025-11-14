num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

total_class_score = 0   
total_scores_count = 0  

for student in range(1, num_students + 1):
    print(f"\nStudent {student}")
    student_total = 0  

    for subject in range(1, num_subjects + 1):
        score = float(input(f"Enter score {subject}: "))
        student_total += score
        total_class_score += score
        total_scores_count += 1

    student_average = student_total / num_subjects
    print(f"Average for Student {student} = {student_average}")

class_average = total_class_score / total_scores_count
print(f"\nOverall Class Average = {class_average}")
