# Author: HROD
#!/usr/bin/env python3
"""Friday Warmup | Trivia Game using Open Trivia Database API"""

import requests

# Define the API URL with specific parameters
URL = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=boolean"

# Function to fetch trivia questions from the API
def get_trivia_questions(api_url):
    # Send a GET request to the API URL
    response = requests.get(api_url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the response JSON data
        data = response.json()
        return data
    else:
        print("Failed to retrieve data from the API.")
        return None

# Function to present a trivia question and get the user's answer
def ask_question(question, choices):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    user_answer = input("Your answer (enter the number): ")
    return user_answer

# Main function to run the trivia game
def main():
    # Get trivia questions from the API using the specified URL
    data = get_trivia_questions(URL)

    if data:
        # Extract the list of questions from the API response
        questions = data.get("results", [])
        correct_answers = 0  # Initialize a counter for correct answers

        for i, question in enumerate(questions, start=1):
            # Ask the question and get the user's answer
            user_answer = ask_question(question["question"], question["incorrect_answers"] + [question["correct_answer"]])

            try:
                user_answer = int(user_answer)
                # Check if the user's answer is correct
                if user_answer == len(question["incorrect_answers"]) + 1:
                    print("Correct!\n")
                    correct_answers += 1  # Increment the correct answer counter
                else:
                    print(f"Wrong! The correct answer is: {question['correct_answer']}\n")
            except ValueError:
                print("Invalid input. Please enter the number corresponding to your choice.\n")

        # Display the final score
        print(f"You answered {correct_answers}/{len(questions)} questions correctly.")

# Entry point of the script
if __name__ == "__main__":
    main()
