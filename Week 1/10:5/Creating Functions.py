import crayons
import yaml

# Function to push commands
def commandpush(devicecmd):
    for device in devicecmd["devices"]:
        ip = device["ip"]
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') 
        # Connect to the device and send the commands here
        for cmd in device["commands"]:
            print(f'Attempting to send command --> {cmd}')

# Function to reboot devices
def devicereboot(ip_list):
    for ip in ip_list:
        print(f"Connecting to {ip}")
        print("REBOOTING NOW!")

# Load device data from YAML file
def load_device_data(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

# Main function
def main():
    """Called at runtime"""

    # Load device data from YAML file
    device_data = load_device_data("device_data.yml")

    print(f"Welcome to the {crayons.blue('Network')} Device Command Pusher") 

    # Run commandpush function
    commandpush(device_data)

    # List of IPs for rebooting
    ip_list = [device["ip"] for device in device_data["devices"]]
    devicereboot(ip_list)

if __name__ == "__main__":
    main()
