# A program for printing detailed information.

employee = "Mr. John May, born on 1998-02-16"

# Extracting the name, surname, initials, and date of birth
name = employee[4:8]                  # Extracts 'John' (starts at index 4, ends before index 8)
surname = employee[9:12]              # Extracts 'May' (starts at index 9, ends before index 12)
date_of_birth = employee[-10:]        # Extracts '1998-02-16' (last 10 characters)
initials = employee[4] + employee[9]  # Extracts 'J' from 'John' and 'M' from 'May'

# Printing the details
print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Born: {date_of_birth}')
print(f'Initials: {initials}')
