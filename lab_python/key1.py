#e1
x = 5
x **= 2 


#e
#a and b
#> b #The program evaluates a, a is truthy, it evaluates b, b is truthy, so it returns the last evaluated value, b.
#a or b
#> a #The program evaluates a, a is truthy, so the or statement is true, so it returns the last evaluated value, a.


del d['fish']        # Remove an element from a dictionary
print(d.get('fish', 'N/A')) 

import numpy as np
a = np.array([True, False, False])
b = np.array([True, True, False])
a & b
#array([ True, False, False], dtype=bool)
a | b
#array([ True,  True, False], dtype=bool)


a= np.random.random((3,3)) 
b= np.eye((3))
print(a)
a*b

#
even_squares = [x +10 for x in nums if x % 2 == 0]
print(even_squares)

# key in lab: list comprehension
import numpy as np
a = np.arange(10,20, 2)
a1 = [x*1.5 for x in a if x%2==0]
a1 = [x for x in a1 if x>20]
a1
list(filter(lambda n: n>20, list(map(lambda x: x*1.5, filter(lambda n: n%2 == 0, a)))))
