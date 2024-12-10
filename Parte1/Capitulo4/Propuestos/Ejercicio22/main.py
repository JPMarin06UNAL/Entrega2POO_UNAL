from employee import Employee

# Ejemplo de uso
name = input("Ingrese el nombre del empleado: ")
hourly_wage = float(input("Ingrese el salario por hora: "))
hours_worked = int(input("Ingrese el total de horas trabajadas en el mes: "))

employee = Employee(name, hourly_wage, hours_worked)
employee.display_salary_info()
