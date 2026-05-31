from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Artificial Intelligence is"

result = generator(
    prompt,
    max_length=100,
    num_return_sequences=1
)

generated_text = result[0]["generated_text"]

print(generated_text)

with open("outputs/generated_text.txt", "w", encoding="utf-8") as file:
    file.write(generated_text)

print("\nOutput saved to outputs/generated_text.txt")