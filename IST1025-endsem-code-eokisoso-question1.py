def calculate_salary(hourly_rate, hours_worked, tax_rate = 0.15):
    '''This function calculates employees net salary while considering a default tax value of 0.15'''
    gross_salary = hourly_rate * hours_worked
    net_salary = gross_salary - tax_rate
    return net_salary

def get_positive_float(prompt):
    '''This function gets a valid positive float from the user and prompts his/her net salary.'''
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

hourly_rate = get_positive_float("Input hourly rate: ")
hours_worked = get_positive_float("Input hours worked: ")

net_salary = calculate_salary(hourly_rate, hours_worked)

print(f"\nNet Salary: {net_salary:}")
