# Calculating average marks of student
total_marks = 100
s_marks = 0
marks = {"Physcis":95,"Chemistry":92,"Maths":77,"Biology":89,"English":79,"Social_Science":85}
for i in marks:
    s_marks = s_marks + marks[i]

percentage = (s_marks)/(len(marks)*total_marks) * 100
print("The percentage of the student in following subjects are: "+str(percentage)+"%")

