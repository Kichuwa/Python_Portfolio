import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Welcome to my Portfolio!")

col1, col2 = st.columns(2)

about_me_text = """
I am Darren Soulier, a programmer who love to create and learn new things.
I have worked with various tech stacks and have been able to grow my skill
sets beyond exclusively development.
"""

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Darren Soulier")
    st.write(about_me_text)

st.text("Below are some project I have built. Feel free to contact me!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

data_files = pandas.read_csv("data.csv", sep=";")


with col3:
    for index, row in data_files[:10].iterrows():
        st.header(row["title"])
        st.image(f'images/{row["image"]}')
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data_files[10:].iterrows():
        st.header(row["title"])
        st.image(f'images/{row["image"]}')
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")
