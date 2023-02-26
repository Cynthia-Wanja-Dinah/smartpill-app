import pandas as pd
import streamlit as st
from datetime import datetime
import altair as alt

# Define the data
sleep_data = pd.DataFrame(columns=['date', 'hours'])

# Define the user interface
st.title("Sleep Tracker App")

with st.form(key='sleep_form'):
    date = st.date_input('Date')
    hours = st.number_input('Hours of sleep')
    submitted = st.form_submit_button('Submit')

# Define the app logic
if submitted:
    sleep_data = sleep_data.append({
        'date': date,
        'hours': hours
    }, ignore_index=True)

# Add data visualization
chart = alt.Chart(sleep_data).mark_bar().encode(
    x='date:T',
    y='hours:Q',
)

st.altair_chart(chart, use_container_width=True)
