# Course code below 
# #!/usr/bin/env python3
# proto = ["ssh", "http", "https"]
# protoa = ["ssh", "http", "https"]
# print(proto)
# proto.append("dns") # this line will add "dns" to the end of our list
# protoa.append("dns") # this line will add "dns" to the end of our list
# print(proto)
# proto2 = [ 22, 80, 443, 53 ] # a list of common ports
# proto.extend(proto2) # pass proto2 as an argument to the extend method
# print(proto)
# protoa.append(proto2) # pass proto2 as an argument to the append method
# print(protoa)



"""
CHALLENGE 01 - Continue writing the script listmethods/listmeth02.py so that it demonstrates AT LEAST one of the methods found on https://docs.python.org/3/tutorial/datastructures.html

Be sure to meet the following criteria:

    Program must run in python3
    Use lots of comments to describe what you're doing-- or what you WANT to do, even if you don't know how to do it yet
    Feel free to use more than one method to manipulate your list data
    You can create a new list if you like
    Add some text to the print statements you use to describe your data (you can make up labels however you wish)
    Contact the instructor if you struggle figuring out how to use methods
"""

#!/usr/bin/env python3

# 2 lists
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

# Print lists
print("Initial proto list:", proto)
print("Initial protoa list:", protoa)

# Append "dns" to both lists
proto.append("dns")
protoa.append("dns")

# Print the lists
print("proto after appending 'dns':", proto)
print("protoa after appending 'dns':", protoa)

# Create a list of ports
proto2 = [22, 80, 443, 53]

# Extend the 'proto' list with proto2
proto.extend(proto2)

# Print the proto
print("proto after extending with proto2:", proto)

# Reset 'proto' and 'protoa'
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

# Append 'proto2' as a single element to 'protoa' using the append method
protoa.append(proto2)

# Print the 'protoa' list after appending 'proto2' as a single element
print("protoa after appending proto2 as a single element:", protoa)

# Challenge
# Use count method
count_in_proto = proto.count("http")
count_in_protoa = protoa.count("http")

# Print the counts
print("Count of 'http' in proto:", count_in_proto)
print("Count of 'http' in protoa:", count_in_protoa)

# Use index method
index_in_proto = proto.index("https")
index_in_protoa = protoa.index("https")

# Print the indices
print("Index of 'https' in proto:", index_in_proto)
print("Index of 'https' in protoa:", index_in_protoa)

