from pathlib import Path

import joblib
import numpy as np
import streamlit as st


MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "models"
    / "final_xgboost_model.pkl"
)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


package = load_model()
model = package["model"]
features = package["features"]
scaler = package["scaler"]
threshold = package["optimal_threshold"]
feature_indices = package["feature_indices"]

st.title("Network Intrusion Detection System")
st.success("Model loaded successfully!")
st.write("Features:", package["features"])
st.write("Number of features:", len(package["features"]))
st.write("Optimal threshold:", package["optimal_threshold"])
st.write("Package keys:", list(package.keys()))
st.subheader("Enter Network Traffic Features")

input_values = {}

with st.form("prediction_form"):
    for feature in features:
        input_values[feature] = st.number_input(
            feature,
            value=0.0,
            format="%.6f"
        )

    submitted = st.form_submit_button("Analyze Traffic")

if submitted:
    raw_values = np.array(
        [input_values[feature] for feature in features],
        dtype=float
    )

    selected_means = scaler.mean_[feature_indices]
    selected_scales = scaler.scale_[feature_indices]

    scaled_values = (
        raw_values - selected_means
    ) / selected_scales

    model_input = scaled_values.reshape(1, -1)

    attack_probability = float(
        model.predict_proba(model_input)[0, 1]
    )

    prediction = int(
        attack_probability >= threshold
    )

    st.write("Attack Probability:", attack_probability)

    if prediction == 1:
        st.error("⚠️ Intrusion / Attack Detected")
    else:
        st.success("✅ Normal / Benign Traffic")