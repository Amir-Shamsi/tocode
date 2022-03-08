import tocode

"""
literal eval function will convert strings which contain:
 - lists
 - tuples
 - dictionaries
 - sets
into the literal eval 
"""

my_string = "{'this': 5, (Alex, Daniel): are good boys, (5, 4): 8.5}"

# you must call the function literal_eval
"""
:argument no_string_quotation: if your strings may not have a quotation
                                like `Alex, Daniel and are good boys`
                                so set it True otherwise leave it.
"""
my_dict = tocode.literal_eval(my_string, no_string_quotation=True)
# now my_dict has the dictionary we want
print(my_dict)

print((my_dict['this']))
print((my_dict[('Alex', 'Daniel')]))
print((my_dict[(5, 4)]))

# enjoy!