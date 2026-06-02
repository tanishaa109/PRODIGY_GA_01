# GPT-2 Text Generation and Fine-Tuning

## Overview

This project demonstrates text generation using OpenAI's GPT-2 model with the Hugging Face Transformers library. Users can enter their own prompts and generate contextually relevant text. The generated output is displayed in the terminal and automatically saved to a text file.

Additionally, GPT-2 was fine-tuned on a custom dataset using Google Colab to understand the complete workflow of dataset preparation, tokenization, model training, and text generation.

---

## Features

* GPT-2 based text generation
* User-defined prompt input
* Contextually relevant text generation
* Automatic output saving
* Fine-tuning on a custom dataset
* Google Colab training workflow
* GitHub version control

---

## Technologies Used

* Python
* GPT-2
* Hugging Face Transformers
* PyTorch
* Google Colab
* Git
* GitHub

---

## Project Structure

```text
PRODIGY_GA_01_GPT2_Text_Generation
│
├── app.py
├── dataset.txt
├── fine_tune_gpt2.ipynb
├── README.md
├── requirements.txt
│
├── outputs
│   └── generated_text.txt
│
└── screenshots
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd PRODIGY_GA_01_GPT2_Text_Generation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the application:

```bash
python app.py
```

Enter a prompt when asked:

```text
Enter your prompt:
Artificial Intelligence is
```

Example Output:

```text
Artificial Intelligence is transforming industries by enabling machines to learn from data and make intelligent decisions.
```

The generated output is automatically saved to:

```text
outputs/generated_text.txt
```

---

## Fine-Tuning GPT-2

A custom dataset was created and used to fine-tune GPT-2 using Hugging Face Transformers in Google Colab.

### Fine-Tuning Workflow

1. Create and prepare a custom dataset
2. Load GPT-2 tokenizer and model
3. Tokenize the dataset
4. Configure training parameters
5. Train the model using Hugging Face Trainer API
6. Save the fine-tuned model
7. Generate text using the fine-tuned model

### Training Details

* Model: GPT-2
* Framework: Hugging Face Transformers
* Environment: Google Colab
* Training Method: Fine-Tuning on Custom Dataset

---

## Sample Dataset

Example entries from the custom dataset:

```text
Artificial Intelligence is transforming industries worldwide.
Machine learning enables computers to learn from data.
Deep learning uses neural networks to solve complex problems.
Generative AI can create human-like text.
Python is a popular language for AI development.
```

---

## Screenshots

Project screenshots are available in the `screenshots` folder and include:

* Application execution
* User input and generated output
* Fine-tuning process
* Training results

---

## Note

GitHub may occasionally display a notebook rendering error due to notebook widget metadata.

If the notebook preview does not load correctly:

1. Download `fine_tune_gpt2.ipynb`
2. Open Google Colab
3. Click **File → Upload Notebook**
4. Select the downloaded notebook
5. Run the notebook cells

All training code, dataset preparation steps, fine-tuning implementation, and generated outputs are included in the notebook.

---

## Learning Outcomes

Through this project, I learned:

* Generative AI fundamentals
* GPT-2 architecture and usage
* Text generation techniques
* Dataset preprocessing
* Tokenization
* Model fine-tuning
* Hugging Face Transformers
* Google Colab workflow
* Git and GitHub project management

---

## Internship Task

Task 01 - GPT-2 Text Generation and Fine-Tuning

Completed as part of the Generative AI Internship Program at Prodigy InfoTech.
