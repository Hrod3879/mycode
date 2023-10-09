import requests

# Part 1: Download the Dracula novel and save it as dracula.txt
url = "https://www.gutenberg.org/files/345/345-0.txt"
response = requests.get(url)
if response.status_code == 200:
    with open("dracula.txt", "wb") as file:
        file.write(response.content)
    print("Dracula novel downloaded and saved as dracula.txt.")
else:
    print("Failed to download the Dracula novel.")

# Part 2: Read the content of the Dracula novel as a file object
with open("dracula.txt", "r", encoding="utf-8") as file:
    dracula_content = file.read()

# Part 3: Loop over every line in Dracula and print each line
for line in dracula_content.splitlines():
    print(line)

# Part 4: Print lines containing the word "vampire" (case-insensitive)
for line in dracula_content.splitlines():
    if "vampire" in line.lower():
        print(line)

# Part 5: Count the lines containing the word "vampire" and its occurrences
vampire_count = 0
vampire_occurrences = 0
for line in dracula_content.splitlines():
    if "vampire" in line.lower():
        vampire_count += 1
        vampire_occurrences += line.lower().count("vampire")

print("Number of lines containing 'vampire':", vampire_count)
print("Number of occurrences of 'vampire':", vampire_occurrences)

# Part 6: Write lines with "vampire" to a second file (vampytimes.txt)
with open("vampytimes.txt", "w", encoding="utf-8") as vampy_file:
    for line in dracula_content.splitlines():
        if "vampire" in line.lower():
            vampy_file.write(line + "\n")
