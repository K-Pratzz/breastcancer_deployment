import streamlit as st
import joblib
import numpy as np
import pandas as pd


model=joblib.load("BreastCancer_Model.pkl")
st.title("Breast Cancer Detection")
st.header("Enter the details")

radius_mean = st.number_input("Enter radius_mean", min_value=6.981, max_value=28.11,value=6.981)

texture_mean = st.number_input("Enter texture_mean", min_value=9.71, max_value=39.28,value=9.71)

perimeter_mean = st.number_input("Enter perimeter_mean", min_value=43.79, max_value=188.5,value=43.79)

area_mean = st.number_input("Enter area_mean", min_value=143.5, max_value=2501.0,value=143.5)

smoothness_mean = st.number_input("Enter smoothness_mean", min_value=0.05263, max_value=0.1634,value=0.05263)

compactness_mean = st.number_input("Enter compactness_mean", min_value=0.01938, max_value=0.3454,value=0.01938)

concavity_mean = st.number_input("Enter concavity_mean", min_value=0.0, max_value=0.4268,value=0.0)

concave_points_mean = st.number_input("Enter concave points_mean", min_value=0.0, max_value=0.2012,value=0.0)

symmetry_mean = st.number_input("Enter symmetry_mean", min_value=0.106, max_value=0.304,value=0.106)

fractal_dimension_mean = st.number_input("Enter fractal_dimension_mean", min_value=0.04996, max_value=0.09744,value=0.04996)

radius_se = st.number_input("Enter radius_se", min_value=0.1115, max_value=2.873,value=0.1115)

texture_se = st.number_input("Enter texture_se", min_value=0.3602, max_value=4.885,value=0.3602)

perimeter_se = st.number_input("Enter perimeter_se", min_value=0.757, max_value=21.98,value=0.757)

area_se = st.number_input("Enter area_se", min_value=6.802, max_value=542.2,value=6.802)

smoothness_se = st.number_input("Enter smoothness_se", min_value=0.001713, max_value=0.03113,value=0.001713)

compactness_se = st.number_input("Enter compactness_se", min_value=0.002252, max_value=0.1354,value=0.002252)

concavity_se = st.number_input("Enter concavity_se", min_value=0.0, max_value=0.396,value=0.0)

concave_points_se = st.number_input("Enter concave points_se", min_value=0.0, max_value=0.05279,value=0.0)

symmetry_se = st.number_input("Enter symmetry_se", min_value=0.007882, max_value=0.07895,value=0.007882)

fractal_dimension_se = st.number_input("Enter fractal_dimension_se", min_value=0.0008948, max_value=0.02984,value=0.0008948)

radius_worst = st.number_input("Enter radius_worst", min_value=7.93, max_value=36.04,value=7.93)

texture_worst = st.number_input("Enter texture_worst", min_value=12.02, max_value=49.54,value=12.02)

perimeter_worst = st.number_input("Enter perimeter_worst", min_value=50.41, max_value=251.2,value=50.41)

area_worst = st.number_input("Enter area_worst", min_value=185.2, max_value=4254.0,value=185.2)

smoothness_worst = st.number_input("Enter smoothness_worst", min_value=0.07117, max_value=0.2226,value=0.07117)

compactness_worst = st.number_input("Enter compactness_worst", min_value=0.02729, max_value=1.058,value=0.02729)

concavity_worst = st.number_input("Enter concavity_worst", min_value=0.0, max_value=1.252,value=0.0)

concave_points_worst = st.number_input("Enter concave points_worst", min_value=0.0, max_value=0.291,value=0.0)

symmetry_worst = st.number_input("Enter symmetry_worst", min_value=0.1565, max_value=0.6638,value=0.1565)

fractal_dimension_worst = st.number_input("Enter fractal_dimension_worst", min_value=0.05504, max_value=0.2075,value=0.05504)

if st.button("Predict"):
    input_data = {
    "radius_mean": radius_mean,
    "texture_mean": texture_mean,
    "perimeter_mean": perimeter_mean,
    "area_mean": area_mean,
    "smoothness_mean": smoothness_mean,
    "compactness_mean": compactness_mean,
    "concavity_mean": concavity_mean,
    "concave_points_mean": concave_points_mean,
    "symmetry_mean": symmetry_mean,
    "fractal_dimension_mean": fractal_dimension_mean,
    "radius_se": radius_se,
    "texture_se": texture_se,
    "perimeter_se": perimeter_se,
    "area_se": area_se,
    "smoothness_se": smoothness_se,
    "compactness_se": compactness_se,
    "concavity_se": concavity_se,
    "concave_points_se": concave_points_se,
    "symmetry_se": symmetry_se,
    "fractal_dimension_se": fractal_dimension_se,
    "radius_worst": radius_worst,
    "texture_worst": texture_worst,
    "perimeter_worst": perimeter_worst,
    "area_worst": area_worst,
    "smoothness_worst": smoothness_worst,
    "compactness_worst": compactness_worst,
    "concavity_worst": concavity_worst,
    "concave_points_worst": concave_points_worst,
    "symmetry_worst": symmetry_worst,
    "fractal_dimension_worst": fractal_dimension_worst
    }

    data = pd.DataFrame([input_data])
    
    ans=model.predict(data)
    if ans[0]==1:
        st.error("The answer is Malignant(Cancerous)")
    else:
        st.success("The answer is Benign(Non-Cancerous)")

