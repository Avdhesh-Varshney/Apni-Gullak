import streamlit as st
from src.utils.animatedText import animatedText

def dashboard():
    st.set_page_config(page_title="My Gullak", page_icon="🌍")
    st.markdown(f"<h1 style='text-align: center;'>{animatedText('Welcome to the \'My Gullak\' Application! 🌈')}</h1>", unsafe_allow_html=True)

    st.markdown("""
    <hr />
    """, unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>Thank you for using this application! 🙏</p>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; color: gray; font-size: 1.2rem;'>
        Note: This app is only for personnel purpose.
    </p>
    """, unsafe_allow_html=True)

    st.markdown(f"""<p style='text-align: center; font-size: 1.5rem;'>Made with ❤️ by <a href="https://github.com/Avdhesh-Varshney" style='text-decoration: none;'>{animatedText("Avdhesh Varshney")}</a></p>""", unsafe_allow_html=True)

dashboard()
