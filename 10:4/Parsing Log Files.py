# Initialize the counter
failed_login_count = 0

# Open the log file for reading
with open('keystone.log', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Check if the line contains the desired expression
        if '- - - - -] Authorization failed' in line:
            # Increment the counter
            failed_login_count += 1

# Display the final count of failed logins
print(f"Number of failed logins: {failed_login_count}")