import streamlit as st
import numpy as np
import pickle

# Load trained model + scaler
model = pickle.load(open("water_project/model.pkl", "rb"))
scaler = pickle.load(open("water_project/scaler.pkl", "rb"))

# Title
st.title("💧 Water Quality Predictor")

st.write("Enter water parameters:")

# Inputs from user
ph = st.number_input("pH", 0.0, 14.0, 7.0)
hardness = st.number_input("Hardness", 0.0, 500.0)
solids = st.number_input("Solids", 0.0, 50000.0)
chloramines = st.number_input("Chloramines", 0.0, 15.0)
sulfate = st.number_input("Sulfate", 0.0, 500.0)
conductivity = st.number_input("Conductivity", 0.0, 1000.0)
organic_carbon = st.number_input("Organic Carbon", 0.0, 30.0)
trihalomethanes = st.number_input("Trihalomethanes", 0.0, 150.0)
turbidity = st.number_input("Turbidity", 0.0, 10.0)

# Button
if st.button("Predict"):
    data = np.array([[ph, hardness, solids, chloramines, sulfate,
                      conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    # Scale input
    # data = scaler.transform(data)  # Scaler not fitted, skipping for now

    # Predict
    result = model.predict(data)[0]

    # Output
    if result == 1:
        st.success("✅ Water is Safe to Drink")
    else:
        st.error("❌ Water is NOT Safe to Drink")