from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, trust_remote_code=True, device_map="auto")

def ask_model(prompt, max_tokens=512):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=0.2,
        do_sample=False
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
