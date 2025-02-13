import streamlit as st
from transformers import pipeline

# Initialize emotion classifier
@st.cache_resource
def load_emotion_classifier():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=3)

# Set up the page
st.title("Text Emotion Detection")
st.write("Enter some text and I'll detect the emotions in it!")

# Get the classifier
classifier = load_emotion_classifier()

# Create text input with a border
st.markdown("""
    <style>
    .stTextArea textarea {
        border: 2px solid #4a90e2;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
user_input = st.text_area("✍️ Express yourself here:", height=100)

if user_input:
    # Add a spinner while processing
    with st.spinner('Analyzing your text... 🤔'):
        results = classifier(user_input)
    
    # Display results with animation
    st.balloons()
    st.subheader("🎯 Detected Emotions:")
    
    # Emoji mapping for emotions
    emotion_emojis = {
        "joy": "😊",
        "sadness": "😢",
        "anger": "😠",
        "fear": "😨",
        "surprise": "😲",
        "love": "❤️",
        "neutral": "😐"
    }
    
    for result in results[0]:
        emotion = result['label']
        score = result['score']
        
        # Create a colorful container for each emotion
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"### {emotion_emojis.get(emotion, '🔍')} ")
            with col2:
                st.markdown(f"### {emotion.capitalize()}")
            
            # Colorful progress bar
            st.markdown(f"""
                <style>
                .stProgress > div > div > div > div {{
                    background-color: {'#FF9999' if score < 0.3 else '#99FF99' if score > 0.7 else '#4a90e2'};
                }}
                </style>""", 
                unsafe_allow_html=True
            )
            st.progress(score)
            st.markdown(f"**Confidence:** {score:.2%}")
            st.markdown("---")