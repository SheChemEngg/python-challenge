#### PyBank
os module is useful in interacting with the operating system.
csv module is used to read from, and write into CSV files.

A name ‘csvreader’ is given to the file including the path.
The file is then opened using ‘UTF-8’ encoding.

Header-row is skipped, and only data is included for calculations.

    import os
    import csv

    Set path to locate file
    csvpath = os.path.join("..", "Resources", "budget_data.csv")

    Open the CSV using the UTF-8 encoding
    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the header row
        header = next(csvreader)
-------------------------------------------------------------------

From the ‘Date’ column, only the month-name is extracted.  Then all occurrences of months are added to obtain the total number of months.

    # Months & total number of months
    months = [row[0].split('-')[0] for row in csvreader]
    num_months = len(months)

    print("\nTotal Months:", num_months)

-------------------------------------------------------------------

From the ‘Profit/Losses’ column, all revenues are summed to obtain the net revenue over the total number of months.
   
    # Net Profit/Loss over the entire period
    net_revenue = sum(int(row[1]) for row in csvreader)
    print(f"\nTotal: ${net_revenue}")

-------------------------------------------------------------------

From the ‘Profit/Losses’ column, revenue change between two consecutive months is recorded. A new list of these revenue changes from one month to the next is created.  The number of months is now reduced by one.
Then the average of the changes in revenue is calculated over the reduced number of months.

    # Net Revenue change from month to month
    changes = []
    month_new = num_months-1

    revenue = [int(row[1]) for row in csvreader]
    for i in range(1, len(revenue)):
        Rev_change = revenue[i] - revenue[i-1]
        changes.append(Rev_change)
        aver_rev_change = sum(change for change in changes)/month_new
    print(f'\nAverage Change: ${round(aver_rev_change, 2)}')

-------------------------------------------------------------------

An empty dictionary ‘date_rev’ is created, with date as the ‘key’, and revenue change from one month to the next as the ‘value’.

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

-------------------------------------------------------------------

The dictionary ‘date_rev’ is  sorted. The maximum revenue-change (value) with the corresponding date (key), and the minimum revenue-change with the corresponding date are printed.

    sorted_date_rev = dict(sorted(date_rev.items(), key=lambda x: x[1]))
    last_key = list(sorted_date_rev.keys())[-1]
    last_value = list(sorted_date_rev.values())[-1]
    print(f'\nGreatest Increase in Profits: {last_key} (${last_value})')

    first_key = list(sorted_date_rev.keys())[0]
    first_value = list(sorted_date_rev.values())[0]
    print(f'\nGreatest Decrease in Profits: {first_key} (${first_value})')
----------------------------------------------------------------------
The output in the required format is written to an output text file.


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

#### Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
Your task is to create a Python script that analyzes the records to calculate each of the following values:

*	The total number of months included in the dataset
*	The net total amount of "Profit/Losses" over the entire period
*	The changes in "Profit/Losses" over the entire period, and then the average of those changes
*	The greatest increase in profits (date and amount) over the entire period
*	The greatest decrease in profits (date and amount) over the entire period

Financial Analysis

----------------------------

Total Months: 86

Total: $22564198

Average Change: $-8311.11

Greatest Increase in Profits: Aug-16 ($1862002)

Greatest Decrease in Profits: Feb-14 ($-1825558)
