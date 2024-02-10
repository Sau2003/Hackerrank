import time

def time_calculate(func):
    def modify(*args,**kwargs):
        start=time.time()
        a=func(*args,**kwargs)                                     # Time required to complete the execution 
        end=time.time()
        time_req=end-start                                         # using time func
        print(f"Time required to execute is {time_req}")
        return a
    return modify

@time_calculate
# def fac_num(num):
#     if num==0:
#         return 1                                         # Using recursion
#     else:
#         return num*fac_num(num-1)

# print(fac_num(5))
def factorial(n):
    f = 1
    for i in range(1, n + 1):                                # Without recursion
        f=f*i
    return f

print(factorial(5))
