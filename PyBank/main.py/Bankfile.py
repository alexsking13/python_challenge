import csv
import os

bankfile = r"C:\Users\Alex\Documents\python_challenge\PyBank\Resources\budget_data.csv"

#Variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_losses_changes = []
dates = []

# Read CSV file
with open(bankfile) as bank_csv:
    bank_reader = csv.reader(bank_csv)
    csv_header = next(bank_reader)  # Read the header and move to the next line

    #Loop through each row
    for row in bank_reader:
        total_months = total_months+1
        profit_loss = int(row[1])
        total_profit_loss = total_profit_loss+profit_loss
        dates.append(row[0])

        # Calculate the change in profit/loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_losses_changes.append(change)
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_losses_changes) / len(profit_losses_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_losses_changes)
greatest_decrease = min(profit_losses_changes)

# Find corresponding dates
increase_index = profit_losses_changes.index(greatest_increase)
decrease_index = profit_losses_changes.index(greatest_decrease)

# Prepare analysis text
analysis_text = (
    "Financial Analysis\n"
    "-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {dates[increase_index + 1]} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {dates[decrease_index + 1]} (${greatest_decrease})\n"
)

# Print results to the terminal
print(analysis_text)

# Export results to a text file
folder_path=r"C:\Users\Alex\Documents\python_challenge\PyBank\analysis"
output_file = "Bank_Data.txt"
file_path=os.path.join(folder_path, output_file)
with open(file_path, 'w') as f:
    f.write(analysis_text)



