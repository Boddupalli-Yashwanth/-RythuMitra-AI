import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
import streamlit as st

st.set_page_config(
    page_title="RythuMitra AI",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 RythuMitra AI")

st.subheader("Your Intelligent Farming Companion")

st.success("Welcome to RythuMitra AI!")

st.write(
    "An AI-powered Smart Farming Assistant "
    "for Indian farmers."
)

st.header("🌱 Farmer Information")

language = st.selectbox(
    "Choose Language / భాషను ఎంచుకోండి",
    ["English", "Telugu"]
)

soil = st.selectbox(
    "Select Soil Type",
    ["Red Soil", "Black Soil", "Sandy Soil", "Clay Soil"]
)

season = st.selectbox(
    "Select Season",
    ["Kharif", "Rabi", "Summer"]
)

water = st.selectbox(
    "Water Availability",
    ["Low", "Medium", "High"]
)

location = st.text_input(
    "Enter Your District",
    placeholder="Example: Warangal"
)

st.header("🤖 AI Farming Assistant")

question = st.text_area(
    "Ask Your Farming Question",
    placeholder="Which crop is suitable for my soil?"
)
if st.button("🌾 Get Farming Advice"):

    if not question.strip():
        st.warning("Please enter a farming question.")

    else:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            st.error("Gemini API key is missing.")

        else:
            prompt = f"""
            You are RythuMitra AI, a smart farming
            assistant for Indian farmers.

            Farmer Details:
            Soil Type: {soil}
            Season: {season}
            Water Availability: {water}
            District: {location}

            Farmer Question:
            {question}

            IMPORTANT:
The farmer has selected {language}.

You MUST answer the farmer's question
entirely in {language}.

If {language} is Telugu:
- Use Telugu script (తెలుగు).
- Write headings and explanations in Telugu.
- Avoid English sentences.
- Use simple Telugu words suitable for farmers.

If {language} is English:
- Respond entirely in English.

Do not switch languages unless the farmer requests it.

            Provide:
            1. Suitable crop recommendations.
            2. Irrigation guidance.
            3. Farming techniques.
            4. Important precautions.

            Use simple language farmers can understand.
            Do not invent current weather or market prices.
            Explain uncertainty and avoid guaranteed results.
            """

            try:
                client = genai.Client(api_key=api_key)

                with st.spinner("Generating AI farming advice..."):
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )

                if response.text:
                    st.success("🌾 AI Farming Advice Generated!")
                    st.markdown(response.text)
                else:
                    st.warning("No response generated.")

            except Exception as e:
                st.error(f"Error: {e}")