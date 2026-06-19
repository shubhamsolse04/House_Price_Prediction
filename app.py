import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("house_price_model.pkl", "rb"))

st.set_page_config(
    page_title="House Price Prediction",
    layout="wide"
)

st.title("House Price Prediction")
st.write("Enter house details to predict the price.")

col1, col2 = st.columns(2)

with col1:
    area = st.slider(
        "Area (sq.ft)",
        min_value=500,
        max_value=20000,
        value=5000
    )

    bedrooms = st.slider(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=3
    )

    bathrooms = st.slider(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )

    stories = st.slider(
        "Stories / Floors",
        min_value=1,
        max_value=10,
        value=2
    )

    parking = st.slider(
        "Parking Spaces",
        min_value=0,
        max_value=10,
        value=1
    )

with col2:
    mainroad = st.selectbox(
        "Main Road",
        ["Yes", "No"]
    )

    guestroom = st.selectbox(
        "Guest Room",
        ["Yes", "No"]
    )

    basement = st.selectbox(
        "Basement",
        ["Yes", "No"]
    )

    hotwaterheating = st.selectbox(
        "Hot Water Heating",
        ["Yes", "No"]
    )

    airconditioning = st.selectbox(
        "Air Conditioning",
        ["Yes", "No"]
    )

    prefarea = st.selectbox(
        "Preferred Area",
        ["Yes", "No"]
    )

    furnishing = st.selectbox(
        "Furnishing Status",
        ["Furnished", "Semi-Furnished", "Unfurnished"]
    )

if st.button("Predict Price"):

    mainroad = 1 if mainroad == "Yes" else 0
    guestroom = 1 if guestroom == "Yes" else 0
    basement = 1 if basement == "Yes" else 0
    hotwaterheating = 1 if hotwaterheating == "Yes" else 0
    airconditioning = 1 if airconditioning == "Yes" else 0
    prefarea = 1 if prefarea == "Yes" else 0

    semi_furnished = 0
    unfurnished = 0

    if furnishing == "Semi-Furnished":
        semi_furnished = 1
    elif furnishing == "Unfurnished":
        unfurnished = 1

    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'stories': [stories],
        'mainroad': [mainroad],
        'guestroom': [guestroom],
        'basement': [basement],
        'hotwaterheating': [hotwaterheating],
        'airconditioning': [airconditioning],
        'parking': [parking],
        'prefarea': [prefarea],
        'furnishingstatus_semi-furnished': [semi_furnished],
        'furnishingstatus_unfurnished': [unfurnished]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("Predicted House Price")

    st.success(f"₹ {prediction:,.0f}")

    st.write(f"In Lakhs: ₹ {prediction/100000:.2f} Lakhs")

    st.write(f"In Crores: ₹ {prediction/10000000:.2f} Crores")