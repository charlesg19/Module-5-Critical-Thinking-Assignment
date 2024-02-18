num_years = int(input('Enter the number of years:\n'))
num_months = 12
year_rain = 0
month_total = 0

for years in range(num_years):
    year = range(num_years)
    print("Enter the following information for year", year[years]+1)
    for months in range(num_months):
        month = range(num_months)
        print("    Enter the amount of rain fail for month", month[months]+1, "in inches: ", end="")
        month_rain = int(input())
        year_rain += month_rain
        month_total += 1

print("Total number of months: {}".format(month_total))
print("Total amount of rainfall: {} inches".format(year_rain))
print("Average rainfall: {} inches per month".format(year_rain / month_total))
