from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"

tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

prompt = "Artificial Intelligence is"

inputs = tokenizer.encode(prompt, return_tensors="pt")

outputs = model.generate(
    inputs,
    max_length=100,
    num_return_sequences=1,
    temperature=0.7,
    do_sample=True
)

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)

with open("outputs/generated_text.txt", "w", encoding="utf-8") as file:
    file.write(generated_text)