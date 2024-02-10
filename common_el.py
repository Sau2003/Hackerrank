def common_finder(l1,l2):
    output=[]                  # def a fun which takes two list as a input and return a list containg common elements
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(common_finder([1,2,3,4,5,7,9],[1,7,8,3]))        