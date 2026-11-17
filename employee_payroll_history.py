class Salary:
    def __init__(self, base_pay, bonus, overtime):
        self.base_pay = base_pay
        self.bonus = bonus
        self.overtime = overtime

    def get_total(self):
        return self.base_pay + self.bonus + self.overtime

    def get_tax(self):
        return self.get_total() * 0.1

    def get_net(self):
        return self.get_total() - self.get_tax()

class WorkHistory:
    def __init__(self, company, position, start_year, end_year):
        self.company = company
        self.position = position
        self.start_year = start_year
        self.end_year = end_year

    def get_years(self):
        return self.end_year - self.start_year

    def to_string(self):
        return "{}\t{}\t{}\t{}\t{}".format(
                    self.company, self.position,self.start_year,
                    self.end_year, self.get_years()
                )

class Employee:
    def __init__(self, name, dept, salary: Salary):
        self.name = name
        self.dept = dept
        self.salary = salary
        self.histories = []

    def add_history(self, workhistory: WorkHistory):
        self.histories.append(workhistory)

    def get_career(self):
        total_career = 0
        if len(self.histories) == 0:
            return 0
        for work_history in self.histories:
            total_career += work_history.get_years()
        return total_career

    def to_string(self):
        return f"{self.name}\t{self.dept}\t{self.get_career()}년\t{self.salary.get_total()}\t{self.salary.get_tax()}\t{self.salary.get_net()}"

if __name__ == "__main__":
    #사원 생성
    kimminsu = Employee("김민수","개발팀",Salary(300,50,20))
    leejieun = Employee("이지은","인사팀",Salary(320,40,30))  #신입
    choiseoyeon = Employee("최서연","개발팀",Salary(350,30,25))

    kimminsu.add_history(WorkHistory("넥슨","사원",2015,2018))
    kimminsu.add_history(WorkHistory("네오위즈","대리",2018,2022))
    choiseoyeon.add_history(WorkHistory("데이터랩","사원",2012,2016))
    choiseoyeon.add_history(WorkHistory("클라우드원","과장",2016,2020))
    choiseoyeon.add_history(WorkHistory("넥스트AI","차장",2020,2023))

    employees = [kimminsu,leejieun,choiseoyeon]

    print("="*70)
    print("이름","부서","총액","세금","실수령액", sep="\t")
    for  emp in employees:
        print(emp.to_string())

    print()
    print("="*70)
    print("\t  근 무 이 력")
    for emp in employees:
        print("[{}] 총 경력 {}년".format(emp.name, emp.get_career()))
        if len(emp.histories) == 0:
            print("이력 없음(신입)")
        for h in emp.histories:
            print(" "+ h.to_string())