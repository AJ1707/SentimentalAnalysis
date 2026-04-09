import streamlit as st
import requests

#PAGE CONFIG

st.set_page_config(
    page_title = "Sentiment Analysis",
    page_icon = "🎞️",
    layout = "centered"
)


st.title("🎞️ MOVIE REVIEW SENTIMENT ANALYZER 🎥")
st.write("ENTER A MOVIE REVIEW AND GET INSTANT SENTIMENT PREDICTION !!")


#INPUT BOX
review = st.text_area("ENTER YOUR MOVIE REVIEW HERE:",height=150)

#PREDICT BUTTON
if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("PLEASE ENTER A REVIEW FIRST!")
    else:
        with st.spinner("ANALYZING..."):

            #CALLING FLASK BACKEND
            response = requests.post(
                # "http://127.0.0.1:8000/predict",
                'https://sentimentalanalysis-2bd7.onrender.com/predict',
                json = {"reviews":review}
            )

            result = response.json()

        #DISPLAY RESULT
        sentiment = result['prediction']
        #confidence = result['confidence']


        if "pos" in sentiment or "neg" in sentiment:
            st.success(f"Sentiment : {sentiment}")
        else:
            st.error(f"Sentiment : {sentiment}")


#TERMINAL COMMAND TO RUN STREAMLIT:
#OPEN NEW TERMINAL AND RUN THE BELOW
#streamlit run streamlit_app.py
