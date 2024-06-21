import streamlit as st
import pandas as pd
from io import StringIO
import  json

st.title(':zap: Streamlit Project Dashboard')
st.text('This is my first public Git repository!')

with st.expander('Statistics'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        data = json.loads(string_data)
        st.json(data)
