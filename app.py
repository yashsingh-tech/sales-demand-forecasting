import streamlit as st
import joblib
import pandas as pd
from pathlib import Path


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Sales & Demand Forecasting",
    page_icon="📈",
    layout="centered"
)


# --------------------------------------------------
# Model Loading
# --------------------------------------------------

MODEL_PATH = (
    Path(__file__).resolve().parent
    / "models"
    / "sales_forecasting_model.pkl"
)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()


# --------------------------------------------------
# App UI
# --------------------------------------------------

st.title("📈 Sales & Demand Forecasting")

st.write(
    "Enter the required sales information to predict expected sales."
)

st.divider()

st.subheader("Sales Information")


store = st.number_input(
    "Store",
    min_value=1,
    value=1,
    step=1
)

item = st.number_input(
    "Item",
    min_value=1,
    value=1,
    step=1
)


lag_1 = st.number_input(
    "Previous Day Sales (Lag 1)",
    min_value=0.0,
    value=50.0,
    step=1.0
)


lag_7 = st.number_input(
    "Sales 7 Days Ago (Lag 7)",
    min_value=0.0,
    value=55.0,
    step=1.0
)


rolling_mean_7 = st.number_input(
    "7-Day Average Sales",
    min_value=0.0,
    value=52.0,
    step=1.0
)


year = st.number_input(
    "Year",
    min_value=2010,
    max_value=2030,
    value=2018,
    step=1
)


month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=1,
    step=1
)


day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=15,
    step=1
)


day_of_week = st.number_input(
    "Day of Week",
    min_value=0,
    max_value=6,
    value=0,
    step=1
)


is_weekend = st.selectbox(
    "Is Weekend?",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🔮 Predict Sales", use_container_width=True):

    input_data = pd.DataFrame(
        [{
            "store": store,
            "item": item,
            "lag_1": lag_1,
            "lag_7": lag_7,
            "rolling_mean_7": rolling_mean_7,
            "year": year,
            "month": month,
            "day": day,
            "day_of_week": day_of_week,
            "is_weekend": is_weekend
        }]
    )

    prediction = model.predict(input_data)[0]

    st.divider()

    st.success("Prediction generated successfully!")

    st.metric(
        label="Predicted Sales",
        value=f"{prediction:.2f} units"
    )