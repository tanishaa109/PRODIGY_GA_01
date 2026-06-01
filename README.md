# GPT-2 Text Generation and Fine-Tuning

## Overview

This project demonstrates text generation using OpenAI's GPT-2 model with the Hugging Face Transformers library. Users can enter their own prompts and generate contextually relevant text. The generated output is displayed on the screen and saved to a text file.

Additionally, GPT-2 was fine-tuned on a custom dataset using Google Colab to understand the model training workflow.

---

## Features

* User-based text generation
* GPT-2 pretrained model integration
* Custom prompt input
* Automatic output saving
* Fine-tuning on a custom dataset
* GitHub version control

---

## Technologies Used

* Python
* Hugging Face Transformers
* PyTorch
* Google Colab
* GPT-2
* Git & GitHub

---

## Project Structure

PRODIGY_GA_01_GPT2_Text_Generation

├── app.py

├── dataset.txt

├── fine_tune_gpt2.ipynb

├── README.md

├── requirements.txt

├── outputs

│ └── generated_text.txt

└── screenshots

---

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run the application:

python app.py

3. Enter a prompt when prompted.

Example:

Enter your prompt:
Artificial Intelligence is

4. View the generated text in the terminal.

5. Generated output is automatically saved in:

outputs/generated_text.txt

---

## Fine-Tuning

A custom dataset was created and used to fine-tune GPT-2 using Hugging Face Transformers in Google Colab.

Training Process:

* Dataset Preparation
* Tokenization
* Model Training
* Text Generation Testing

---

## Sample Output

Prompt:
Artificial Intelligence is

Generated Output:
Artificial Intelligence is transforming industries by enabling machines to learn from data and make intelligent decisions.

---

## Internship Task

Task 01 - GPT-2 Text Generation and Fine-Tuning

Completed as part of the Generative AI Internship Program at Prodigy InfoTech.
