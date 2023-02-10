import streamlit as st
import pandas as pd
import tabula

def submit():
    dfs = tabula.read_pdf(file_path, multiple_tables=False, pages="all")
    tables = [pd.DataFrame(df) for df in dfs]
    
    result = pd.concat(tables)
    result = result.dropna()
    result.columns = [' '.join(map(str, x)) for x in zip(list(result.columns), list(result.iloc[0]))]
    result.drop(result.index[0], inplace=True)
    result.to_excel(output_name)
    st.write("Submit button pressed")

file_path = st.file_uploader("Select a file", type=["pdf"])
output_name = st.text_input("Output file name:")

if st.button("Submit"):
    submit()
