#!/usr/bin/python3 
"""
CHALLENGE
Use Paramiko to create an SFTP session and transport files into a directory determined by the user
"""

import paramiko  # Allows Python to SSH
import os  # Low-level operating system commands
import getpass  # Used to accept passwords

def transfer_to_remote_dir():
    """Ask the user for the full path of the directory to transfer files to."""
    while True:
        remote_dir = input("What directory on the remote host would you like to transfer files to (default: /tmp/)? ")
        if not remote_dir:
            remote_dir = "/tmp/"
            break
        elif remote_dir.startswith("/") and remote_dir.endswith("/"):
            break
        print("You must enter a full path for the remote host. Full paths must begin and end with '/'.")
    return remote_dir

def move_files_to_remote(sftp):
    """Move files across an SFTP Paramiko channel."""
    remote_dir = transfer_to_remote_dir()

    local_dir = "/home/student/filestocopy/"
    
    for filename in os.listdir(local_dir):
        if not os.path.isdir(os.path.join(local_dir, filename)):
            sftp.put(os.path.join(local_dir, filename), os.path.join(remote_dir, filename))

def main():
    """Runtime"""
    # Define the connection details
    hostname = "10.10.2.3"
    port = 22
    username = "bender"

    # Connect using a password (you can modify this for key-based authentication)
    password = getpass.getpass("Enter your password: ")

    try:
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=password)

        # Create an SFTP connection object
        sftp = transport.open_sftp()

        # Call the function to move files
        move_files_to_remote(sftp)

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'sftp' in locals():
            sftp.close()
        transport.close()

if __name__ == "__main__":
    main()
