#!/usr/bin/python3

!pip install gradio openai

import openai
import gradio as gr

# Replace with your actual OpenAI API key
OPENAI_API_KEY = "your_openai_api_key"
openai.api_key = OPENAI_API_KEY

def generate_code(prompt, model='gpt-3.5-turbo', max_tokens=100, n=1, temperature=0.7):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        temperature=temperature
    )
    return response.choices[0].text.strip()

def chatbot(prompt):
    model = 'gpt-3.5-turbo'  # You can change this to 'gpt-4' if you prefer
    generated_text = generate_code(prompt, model=model)
    return generated_text

if __name__ == "__main__":
    input_text = gr.inputs.Textbox(lines=5, label="Enter your prompt")
    output_text = gr.outputs.Textbox(label="Generated response")

    gr.Interface(fn=chatbot, inputs=input_text, outputs=output_text, title="Code Generation Chatbot").launch()
