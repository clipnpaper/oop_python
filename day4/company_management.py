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

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_payroll(self):
        payroll = 0
        if len(self.employees) == 0:
            return 0
        for em in self.employees:
            payroll += em.salary.get_total()
        return payroll

    def get_avg_career(self):
        total_career = 0
        if len(self.employees) == 0:
            return 0
        for em in self.employees:
            total_career += em.get_career()
        return total_career / len(self.employees)

    def print_members(self):
        print(f"[{self.name}]")
        print(f"{'이름':　<6}{'경력':<6}{'급여 총액':<8}{'세금':<10}실수령액")
        print("-" * 50)
        for em in self.employees:
            print(f"{em.name:　<6}{str(em.get_career()) + '년':<7}{em.salary.get_total():<12}{em.salary.get_tax():<12}{em.salary.get_net()}")

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department: Department):
        self.departments.append(department)

    def get_employee_count(self):
        total_employee = 0
        if len(self.departments) == 0:
            return 0
        for Dep in self.departments:
            total_employee += len(Dep.employees)
        return total_employee

    def get_payroll(self):
        total_payroll = 0
        if len(self.departments) == 0:
            return 0
        for Dep in self.departments:
            total_payroll += Dep.get_payroll()
        return total_payroll

    def print_report(self):
        print(f"{'부서':　<9}{'인원':<6}{'급여 총액':<8}평균 경력")
        print("-" * 50)
        for Dep in self.departments:
            print(f"{Dep.name:　<9}{str(len(Dep.employees)) + '명':<7}{Dep.get_payroll():<12}{Dep.get_avg_career()}년")
        print("-" * 50)
        print(f"{self.name:　<9}{str(self.get_employee_count()) + '명':<7}{self.get_payroll():<12}")

if __name__ == "__main__":
    # 사원 생성
    kimminsu = Employee("김민수", "개발팀", Salary(300, 50, 20))
    choiseoyeon = Employee("최서연", "개발팀", Salary(350, 30, 25))
    leejieun = Employee("이지은", "인사팀", Salary(320, 40, 30))
    parkjunho = Employee("박준호", "영업팀", Salary(300, 30, 20))   # 신입
    jungharin = Employee("정하린", "마케팅팀", Salary(310, 45, 30))

    # 근무이력 (부서별 평균 경력: 개발 9.0 / 인사 4.0 / 영업 0.0 / 마케팅 3.0)
    kimminsu.add_history(WorkHistory("넥슨", "사원", 2015, 2018))
    kimminsu.add_history(WorkHistory("네오위즈", "대리", 2018, 2022))
    choiseoyeon.add_history(WorkHistory("데이터랩", "사원", 2012, 2016))
    choiseoyeon.add_history(WorkHistory("클라우드원", "과장", 2016, 2020))
    choiseoyeon.add_history(WorkHistory("넥스트AI", "차장", 2020, 2023))
    leejieun.add_history(WorkHistory("한빛소프트", "사원", 2018, 2022))
    jungharin.add_history(WorkHistory("미디어랩", "사원", 2021, 2024))

    # 부서 생성 및 사원 배치
    dev = Department("개발팀")
    dev.add_employee(kimminsu)
    dev.add_employee(choiseoyeon)

    hr = Department("인사팀")
    hr.add_employee(leejieun)

    sales = Department("영업팀")
    sales.add_employee(parkjunho)

    marketing = Department("마케팅팀")
    marketing.add_employee(jungharin)

    # 회사 생성 및 부서 등록
    company = Company("블루웨이브 전체")
    company.add_department(dev)
    company.add_department(hr)
    company.add_department(sales)
    company.add_department(marketing)

    # 부서 순회 -> 사원 순회 보고서 출력
    company.print_report()

    # 부서별 사원 목록 출력
    for dept in company.departments:
        print()
        dept.print_members()