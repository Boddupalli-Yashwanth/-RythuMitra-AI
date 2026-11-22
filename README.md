🌾 RythuMitra AI

Smart Farming Assistant for Indian Farmers

Empowering Indian Farmers Through Artificial Intelligence

RythuMitra AI is an AI-powered smart farming assistant designed to help Indian farmers make informed agricultural decisions through personalized farming guidance in their preferred language.

The application uses Google’s Gemini AI to generate farming recommendations based on soil type, season, water availability, location, and farmers’ questions.

🌐 Live Application

Try RythuMitra AI:

https://rythumitra-ai.streamlit.app

⸻

🎯 Problem Statement

Agriculture is the backbone of India’s economy, but many farmers face challenges such as:

* Limited access to agricultural experts.
* Difficulty selecting suitable crops.
* Water scarcity and irrigation challenges.
* Lack of easily accessible farming information.
* Language barriers when using digital agricultural services.
* Limited awareness of sustainable farming practices.

Farmers need an accessible digital assistant that can provide understandable, personalized agricultural guidance.

💡 Proposed Solution

RythuMitra AI addresses these challenges through a multilingual AI-powered farming assistant.

Farmers enter their agricultural conditions, including soil type, season, water availability, and district.

The application processes this information along with the farmer’s question using Gemini AI and generates relevant farming suggestions.

The goal is to make agricultural information more accessible, especially for Telugu-speaking farmers.

⸻

🚀 Key Features

1. AI-Powered Farming Assistant

Uses Gemini AI to generate responses to agricultural questions.

2. Multilingual Support

Supports English and Telugu to improve accessibility.

3. Soil-Based Crop Recommendations

Provides crop suggestions based on selected soil conditions.

4. Seasonal Farming Guidance

Considers Kharif, Rabi, and Summer agricultural seasons.

5. Water Availability Consideration

Takes low, medium, or high water availability into account when generating recommendations.

6. Location-Based Context

Uses the farmer’s district as additional context for farming suggestions.

7. Simple User Interface

Provides an easy-to-use interface developed using Streamlit.

⸻

🛠️ Technology Stack

Technology	Purpose
Python	Backend programming
Streamlit	Web application interface
Google Gemini AI	AI-powered farming recommendations
Google Gen AI SDK	Gemini API integration
Python-dotenv	Local environment variable management
GitHub	Source code hosting
Streamlit Community Cloud	Application deployment

⸻

⚙️ How It Works

Step 1: Farmer opens RythuMitra AI.

Step 2: Farmer selects a preferred language.

Step 3: Farmer enters soil type, agricultural season, water availability, and district.

Step 4: Farmer asks an agricultural question.

Step 5: Gemini AI processes the question and provided farming conditions.

Step 6: The application displays farming recommendations in the selected language.

Application Workflow

          FARMER
             |
             v
     RythuMitra AI
             |
             v
    Enter Farming Details
             |
             v
      Ask a Question
             |
             v
       Gemini AI API
             |
             v
    Generate Farming Advice
             |
             v
     English / Telugu
             |
             v
           FARMER

⸻

💻 Installation and Setup

Prerequisites

* Python
* Internet connection
* Gemini API key

1. Clone the Repository

git clone https://github.com/Boddupalli-Yashwanth/-RythuMitra-AI.git

2. Open the Project Directory

cd -- -RythuMitra-AI

3. Create a Virtual Environment

python3 -m venv .venv

4. Activate the Environment

For macOS/Linux:

source .venv/bin/activate

5. Install Dependencies

pip install -r requirements.txt

6. Configure Gemini API

Create a .env file in the project directory.

Add:

GEMINI_API_KEY=your_api_key_here

Never upload your actual API key to GitHub.

7. Run the Application

streamlit run app.py

Open the local address displayed in Terminal.

⸻

🌱 Example Use Case

Farmer Information:

* Location: Wanaparthy, Telangana
* Soil Type: Red Soil
* Season: Kharif
* Water Availability: Low
* Language: Telugu

Farmer Question:

నా దగ్గర ఎర్ర నేల ఉంది. నీటి సౌకర్యం తక్కువగా ఉంది. ఖరీఫ్ సీజన్‌లో ఏ పంటలు సాగు చేయడం మంచిది?

AI-Generated Guidance:

The application can suggest crops such as millets and pulses, explain irrigation considerations, and provide farming precautions.

Recommendations are informational and should be verified against local agricultural conditions.

⸻

🔮 Future Enhancements

Potential improvements include:

1. Real-time weather forecast integration.
2. Crop disease detection using image recognition.
3. Agricultural market price information.
4. Voice-based interaction in regional languages.
5. Government agricultural scheme information.
6. More Indian regional languages.
7. Soil testing report analysis.

These are planned improvements and are not part of the current implementation.

⸻

⚠️ Disclaimer

RythuMitra AI provides AI-generated agricultural information.

Recommendations may be incomplete or inaccurate. Farmers should verify important decisions with qualified agricultural professionals and reliable local agricultural resources.

The application does not currently verify recommendations using real-time weather, soil testing, or market data.

⸻

🏆 Hackathon

Event: IDEA/FORGE Online Hackathon

Track: Climate, Resource Infrastructure & Global Supply Resilience

Project: RythuMitra AI — Smart Farming Assistant

Objective: Improve access to agricultural guidance through multilingual artificial intelligence.

⸻

👨‍💻 Developer

Boddupalli Yashwanth

Computer Science Student

GitHub: Boddupalli-Yashwanth

⸻

🌾 RythuMitra AI

Smarter Farming. Better Decisions. Empowered Farmers.