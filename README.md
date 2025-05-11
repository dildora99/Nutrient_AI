🍎 Nutrient AI System
Nutrient AI is a Streamlit-powered AI assistant that helps users improve their health by generating meal plans, personalized food imagery, and interactive nutrition chats—all driven by OpenAI's GPT-4 and DALL·E APIs.

🧠 Features
💬 AI Nutrition Chatbot
Ask questions and receive tailored advice on nutrient deficiencies, healthy eating, and cooking tips.

🍽️ Food Image Generator
Describe any dish or use a preset prompt to generate high-quality, stylized images of meals using DALL·E.

📋 Personalized Meal Plan Creator
Generate detailed multi-day meal plans based on selected nutrient deficiencies, dietary restrictions, and meal preferences.

🖼️ Image Gallery
Browse and revisit your previously generated food images.

🚀 How to Run
Clone this repo

bash
Copy
Edit
git clone https://github.com/your-username/nutrient-ai.git
cd nutrient-ai
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set your OpenAI API key
In your .env file or terminal:

bash
Copy
Edit
export OPENAI_API_KEY="your-openai-key"
Run the app

bash
Copy
Edit
streamlit run app.py
📂 File Structure
bash
Copy
Edit
nutrient-ai/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Required Python packages
├── .env                   # Your OpenAI API key (not tracked in git)
└── README.md              # Project documentation
🔧 Requirements
streamlit

openai

Pillow

