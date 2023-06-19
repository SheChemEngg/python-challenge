
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

print('\nFinancial Analysis\n')
print('-'*25)

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Months & total number of months
    months = [row[0].split('-')[0] for row in csvreader]
    num_months = len(months)

    print("\nTotal Months:", num_months)

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Net Profit/Loss over the entire period
    net_revenue = sum(int(row[1]) for row in csvreader)
    print(f"\nTotal: ${net_revenue}")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Net Revenue change from month to month
    changes = []
    month_new = num_months-1

    revenue = [int(row[1]) for row in csvreader]
    for i in range(1, len(revenue)):
        Rev_change = revenue[i] - revenue[i-1]
        changes.append(Rev_change)
        aver_rev_change = sum(change for change in changes)/month_new
    print(f'\nAverage Change: ${round(aver_rev_change, 2)}')


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Net Revenue change from month to month
    revenue = []
    dates = []
    date_rev = {}

    # Iterate over each row in the CSV
    for row in csvreader:
        date = row[0]
        rev = int(row[1])

        # Add date and revenue to respective lists
        dates.append(date)
        revenue.append(rev)

        # Calculate revenue change from month to month
        if len(revenue) > 1:
            rev_change = revenue[-1] - revenue[-2]
            date_rev[date] = rev_change

    sorted_date_rev = dict(sorted(date_rev.items(), key=lambda x: x[1]))
    last_key = list(sorted_date_rev.keys())[-1]
    last_value = list(sorted_date_rev.values())[-1]
    print(f'\nGreatest Increase in Profits: {last_key} (${last_value})')

    first_key = list(sorted_date_rev.keys())[0]
    first_value = list(sorted_date_rev.values())[0]
    print(f'\nGreatest Decrease in Profits: {first_key} (${first_value})')
#--------------------------------------------------------------------------------------------------

# https://www.pythontutorial.net/python-basics/python-write-text-file/
# Specify the file to write to
output_path = os.path.join("..", "Analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write('\nFinancial Analysis\n\n')
    txtfile.write('-' * 25)
    txtfile.write(f"\n\nTotal Months: {num_months}")
    txtfile.write(f"\n\nTotal: ${net_revenue}")
    txtfile.write(f'\n\nAverage Change: ${round(aver_rev_change, 2)}')
    txtfile.write(f'\n\nGreatest Increase in Profits: {last_key} (${last_value})')
    txtfile.write(f'\n\nGreatest Decrease in Profits: {first_key} (${first_value})')

