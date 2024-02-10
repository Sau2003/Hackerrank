# # double star operator 
# # dict dega

# def func(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
# # print(func(first_name='saurabh',last_name='kuche'))        
# d={'name':'saurabh','age': '19'}
# print
# print(func(**d))        

# order is very imp in kwargs
def func(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('Saurabh',1,2,3,a=1,b=2)    
