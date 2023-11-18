import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to generate random data for the example
def generate_random_data(start_date, end_date):
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    data = {'Date': date_range, 'Value': np.random.randn(len(date_range))}
    return pd.DataFrame(data)

# Streamlit app
st.title('Stock Time Series Forecasting')

# Date selection widgets
from_date = st.date_input('From Date', pd.to_datetime('2022-01-01'))
to_date = st.date_input('To Date', pd.to_datetime('2022-12-31'))

# Button to generate graph
if st.button('Generate Graph'):
    # Check if the date range is valid
    if from_date <= to_date:
        # Generate random data for the selected date range (replace with your data)
        data = generate_random_data(from_date, to_date)

        # Plot the graph
        plt.figure(figsize=(12, 6))
        plt.plot(data['Date'], data['Value'])
        plt.title('Generated Graph')
        plt.xlabel('Date')
        plt.ylabel('Value')
        st.pyplot()

    else:
        st.warning('Please select a valid date range.')

# Optionally, display the selected date range
st.text(f'Selected Date Range: {from_date} to {to_date}')

