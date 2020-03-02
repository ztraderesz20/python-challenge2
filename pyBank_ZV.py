import os
import csv

#  Define path to data file
budget_csv = os.path.join('Resources', 'budget_data.csv')

#  Open and read csv data file
with open(budget_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    
#  Initialize total_pnl variable to 0; create empty named lists to hold extracted values from dataset.   
    total_pnl = 0
    months = []
    pnl = []
        
    for row in csv_reader:
#  ANSWER.2        
        total_pnl += int(row[1])
    
#  Creates 2 lists for dates and P/L.    
        months.append(row[0])
        pnl.append(row[1])

#  ANSWER.1                        
    total_months = len(months)
#--------------------------------------------------------------------------------------------------    
    
#  Extract p/l values and create 2 new lists.  End_pnl list is offset by 1 index value from start_pnl list.
#  Convert list elements to integer type
end_pnl = pnl[1:total_months]
end_list = map(int, end_pnl) 

start_pnl = pnl[0:total_months]
start_list = map(int, start_pnl) 

# Combine both lists to create [end_pnl,start_pnl] elements
zip_list = zip(end_list, start_list)

#  Create empty net_pnl[] to hold values from subtraction (end_pl - start_pnl = net_pnl).
#  loop through all rows to preform calculation.
net_pnl=[]
for end_list_i, start_list_i in zip_list:
    net_pnl.append(end_list_i - start_list_i)

#  Determine length of net_pnl[] for denominator; sum all elements for numerator; calculate average net p/l.
net_months = len(net_pnl)
total_net_pnl = sum(net_pnl)

#  ANSWER.3
Avg_net_pnl = total_net_pnl / net_months

#  ANSWER.4
max_profit = max(net_pnl)

#  Add element [0] to net_pnl[] to match length of total_months[]. We need to include
#  Header to correctly map date to max/min in net_P/L[].
#-------------------------------------------------------------------------------------
net_pnl_offset = [0]
net_pnl_align = net_pnl_offset + net_pnl

#Loop through net_pnl_align[] and find index value for element == max_profit;
# match index value  found and apply to months[] to find corresponding date == max_profit
#---------------------------------------------------------------------------------------------
max_p_index = [i for i in range(len(net_pnl_align)) if net_pnl_align[i] == max_profit]
max_date = (max_p_index[0])
#  Answer.5
max_p_date = months[max_date]

#  ANSWER.6
min_profit = min(net_pnl)

min_p_index = [i for i in range(len(net_pnl_align)) if net_pnl_align[i] == min_profit]
min_date = (min_p_index[0])
#  ANSWER.7
min_p_date = months[min_date]

#  Output formatting to terminal
#------------------------------------------------------------------------------------------------
print( 'Financial Analysis')
print('------------------------------------')
print(f'Total Months:  {total_months}')
print(f'Total:  $ {total_pnl}')
print(f'Average Change:  ${Avg_net_pnl:.2f}')
print(f'Greatest Increase in Profits: {max_p_date} ($ {max_profit})')
print(f'Greatest Decrease in Profits: {min_p_date} ($ {min_profit})')

#  Output results to data file

results_budget_file = os.path.join('output','results_budget.csv')
with open(results_budget_file, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Total Months:', total_months])
    csvwriter.writerow(['Total P/L:', total_pnl])
    csvwriter.writerow(['Average Change:', Avg_net_pnl])
    csvwriter.writerow(['Greatest Increase in Profits:', max_p_date,max_profit])
    csvwriter.writerow(['Greatest Decrease in Profits:', min_p_date,min_profit])

