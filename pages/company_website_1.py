import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('The Best Company')
company_description = """
A company description is an overview or summary of a business. 
It's an important part of a business plan that often briefly describes an organization's history, 
location, mission statement, management personnel and, when appropriate, legal structure.
"""
st.write(company_description)
st.subheader('Our team')

col1, col2, col3 = st.columns(3)
data=pd.read_csv('resources/company_website_1/data.csv',sep=',')

with col1:
    for index, row in data[0:4].iterrows():
        st.subheader((row['first name']+' '+row['last name']).title())
        st.write(row['role'])
        st.image('resources/company_website_1/images/'+row['image'])

with col2:
    for index, row in data[4:8].iterrows():
        st.subheader((row['first name']+' '+row['last name']).title())
        st.write(row['role'])
        st.image('resources/company_website_1/images/'+row['image'])

with col3:
    for index, row in data[8:].iterrows():
        st.subheader((row['first name']+' '+row['last name']).title())
        st.write(row['role'])
        st.image('resources/company_website_1/images/'+row['image'])