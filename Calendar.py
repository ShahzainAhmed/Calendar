# Importing the Calendar module of Python.
import calendar 
# Asking for month and year.
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
# display the calendar
print(calendar.month(yy,mm))
