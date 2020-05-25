# Importing the Calendar module of Python.
import calendar 

# Asking for month and year from the user.
yy = int(input("Enter a year: "))
mm = int(input("Enter a month: "))

# Now this will display the calendar based on given month and year by the user.
print(calendar.month(yy,mm))
