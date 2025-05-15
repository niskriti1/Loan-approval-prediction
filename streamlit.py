import streamlit as st
import numpy as np
import pickle
import base64

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Page setup
st.set_page_config(page_title="Loan Approval Predictor", layout="wide")


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_path = 'money.jpg'  # replace with your local image path
img_base64 = get_base64_of_bin_file(img_path)

html_code = f"""
<style>
.custom-img {{
    width: 100%;
    height: 250px;
    object-fit: fit;
}}
</style>
<img src="data:image/jpg;base64,{img_base64}" class="custom-img"/>
"""

st.markdown(html_code, unsafe_allow_html=True)


st.title("🏦 Loan Approval Predictor")
st.write("Fill in the details to check your chances of loan approval.")



st.markdown("### 📋 Applicant Details")
with st.container():
    no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10)
    education = st.selectbox("Education", ['Graduate', 'Not Graduate'])
    self_employed = st.selectbox("Self Employed", ['Yes', 'No'])
    income_annum = st.number_input("Annual Income (Rs)", min_value=0)
    loan_amount = st.number_input("Loan Amount (Rs)", min_value=0)
    loan_term = st.number_input("Loan Term (year)", min_value=0)
    cibil_score = st.slider("CIBIL Score", 300, 900, step=1)
    residential_assets_value = st.number_input("Residential Assets Value (Rs)", min_value=0)
    commercial_assets_value = st.number_input("Commercial Assets Value (Rs)", min_value=0)
    luxury_assets_value = st.number_input("Luxury Assets Value (Rs)", min_value=0)
    bank_asset_value = st.number_input("Bank Asset Value (Rs)", min_value=0)

# Categorical mappings
education_map = {'Graduate': 1, 'Not Graduate': 0}
self_employed_map = {'Yes': 1, 'No': 0}

# Prepare input
raw_input = np.array([[
    no_of_dependents,
    education_map[education],
    self_employed_map[self_employed],
    income_annum,
    loan_amount,
    loan_term,
    cibil_score,
    residential_assets_value,
    commercial_assets_value,
    luxury_assets_value,
    bank_asset_value
]])

scaled_input = scaler.transform(raw_input)


st.markdown("### 🧾 Prediction Result")
if st.button("Predict Loan Approval"):
    prediction = model.predict(scaled_input)[0]
    proba = model.predict_proba(scaled_input)[0][1]

    st.success(f"You have a {proba*100:.1f}% chance of loan approval!")
