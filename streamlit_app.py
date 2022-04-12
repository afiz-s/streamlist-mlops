import streamlit as st 

st.write('Hello World!')

st.header('1. Streamlit Button Example')

if st.button('Say Hello'):
    st.write('Why Hello!!')
else:
    st.write('Goodbye!')