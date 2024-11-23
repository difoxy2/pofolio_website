import streamlit as st
import pandas as pd
import smtplib, ssl
import os

host = 'smtp.gmail.com'
port = 465
context = ssl.create_default_context()
username='bigdk0900ft@gmail.com'
receiver='bigdk0900ft@gmail.com'
password=os.getenv('GOOGLE_APP_PW_1')


with st.form(key='my_form'):
    user_email= st.text_input('Your email: ')
    opt = pd.read_csv('resources/company_website_1/topics.csv')['topic']
    user_topic=st.selectbox('Topic',options=opt)
    user_message=st.text_area('Your message')

    message=f"""\
Subject: New message from {user_email}
New message from {user_email}
Topic is {user_topic}
{user_message}

"""

    btn_submit=st.form_submit_button('Submit')

    if btn_submit:
        st.info('Sending...')
        with smtplib.SMTP_SSL(host,port,context=context) as server:
            server.login(username,password)
            server.sendmail(username,receiver,message)
        st.info('Email sent!')