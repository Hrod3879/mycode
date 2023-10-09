'''
Author Hrod
What is your name?

“Python is a _________ language that lets you _______ more _______ and integrate your ________ more effectively.

You can learn to _________ Python and see almost _________  _________ in productivity and _______  maintenance costs.”
'''

# Greet User
print("What is your name?")
name = input()
print(f"Hello {name}!")

# First function getting 4 variables from user, then combine them into a sentence 
def first_sentence():
    print("Python is a _________ language")
    adj = input()
    print("that lets you _______ more")
    verb1 = input()
    print("more _______ and integrate")
    verb2 = input()
    print("and integrate your ________ more effectively.")
    object1 = input()
    return(f"Python is a {adj} language that lets you {verb1} more {verb2} and integrate your {object1} more effectively.")

# Second function getting 4 variables from user, then combine them into a sentence 
def second_sentence():
    print("You can learn to _________ Python")
    verb3 = input()
    print("see almost _________")
    adj1 = input()
    print(" _________ in productivity")
    verb4 = input()
    print("and _______  maintenance costs.")
    verb5 = input()
    return(f"Python is a {verb3} language that lets you {adj1} more {verb4} and integrate your {verb5} more effectively.")


print(first_sentence())
print(second_sentence())


