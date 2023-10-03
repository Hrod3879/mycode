# #!/usr/bin/env python3
# """Alta3 Research | RZFeeser
#    List - making selections from complex lists"""

# def main():

#     # create a list called list1
#     list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

#     # display list1
#     print(list1)

#     # display list1[1] which should only display arista_eos
#     print(list1[1])

#     # create a new list containing a single item
#     list2 = ["juniper"]

#     # extend list1 by list2 (combine both lists together into a single list)
#     list1.extend(list2)

#     # display list1, which now contains juniper
#     print(list1)

#     # create list3
#     list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

#     # use the append operation to append list1 by list3
#     list1.append(list3)

#     # display the new complex list1
#     print(list1)

#     # display the list of IP addresses
#     print(list1[4])

#     # display the first item in the list (0th item) - first IP address
#     print(list1[4][0])

# main()

"""
CHALLENGE: Create a list of at least five animals with three letter names and have your program output them to the screen. No need to be fancy, just load some animals in a list, and print them out, like the list below. If you get stuck, as the instructor for some help. When you finish. Save your code as /home/student/mycode/advlist/animal-list.py

Fox Fly Ant Bee Cod Cat Dog Yak Cow Hen Koi Hog Jay Kit
"""

# Create a list of animals with three-letter names
animal_list = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Cow", "Hen", "Koi", "Hog", "Jay", "Kit"]

# Print the list of animals
for animal in animal_list:
    print(animal, end=" ")

# Add a newline character at the end to separate the output
print()
