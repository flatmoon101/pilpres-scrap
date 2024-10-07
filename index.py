import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

st.title("Data Scraping Pilpres 2024")
st.markdown("------------------------------------------------------------------------------------")

df_anies = pd.read_csv("clean_anies.csv")
df_ganjar = pd.read_csv("clean_ganjar.csv")
df_prabowo = pd.read_csv("clean_prabowo.csv")
    
with st.sidebar:
    selected = option_menu("Calon", ["Anies","Ganjar", "Prabowo"])

color_mapping = {
            'positive': 'blue',
            'neutral': 'lightblue',
            'negative': 'red'
        }

if selected == "Anies":

    img = Image.open('anies.png')
    st.image(img)

    st.subheader("Trend sentimen Anies")
    col1, col2 = st.columns(2)

    with col1:
        df_anies['date'] = pd.to_datetime(df_anies['created_at'], format="%a %b %d %H:%M:%S %z %Y").dt.day
        df_anies1 = df_anies.groupby(['date','label']).size().reset_index()
        df_anies1 = df_anies1.sort_values(['label'],ascending=False)
        df_anies1.rename(columns = {0:'jumlah sentimen'}, inplace = True)

        fig2 = px.line(df_anies1, x="date", y="jumlah sentimen", color='label',width=600, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Tren analisis Anies (roberta)')
        st.plotly_chart(fig2,use_container_width=True)

        # row 2
        df_anies1 = df_anies.groupby(['date','label_bert']).size().reset_index()
        # df_anies1 = df_anies1.sort_values(['label_bert'],ascending=False)
        df_anies1.rename(columns = {0:'jumlah sentimen'}, inplace = True)

        fig2 = px.line(df_anies1, x="date", y="jumlah sentimen", color='label_bert',width=600, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Tren analisis Anies (indobert)')
        st.plotly_chart(fig2,use_container_width=True)

    with col2:
        sentiment_count = df_anies.groupby(['label'])['label'].count()
        sentiment_count = pd.DataFrame({'Sentiments':sentiment_count.index,'sentiment':sentiment_count.values})
        fig = px.pie(sentiment_count,values='sentiment',names='Sentiments',width=550, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Distribution Sentimen Anies (roberta)')
        st.plotly_chart(fig,use_container_width=True)

        # row 2
        sentiment_count = df_anies.groupby(['label_bert'])['label_bert'].count()
        sentiment_count = pd.DataFrame({'Sentiments':sentiment_count.index,'sentiment':sentiment_count.values})
        fig = px.pie(sentiment_count,values='sentiment',names='Sentiments',width=550, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Distribution Sentimen Anies (indobert)')
        st.plotly_chart(fig,use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Positif (roberta)")
        st.write(df_anies[df_anies['label'] == 'positive'][['full_text', 'score']])

        st.subheader("Netral (roberta)")
        st.write(df_anies[df_anies['label'] == 'neutral'][['full_text', 'score']])

        st.subheader("Negatif (roberta)")
        st.write(df_anies[df_anies['label'] == 'negative'][['full_text', 'score']])

    with col2:
        st.subheader("Positif (indobert)")
        st.write(df_anies[df_anies['label_bert'] == 'positive'][['full_text', 'score']])

        st.subheader("Netral (indobert)")
        st.write(df_anies[df_anies['label_bert'] == 'neutral'][['full_text', 'score']])

        st.subheader("Negatif (indobert)")
        st.write(df_anies[df_anies['label_bert'] == 'negative'][['full_text', 'score']])
        
if selected == "Ganjar":

    img = Image.open('ganjar.png')
    st.image(img)

    st.subheader("Trend sentimen Ganjar")
    col1, col2 = st.columns(2)
    
    with col1:
        df_ganjar['date'] = pd.to_datetime(df_ganjar['created_at'], format="%a %b %d %H:%M:%S %z %Y").dt.day
        df_ganjar1 = df_ganjar.groupby(['date','label']).size().reset_index()
        df_ganjar1 = df_ganjar1.sort_values(['label'],ascending=False)
        df_ganjar1.rename(columns = {0:'jumlah sentimen'}, inplace = True)

        fig2 = px.line(df_ganjar1, x="date", y="jumlah sentimen", color='label',width=600, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Tren analisis ganjar (roberta)')
        st.plotly_chart(fig2,use_container_width=True)

        # row 2
        df_ganjar1 = df_ganjar.groupby(['date','label_bert']).size().reset_index()
        df_ganjar1 = df_ganjar1.sort_values(['label_bert'],ascending=False)
        df_ganjar1.rename(columns = {0:'jumlah sentimen'}, inplace = True)

        fig2 = px.line(df_ganjar1, x="date", y="jumlah sentimen", color='label_bert',width=600, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Tren analisis ganjar (indobert)')
        st.plotly_chart(fig2,use_container_width=True)

    with col2:
        sentiment_count = df_ganjar.groupby(['label'])['label'].count()
        sentiment_count = pd.DataFrame({'Sentiments':sentiment_count.index,'sentiment':sentiment_count.values})
        fig = px.pie(sentiment_count,values='sentiment',names='Sentiments',width=550, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Distribution Sentimen ganjar (roberta)')
        st.plotly_chart(fig,use_container_width=True)

        # row 2
        sentiment_count = df_ganjar.groupby(['label_bert'])['label_bert'].count()
        sentiment_count = pd.DataFrame({'Sentiments':sentiment_count.index,'sentiment':sentiment_count.values})
        fig = px.pie(sentiment_count,values='sentiment',names='Sentiments',width=550, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Distribution Sentimen ganjar (indobert)')
        st.plotly_chart(fig,use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Positif (roberta)")
        st.write(df_ganjar[df_ganjar['label'] == 'positive'][['full_text', 'score']])

        st.subheader("Netral (roberta)")
        st.write(df_ganjar[df_ganjar['label'] == 'neutral'][['full_text', 'score']])

        st.subheader("Negatif (roberta)")
        st.write(df_ganjar[df_ganjar['label'] == 'negative'][['full_text', 'score']])

    with col2:
        st.subheader("Positif (indobert)")
        st.write(df_ganjar[df_ganjar['label_bert'] == 'positive'][['full_text', 'score']])

        st.subheader("Netral (indobert)")
        st.write(df_ganjar[df_ganjar['label_bert'] == 'neutral'][['full_text', 'score']])

        st.subheader("Negatif (indobert)")
        st.write(df_ganjar[df_ganjar['label_bert'] == 'negative'][['full_text', 'score']])

if selected == "Prabowo":

    img = Image.open('prabowo.png')
    st.image(img)

    st.subheader("Trend sentimen Prabowo")
    col1, col2 = st.columns(2)
    
    with col1:
        df_prabowo['date'] = pd.to_datetime(df_prabowo['created_at'], format="%a %b %d %H:%M:%S %z %Y").dt.day
        df_prabowo1 = df_prabowo.groupby(['date','label']).size().reset_index()
        df_prabowo1 = df_prabowo1.sort_values(['label'],ascending=False)
        df_prabowo1.rename(columns = {0:'jumlah sentimen'}, inplace = True)

        fig2 = px.bar(df_prabowo1, x="date", y="jumlah sentimen", color='label',width=600, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Tren analisis Prabowo (roberta)')
        st.plotly_chart(fig2,use_container_width=True)

        # row 2
        df_prabowo1 = df_prabowo.groupby(['date','label_bert']).size().reset_index()
        df_prabowo1 = df_prabowo1.sort_values(['label_bert'],ascending=False)
        df_prabowo1.rename(columns = {0:'jumlah sentimen'}, inplace = True)

        fig2 = px.bar(df_prabowo1, x="date", y="jumlah sentimen", color='label_bert',width=600, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Tren analisis Prabowo (indobert)')
        st.plotly_chart(fig2,use_container_width=True)

    with col2:
        sentiment_count = df_prabowo.groupby(['label'])['label'].count()
        sentiment_count = pd.DataFrame({'Sentiments':sentiment_count.index,'sentiment':sentiment_count.values})
        fig = px.pie(sentiment_count,values='sentiment',names='Sentiments',width=550, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Distribution Sentimen Prabowo (roberta)')
        st.plotly_chart(fig,use_container_width=True)

        # row 2
        sentiment_count = df_prabowo.groupby(['label_bert'])['label_bert'].count()
        sentiment_count = pd.DataFrame({'Sentiments':sentiment_count.index,'sentiment':sentiment_count.values})
        fig = px.pie(sentiment_count,values='sentiment',names='Sentiments',width=550, 
            height=400, color_discrete_map=color_mapping).update_layout(title_text='Distribution Sentimen ganjar (indobert)')
        st.plotly_chart(fig,use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Positif (roberta)")
        st.write(df_prabowo[df_prabowo['label'] == 'positive'][['full_text', 'score']])

        st.subheader("Netral (roberta)")
        st.write(df_prabowo[df_prabowo['label'] == 'neutral'][['full_text', 'score']])

        st.subheader("Negatif (roberta)")
        st.write(df_prabowo[df_prabowo['label'] == 'negative'][['full_text', 'score']])

    with col2:
        st.subheader("Positif (indobert)")
        st.write(df_prabowo[df_prabowo['label_bert'] == 'positive'][['full_text', 'score_bert']])

        st.subheader("Netral (indobert)")
        st.write(df_prabowo[df_prabowo['label_bert'] == 'neutral'][['full_text', 'score_bert']])

        st.subheader("Negatif (indobert)")
        st.write(df_prabowo[df_prabowo['label_bert'] == 'negative'][['full_text', 'score_bert']])