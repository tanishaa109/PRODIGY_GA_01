from transformers import pipeline

def main():
    print("=== GPT-2 Text Generation App ===")

    # Load model
    generator = pipeline("text-generation", model="gpt2")

    # Take user input
    prompt = input("\nEnter your prompt: ")

    # Generate text
    result = generator(
        prompt,
        max_length=80,
        num_return_sequences=1
    )

    generated_text = result[0]["generated_text"]

    print("\n=== Generated Output ===\n")
    print(generated_text)

    # Save output to file
    with open("outputs/generated_text.txt", "a", encoding="utf-8") as f:
        f.write("\n" + "="*50 + "\n")
        f.write("PROMPT: " + prompt + "\n")
        f.write("OUTPUT:\n" + generated_text + "\n")

    print("\n✔ Output saved to outputs/generated_text.txt")


if __name__ == "__main__":
    main()