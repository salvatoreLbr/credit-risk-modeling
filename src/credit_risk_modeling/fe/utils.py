import streamlit as st


def change_language():
    st.sidebar.selectbox('', ['en', 'it'], key="language_choice", on_change=set_language())

def get_language():
    return st.session_state["language"]

def set_language():
    if "language_choice" not in st.session_state:
        st.session_state["language_choice"] = "en"
    language = st.session_state.language_choice
    st.session_state["language"] = language
