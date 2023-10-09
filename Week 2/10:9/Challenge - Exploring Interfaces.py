# #!/usr/bin/env python3

# import netifaces

# print(netifaces.interfaces())

# for i in netifaces.interfaces():
#     print('\n********Details of Interface - ' + i + ' ************')
#     print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
#     print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address


# #!/usr/bin/env python3
# """Alta3 Research | Exploring interfaces library"""

# import netifaces

# print(netifaces.interfaces())

# for i in netifaces.interfaces():
#     print('\n********Details of Interface - ' + i + ' ************')
#     try:
#         print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
#         print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
#     except:          # This is a new line
#         print('Could not collect adapter information') # Print an error message



# #!/usr/bin/env python3
# """Alta3 Research | Exploring interfaces library"""

# import netifaces

# print(netifaces.interfaces())

# for i in netifaces.interfaces():
#     print('\n****** details of interface - ' + i + ' ******')
#     try:
#         print('MAC: ', end='') # This print statement will always print MAC without an end of line
#         print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
#         print('IP: ', end='')  # This print statement will always print IP without an end of line
#         print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
#     except:          # This is a new line
#         print('Could not collect adapter information') # Print an error message


#!/usr/bin/env python3
"""Challenge: Find the MAC and IP of an interface"""

import netifaces

def find_mac(interface_name):
    """Passed interface name (string), returns the MAC of that interface (string)"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_LINK])[0]['addr']    # The MAC address

def find_ip(interface_name):
    """Passed interface name (string), returns the IP of that interface (string)"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_INET])[0]['addr']     # The IP address

def main():
    """Runtime"""
    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try:
            print('MAC:', find_mac(i)) # Display MAC address information for the adapter
            print('IP:', find_ip(i))   # Display IP address information for the adapter
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message

if __name__ == "__main__":
    main()
