def reverse_elements(l):
   r_list=[]
   for i in range(len(l)):
      popped_item=l.pop()                  # def a fun that takes list as a input and returns reveesed list
      r_list.append(popped_item)
   return r_list 
numbers=[1,2,3]
print(reverse_elements(numbers))

     