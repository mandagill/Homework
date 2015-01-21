from melons import melon_name, melon_seedless, melon_price

# Need the ability to track flesh color, rind color and weight

def main():

    while True:

        desired_melon = input("Which melon would you like to see information for? > ")

        if desired_melon == 'q' or desired_melon == 'quit':
            break
        elif:
            #TODO wire up this function call after writing and testing fetch_melon_data
            desired_melon in index_of_melons:
                melon_data = fetch_melon_data(desired_melon)
                print "%ss %s seeds and are $%0.2f" % ( name, hashasnot, price)


        else:
            print "I'm sorry\, I don't understand which melon you're looking for.'"


def fetch_melon_data(name):
    #TODO refactor this to take only the key value as a parameter and return a 
    #data structure that will print all the requested data points
    #Need to rework the melon data structure to get *all* the new data points
	
    	
# The following line relies on the tuple values always being in the same order. Suboptimal but 
# simpler to implement than tons of nested dictionaries.
# TODO handle the boolean value in the tuple for each melon; may want to conisder a different 
# data type for the seedless value. 

fetch_melon_data(requested_melon)



if __name__ == '__main__':
    for i in melon_name.keys():
        print_melon(melon_name[i], melon_seedless[i], melon_price[i])
