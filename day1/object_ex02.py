#딕셔너리를 리턴하는 함수를 선언
def create_student(name,korean,math,english,science):
    return {
        "name":name,
        "korean": korean,
        "math": math,
        "english":english,
        "science":science
    }
students = [
    create_student("김유미",80,90,95,70),
    create_student("이서진",80,90,95,70),
    create_student("나형석",80,90,95,70),
    create_student("유재석",80,90,95,70),
    create_student("서유미",80,90,95,70),
   ]

# 학생을 처리하는 함수 3개를 구현하세요
# 학생 한명의 총점을 리턴하는 함수 : student_get_sum(student)
def student_get_sum(student):
    score_sum = student["korean"]+student["english"]+student["math"]+student["science"]
    return score_sum

# 학생 한명의 평균을 리턴하는 함수 : student_get_average(student)
def student_get_average(student):
        score_avg = student_get_sum(student) / 4
        return score_avg

# 학생 한명의 점수를 출력하는 함수 : student_to_string(student)
def student_to_string(student):
        return "{}\t{}\t{}".format(student["name"], student_get_sum(student), student_get_average(student))


# 학생명단(성적표) 출력하세요
print("이름","총점","평균",sep="\t")
for student in students:
        print(student_to_string(student))