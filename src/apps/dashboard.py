import streamlit as st

def dashboard():
    st.set_page_config(page_title="My Gullak", page_icon="🌍")
    st.markdown("<h1 style='text-align: center;'>Welcome to the 'My Gullak' Application! 🌈</h1>", unsafe_allow_html=True)

    st.markdown("""
    <hr />
    """, unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; font-size: 18px;'>Thank you for using this application! 🙏</p>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; color: gray;'>
        Note: This app is for personnel purposes only and does not advertisement any videos.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""<p style='text-align: center;'>Made with ❤️ by Avdhesh Varshney</p>""", unsafe_allow_html=True)

dashboard()
