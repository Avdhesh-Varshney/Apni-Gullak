import streamlit as st
from PIL import Image

def profile():
    st.set_page_config(page_title="Profile", page_icon="👤")
    st.title("👤 Profile Page")

    col1, col2 = st.columns([1, 3])
    with col1:
        image = Image.open(f"assets/img/{st.session_state.username}.png")
        st.image(image, width=100)
    with col2:
        st.write(f"**Name:** {st.session_state.name}")
        st.write(f"**Username:** @{st.session_state.username}")
    
    st.markdown("---")
    
    st.write("### User Details")
    
    col3, col4 = st.columns(2)
    with col3:
        st.write(f"**🛠 Role:** {st.session_state.role}")
        st.write(f"**🎂 Age:** {st.session_state.age}")
    with col4:
        st.write(f"**⚥ Gender:** {st.session_state.gender}")
        st.write(f"**📧 Email:** {st.session_state.email}")
    
    st.markdown("---")
    
    st.write("### About Me")
    st.write(st.session_state.about)
