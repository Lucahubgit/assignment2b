import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Assignment 2B, DV4S",
    layout="wide",
    initial_sidebar_state="expanded"
    )

st.markdown("""
    <style>
    /* Set background color for the entire page */
    .stApp {
        background-color: #f0f8ff; /* Light blue background */
    }
    /* Set text color for text of the entire app */
    .stApp {
        color: #00008b; /* Dark blue color */
    }
    </style>
""", unsafe_allow_html=True)

st.title("Satisfaction survey")

st.subheader('Please fill in the form below')

with st.form('User information'):
    user_name=st.text_input('Name:',placeholder='Write your name here')
    rating=st.slider('Select a satisfaction value: ', 1, 5, 3)
    st.write('Selected value: ', rating)
    comments=st.text_area('Additional comments:',placeholder='Feel free to write what you want')
    submitted=st.form_submit_button('Submit')

if submitted:
    if not user_name.strip():  # Check if the Name field is empty
        st.error('The "Name" field is mandatory. Please fill it in.')
    else:
        st.write('**Form submitted with the following information:**  \n'
                f'Name: {user_name}  \n'
                f'Rating: {rating}  \n'
                f'Comments: {comments}')
        if rating<3:
            st.markdown('<p style="color:red; font-size:18px;">'
                        '<b>Warning!</b> Rating value is lower than 3</p>',
                        unsafe_allow_html=True)
        else:
            st.markdown('<p style="color:green; font-size:18px;">'
                        '<b>Success!</b> Rating value is higher than 3</p>',
                        unsafe_allow_html=True)
