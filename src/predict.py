
import joblib
import pandas as pd


# Load the trained Random Forest model
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model_path = BASE_DIR / "models" / "sales_forecasting_model.pkl"

model = joblib.load(model_path)


def predict_sales(
    store,
    item,
    lag_1,
    lag_7,
    rolling_mean_7,
    year,
    month,
    day,
    day_of_week,
    is_weekend
):
    """
    Generate sales prediction using the trained Random Forest model.
    """

    # Create input data with the same feature names
    # used during model training
    input_data = pd.DataFrame([{
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
    }])

    # Generate prediction
    prediction = model.predict(input_data)

    return prediction[0]


# Example prediction
if __name__ == "__main__":

    prediction = predict_sales(
        store=1,
        item=1,
        lag_1=50,
        lag_7=55,
        rolling_mean_7=52,
        year=2018,
        month=1,
        day=15,
        day_of_week=0,
        is_weekend=0
    )

    print(f"Predicted Sales: {prediction:.2f} units")

