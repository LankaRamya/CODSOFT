def simple_chatbot(user_input):
    user_input = user_input.lower() # Convert user input to lowercase for easier matching

    if "hello" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here and ready to assist you!"

    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    elif "thank you" in user_input:
        return "You're welcome! If you have more questions, feel free to ask."

    else:
        return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

# Main loop for interacting with the chatbot
def main():
    print("Chatbot: Hi there! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
