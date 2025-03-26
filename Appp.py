import streamlit as st

from openai import OpenAI  # Updated import

import os

from typing import List

 

# ========== Initialize OpenAI Client ==========

client = OpenAI(api_key="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")  # Updated initialization

 

# ========== Streamlit App Title ==========

st.set_page_config(page_title="Nutrient AI System", page_icon="🍎", layout="wide")

st.title("🍎 Nutrient AI 💊")

 

# ========== Sidebar ==========

st.sidebar.title("What would you like to do?")

option = st.sidebar.selectbox("Choose an option:", ("Chat with AI", "Generate Image"))

 

# Add a button to clear conversation history

if st.sidebar.button("Clear Conversation History"):

    st.session_state.conversation_history = []

 

# ========== Block 1: Few-Shot Prompting Function With Memory ==========

if "conversation_history" not in st.session_state:

    st.session_state.conversation_history = [

        {"role": "system", "content": "You are a helpful and knowledgeable AI system that provides nutritional advice and meal suggestions based on user needs and allergies."}

    ]

 

def update_conversation(role: str, content: str):

    """Store conversation history for memory."""

    st.session_state.conversation_history.append({"role": role, "content": content})

    # Optional: Limit conversation history to last N messages

    if len(st.session_state.conversation_history) > 20:  # Keep last 20 messages

        st.session_state.conversation_history = st.session_state.conversation_history[-20:]

 

# ========== Block 2: Chatbot Interaction ==========

if option == "Chat with AI":

    st.header("💬 Chat with the AI")

    user_input = st.text_input("Enter your question or request:")

 

    if st.button("Send") and user_input:

        # Add the user's message to the conversation history

        update_conversation("user", user_input)

       

        try:

            # Send the conversation history to the model (updated API call)

            response = client.chat.completions.create(

                model="gpt-4",

                messages=st.session_state.conversation_history

            )

           

            # Extract the AI's response (updated syntax)

            chatbot_response = response.choices[0].message.content

           

            # Display the response

            st.success(f"AI: {chatbot_response}")

           

            # Store the AI's response in the conversation history

            update_conversation("assistant", chatbot_response)

 

        except Exception as e:

            st.error(f"Error: {e}")

 

    # Display conversation history

    st.subheader("Conversation History")

    for msg in st.session_state.conversation_history[1:]:  # Skip system message

        st.text(f"{msg['role'].capitalize()}: {msg['content']}")

 

# ========== Block 3: Text-to-Image Generation ==========

if option == "Generate Image":

    st.header("🖼️ Generate an Image with AI")

    description = st.text_input("Describe the image you want to generate:")

 

    if st.button("Generate Image") and description:

        try:

            response = client.images.generate(  # Updated API call

                prompt=description,

                n=1,

                size="512x512"

            )

            image_url = response.data[0].url  # Updated syntax

            st.image(image_url, caption="Generated Image", use_column_width=True)

 

        except Exception as e:

            st.error(f"Error: {e}")