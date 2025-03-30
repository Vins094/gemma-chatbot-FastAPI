# model_utils.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from config import MODEL_NAME, HF_TOKEN_FILE_PATH

# Step 1: Read Hugging Face Token from a File
def read_hf_token(file_path=HF_TOKEN_FILE_PATH):
    with open(file_path, "r") as file:
        return file.read().strip()

# Load Hugging Face Token
HF_TOKEN = read_hf_token()

# Step 2: Load the Gemma Model and Tokenizer
def load_model_and_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, 
        torch_dtype=torch.bfloat16, 
        token=HF_TOKEN
    )
    return model, tokenizer

# Function to generate a response based on the model
def generate_response(query, model, tokenizer):
    # Tokenize the input query with attention mask
    inputs = tokenizer(query, return_tensors="pt", padding=True, truncation=True, max_length=512)

    # Ensure model has a proper pad_token_id
    if model.config.pad_token_id is None or model.config.pad_token_id == model.config.eos_token_id:
        model.config.pad_token_id = tokenizer.pad_token_id  # Assign a distinct padding token

    # Generate response using the model
    output = model.generate(
        input_ids=inputs['input_ids'],
        attention_mask=inputs['attention_mask'],  # Explicitly pass attention mask
        max_length=100,
        num_return_sequences=1,
        pad_token_id=model.config.pad_token_id  # Use model's pad_token_id
    )

    # Decode the output to a human-readable format
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Post-processing to avoid repetition of the input in the response
    response = response.replace(query, "").strip()

    return response

