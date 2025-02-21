# Emotion Analysis On Text
## Text Emotion Detection

A simple and efficient Streamlit web app that uses a transformer-based emotion classifier to detect emotions in text. Enter any text, and the app will predict the top 3 emotions along with confidence scores and display them with colorful progress bars and emojis.

## Overview

This project leverages the HuggingFace Transformers library and the pre-trained model `j-hartmann/emotion-english-distilroberta-base` to perform text-based emotion detection. It is designed with simplicity and efficiency in mind—perfect for demonstrating your skills in neural networks, transformers, and deploying machine learning apps.

## Features

- **Intuitive User Interface:** Built with Streamlit, the app offers a clean and engaging interface.
- **Real-Time Emotion Analysis:** Processes user input and returns the top 3 emotions along with confidence scores.
- **Dynamic Visuals:** Uses emojis and color-coded progress bars to visualize emotion confidence levels.
- **Efficient Model Loading:** Caches the transformer model to speed up subsequent predictions.
- **Lightweight & Impactful:** A compact codebase that showcases how to integrate state-of-the-art NLP models into interactive applications.

## Installation

### 1. Clone the Repository
```
git clone https://github.com/rakshi001/emotion_analyis_on_text.git
cd emotion_analyis_on_text
```
2. Create and Activate a Virtual Environment
```
python -m venv venv
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
3. Install Dependencies
Make sure you have a requirements.txt file that includes at least:

streamlit
transformers

Then run:
```
pip install -r requirements.txt
```
Usage
To run the app locally, simply execute:
```
streamlit run app.py
```
This command will launch your default browser and display the app. Enter text into the input area and watch the app analyze and display the detected emotions.

Code Overview
Model Loading:

The app uses Streamlit’s ```@st.cache_resource decorator``` to load and cache the emotion classifier from the Transformers pipeline.

User Interface:
A styled text area allows users to enter text. Custom CSS is used to enhance the input box appearance.

Emotion Detection & Visualization:
The classifier predicts the top 3 emotions, which are then displayed with corresponding emojis and progress bars. The progress bar color dynamically changes based on the prediction confidence.

Deployment
This app is ready for deployment on Streamlit Cloud:

Push your code to GitHub.
Log in to Streamlit Cloud.
Create a new app by linking to your GitHub repository and specifying the entry file (e.g., app.py).
Deploy and share your app with the world!
Contributing
Contributions are welcome! Feel free to open issues or pull requests if you have suggestions or improvements.

License
This project is licensed under the MIT License.

Acknowledgements

HuggingFace Transformers for the pre-trained emotion model.
Streamlit for an easy way to build interactive data apps.

You can practically check out the project here which is a deployed version .

https://emotionanalyisontext-fmqftbvhq8fnksxou3jkks.streamlit.app/ 
