# This is an example for instance variables and class variables.
class Employee:
    # Class Variables
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        # Variables with Self are instance variables.
        # Instance variables can have values for the instance of the class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    @property
    def email(self):
        return "{} {}@email.com".format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first =first
        self.last = last

    @fullname.deleter
    def fullname(self): # del emp1.fullname
        print("delete name")
        self.first = none
        self.last = none

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self): # This method
        return "Employee('{}' ,'{},'{}'".format(self.first,self.last,self.pay)

    def __str__(self):
        return "Employee('{}' ,'{}".format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay  # print(emp1 + emp1)

    def __len__(self):
        return len(self.fullname())

    # Class methods are alternative constructors
    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        Employee(first, last, print())
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Class Developer inherits Employee class
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # More maintainable when single or multi inheritance
        # Employee.__init__(self,first,last,pay) for single inheritance
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)  # More maintainable when single or multi inheritance
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for employee in self.employees:
            print(employee.fullname())


dev1 = Developer('corey', 'Schafer', 50000, 'Python')
dev2 = Developer('John', 'Smith', 50000, 'Java')
print(dev1.email, dev1.prog_lang)
dev1.apply_raise()
print(dev1.pay)

man1 = Manager('George','McKinney','120000',[dev1])
man1.add_emp(dev2)
print(man1.email)
man1.print_emps()
man1.remove_emp(dev1)
man1.print_emps()
print(isinstance(man1,Manager))
print(issubclass(Developer,Employee))
"""
print(help(Developer))
import datetime

my_date = datetime.date(2016, 5, 10)
print(Employee.is_workday(my_date))

emp1 = Employee('corey', 'Schafer', 50000)
emp2 = Employee('john', 'smith', 50000)
print(emp1.fullname())
print(Employee.fullname(emp1))

print(emp1.pay)
print(emp2.pay)
print(Employee.__dict__)

emp1.raise_amount = 1.05
emp1.apply_raise()
print(emp1.pay)
print(emp2.pay)
print(Employee.__dict__)

print(Employee.num_of_emps)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
Employee.set_raise(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

Employee.raise_amount = 1.07

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)


"""
