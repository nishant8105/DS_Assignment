# Employee dictionary
employees = {
    101: {
        "name": "Satya",
        "age": 27,
        "department": "HR",
        "salary": 50000
    },
    102: {
        "name": "Anjali",
        "age": 30,
        "department": "Finance",
        "salary": 65000
    },
    103: {
        "name": "Ravi",
        "age": 25,
        "department": "IT",
        "salary": 70000
    },
    104: {
        "name": "Meena",
        "age": 29,
        "department": "Marketing",
        "salary": 55000
    }
}

def menu():
    print('''
1. Add Employee
2. View All Employees
3. Search for Employee
4. Exit
''')
    choice = int(input("Choose number from menu: "))
    return choice

def Add_Employee():
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employees:
        print("Enter valid ID")
        Add_Employee()
    else :
        emp_info = {}
        emp_info["name"] = input("Enter your name: ")
        emp_info["age"] = int(input("Enter your age: "))
        emp_info["department"] = input("Enter your department: ")
        emp_info["salary"] = input("Enter your salary: ")
        employees[emp_id] = emp_info
        print("Employee details are Succesfully added.")
    
    

def View_all_Employees ():
    if not employees :
        print("No employee available")
    else :
        print(f"{"Employee ID" : <13} {"Name" : <10} {"Department" : <11} {"Age" : <5} Salary")
        for emp_id,details in employees.items():
            print(f"{emp_id : ^10} {details["name"] : ^10} {details['department'] : ^15} {details['age'] : ^2} {details['salary'] : ^10}")

def Search_Employee ():
        emp_id = int(input("Enter Employee ID: "))
        if emp_id not in employees :
            print("Employee not found")
        else :
            print(employees[emp_id])


while True :
    option = menu()
    if option == 1 :
        Add_Employee()
    elif option == 2 :
        View_all_Employees()
    elif option == 3 :
        Search_Employee()
    elif option == 4 :
        print("Thank you")
        break
    else :
        print("Choose valid option")