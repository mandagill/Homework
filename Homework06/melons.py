# Need the ability to track flesh color, rind color and weight
# Let's nest some dictionaries, eh?
# Using a tuple since it's immutablem so querying on index will be (a bit more) reliable.

# Tuple values: 0=price, 1=flesh color, 2=rind color, 3=weight, 4=seedless?

melons = {
    'Honeydew': (0.99, 'green', 'pale green', '2 lbs', True),
    'Crenshaw': (2.00, None, None, '1.5 lbs', False),
    'Crane': (2.50, None, None, '1 lb', False),
    'Casaba': (2.50, None, None, '4 lb', False),
    'Cantaloupe': (0.99, 'orange', 'tan', '1.5 lb', False)
    
}
