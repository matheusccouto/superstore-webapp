""" Web application. """

import pandas as pd
import requests
import streamlit as st

URL = r"https://superstore-api.azurewebsites.net/"


@st.cache(show_spinner=False)
def predict_sales(weeks: int) -> pd.Series:
    """Predict sales for a number of weeks ahead."""
    # Get response and convert it to a pandas series.
    endpoint = URL + r"v1/sales/"
    params = dict(weeks=weeks)
    response = requests.get(endpoint, params=params)
    series = pd.Series(response.json())

    # Index comes as string, it must be converted to datetime.
    series.index = pd.to_datetime(series.index)
    # Set frequency.
    series.index.freq = "W"
    # Set name.
    series.name = "Sales"

    return series


st.set_page_config("Superstore")

st.title("Superstore")
st.text("Time series predictions for the Superstore dataset")

st.header("Forecast Sales")
n_weeks = st.slider(
    "Weeks ahead:",
    min_value=1,
    max_value=100,
    value=50,
    step=1,
    help="Number of weeks aheat to forecast sales.",
)
with st.spinner("Loading..."):
    st.line_chart(predict_sales(n_weeks))
