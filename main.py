#https://difoxy2-pofolio-website-main-g11fkm.streamlit.app/

import streamlit as st
import pandas as pd

#st.set_page_config(layout='wide')

col1, col2 = st.columns(2,gap="small",vertical_alignment='bottom')

with col1:
    st.image('resources/main/my_pict.jpg',width=300)

with col2:
    st.header('Helen Lai')
    text1="""
    I am Helen Lai. \n
    I am self-teaching to be backend software developer so I can move to other country. \n
    I am building this pofolio website to showcase my project in an interactive way.
    """
    st.info(text1)

st.write('Below you can find some projects that I build. Feel free to contact me!')


app_details = pd.read_csv('resources/main/data.csv',sep=';')
col3, col4 = st.columns(2,vertical_alignment='center')

with col3:  
    for index, row in app_details[0::2].iterrows(): #odd items --> some_list[start:stop:step]
        st.title(row['title'])
        st.image('resources/main/app_img/'+str(index+1)+'.png')
        st.write(row['description'])
        st.markdown("[Source code](%s)" % row['url'])

with col4:  
    for index, row in app_details[1::2].iterrows(): #even items --> some_list[start:stop:step]
        st.title(row['title'])
        st.image('resources/main/app_img/'+str(index+1)+'.png')
        st.write(row['description'])
        st.markdown("[Source code](%s)" % row['url'])
        