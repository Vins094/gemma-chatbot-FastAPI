# chatbot.py
from model_utils import load_model_and_tokenizer, generate_response

def derma_bot():
    print("Hi, I am DermaBot. What is your name?")
    
    # Capture the user's name for personalized interaction
    user_name = input("You: ")
    
    print(f"Nice to meet you, {user_name}! How can I assist you today?")

    # Load the model and tokenizer
    model, tokenizer = load_model_and_tokenizer()

    while True:
        # Get user input
        user_input = input(f"You: ")

        # If user says 'exit' or 'bye', end the conversation
        if user_input.lower() in ["exit", "bye", "quit", "stop"]:
            print(f"DermaBot: Goodbye {user_name}! Have a great day!")
            break

        # Generate a response based on the user query
        response = generate_response(user_input, model, tokenizer)

        # Output the bot's response
        print(f"DermaBot: {response}")

# Step 4: Start Chat
if __name__ == "__main__":
    derma_bot()
