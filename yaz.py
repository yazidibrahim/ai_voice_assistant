from hugchat import hugchat
from engine.features import chatBot
           
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

def Mixtral7B(prompt, instructions, temperature=0.1, max_new_token=2, top_p=0.95):
    try:
        response = chatBot(prompt)
        if response:
            return response
        else:
            print("Error: Empty response from chatBot.")
            return ""  # Return empty string if response is empty
    except Exception as e:
        print("Error in Mixtral7B:", e)
        return ""  # Return empty string on error

def decisionModel(prompt):
    instructions_query = """
    You are the Decision Making Model.
    If the user asks a question or seeks information, the model should provide an answer.
    Example: "Who is the Prime Minister of Canada, what is an apple, where is,how,why,tell me"
    """

    instructions_task = """
    You are the Decision Making Model.
    If the user gives an instruction or requests an action, the model should reply sorry i can't do that,we are working for that.
    Example: "Please set a reminder for tomorrow."
    Example(output): "sorry i can't do that,we are working for that."
    """

    # Determine the type of input (query or task) based on the prompt

    if "what" or "where" or "who" in prompt.lower() or "?" in prompt:
        instructions = instructions_query
    else:
        instructions = instructions_task

    # Format the prompt with the appropriate instructions
    formatted_prompt = f"{prompt}\n{instructions}"
    return formatted_prompt

def L1(prompt):
    formatted_prompt = decisionModel(prompt)
    response = Mixtral7B(formatted_prompt, instructions=None)  # Use None for instructions
    return response

# Example usage:
def main():
    user_prompt = input("User: ")  # User input
    result = L1(user_prompt)
    print("Chatbot:", result) 

if __name__ == "__main__":
    main()
