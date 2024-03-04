from transformers import AutoTokenizer, AutoModelForCausalLM

import yaml

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

config = read_config('config.yml')

hf_token = config['HF_TOKEN']


tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b", token=hf_token)
model = AutoModelForCausalLM.from_pretrained("google/gemma-7b", token=hf_token)

input_text = "Write me a poem about Reinforcement Learning."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))
