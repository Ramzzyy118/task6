def simple_chatbot():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi there!")
        elif user_input == "how are you?":
            print("Bot: I'm just a bot, but I'm doing great!")
        elif user_input == "what's your name?":
            print("Bot: I'm a simple chatbot!")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

simple_chatbot()
