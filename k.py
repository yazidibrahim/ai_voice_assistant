from hugchat import hugchat

def chatBot(query):
    try:
        user_input = query.lower()
        chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)
        response = chatbot.chat("give answer in 1 sentence: " + user_input)
        return str(response).strip()  # Ensure the response is converted to a string and stripped
    except Exception as e:
        print("Error in chatBot:", e)
        return ""  # Return empty string on error

def decisionModel(user_input):
    # Define keywords or rules to differentiate between Query and Automation
    query_keywords = ["who", "what", "where", "when", "how"]
    automation_keywords = ["open", "close", "play", "stop", "search"]

    # Check if the user input indicates a Query or Automation
    if any(keyword in user_input.lower() for keyword in query_keywords):
        return "Query"
    elif any(keyword in user_input.lower() for keyword in automation_keywords):
        return "Automation"
    else:
        return "Unknown"  # Handle other cases if needed

def handleQuery(user_input):
    # Handle Query by calling chatBot to get the response
    response = chatBot(user_input)
    return response

def handleAutomation(user_input):
    # Handle Automation based on specific tasks or commands
    if "open" in user_input.lower():
        # Perform the action (e.g., open Chrome)
        print("Opening Chrome...")
        return "Opening Chrome..."
    elif "play" in user_input.lower():
        # Perform the action (e.g., play music)
        print("Playing music...")
        return "Playing music..."
    else:
        return "Unknown automation command"

def processInput(user_input):
    # Determine the intent of the user input
    intent = decisionModel(user_input)

    # Perform action based on the detected intent
    if intent == "Query":
        response = handleQuery(user_input)
    elif intent == "Automation":
        response = handleAutomation(user_input)
    else:
        response = "Intent not recognized"

    return response

# Example usage:
def main():
    while True:
        user_input = input("User: ")  # User input
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = processInput(user_input)
        if response:
            print("Chatbot:", response)  # Print the response if it's not empty

if __name__ == "__main__":
    main()
'''
instructions_L1 = """
    You are the Decision Making Model.
    Select one of the options below:
    -> 'Query' if the input is a question that the chatbot should answer.
    -> 'Automation' if the input is an instruction related to performing tasks.
    ***The output should be only one word***
    Example (1): hello, can you open Chrome for me?
    Example Output (1): Automation
    Example (2): Who is Akshay Kumar?
    Example Output (2): Query
    """

    instructions_L2 = """
    Today is 15/03/2024.
    You are the Decision Making Model.
    Select one of the options below:
    -> 'Before' if the information is before 07/02/2023 (past events or chatbot responses).
    -> 'After' if the information is after 07/02/2023 (future events or current information).
    ***The output should be only one word***
    Example (1): Who was Akbar?
    Example Output (1): Before
    Example (2): Who is currently working as CEO of Microsoft?
    Example Output (2): After
    """

    # Determine the appropriate instruction set based on the prompt
    if "15/03/2024" in prompt:
        instructions = instructions_L2
    else:
        instructions = instructions_L1

    # Format the prompt with the appropriate instruction set
    formatted_prompt = f"{prompt} {instructions}"
    return formatted_prompt
'''