# square={1:1,2:4,3:9}
square={f"square of {num} is":num**2 for num in range(1,11)}
for key,value in square.items():
    print(f"{key}:{value}")


# word count
string="Saurabh"
word_count={char: string.count(char) for char in string}
print(word_count)

# if else in dict comprehension
odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)

  