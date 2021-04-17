# Import modules
import os
import csv

def main():
    # set the path for collecting the ellection data
    csv_path = os.path.join('Resources', 'budget_data.csv')
    csv_write = os.path.join('Analysis', 'Budget_Analysis.txt')
    
    # Initialize variables
    total_months = 0
    net_total_amount = 0
    average_change = 0
    greatest_increase = float('-inf')   # sets the lower limit for the revenue change to help find max increase in revenue 
    greatest_decrease = float('inf')    # sets the upper limit for the revenue change to hep find min decrease in revenue 
    greatest_increase_date = 'Mon-Year'
    greatest_decrease_date = 'Mon-Year'
    prev_revenue = None     # this enebles us to skip the first revenue row when computing the change in revenue
    revenue_change_ls = []

    # read the csv
    with open(csv_path, newline='') as f:       #quivalent to f = open(csv_reader, 'r'), f('close')
        reader = csv.reader(f, delimiter=',')
        #skip header
        csv_header = next(f, None)
        # loop thru data
        for row in reader:
            revenue = int(row[1]) 
            # update total months, this gives us the total number of months
            total_months += 1
            # update the net total revenue, sums the revenues from all months
            net_total_amount += revenue
            # this next code will skip the first revenue row since there is no previous revenue to compute a change
            if prev_revenue is not None:
                # compute the change in revenue
                rev_change = revenue - prev_revenue
                # append the revenue change to the revenue change list
                revenue_change_ls.append(rev_change)
                # update the greatest increase
                if rev_change > greatest_increase:
                    greatest_increase = rev_change
                    greatest_increase_date = row[0]
                # update the greatest decrease
                if rev_change < greatest_decrease:
                    greatest_decrease = rev_change
                    greatest_decrease_date = row[0]
            # update prev_revenue
            prev_revenue = revenue
    #update average change
    average_change += round(sum(revenue_change_ls) / len(revenue_change_ls), 2)

    # create the output file
    output = (
        f'Financial Analysis\n'
        f'-------------------------\n'
        f'Total Months: {total_months}\n'
        f'Total: ${net_total_amount}\n'
        f'Average Change: ${average_change}\n'
        f'Greatest increase in profits: {greatest_increase_date} (${greatest_increase})\n'
        f'Greatest decrease in profits: {greatest_decrease_date} (${greatest_decrease})\n'
    )
    
    # print the results to the output file
    print (output)

    with open(csv_write, 'w') as f:
        f.write(output)

if __name__ == "__main__":
    main()
