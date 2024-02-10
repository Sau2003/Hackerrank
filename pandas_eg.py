import pandas as pd
s1=pd.Series([1,2,3,4,5])
print(s1)
type(s1)

# For alphabetical index
import pandas as pd
s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s1)
type(s1)

# series obj from dict
import pandas as pd
sa=pd.Series({'a':10,'b':20,'c':30})
print(sa)

# changing index in dict
import pandas as pd
sa=pd.Series({'a':10,'b':20,'c':30},index=['b','c','d','a'])
print(sa)

# Extracting a single element
s1=pd.Series([1,2,3,4,5,6,7,8,9])
print(s1[3])

# Extracting a  element from back
s1=pd.Series([1,2,3,4,5,6,7,8,9])
print(s1[-3:])

# Extracting a seq of element
s1=pd.Series([1,2,3,4,5,6,7,8,9])
s2=pd.Series([10,20,30,40,50])
# print(s1[:4])

# Addition 
print(s1+2)
print(s1+s2)