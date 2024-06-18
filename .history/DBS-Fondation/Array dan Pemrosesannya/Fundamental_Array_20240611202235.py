# Fundamental Array

x = [1, 2, 3, 4, 5]
print(x)

"""
Output:
[1, 2, 3, 4, 5]
"""

import array

x = array.array("i",[1, 2, 3, 4, 5])
print(x)
print(type(x))

"""
Output:
array('i', [1, 2, 3, 4, 5])
<class 'array.array'>
"""