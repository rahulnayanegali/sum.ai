import json
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load Hugging Face token
config_data = json.load(open("config.json"))
HF_TOKEN = config_data["HF_TOKEN"]

model_name = "meta-llama/Llama-2-7b-hf"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=HF_TOKEN)

# Save the model and tokenizer locally
local_model_path = "./local_llama2_model"
tokenizer.save_pretrained(local_model_path)
model.save_pretrained(local_model_path)

print("Model and tokenizer have been saved locally.")
