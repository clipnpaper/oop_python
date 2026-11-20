class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def student_get_totalscore(self):
        return self.korean +\
            self.math +\
            self.english +\
            self.science

    def student_get_average(self):
        return self.student_get_totalscore() / 4.0

    def to_string(self):
        return f"{self.name}\t{self.student_get_totalscore()}\t{self.student_get_average()}"
        
Students = [Student("김유미",80,90,95,70),
            Student("이서진",80,90,95,70), 
            Student("나형석",80,90,95,70), 
            Student("유재석",80,90,95,70), 
            Student("서유미",80,90,95,70)]

print("이름","총점","평균",sep="\t")
for student in Students:
    print(student.to_string())