def find_leap_years(start_year, end_year):
    leap_years = []
    for year in range(1700, 2100 + 1):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap_years.append(year)
    return leap_years

start_year = 1700
end_year = 2100
leap_years = find_leap_years(start_year, end_year)
print(leap_years)
