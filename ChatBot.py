import google.generativeai as genai
import gradio as gr

# Set up Gemini API Key
genai.configure(api_key="API_KEY")

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash-lite")

# Message history
messages = [{"role": "system", "content": "You are a helpful AI Assistant."}]

def chatbot(user_input):
    if not user_input.strip():
        return "⚠️ Please enter a valid message."

    messages.append({"role": "user", "content": user_input})
    
    try:
        response = model.generate_content(user_input)
        reply = response.text  # Extract response text

        messages.append({"role": "assistant", "content": reply})
        return reply

    except Exception as e:
        return f"❌ Error: {str(e)}"

# Gradio UI
inputs = gr.Textbox(lines=7, label="Chat with AI")
outputs = gr.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Gemini Chatbot PowerBy Kalpesh Parmar",
             description="Chat with Google AI (Gemini2.0)").launch(share=True)
