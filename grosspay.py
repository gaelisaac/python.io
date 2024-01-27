def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_gross_pay(hours, rate):
    return hours * rate

def main():
    hours = get_input("Enter hours worked: ")
    rate = get_input("Enter rate per hour: ")
    gross_pay = calculate_gross_pay(hours, rate)
    print(f"Gross pay: ksh{gross_pay:.2f}")

if __name__ == "__main__":
    main()