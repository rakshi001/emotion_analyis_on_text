# Emotion Analysis on Text 😊

## Overview ✨
**Emotion Analysis on Text** is a sleek Streamlit web app that leverages a transformer-based emotion classifier to detect and visualize emotions in any text you provide. This project is perfect for showcasing modern techniques in neural networks, transformers, and interactive machine learning applications.

## Features 🚀
- **Intuitive Interface:** A clean, user-friendly design built with Streamlit.
- **Real-Time Analysis:** Instantly processes your text input to display the top 3 detected emotions with corresponding confidence scores.
- **Dynamic Visualization:** Enjoy colorful progress bars and expressive emojis that bring the emotion predictions to life.
- **Optimized Performance:** Efficient model loading with caching ensures rapid responses.
- **Lightweight & Impactful:** A compact codebase that effectively demonstrates state-of-the-art NLP integration.

## Demo 🎥
Experience the app in action:
![Emotion Analysis Demo](https://raw.githubusercontent.com/rakshi001/emotion_analyis_on_text/main/sentiment_analysis_image1.png)

## Installation 🛠️

### 1. Clone the Repository
```bash
git clone https://github.com/rakshi001/emotion_analyis_on_text.git
cd emotion_analyis_on_text
```
2. Set Up a Virtual Environment
```
python -m venv venv
# For Linux/Mac:
source venv/bin/activate
# For Windows:
venv\Scripts\activate
```
3. Install Dependencies
Ensure you have the necessary packages listed in your requirements.txt (including streamlit and transformers), then run:
```
pip install -r requirements.txt
```
Usage ⚡
Launch the app locally by executing:
```
streamlit run app.py
```
Your default web browser will open, and you can begin typing text to see the emotion predictions and visualizations in real time.

Code Overview 💻
Model Loading: Utilizes Streamlit’s @st.cache_resource to efficiently load and cache the HuggingFace emotion classifier.

User Interface: Features a styled text area enhanced with custom CSS for an engaging look.

Emotion Visualization: The classifier outputs the top 3 emotions, which are then displayed with intuitive emojis and dynamic progress bars that adjust in color based on confidence levels.

### Deployment 🌐

Deploy your app on Streamlit Cloud by following these steps:

Push your code to GitHub.
Log in to Streamlit Cloud.
Create a new app by linking your GitHub repository and specifying the entry file (e.g., app.py).
Deploy and share your app with the world!
Contributing 🤝
Contributions are welcome! If you have ideas or improvements, please open an issue or submit a pull request.

License 📄
This project is licensed under the MIT License.

Acknowledgements 🙏

HuggingFace Transformers: For providing the pre-trained emotion model.

Streamlit: For making it easy to build and deploy interactive data apps.

## Explore the deployed project here: [Emotion Analysis on Text](https://emotionanalyisontext-fmqftbvhq8fnksxou3jkks.streamlit.app/)
