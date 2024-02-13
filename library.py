from datetime import datetime

def calculate_fine(book_id, due_date, return_date):
    # Calculate the days overdue
    due_date = datetime.strptime(due_date, '%Y-%m-%d')
    return_date = datetime.strptime(return_date, '%Y-%m-%d')
    days_overdue = (return_date - due_date).days

    # Determine the fine rate based on the number of days overdue
    if days_overdue <= 7:
        fine_rate = 20
    elif 8 <= days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100

    # Calculate the fine amount
    fine_amount = days_overdue * fine_rate

    # Display the results
    print("Bookid:", book_id)
    print("Duedate:", due_date.strftime('%Y-%m-%d'))
    print("Returndate:", return_date.strftime('%Y-%m-%d'))
    print("Daysovertime:", days_overdue)
    print("Dayoverdue:", "Yes" if days_overdue > 0 else "No")
    print("Finerate:", fine_rate)
    print("Fineamount:", fine_amount)

# Get inputs from the user
book_id = input("Enter book id: ")
due_date = input("Enter due date (yyyy-mm-dd): ")
return_date = input("Enter return date (yyyy-mm-dd): ")

# Calculate the fine
calculate_fine(book_id, due_date, return_date)