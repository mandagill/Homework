"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

"""

def main():
    salespeople = []
    melons_sold = []

    f = open("sales_report.csv")
    for line in f:
        line = line.rstrip()
        entries = line.split(",")
        salesperson = entries[0]
        melons = int(entries[2])

# Checks if the salesperson has been added to the list
        if salesperson in salespeople:
            position = salespeople.index(salesperson)
            #If so, adds the melon sales count to the point in the melons sold list that corresponds to the sales person's sales
            melons_sold[position] += melons
        else:
            #If not, add the sales person and the melons sold to the end of their respective lists.
            salespeople.append(salesperson)
            melons_sold.append(melons)


    for i in range(len(salespeople)):
        print "%s sold %d melons" % (salespeople[i], melons_sold[i])



if __name__ == "__main__":
    main()
