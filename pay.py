class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        raise NotImplementedError("Subclass must implement this method")


class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission_value):
        super().__init__(emp_id, name, weekly_salary)
        self.commission_value = commission_value

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission_value