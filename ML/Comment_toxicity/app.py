import streamlit as st
import pandas as pd
import re
import pickle
import nltk
from nltk.corpus import stopwords
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences

from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model 

# --- Page Configuration ---
st.set_page_config(
    page_title="Comment Toxicity Detection",
    page_icon="🛡️",
    layout="wide"
)

# --- Load Model and Tokenizer (Cached) ---
@st.cache_resource
def load_assets():
    """Loads the pre-trained model and tokenizer."""
    try:
        model = load_model('toxicity_model.h5')
        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)
        # Download stopwords if not already present
        try:
            stopwords.words('english')
        except LookupError:
            nltk.download('stopwords')
        return model, tokenizer
    except Exception as e:
        st.error(f"Error loading assets: {e}")
        st.error("Please make sure 'toxicity_model.h5' and 'tokenizer.pickle' are in the same directory as app.py.")
        return None, None

model, tokenizer = load_assets()
MAX_SEQUENCE_LENGTH = 250
LABEL_COLS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

# --- Preprocessing Function ---
def preprocess_text(text):
    """Cleans and preprocesses text data for prediction."""
    text = str(text)
    text = re.sub('[^a-zA-Z]', ' ', text).lower()
    words = text.split()
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    return ' '.join(words)

# --- Prediction Function ---
def predict_toxicity(texts):
    """Predicts toxicity for a list of texts."""
    if model is None or tokenizer is None:
        return None
    processed_texts = [preprocess_text(t) for t in texts]
    sequences = tokenizer.texts_to_sequences(processed_texts)
    padded_sequences = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
    predictions = model.predict(padded_sequences)
    return predictions

# --- UI Components ---

def render_prediction_interface(use_case_description):
    st.markdown(f"**Use Case:** {use_case_description}")
    st.write("This tool can be integrated into platforms to automatically flag harmful comments, reducing moderator workload and fostering a safer online environment.")
    st.divider()

    # Single Comment Prediction
    st.subheader("Real-Time Single Comment Analysis")
    user_input = st.text_area("Enter a comment to analyze:", "", height=100, key=f"text_area_{st.session_state.page}")
    if st.button("Analyze Comment", key=f"button_{st.session_state.page}"):
        if user_input:
            with st.spinner('Analyzing...'):
                prediction = predict_toxicity([user_input])
                if prediction is not None:
                    st.write("**Toxicity Analysis Results:**")
                    results_df = pd.DataFrame(prediction, columns=LABEL_COLS)
                    for label in LABEL_COLS:
                        probability = results_df[label][0]
                        st.write(f"**{label.replace('_', ' ').title()}**")
                        st.progress(probability)
                        st.write(f"{probability:.2%}")
        else:
            st.warning("Please enter a comment to analyze.")

    st.divider()

    # Bulk Prediction
    st.subheader("Bulk Comment Analysis via CSV Upload")
    uploaded_file = st.file_uploader("Upload a CSV file with a 'comment_text' column", type=["csv"], key=f"uploader_{st.session_state.page}")
    if uploaded_file is not None:
        try:
            df_bulk = pd.read_csv(uploaded_file)
            if 'comment_text' not in df_bulk.columns:
                st.error("The uploaded CSV must contain a column named 'comment_text'.")
            else:
                st.write("**Uploaded Data Preview:**")
                st.dataframe(df_bulk.head())
                if st.button("Run Bulk Analysis", key=f"bulk_button_{st.session_state.page}"):
                    with st.spinner('Processing bulk data... This may take a while.'):
                        predictions = predict_toxicity(df_bulk['comment_text'].tolist())
                        if predictions is not None:
                            pred_df = pd.DataFrame(predictions, columns=LABEL_COLS)
                            result_df = pd.concat([df_bulk, pred_df], axis=1)
                            st.success("Analysis Complete!")
                            st.dataframe(result_df)

                            # Provide download link
                            csv = result_df.to_csv(index=False).encode('utf-8')
                            st.download_button(
                                label="Download Results as CSV",
                                data=csv,
                                file_name='toxicity_analysis_results.csv',
                                mime='text/csv',
                            )
        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")

# --- Main Application ---
st.title("🛡️ Deep Learning for Comment Toxicity Detection")

if model is None or tokenizer is None:
    st.stop()

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Project Overview",
    "Social Media Platforms",
    "Online Forums & Communities",
    "Content Moderation Services",
    "Brand Safety & Reputation",
    "E-learning Platforms",
    "News Websites & Media"
])
st.session_state.page = page # To manage unique keys for widgets

# --- Page Content ---
if page == "Project Overview":
    st.header("Project Overview")
    st.markdown("""
    **Problem Statement:** Online communities face significant challenges from toxic comments, including harassment and hate speech. This project aims to develop an automated system using deep learning to detect and flag toxic comments in real-time, helping to maintain healthy online discourse.
    
    **Approach:**
    1.  **Data Preparation**: Cleaned and preprocessed a dataset of online comments.
    2.  **Model Development**: Trained a Long Short-Term Memory (LSTM) deep learning model to perform multi-label classification on six categories of toxicity.
    3.  **Application**: Built this interactive Streamlit web app for real-time and bulk comment analysis.
    """)
    
    st.subheader("Model Performance")
    col1, col2 = st.columns(2)
    with col1:
        st.image('loss_curve.png', caption='Model Loss over Epochs')
    with col2:
        st.image('accuracy_curve.png', caption='Model Accuracy over Epochs')

elif page == "Social Media Platforms":
    st.header("Use Case: Social Media Platforms")
    render_prediction_interface("Automatically detect and filter toxic comments in real-time to protect users from harassment and abuse.")

elif page == "Online Forums & Communities":
    st.header("Use Case: Online Forums & Communities")
    render_prediction_interface("Integrate toxicity detection to efficiently moderate user-generated content and maintain a constructive community atmosphere.")

elif page == "Content Moderation Services":
    st.header("Use Case: Content Moderation Services")
    render_prediction_interface("Leverage this model to enhance moderation capabilities, providing a scalable solution for clients' platforms.")

elif page == "Brand Safety & Reputation":
    st.header("Use Case: Brand Safety & Reputation Management")
    render_prediction_interface("Ensure that advertisements and sponsored content appear in safe, brand-appropriate online environments by scanning comment sections.")

elif page == "E-learning Platforms":
    st.header("Use Case: E-learning Platforms & Educational Websites")
    render_prediction_interface("Create safer online learning environments by moderating discussion boards and chat features for students and educators.")

elif page == "News Websites & Media":
    st.header("Use Case: News Websites & Media Outlets")
    render_prediction_interface("Utilize toxicity detection to moderate user comments on articles and posts, ensuring discussions remain relevant and civil.")