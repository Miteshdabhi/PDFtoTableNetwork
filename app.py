import streamlit as st
import pandas as pd
import numpy as np
from datetime import timedelta

def submit():
    deliveroo_data = pd.read_csv(file_path)
    deliveroo_data['Time Submitted'] = pd.to_datetime(deliveroo_data['Time Submitted'], format='%H:%M:%S')
    deliveroo_data['Date Submitted'] = pd.to_datetime(deliveroo_data['Date Submitted'],format="%Y/%m/%d")
    deliveroo_data['Time Hour'] = pd.DatetimeIndex(deliveroo_data['Time Submitted']).hour
    report_dates = []
    for index,row in deliveroo_data.iterrows():
        if row['Time Hour'] < 6:
            yesterday = row['Date Submitted'] - timedelta(days=1)
            report_dates.append(yesterday.strftime('%Y-%m-%d'))
        else:
            today = row['Date Submitted']
            report_dates.append(today)
    deliveroo_data['NewDate'] = report_dates
    df = pd.pivot_table(deliveroo_data,values='Subtotal',index='NewDate',columns=['Restaurant Name'],aggfunc=np.sum).fillna("")
    df.to_excel(output_name + '.xlsx')

file_path = st.file_uploader("Select a file", type=["csv"])
output_name = st.text_input("Output file name:")

if st.button("Submit"):
    submit()
