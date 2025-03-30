
# DermaBot - Chatbot using FastAPI and Gemma Model 

## Description

**DermaBot** is an AI-powered chatbot built using the **Gemma Model** from Hugging Face and served through **FastAPI**. This bot provides intelligent conversational capabilities.

### Features:
- Powered by **Gemma-2B-IT** (a large pre-trained model)
- Natural language conversation flow
- FastAPI backend for scalable deployment
- Two interaction modes:
  - Direct testing via `chatbot.py` (VSCode/local testing)
  - API endpoint via `main.py` (production deployment)
- Context-aware responses
- Easy integration with Hugging Face models

## Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **Hugging Face Transformers**: Library for state-of-the-art NLP models
- **PyTorch**: Deep learning framework
- **Uvicorn**: ASGI server for FastAPI
- **Python 3.10+**: Primary programming language

## Project Structure
├── .gitignore
├── LICENSE
├── README.md
├── chatbot.py # Local testing script
├── config.py # Configuration settings
├── hf_token.txt # Hugging Face token storage
├── main.py # FastAPI application
├── model_utils.py # Model helper functions
├── requirements.txt # Dependencies


## Setup Instructions

### Prerequisites

1. Python 3.10 or later
2. Hugging Face account with access to Gemma models
3. Valid Hugging Face token

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Your location/to clone repository.git
   cd Project_folder
   
2. Create and activate virtual environment:
    python -m venv myenv
	activate myenv 
	
3. Install dependencies:
      pip install -r requirements.txt
	  
4. Add your Hugging Face token to hf_token.txt


## Runing the code
1. For local testing in vscode 
     python chatbot.py
2. For API model
     uvicorn main:app --reload
	 Access the API at http://localhost:8000
	 API Endpoints
     POST /chat: Main conversation endpoint

     GET /docs: Interactive API documentation
	 

## Example conversation 
  {
  "response": "Artificial intelligence (AI) is the ability of a computer or machine to perform tasks that typically require human intelligence...",
  "conversation_history": [
    "DermaBot: How can I assist you today?",
    "User: What is AI?",
    "DermaBot: Artificial intelligence (AI) is the ability..."
  ]
} 