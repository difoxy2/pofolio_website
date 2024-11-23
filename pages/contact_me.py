import streamlit as st
import smtplib, ssl
import os

host = 'smtp.gmail.com'
port = 465
context = ssl.create_default_context()
username='bigdk0900ft@gmail.com'
receiver='bigdk0900ft@gmail.com'
password=os.getenv('GOOGLE_APP_PW_1')


st.title('Contact Me')

with st.form(key='my_form'):
    user_email = st.text_input('Your email:')
    user_message = st.text_area('message: ')

    message=f"""\
Subject: New message from {user_email}
New message from {user_email}
{user_message}
    """

    submit_btn = st.form_submit_button('submit')
    if submit_btn:
        st.info('Sending...')
        with smtplib.SMTP_SSL(host,port,context=context) as server:
            server.login(username,password)
            server.sendmail(username,receiver,message)
        st.info('Email sent!')