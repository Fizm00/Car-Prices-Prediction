import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load("car_price_prediction_model.pkl")

# Aplikasi Streamlit
st.title("Prediksi Harga Mobil")

# Input fitur dari pengguna
year = st.number_input("Tahun Mobil", min_value=1980, max_value=2024, value=2015)
engine_hp = st.number_input("Tenaga Mesin (HP)", min_value=50, max_value=1000, value=300)
engine_cylinders = st.number_input("Jumlah Silinder Mesin", min_value=2, max_value=12, value=6)
doors = st.number_input("Jumlah Pintu", min_value=2, max_value=5, value=4)
highway_mpg = st.number_input("Konsumsi BBM di Jalan Tol (MPG)", min_value=10, max_value=50, value=25)
city_mpg = st.number_input("Konsumsi BBM di Kota (MPG)", min_value=5, max_value=40, value=20)
popularity = st.number_input("Popularitas Mobil", min_value=0, max_value=10000, value=4000)

# Pilihan kategori
engine_fuel_type = st.selectbox("Jenis Bahan Bakar", 
    ["regular unleaded", "premium unleaded (required)", "premium unleaded (recommended)", "diesel", "flex-fuel (unleaded/E85)"])
transmission_type = st.selectbox("Jenis Transmisi", 
    ["MANUAL", "AUTOMATIC", "AUTOMATED_MANUAL", "DIRECT_DRIVE", "UNKNOWN"])
driven_wheels = st.selectbox("Sistem Penggerak", 
    ["all wheel drive", "front wheel drive", "rear wheel drive"])
vehicle_size = st.selectbox("Ukuran Kendaraan", 
    ["Compact", "Midsize", "Large"])

# Tombol prediksi
if st.button("Prediksi Harga"):
    # Data input dalam bentuk DataFrame
    input_data = pd.DataFrame({
        "Year": [year],
        "Engine HP": [engine_hp],
        "Engine Cylinders": [engine_cylinders],
        "Number of Doors": [doors],
        "highway MPG": [highway_mpg],
        "city mpg": [city_mpg],
        "Popularity": [popularity],
        "Engine Fuel Type": [engine_fuel_type],
        "Transmission Type": [transmission_type],
        "Driven_Wheels": [driven_wheels],
        "Vehicle Size": [vehicle_size]
    })

    # Prediksi harga
    prediction = model.predict(input_data)
    
    # Tampilkan hasil prediksi
    st.success(f"Harga Prediksi Berdasarkan Perhitungan Adalah Sebesar: ${prediction[0]:,.2f}")
