import csv
from tabulate import tabulate 
import os

if not os.path.exists('EmployeePayroll'):
    os.makedirs('EmployeePayroll')

if not os.path.isfile('EmployeePayroll/employees.csv'):
    with open('EmployeePayroll/employees.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['ID', 'F_Name', 'L_Name', 'Depart.', 'Pay', 'Bonus', 'Deduct.', 'Salary'])


class Employee:
    
    def __init__(self, empid, fname, lname, depart, pay, bonus, deduction,):
        self.empid = empid
        self.fname = fname
        self.lname = lname
        self.depart = depart
        self.pay = int(pay)
        self.bonus = int(bonus)
        self.deduction = int(deduction)

    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"
    @property
    def finalSalary(self):
        return self.pay+self.bonus-self.deduction

    def toList(self):
        return [self.empid, self.fname, self.lname, self.depart, self.pay, self.bonus, self.deduction, self.finalSalary]

    @staticmethod
    def addEmployee():
        while True:
            empid = input("Enter the Employee's ID (or type \'exit\' to cancel adding the data): ")
            if empid.lower() == 'exit':
                return
            if not empid.isdigit():
                print("Only numbers are allowed as Employee ID! Please enter again.")
                continue

            unique = True
            with open('EmployeePayroll/employees.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for row in csv_reader:
                    if row[0] == empid:
                        print("Employee with this ID already exists! Please use a unique ID.")
                        unique = False
                        break

            if unique:
                break


        fname = input("Enter the First Name: ")
        lname = input("Enter the Last Name: ")
        depart = input("Enter the Department: ")
        while True:
            try:
                pay = int(input("Enter the Pay amount: "))
                break
            except ValueError:
                print("Invalid input! Enter an integer")
            
        while True:
            try:
                bonus = int(input("Enter the Bonus amount: "))
                break
            except ValueError:
                print("Invalid input! Enter an integer")

        while True:
            try:
                deduction = int(input("Enter the Deduction amount: "))
                break
            except ValueError:
                print("Invalid input! Enter an integer")


        emp = Employee(empid, fname, lname, depart, pay, bonus, deduction)

        with open('EmployeePayroll/employees.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(emp.toList())
            
        print("Employee added successfully!")

    @staticmethod
    def showEmployee():
        with open('EmployeePayroll/employees.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = list(csv_reader)
            if len(data)<=1:
                print("No Employee data found! Try entering some data first")
                return
            print(tabulate(data, headers = 'firstrow', tablefmt='pretty'))

    @staticmethod
    def delEmployee():

        while True:
            empid = input("Enter the Employee's ID: ")
            if empid.isdigit():
                break
            else:
                print("Only numbers are allowed as Employee ID! Please Enter again.")
            
        data = []
        found = False
        print("")
        with open('EmployeePayroll/employees.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for rows in csv_reader:
                if rows[0] == empid:
                    found = True
                    print(f"Employee {empid} Data deleted successfully!")
                    continue
                data.append(rows)

        if found:
            with open('EmployeePayroll/employees.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(data)
                    
        elif not found:
            print("Employee not found!")
            
            

    @staticmethod
    def searchEmpID():
        found = False
        empid = input("Enter Employee's ID to search: ")    
        print("")
        with open('EmployeePayroll/employees.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for rows in csv_reader:
                if rows[0] == empid:
                    found = True
                    for cell in rows:
                        print(cell, end = "\t")
                    print("")
                
        if not found:
            print("Employee not found!")

    @staticmethod
    def giveBonus():
        data = []
        found = False
        updated = False
        empid = input("Enter Employee ID: ")
        print("")
        with open('EmployeePayroll/employees.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for rows in csv_reader:
                if rows[0] == empid:
                    found = True
                    print(f"Employees Current Bonus: {rows[5]}")
                    while True:
                        try:
                            bns = int(input("Enter the new bonus amount: "))
                            break
                        except ValueError:
                            print("Invalid input! Enter an integer")
                    rows[5] = str(bns)
                    rows[7] = str(int(rows[4]) + int(rows [5]) - int(rows[6]))
                    print(f"Bonus of Employee {empid} successfully updated!")
                    updated = True
                data.append(rows)
                
        if updated:
             with open('EmployeePayroll/employees.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(data)
        if not found:
            print("Employee ID not found, Try again later")

    @staticmethod
    def deductSalary():
        data = []
        found = False
        updated = False
        empid = input("Enter Employee ID: ")
        print("")
        with open('EmployeePayroll/employees.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for rows in csv_reader:
                if rows[0] == empid:
                    found = True
                    print(f"Currently amount being deducted from salary: {rows[6]}")
                    while True:
                        try:
                            dedc = int(input("Enter the new deduction amount: "))
                            break
                        except:
                            print("Invalid input! Enter an integer")
                    rows[6] = str(dedc)
                    rows[7] = str(int(rows[4]) + int(rows [5]) - int(rows[6]))
                    print(f"Deduction of Employee {empid} successfully updated!")
                    updated = True
                data.append(rows)
                
        if updated:
             with open('EmployeePayroll/employees.csv', 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(data)
        if not found:
            print("Employee ID not found, Try again later")


while True:
    print("\nEmployee Payroll System")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Give Bonus to an Employee")
    print("5. Deduct salary of an Employee")
    print("6. Delete an Employee's Data")
    print("7. Exit")

    try:
        choice = int(input("Enter your Choice (1/2/3/4/5/6/7): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    print("")

    if choice == 1:
        Employee.addEmployee()
    elif choice == 2:
        Employee.showEmployee()
    elif choice == 3:
        Employee.searchEmpID()
    elif choice == 4:
        Employee.giveBonus()   
    elif choice == 5:
        Employee.deductSalary()
    elif choice == 6:
        Employee.delEmployee()
    elif choice == 7:
        print("Exiting the program...")
        break
    else:
        print("Invalid Choice! Please try again.")