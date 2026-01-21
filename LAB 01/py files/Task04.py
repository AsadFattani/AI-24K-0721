
def calculateSalary(salary):
    HRA = 0.10 * salary
    DA = 0.05 * salary

    return salary + HRA + DA

salary = float(input("Enter the basic salary: "))
totalSalary = calculateSalary(salary)
print(f"Total salary is: {totalSalary}")
