def reverse_elements(l):
    elements=[]
    for i in l:   # def a fun that takes list of word as argument and return list with reverse of every word
        elements.append(i[::-1])
    return elements
words=['saurabh','shree','ram']
print(reverse_elements(words))    