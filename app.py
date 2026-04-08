import streamlit as st
import os
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="Retail Strategy AI", page_icon="🛍️")
st.title("🛍️ Retail Strategy & Management Assistant")
st.write("Powered by Gemma 2. Ask me about inventory optimization, omnichannel strategy, or market analysis.")

# 2. Securely load the API key from Streamlit Secrets
# (We will set this up in Step 4)
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
client = Groq()

# 3. Define the System Persona
system_prompt = """You are an expert management consultant specializing in the retail domain. 
Provide structured, analytical, and actionable advice. Use frameworks where appropriate."""

# 4. User Interface
user_input = st.text_area("Enter your business scenario or question:")

if st.button("Generate Strategy"):
    if user_input:
        with st.spinner("Analyzing..."):
            # Call the free Gemma model hosted on Groq
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                model="gemma2-9b-it", # Specifying the Gemma model
                temperature=0.7,
                max_tokens=1024,
            )
            
            # Display the result
            result = chat_completion.choices[0].message.content
            st.success("Analysis Complete!")
            st.markdown(result)
    else:
        st.warning("Please enter a query first.")
