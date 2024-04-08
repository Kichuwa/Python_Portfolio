import streamlit as st

st.set_page_config(layout="wide")

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
