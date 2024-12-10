import streamlit as st
from enum import Enum
import sys
sys.path.append('C:\\Users\\guita\\OneDrive\\Área de Trabalho\\Github\\ODS3-TrabFinal')
from classifier.classifier import TweetClassifier

# Define the TweetLabel Enum
class TweetLabel(Enum):
    LABEL_0 = "Não há agressividade detectada nesse tweet"
    LABEL_1 = "Agressividade detectada no tweet"

    @staticmethod
    def get_translation(label):
        try:
            return TweetLabel[label].value
        except KeyError:
            return "Rótulo desconhecido"

# Initialize the classifier
tweet_classifier = TweetClassifier(
    model_name="GuiTap/bert-base-multilingual-cased-finetuned-hate-speech-ptbr",
    tokenizer_name="GuiTap/bert-base-multilingual-cased-finetuned-hate-speech-ptbr"
)

# CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://t.ctcdn.com.br/F-_09sMGXHTPyLYXqxGiUZ_NO5M=/1200x675/smart/i772128.png');
        background-size: cover;
    }
    h1 {
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }
    .response-box {
        background-color: rgba(0, 0, 0, 0.8);
        color: #FFD700;
        font-size: 1.5rem;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #FFD700;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Detector de tweets agressivos")

st.markdown('Digite aqui o tweet suspeito:', unsafe_allow_html=True)
user_input = st.text_input("")

if st.button("Enviar"):
    if user_input.strip():
        try:
            # Use the classifier to get the prediction
            prediction = tweet_classifier.classify(user_input)
            label = prediction['label']
            confidence = prediction['score']

            # Translate the label using TweetLabel enum
            translated_label = TweetLabel.get_translation(label)
            
            # Display the result
            st.markdown(
                f"""
                <div class="response-box">
                    <strong>Predição:</strong> {translated_label}<br>
                </div>
                """,
                unsafe_allow_html=True,
            )
        except ValueError as e:
            st.warning(str(e))
    else:
        st.warning("Por favor, digite algo antes de enviar.")
