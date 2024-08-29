
# Create a new file named "employees.txt"
def employee_file(employees):
    file_name = "employees.txt"

    with open(file_name,'w') as file:
        file.write("Name\t\tAge\tSalary\n")
        for i in employees:
            file.write(f"{i[0]}\t\t{i[1]}\t{i[2]}\n")
        
        print(f"File '{file_name}' has been created with employee details.")

if __name__ == '__main__':
    employees = [
        ('Shiv',29,30000),
        ('Aman',22,40000),
        ('Vaish',26,50000),
    ]

    employee_file(employees)


