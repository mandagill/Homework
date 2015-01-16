
def check_if_underpaid(a_sales_record):
    
    CUST_NAME = 1
    NUMBER_OF_MELONS = 2
    CUST_PAID = 3
    MELON_COST = 1.00
    
    customer_expected = float(a_sales_record[NUMBER_OF_MELONS]) * MELON_COST
    if customer_expected > float(a_sales_record[CUST_PAID]):
        print a_sales_record[CUST_NAME], "paid %.2f, expected %.2f" % (float(a_sales_record[CUST_PAID]), customer_expected)
    else:
        print "All good, here. "
        

def main():
    
    cust1 = ['#1', 'Joe', 5, 5.0]
    cust2 = ['#2', 'Frank', 6, 6.0]
    cust3 = ['#3', 'Sally', 3, 3.0]

    cust6 = ['#6', 'Ashley', 3, 2.0]

    f = open('customer_orders.csv')

    for each in f:

        current_line = each.split(',')
    check_if_underpaid(current_line)

# This is test data that was hardcoded in the original file. Put some of it in lists so the 
#check_if_underpaid function can use it. 

    # customer1_name = "Joe"
    # customer1_melons = 5
    # customer1_paid = 5.00
    #
    # customer2_name = "Frank"
    # customer2_melons = 6
    # customer2_paid = 6.00
    #
    # customer3_name = "Sally"
    # customer3_melons = 3
    # customer3_paid = 3.00
    #
    # customer4_name = "Sean"
    # customer4_melons = 9
    # customer4_paid = 9.50
    #
    # customer5_name = "David"
    # customer5_melons = 4
    # customer5_paid = 4.00
    #
    # customer6_name = "Ashley"
    # customer6_melons = 3
    # customer6_paid = 2.00

if __name__ == "__main__":
    main()
