import streamlit as st
import joblib

model=joblib.load("BreastCancer_Model.pkl")
st.title("Breast Cancer Detection")
st.header("Enter the details")

radius_mean = st.number_input("Enter radius_mean", min_value=6.981, max_value=28.11)
texture_mean = st.number_input("Enter texture_mean", min_value=9.71, max_value=39.28)
perimeter_mean = st.number_input("Enter perimeter_mean", min_value=43.79, max_value=188.5)
area_mean = st.number_input("Enter area_mean", min_value=143.5, max_value=2501.0)
smoothness_mean = st.number_input("Enter smoothness_mean", min_value=0.05263, max_value=0.1634)
compactness_mean = st.number_input("Enter compactness_mean", min_value=0.01938, max_value=0.3454)
concavity_mean = st.number_input("Enter concavity_mean", min_value=0.0, max_value=0.4268)
concave_points_mean = st.number_input("Enter concave points_mean", min_value=0.0, max_value=0.2012)
symmetry_mean = st.number_input("Enter symmetry_mean", min_value=0.106, max_value=0.304)
fractal_dimension_mean = st.number_input("Enter fractal_dimension_mean", min_value=0.04996, max_value=0.09744)
radius_se = st.number_input("Enter radius_se", min_value=0.1115, max_value=2.873)
texture_se = st.number_input("Enter texture_se", min_value=0.3602, max_value=4.885)
perimeter_se = st.number_input("Enter perimeter_se", min_value=0.757, max_value=21.98)
area_se = st.number_input("Enter area_se", min_value=6.802, max_value=542.2)
smoothness_se = st.number_input("Enter smoothness_se", min_value=0.001713, max_value=0.03113)
compactness_se = st.number_input("Enter compactness_se", min_value=0.002252, max_value=0.1354)
concavity_se = st.number_input("Enter concavity_se", min_value=0.0, max_value=0.396)
concave_points_se = st.number_input("Enter concave points_se", min_value=0.0, max_value=0.05279)
symmetry_se = st.number_input("Enter symmetry_se", min_value=0.007882, max_value=0.07895)
fractal_dimension_se = st.number_input("Enter fractal_dimension_se", min_value=0.0008948, max_value=0.02984)
radius_worst = st.number_input("Enter radius_worst", min_value=7.93, max_value=36.04)
texture_worst = st.number_input("Enter texture_worst", min_value=12.02, max_value=49.54)
perimeter_worst = st.number_input("Enter perimeter_worst", min_value=50.41, max_value=251.2)
area_worst = st.number_input("Enter area_worst", min_value=185.2, max_value=4254.0)
smoothness_worst = st.number_input("Enter smoothness_worst", min_value=0.07117, max_value=0.2226)
compactness_worst = st.number_input("Enter compactness_worst", min_value=0.02729, max_value=1.058)
concavity_worst = st.number_input("Enter concavity_worst", min_value=0.0, max_value=1.252)
concave_points_worst = st.number_input("Enter concave points_worst", min_value=0.0, max_value=0.291)
symmetry_worst = st.number_input("Enter symmetry_worst", min_value=0.1565, max_value=0.6638)
fractal_dimension_worst = st.number_input("Enter fractal_dimension_worst", min_value=0.05504, max_value=0.2075)

if st.button("Predict"):
    data=[[radius_mean,texture_mean,perimeter_mean,
       area_mean,smoothness_mean,compactness_mean,concavity_mean,
       concave_points_mean,symmetry_mean,fractal_dimension_mean,
       radius_se,texture_se,perimeter_se,area_se,smoothness_se,
       compactness_se,concavity_se,concave_points_se,symmetry_se,
       fractal_dimension_se,radius_worst,texture_worst,
       perimeter_worst, area_worst,smoothness_worst,
       compactness_worst,concavity_worst,concave_points_worst,
       symmetry_worst,fractal_dimension_worst]]
    
    ans=model.predict(data)
    if ans[0]==1:
        st.error("The answer is Malignant(Cancerous)")
    else:
        st.success("The answer is Benign(Non-Cancerous)")
