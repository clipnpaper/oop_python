# 학생 리스트 (Students)를 선언해 주세요. 5명의 학생정보를 아래 속성으로 저장하세요
# 학생은 이름(name), 국어(korean),영어(english),수학(math),과학(science)속성갖는다

def create_student(name, korean, math, english, science):
    return {
        "이름" : name,
        "국어" : korean,
        "수학" : math,
        "영어" : english,
        "과학" : science,
    }


students = [
    create_student("김현준", 80, 100, 90 ,70),
    create_student("이상훈", 90, 90, 70, 70),
    create_student("이서진",80,90,95,70),
    create_student("나형석",80,90,95,70),
    create_student("유재석",80,90,95,70),
    create_student("서유미",80,90,95,70),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    total = 0
    for value in student.values():
        if type(value) == str: continue
        total += value
    average = total / 4.0
    print(student["이름"], total, average, sep="\t")
