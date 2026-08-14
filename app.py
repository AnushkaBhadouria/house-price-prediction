import streamlit as st
import joblib
import numpy as np

model = joblib.load("house_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🏠 House Price Prediction")

bedrooms = st.number_input("Bedrooms", 0.0, 10.0, 3.0)
bathrooms = st.number_input("Bathrooms", 0.0, 10.0, 2.0)
sqft_living = st.number_input("Living Area (sqft)", 100, 10000, 1500)
sqft_lot = st.number_input("Lot Area (sqft)", 500, 500000, 5000)
floors = st.number_input("Floors", 1.0, 5.0, 1.0)
waterfront = st.selectbox("Waterfront", [0, 1])
view = st.slider("View", 0, 4, 0)
condition = st.slider("Condition", 1, 5, 3)
sqft_above = st.number_input("Above Ground Area", 100, 10000, 1200)
sqft_basement = st.number_input("Basement Area", 0, 5000, 0)
yr_built = st.number_input("Year Built", 1900, 2025, 2000)
yr_renovated = st.number_input("Year Renovated", 0, 2025, 0)

if st.button("Predict Price"):

    data = np.array([[bedrooms,
                      bathrooms,
                      sqft_living,
                      sqft_lot,
                      floors,
                      waterfront,
                      view,
                      condition,
                      sqft_above,
                      sqft_basement,
                      yr_built,
                      yr_renovated]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")