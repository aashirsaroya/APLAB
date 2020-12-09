print("Enter number of employees")
n = int(input())
employees = []
print('Enter the details of each employee as required')
for i in range(0,n):
	id = int(input("ID : "))
	name = input("Name : ")
	sal = int(input("Salary : "))
	dept = input("Department : ")
	print()
	emp = (id, name, sal, dept)
	employees.append(emp)

id = int(input("Please enter ID to search for : "))
f = False
for emp in employees:
	if emp[0] == id:
		f = True
		print("ID : ", emp[0])
		print("Name : ", emp[1])
		print("Salary : ", emp[2])
		print("Department : ", emp[3])
		break

if not f:
	print("Employee does not exist")
