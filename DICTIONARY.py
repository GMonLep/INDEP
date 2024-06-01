"""How to create a dictonary in Python.

You use the dict() function in Python to create a dictionary. This function takes two arguments:

  - The first argument is a list of keys.

  - The second argument is a list of values.

Keys must be made up of only one element.
Values can be of any type, including list, tuple, integer, and so on.
   dictionary_example={"a":harry, "b": carry}

a and b would be keys, whereas harry and carry would be values

"""

# empty dictionary
my_dict = {}


# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}


# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}


# using dict()
my_dict = dict({1:'apple', 2:'ball'})


# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
