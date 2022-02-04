import os
import csv

file = os.path.join('..', 'Resources', 'budget_data.csv')
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    months = []
    profit_or_loss = []
    month_minus_month = []
    
    for row in csvreader:
        months.append(row[0])
        profit_or_loss.append(int(row[1]))
    for i in range(len(profit_or_loss)-1):
        month_minus_month.append(profit_or_loss[i+1]-profit_or_loss[i])
                      
increase = max(month_minus_month)
decrease = min(month_minus_month)

month_increase = month_minus_month.index(max(month_minus_month))+1
month_decrease = month_minus_month.index(min(month_minus_month))+1

print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(months)}")
print(f"Total: ${sum(profit_or_loss)}")
print(f"Average Change: {round(sum(month_minus_month)/len(month_minus_month),2)}")
print(f"Greatest Increase in Profits: {months[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {months[month_decrease]} (${(str(decrease))})")      

output_file = os.path.join(".", 'financial_analysis.txt')
with open(output_file,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(months)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit_or_loss)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(month_minus_month)/len(month_minus_month),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {months[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {months[month_decrease]} (${(str(decrease))})")