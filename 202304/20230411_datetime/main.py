


# import datetime

# x = datetime.datetime.today()
# print(x)

# # 12:43:45.571871

# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=5))
# print(now + datetime.timedelta(days=20, hours=8))


# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=5))
# print(now + datetime.timedelta(days=20, hours=8))



# import datetime
# y = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(y)
# # 2020-02-29 18:20:50

# print(y.strftime("%A, %d. %B %Y %I:%M%p"))


#Write a function that calculates difference in days between two datetimes. 

from datetime import date

d0 = date(2022, 4, 11)
d1 = date(2023, 5, 11)
delta = d1 - d0
print(delta.days)



#Write a function that takes a datetime object, which will represent employees starting work day. 
# nd will return amount of total holidays gained during the work until today. 1 Month = 1.6 day off


# def calculate_holidays_gained(start_date):

   
#     current_date = datetime.datetime.now()  
#     delta = current_date - start_date  
#     months = delta.days / 30.42  
#     holidays_gained = months * 1.6 
#     return holidays_gained

# a = calculate_holidays_gained(datetime.datetime(2023, 1, 1))
# print(a)














#find next 3 Fridays that happend to be Friday the 13th (classic)

# from datetime import timedelta, date

# def friday13s(from_date=date.today()):
#     d = from_date + timedelta(13 - from_date.day)  

#     def increment_month(d):
#         mm = 1 if d.month == 12 else d.month + 1
#         yy = d.year + 1 if mm == 1 else d.year
#         return date(yy, mm, d.day)

#     if from_date > d:
#         d = increment_month(d)

#     while True:
#         if d.weekday() == 4:
#             yield d
#         d = increment_month(d)


# from itertools import islice

# for d in islice(friday13s(), 10):
#     print(d)



# import datetime

# def get_last_friday():

#     today = datetime.date.today()  # Get the current date
#     days_since_last_friday = (today.weekday() - 4) % 7  # Calculate the number of days since last Friday
#     last_friday = today - datetime.timedelta(days=days_since_last_friday)  # Subtract the days from current date
#     return datetime.datetime.combine(last_friday, datetime.time.min)  # Combine with minimum time to get datetime object

# a = get_last_friday()
# print(a)




# import calendar

# def get_last_day(year, month):
#     """
#     Returns the last day of a specified year and month.

#     Args:
#         year (int): The year.
#         month (int): The month.

#     Returns:
#         int: The last day of the specified year and month.
#     """
#     # Get the maximum day for the given year and month
#     max_day = calendar.monthrange(year, month)[1]
#     return max_day

# # Input year and month
# year = int(input("Enter the year: "))
# month = int(input("Enter the month: "))

# # Call the function to get the last day
# last_day = get_last_day(year, month)

# # Print the result
# print(f"The last day of {calendar.month_name[month]} {year} is {last_day}.")
