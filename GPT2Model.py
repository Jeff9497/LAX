from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Function to generate text
def generate_text(prompt):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    attention_mask = torch.ones(inputs.shape, dtype=torch.long)
    outputs = model.generate(
        inputs,
        attention_mask=attention_mask,  # Add this line to explicitly pass the attention mask
        max_length=100,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        repetition_penalty=2.0  # Adding repetition_penalty to reduce repetitive outputs
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# Welcome message
print("Welcome to LAX chat! Let's talk.")

# Chat loop
while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        response = generate_text(user_input)
        print(f"LAX28: {response}")

    except KeyboardInterrupt:
        print("\nGoodbye!")
        break
