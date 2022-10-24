# You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
def correct_sentence(text: str) -> str:
    # your code here
   
    return None


print("Example:")
print(correct_sentence("happy Diwali."))


 # These "asserts" are used for self-checking and not for an auto-testing

assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
assert correct_sentence("hi") == "Hi."
assert correct_sentence("happy Diwali") == "Happy Diwali."
assert correct_sentence("welcome to my repo") == "Welcome to my repo."
assert correct_sentence("happy coding") == "Happy coding."


print("The mission is done! ")

# expected output: 
#Happy Diwali.
#The mission is done!