cupcake_invoices = open('CupcakeInvoices.csv')
#Loop through all the data and print each row.
for line in cupcake_invoices:
    print(line)
#Loop through all the data and print the type of cupcakes purchased.
cupcake_invoices.seek(0,0)
for line in cupcake_invoices:
    if 'Chocolate' in line:
        print('Chocolate')
    elif 'Vanilla' in line:
        print('Vanilla')
    elif 'Strawberry' in line:
        print('Strawberry')

#Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
cupcake_invoices.seek(0,0)
for line in cupcake_invoices:
    line = line.rstrip('\n').split(',')
    print(line)
    cost = []
    value_one = float(line[-1])
    value_two = float(line[-2])
    order_total = value_one * value_two
    cost.append(order_total)
    print(cost)


#Loop through all the data, and print out the total for all invoices combined.

cupcake_invoices.seek(0,0)
total = 0
for line in cupcake_invoices:
    values = line.split(',')
    total = total + (int(values[3]) * float(values[4]))

print (f'The total is {total}')

cupcake_invoices.close()

import matplotlib.pyplot as plt 

# x axis values 
x = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"] 
# corresponding y axis values 
y = [10,40,32,84,60,52,18] 

# plotting the points
plt.plot(x, y) 

# naming the x axis 
plt.xlabel('Day Purchased') 
# naming the y axis 
plt.ylabel('Cupcakes Purchased') 

# giving a title to my graph 
plt.title('My Cupcake Sales') 

# function to show the plot 
plt.show()