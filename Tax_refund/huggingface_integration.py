from transformers import pipeline

# Load a pre-trained text generation model from Hugging Face (e.g., GPT-2)
generator = pipeline("text-generation", model="gpt2")

# Function to generate a tax summary using GPT-2
def generate_tax_summary(refund_amount):
    prompt = f"Explain a tax refund of ${refund_amount} in simple terms."
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']
