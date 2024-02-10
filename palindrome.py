# Python prgram to check whether the number or word is palindrome or not
def is_palindrome(word):
    reversed_word=word[::-1]
    if word==reversed_word:
        return True
    else:
        return False
    
word=input("Enter the word or a number")
check=is_palindrome(word)
print(f"{check}")    



