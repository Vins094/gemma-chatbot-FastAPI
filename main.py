from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model_utils import load_model_and_tokenizer, generate_response

# Initialize FastAPI app
app = FastAPI()

# Load the model and tokenizer globally
model, tokenizer = load_model_and_tokenizer()

# In-memory storage for conversation history (to simulate sessions)
conversation_history = {}

# Define the structure of the user query request
class QueryRequest(BaseModel):
    query: str  # User's query
    session_id: str  # To track the user session

# Greeting function to personalize the chat
def get_greeting(session_id):
    if session_id not in conversation_history:
        return "Hi, I am DermaBot. What is your name?"
    else:
        return "How can I assist you today?"

# Function to check if the conversation should end
def should_end_conversation(user_input):
    end_words = ["exit", "bye", "quit", "stop"]
    return any(word in user_input.lower() for word in end_words)

# POST endpoint to handle chat requests
@app.post("/chat")
async def chat(query_request: QueryRequest):
    try:
        # Retrieve the query and session ID from the request
        user_query = query_request.query
        session_id = query_request.session_id

        # Initialize conversation history if it's a new session
        if session_id not in conversation_history:
            conversation_history[session_id] = []

            # Start with a greeting if it's a new session
            greeting = get_greeting(session_id)
            conversation_history[session_id].append(f"DermaBot: {greeting}")
            return {"response": greeting, "conversation_history": conversation_history[session_id]}

        # If session exists, continue the conversation
        history = conversation_history[session_id]
        history.append(f"User: {user_query}")

        # Check if the user wants to end the conversation
        if should_end_conversation(user_query):
            goodbye_message = f"DermaBot: Goodbye! Have a great day!"
            history.append(goodbye_message)
            conversation_history[session_id] = history  # Save the conversation history
            return {"response": goodbye_message, "conversation_history": history}

        # Generate the response from the chatbot
        bot_response = generate_response(user_query, model, tokenizer)
        history.append(f"DermaBot: {bot_response}")

        # Save the updated conversation history
        conversation_history[session_id] = history

        # Return the bot's response along with the conversation history
        return {"response": bot_response, "conversation_history": history}

    except Exception as e:
        # Handle exceptions if something goes wrong
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

# Run the FastAPI server with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)




